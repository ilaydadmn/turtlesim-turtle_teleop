import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5  # 0.5 saniyede bir mesaj yayınla
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        msg = Twist()
        
        # İlk 3 saniye boyunca ileri git
        if time.time() - self.start_time < 3.0:
            msg.linear.x = 0.5  # İleri hız
            msg.angular.z = 0.0 # Dönme yok
            self.get_logger().info('Publishing Forward...')
        else:
            msg.linear.x = 0.0  # Dur
            msg.angular.z = 0.0 # Dönme yok
            self.get_logger().info('Stopping.')
            self.timer.cancel() # 3 saniye sonra durdurucu kapat

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

