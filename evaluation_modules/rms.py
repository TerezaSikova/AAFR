import numpy as np
import transforms3d
from scipy.spatial.transform import Rotation as R

def run2(obj2, gt_pcd, RM_ground,result_transformation):
    def change_angle(angle):
        if angle < 0:
            angle = angle + np.pi
        return angle%np.pi
    change_my_angle = np.vectorize(change_angle)

    T_ground, R_ground, _, _ = transforms3d.affines.decompose44(RM_ground)
    R_result = change_my_angle(R_ground%np.pi)

    T_result, R_result, _, _ = transforms3d.affines.decompose44(result_transformation)
    R_result = change_my_angle(R_result%np.pi)

    inv = np.linalg.inv(result_transformation)

    T_result_test, R_result_test, _, _ = transforms3d.affines.decompose44(inv)
    R_result_test = change_my_angle(R_result_test%np.pi)
    R_result_test
    R_error = (np.sqrt(np.sum(np.square(R_ground - R_result_test))))
    T_error = (np.sqrt(np.sum(np.square(T_ground - T_result_test))))


    R_error = (np.sqrt(np.sum(np.square(R_ground - R_result))))
    T_error = (np.sqrt(np.sum(np.square(T_ground - T_result))))
    print("Rotation", inv[:3,:3])
    print("Transalation",inv[:3,3])

    """
    T_ground, R_ground, _, _ = transforms3d.affines.decompose44(RM_ground)
    T_result, R_result, _, _ = transforms3d.affines.decompose44(result_transformation)

    # translation RMSE
    T_error = np.linalg.norm(T_ground - T_result)

    # rotation difference matrix
    R_diff = np.dot(R_ground.T, R_result)

    # angle difference (rotation error)
    trace = np.clip(np.trace(R_diff), -1.0, 3.0)
    angle_error_rad = np.arccos((trace - 1) / 2.0)
    angle_error_deg = np.degrees(angle_error_rad)"""
    return {"R_error":R_error,"T_error":T_error}

def run(obj2, gt_pcd, RM_ground,result_transformation):
    original_points = np.asarray(obj2.points)
    rotated_back_points = np.asarray(gt_pcd.points)

    diffs = original_points - rotated_back_points
    mse = np.mean(np.sum(diffs ** 2, axis=1))
    print("MSE:", mse)
    rmse = np.sqrt(mse)
    print("RMSE:", rmse)

    return {"RMSE": rmse, "MSE": mse}