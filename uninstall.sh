#!/usr/bin/env bash

path=$(python -c 'import site; print(site.getsitepackages()[0])')
rm -r $path'/sway_save_outputs*'
rm /usr/bin/sway-save-outputs
