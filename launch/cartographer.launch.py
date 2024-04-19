#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

### IMPORTANT ###
# This launch file works only with robot in namespace "vikings_bot_1"
#################

def generate_launch_description():

    use_sim_arg = DeclareLaunchArgument("use_sim", default_value="true",
        description="Use simulation clock or real time"
    )

    package_name = "vikings_bot_cartographer_slam"

    cartographer_config_dir = os.path.join(get_package_share_directory(package_name), 'config')
    configuration_basename = 'cartographer.lua'

    # RVIZ configuration file
    rviz_file = "rviz.rviz"
    rviz_config_dir = os.path.join(get_package_share_directory(package_name), "rviz", rviz_file)


    return LaunchDescription([
        use_sim_arg,
        
        Node(
            package='cartographer_ros', 
            executable='cartographer_node', 
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': LaunchConfiguration("use_sim")}],
            arguments=['-configuration_directory', cartographer_config_dir,
                       '-configuration_basename', configuration_basename],
            remappings=[
                ("/scan", "/vikings_bot_1/lidar_scan"),
                ("/odom", "/vikings_bot_1/odom"),
            ],
        ),

        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            output='screen',
            name='occupancy_grid_node',
            parameters=[{'use_sim_time': LaunchConfiguration("use_sim")}],
            arguments=['-resolution', '0.05', '-publish_period_sec', '1.0']
        ),
        

        Node(
            package="rviz2",
            executable="rviz2",
            output="screen",
            parameters=[{
                "use_sim_time": LaunchConfiguration("use_sim"),
            }],
            arguments=[
                "-d", rviz_config_dir
            ]
        )

    ]) 
