
# RGB LED strip with animations

tested model:
```
some cheap chinese RGB led strip with animations
```

```
bit order = LSB
type = NEC
address = 0xEF00
command = // see the list below
```

```
0xFC03    on
0xFD02    off
0xFE01    brightness_down
0xFF00    brightness_up
0xFB04    red
0xFA05    green
0xF906    blue
0xF807    white
0xF40B    anim_flash
0xF00F    anim_strobe
0xEC13    anim_fade
0xE817    anim_smooth
0xF708    orange
0xF609    lime
0xF50A    light_blue
0xF30C    orange_red
0xF20D    cyan
0xF10E    purple
0xEF10    peach
0xEE11    dark_cyan
0xED12    dark_magenta
0xEB14    yellow
0xEA15    torquoise
0xE916    magenta
```

# Another RGB LED strip with animations

tested model:
```
some cheap chinese RGB led strip with animations
```

```
bit order = LSB
type = NEC
address = 0xFF00
command = // see the list below
```

```
0xBA45    on
0xB847    off
0xB946    timer_off
0xF807    brightness_down
0xBB44    brightness_up
0xBF40    anim_flash
0xBC43    anim_fade
0xEA15    anim_smooth
0xBD42    2h_timer
0xAD52    4h_timer
0xB54A    6h_timer
0xF609    white
0xE916    red
0xE619    green
0xF20D    blue
0xF30C    orange
0xE718    dark_cyan
0xA15E    violet
0xF708    yellow
0xE31C    cyan
0xA55A    magenta
```
