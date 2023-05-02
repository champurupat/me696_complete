make sure waffle and gazebo model path is exported in your .bashrc

sample workflow
```
cd
mkdir me696_hh2_ws
cd me696_hh2_ws
git clone git@github.com:champurupat/me696_navigation_holmes.git # using ssh here, swap for https url if necessary
mv me696_navigation_holmes src # rename github repo to src
colcon build
```
to launch gazebo of holmes hall second floor fresh terminal, be in the me696_hh2_ws directory
```
cd
cd me696_hh2_ws
. install/setup.bash
ros2 launch holmes_nav holmes_hall.launch.py
```
