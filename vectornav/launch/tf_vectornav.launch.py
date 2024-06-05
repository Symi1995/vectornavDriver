from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    base_link_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='golf_vectornav_base_link_tf',
        arguments=['0', '0', '0', '0', '0', '0', 'golf/base_link', 'golf/vectornav'],
        output='screen'
    )

    return LaunchDescription([
        base_link_tf
    ])