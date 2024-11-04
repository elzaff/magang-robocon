import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_turtle)
        self.step = 0  # Inisialisasi langkah untuk mengontrol gerakan

    def move_turtle(self):
        msg = Twist()

        # Daftar aksi berdasarkan langkah untuk menggambar huruf "R"
        if self.step == 0:
            msg.angular.z = 0.52  # Putar ke kanan
            self.get_logger().info('Menggambar Logo Robocon')
        
        elif self.step == 1:
            time.sleep(1)
            msg.linear.x = 1.5  # Maju
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 2:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = 2.0  # Putar ke kanan
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 3:
            time.sleep(1)
            msg.linear.x = 3.0  # Maju
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 4:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 5:
            time.sleep(1)
            msg.linear.x = 1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 6:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -2.09
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 7:
            time.sleep(1)
            msg.linear.x = 4.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 8:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 9:
            time.sleep(1)
            msg.linear.x = 0.7
            self.get_logger().info('Menggambar Logo Robocon')

        # Langkah-langkah lainnya untuk menyelesaikan gambar huruf "R"
        elif self.step == 10:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 11:
            time.sleep(1)
            msg.linear.x = 1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 12:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = 2.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 13:
            time.sleep(1)
            msg.linear.x = 1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 14:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 15:
            time.sleep(1)
            msg.linear.x = 0.7
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 16:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -2.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 17:
            time.sleep(1)
            msg.linear.x = 1.2
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 18:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = 1.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 19:
            time.sleep(1)
            msg.linear.x = 2.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 20:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -2.0
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 21:
            time.sleep(1)
            msg.linear.x = 2.5
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 22:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -1.5
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 23:
            time.sleep(1)
            msg.linear.x = 0.7
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 24:
            time.sleep(1)
            msg.linear.x = 0.0
            msg.angular.z = -1.5
            self.get_logger().info('Menggambar Logo Robocon')

        elif self.step == 25:
            time.sleep(1)
            msg.linear.x = 0.5
            self.get_logger().info('Menggambar Logo Robocon')

        # Publikasikan pesan dan tingkatkan langkah
        self.publisher.publish(msg)
        self.step += 1

        # Selesai setelah semua langkah selesai
        if self.step > 25:
            self.get_logger().info('Menggambar Logo Robocon selesai.')
            self.timer.cancel()  # Hentikan timer

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)

    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
