# sway-save-outputs

This simple script is intended to use on sway Wayland compositor together with output management software like [wdisplays](https://github.com/artizirk/wdisplays).
The latter offers a great GUI to config and apply changes, but doesn't save changes anywhere: 
[I'm using Sway, why aren't my display settings saved when I log out?](https://github.com/artizirk/wdisplays#im-using-sway-why-arent-my-display-settings-saved-when-i-log-out).
A possible workaround is:

1. In sway config include outputs configuration from an external file:

```text
include ~/.config/sway/outputs
```

2. run `wdisplays`, and this scripts afterwards:

`wdisplays && sway-save-outputs`

The script reads the current output configuration, with a little help from the `python-i3ipc` module (dependency!), and saves it to `~/.config/sway/outputs`.
