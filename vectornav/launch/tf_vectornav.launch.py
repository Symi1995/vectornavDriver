from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    vectornav_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='golf_vectornav_base_link_tf',
        arguments=[
            '--x',     '-1.464',
            '--y',     '0.035.5',
            '--z',     '-0.258',
            '--yaw',   '0',
            '--pitch', '0',
            '--roll',  '0',

            '--frame-id',      'golf/vectornav',
            '--child-frame-id','golf/base_link'],
        output='screen'
    )

    return LaunchDescription([
        vectornav_tf
    ])