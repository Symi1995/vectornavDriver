from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # vectornav_imu_tf = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='golf_vectornav_base_link_tf',
    #     arguments=['1.464', '-0.035.5', '0.258', '0', '0', '0', 'golf/vectornav_imu', 'golf/base_link'],
    #     output='screen'
    # )

    base_link_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='golf_vectornav_base_link_tf',
        arguments=['-0.760', '-0.485', '-1.129', '0', '0', '0', 'golf/base_link', 'golf/vectornav'],
        output='screen'
    )

    return LaunchDescription([
        base_link_tf
    ])