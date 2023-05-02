import geometry_msgs.msg
import irobot_create_msgs.action
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

class GoalTranslator(Node):
    def __init__(self):
        super().__init__('goal_translator')
        self.sub = self.create_subscription(geometry_msgs.msg.PoseStamped,
                                            'goal_pose',
                                            self.listener_callback,
                                            10)
        self.sub
        self.nav2pos = ActionClient(
                self,
                irobot_create_msgs.action.NavigateToPosition,
                'navigate_to_position')

    def listener_callback(self, msg):
        print(msg)
        goal_msg = irobot_create_msgs.action.NavigateToPosition.Goal()
        goal_msg.achieve_goal_heading = True
        goal_msg.goal_pose = msg
        self.nav2pos.wait_for_server()
        return self.nav2pos.send_goal_async(goal_msg)
        

def main():
    rclpy.init()

    goal_translator = GoalTranslator()

    rclpy.spin(goal_translator)

    goal_translator.destroy_node()
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()
