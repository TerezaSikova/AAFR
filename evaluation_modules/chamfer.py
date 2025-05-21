from evaluation_pairwise.utils import chamfer_distance

def run(obj2, gt_pcd, RM_ground,result_transformation):

    cd_result = chamfer_distance(obj2.points, gt_pcd.points)
    print("Chamfer distance: ", cd_result)

    return {"Chamfer distance": cd_result}
