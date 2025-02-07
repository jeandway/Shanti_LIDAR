#!/usr/bin/env python

import roslaunch
import rospy
import rospkg

if __name__ == '__main__':
    rospy.init_node('rplidar', anonymous=True)
    rospack = rospkg.RosPack()
    path = rospack.get_path('rplidar_ros')
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    launch = roslaunch.parent.ROSLaunchParent(uuid, [path + '/launch/rplidar.launch'])
    launch.start()
    
    # roslaunch API is very unstable, hence the node starting then stopping after a few seconds
