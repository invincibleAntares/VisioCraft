import open3d as o3d
import numpy as np

# Create a simple point cloud
pcd = o3d.geometry.PointCloud()
points = np.random.rand(100, 3)  # 100 random 3D points
pcd.points = o3d.utility.Vector3dVector(points)

# Display the point cloud
o3d.visualization.draw_geometries([pcd])
