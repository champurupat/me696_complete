make sure waffle and gazebo model path is exported in your .bashrc

sample workflow
```
cd
mkdir me696_hh2_ws
cd me696_hh2_ws
git clone git@github.com:champurupat/me696_complete.git # using ssh here, swap for https url if necessary
mv me696_complete src # rename github repo to src
colcon build
```
to launch gazebo of holmes hall second floor fresh terminal, be in the me696_hh2_ws directory
```
cd
cd me696_hh2_ws
. install/setup.bash
ros2 launch holmes_nav holmes_hall.launch.py
```
to launch wall follower run the following commands in different terminals in this order:
```
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True autostart:=False # for nav2 navigation suite

ros2 launch holmes_nav holmes_hall.launch.py # spawn tb3 in hh2

ros2 launch slam_toolbox online_async_launch.py # to launch slam too

ros2 run rviz2 rviz2 -d $(ros2 pkg prefix nav2_bringup)/share/nav2_bringup/rviz/nav2_default_view.rviz # to bring up rviz gui

ros2 run autonomy state_estimator_node 

ros2 run autonomy autonomy_node 
```
then send a goal pose msg, in this example can change x and y coordinates:
```
ros2 topic pub -1 /goal geometry_msgs/msg/Pose '{position: {x: 0.0, y: -10.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}'
```
