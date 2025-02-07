In karina_VLP16_points.launch:
  To change the LIDAR FOV, change the view_width parameter (0 < view_width < 2*pi)
  To set the LIDAR view direction, change the view_direction parameter (0 < view_direction < 2*pi)
  This launch file launches karina_transform_nodelet.launch

In karina_transform_nodelet.launch:
  Added args and params view_width and view_direction <-- it should not be necessary to change these
  
karina_hector_slam.launch launches the hector_slam and mapping
  Launches karina_mapping_params.launch and geotiff_mapper.launch
  
karina_mapping_params:
  Just parameters for the hector mapping
