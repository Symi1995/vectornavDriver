import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    this_dir = get_package_share_directory('vectornav')
    
    # Vectornav
    vectornav_cmd = Node(
        namespace='golf',
        package='vectornav', 
        executable='vectornav',
        output='screen',
        parameters=[os.path.join(this_dir, 'config', 'vectornav.yaml')])
    
    vectornav_sensor_msgs_cmd = Node(
        namespace='golf',
        package='vectornav', 
        executable='vn_sensor_msgs',
        output='screen',
        parameters=[os.path.join(this_dir, 'config', 'vectornav.yaml')])

    vectornav_broadcaster = Node(
        namespace='golf',
        package='vectornav',
        executable='broadcaster',
        output='screen')
    
    tf_vectornav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            get_package_share_directory('vectornav') + '/launch/tf_vectornav.launch.py'
        )
    )

    return LaunchDescription([
        tf_vectornav,
        vectornav_cmd,
        vectornav_sensor_msgs_cmd,
        vectornav_broadcaster
    ])

    return ld