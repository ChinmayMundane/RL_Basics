from metadrive.envs.varying_dynamics_env import VaryingDynamicsEnv
from metadrive.component.vehicle.vehicle_type import vehicle_type
import tqdm
import logging

# training_env = VaryingDynamicsEnv(dict(
#         num_scenarios=1000,  
        
#         # Stop randomizing them
#         # random_lane_width=True,
#         # random_agent_model=True,
#         # random_lane_num=True
    
#         # We will sample each parameter from (min_value, max_value)
#         # You can set it to None to stop randomizing the parameter.
#         random_dynamics=dict(
#             max_engine_force=(100, 3000),
#             max_brake_force=(20, 600),
#             wheel_friction=(0.1, 2.5),
#             max_steering=(10, 80),  # The maximum steering angle if action = +-1
#             mass=(300, 3000)
#         ),
#         log_level=logging.WARNING
#     ))

# env_seed=1000
# lane_nums = set()
# lane_widths = set()
# vehicle_models = set()
# traffic_vehicle_models = set()

# # collect statistics
# to_collect_set = {k: set() for k in ["max_engine_force", 
#                                      "max_brake_force", 
#                                      "wheel_friction", 
#                                      "max_steering", 
#                                      "mass"]}

# maps_to_sample = 50
# end_seed = training_env.config["start_seed"] + maps_to_sample
# for env_seed in range(training_env.config["start_seed"], end_seed):
    
#     # use `seed` argument to choose which scenario to run
#     training_env.reset(seed=env_seed)
#     lane_nums.add(training_env.current_map.config["lane_num"]) 
#     lane_widths.add(training_env.current_map.config["lane_width"])
#     vehicle_models.add(training_env.agent.__class__.__name__)
#     traffic_models = set([obj.__class__ for obj in training_env.engine.traffic_manager.spawned_objects.values()])
#     traffic_vehicle_models = traffic_vehicle_models.union(traffic_models)
#     assert vehicle_type[training_env.agent.config["vehicle_model"]] is training_env.agent.__class__
    
#     # collect more
#     for k, v in to_collect_set.items():
#         v.add(training_env.agent.config[k])
    
# training_env.close()

# print("Number of lanes in {} maps are: {}".format(maps_to_sample, lane_nums))
# print("{} maps have {} different widths".format(maps_to_sample, len(lane_widths)))
# print("The policy is learning to drive vehicles with {} different dyamics".format(len(to_collect_set["wheel_friction"])))

# assert all([len(s)==50 for s in to_collect_set.values()])
# assert lane_nums == {3}
# assert len(lane_widths) == 1
# assert vehicle_models == set([vehicle_type["varying_dynamics"].__name__])
# assert len(traffic_vehicle_models) == 4




# Wheel Friction 
from metadrive.policy.idm_policy import IDMPolicy
from metadrive.envs.varying_dynamics_env import VaryingDynamicsEnv
import pygame
import matplotlib.pyplot as plt
from metadrive.utils import generate_gif
import cv2
from IPython.display import Image


# def run_env(friction):
#     env = VaryingDynamicsEnv(dict(num_scenarios=1, 
#                                   traffic_density=0,
#                                   agent_policy=IDMPolicy,
#                                   map="C",
#                                   random_dynamics=dict(wheel_friction=(friction, friction)),
#                                   log_level=50))
#     env.reset(seed=0)
#     try:
#         for i in range(1000):
#             o,r,d,_,info = env.step([0,0])
#             env.render(mode="topdown", 
#                        scaling=6, 
#                        window=True,
#                        camera_position=(70, -60), 
#                        screen_size=(700, 1000),
#                        screen_record=True,
#                        draw_target_vehicle_trajectory=True)
#             if d:
#                 assert info["out_of_road"] if friction < 0.2 else info["arrive_dest"]
#                 break
#         frames=env.top_down_renderer.screen_frames
#     finally:
#         env.close()
#     return frames

# # draw
# f_1=run_env(0.1)  # if value is > 0.2 , vehicle doesnt go out of road
# f_2=run_env(1.2)
# frames = []
# for i in range(len(f_2)):
#     frames.append(cv2.hconcat([f_1[min(i, len(f_1)-1)], f_2[i]]))
# generate_gif(frames)

# Image(open("demo.gif", "rb").read())



# Termination 
from metadrive.utils import print_source
from metadrive import MetaDriveEnv
print_source(MetaDriveEnv.done_function)

