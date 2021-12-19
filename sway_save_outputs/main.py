#!/usr/bin/env python3
import os
import sys
import argparse
from sway_save_outputs.__about__ import __version__


def list_outputs():
    try:
        from i3ipc import Connection
    except ModuleNotFoundError:
        print("'python-i3ipc' package required, terminating", file=sys.stderr)
        sys.exit(1)

    i3 = Connection()
    tree = i3.get_tree()
    outputs_dict = {}

    for item in tree:
        if item.type == "output" and not item.name.startswith("__"):
            outputs_dict[item.name] = {"x": item.rect.x,
                                       "y": item.rect.y,
                                       "width": item.rect.width,
                                       "height": item.rect.height}

            outputs_dict[item.name]["transform"] = item.ipc_data["transform"] if "transform" in item.ipc_data else None
            outputs_dict[item.name]["scale"] = float(item.ipc_data["scale"]) if "scale" in item.ipc_data else None
            outputs_dict[item.name]["refresh"] = int(
                round(item.ipc_data["current_mode"]["refresh"] / 1000, 0)) if "refresh" in item.ipc_data[
                "current_mode"] else None

    return outputs_dict


def save_list_to_text_file(data, file_path):
    text_file = open(file_path, "w")
    for line in data:
        text_file.write(line + "\n")
    text_file.close()


def main():
    config_path = os.path.join(os.getenv("HOME"), ".config/sway/outputs")
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--file",
                        type=str,
                        default=config_path,
                        help="full path to save outputs to; default: {}".format(config_path))
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version="%(prog)s version {}".format(__version__),
                        help="display version information")
    args = parser.parse_args()

    outputs = []
    outputs_dict = list_outputs()
    for key in outputs_dict:
        outputs.append('output "%s" {' % key)
        outputs.append('    mode %sx%s@%dHz' % (
            outputs_dict[key]["width"], outputs_dict[key]["height"], outputs_dict[key]["refresh"]))
        outputs.append('    pos {} {}'.format(outputs_dict[key]["x"], outputs_dict[key]["y"]))
        if outputs_dict[key]["transform"]:
            outputs.append('    transform {}'.format(outputs_dict[key]["transform"]))
        if outputs_dict[key]["scale"]:
            outputs.append('    scale {}'.format(outputs_dict[key]["scale"]))
        outputs.append("}")

    print("Saving to {}".format(args.file))
    save_list_to_text_file(outputs, args.file)


if __name__ == '__main__':
    main()
