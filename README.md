# vikings_bot_cartographer_slam

This repository contains package, which allows to generate map using real or simulated robot. 

__Make sure that real robot or simulation is already running__

__This cartographer works only for robot in `vikings_bot_1` namespace.
Edit `./config/cartographer.lua` file to use with another robot__ 

### 1. Start cartographer
```ros2 launch vikings_bot_cartographer_slam cartographer.launch.py``` 
#### Parameters:
- `use_sim`: Whether to use simulated or real robot -> *bool*, default *true*
- `use_rviz`: whether to automatically open `rviz2` -> *bool*, default *true*

### 2. Save the map
```ros2 run nav2_map_server map_saver_cli -f map_name```

