
#include <ros/ros.h>
#include <cmath>
#include <std_msgs/Int64.h>

#define student_id 2023741071    //조이스틱 감도 조절

class hw
{
public:
  hw();
  ~hw();

private:
  void topic_Callback(const std_msgs::Int64::ConstPtr& topic);

  ros::NodeHandle n;
  ros::Subscriber sub_;  
};

hw::topic_Callback(const std_msgs::Int64::ConstPtr& topic){
ROS_INFO("my student id: %d",topic);
}

hw::hw()
{
  sub_ = n.subscribe<std_msgs::Int64>("topic", 100, &hw::topic_Callback, this);
}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "vel");  // ROS 노드를 초기화하고 vel 이라는 노드를 생성함.
  hw vel;          // Joy_cmd_vel_mani 클래스의 객체를 생성함.

  ros::Rate loop_rate(33);  // 노드가 주기적으로 실행되도록 루프를 설정함.
  while (ros::ok())         // ROS가 정상적으로 실행 중인 동안 계속해서 루프를 실행함.
  {
    vel.operate();      // operate 함수를 호출함.
    ros::spinOnce();    // 콜백 함수를 호출하고 메시지 큐를 처리함.
    loop_rate.sleep();  // 설정된 주기에 따라 루프를 대기
  }
  return 0;
}
 
