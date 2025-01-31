#include "vectornav_msgs/msg/common_group.hpp"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"


class FramePublisher : public rclcpp::Node
{
public:
  FramePublisher()
  : Node("FramePublisher")
  {

    // Initialize the transform broadcaster
    tf_broadcaster_ = std::make_unique<tf2_ros::TransformBroadcaster>(this);

    subscription_ = this->create_subscription<vectornav_msgs::msg::CommonGroup>(
      "vectornav/raw/common", 10, std::bind(
        &FramePublisher::vn_transform, this, std::placeholders::_1));
  }

private:
  void vn_transform(const vectornav_msgs::msg::CommonGroup msg)
  {
    geometry_msgs::msg::TransformStamped t;

    t.header.stamp = this->get_clock()->now();
    t.header.frame_id = "world";
    t.child_frame_id = "vectornav";

    t.transform.translation.x = msg.position.x;
    t.transform.translation.y = msg.position.y;
    t.transform.translation.z = msg.position.z;

    t.transform.rotation.x = msg.quaternion.x;
    t.transform.rotation.y = msg.quaternion.y;
    t.transform.rotation.z = msg.quaternion.z;
    t.transform.rotation.w = msg.quaternion.w;


    // Send the transformation
    tf_broadcaster_->sendTransform(t);
  }

  rclcpp::Subscription<vectornav_msgs::msg::CommonGroup>::SharedPtr subscription_;
  std::shared_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<FramePublisher>());
  rclcpp::shutdown();
  return 0;
}