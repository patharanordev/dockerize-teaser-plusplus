import copy
import time
import numpy as np
import open3d as o3d
from open3d import geometry
import teaserpp_python
import sys
import os

NOISE_BOUND = 0.05
N_OUTLIERS = 1700
OUTLIER_TRANSLATION_LB = 5
OUTLIER_TRANSLATION_UB = 10

def get_angular_error(R_exp, R_est):
    """
    Calculate angular error
    """
    return abs(np.arccos(min(max(((np.matmul(R_exp.T, R_est)).trace() - 1) / 2, -1.0), 1.0)));


if __name__ == "__main__":
    
    print("==================================================")
    print("        TEASER++ Python registration example      ")
    print("==================================================")
    
    src_pcs = sys.argv[1]
    dst_pcs = sys.argv[2]
    limit = sys.argv[3]
    
    print('src_pcs:', src_pcs)
    print('dst_pcs:', dst_pcs)
    
    src = o3d.io.read_point_cloud(src_pcs)
    dst = o3d.io.read_point_cloud(dst_pcs)
    
    src = np.asarray(src.points)[:int(limit), :]
    dst = np.asarray(dst.points)[:int(limit), :]

    src = np.transpose(src)
    dst = np.transpose(dst)
    print('src:', src.shape)
    print('dst:', dst.shape)
        
    # Populating the parameters
    solver_params = teaserpp_python.RobustRegistrationSolver.Params()
    solver_params.cbar2 = 1
    solver_params.noise_bound = NOISE_BOUND
    solver_params.estimate_scaling = False
    solver_params.rotation_estimation_algorithm = teaserpp_python.RobustRegistrationSolver.ROTATION_ESTIMATION_ALGORITHM.GNC_TLS
    solver_params.rotation_gnc_factor = 1.4
    solver_params.rotation_max_iterations = 100
    solver_params.rotation_cost_threshold = 1e-12

    solver = teaserpp_python.RobustRegistrationSolver(solver_params)
    start = time.time()
    solver.solve(src, dst)
    end = time.time()

    solution = solver.getSolution()

    print("=====================================")
    print("          TEASER++ Results           ")
    print("=====================================")

    print("Estimated rotation: ")
    print(solution.rotation)
    print("Estimated translation: ")
    print(solution.translation)
    print("Time taken (s): ", end - start)

