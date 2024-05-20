""""
# args:
# Using Waymo data: --waymo 
# Using Topdown renderer --topdown
python -m metadrive.examples.drive_in_real_env

"""

# from metadrive.engine.asset_loader import AssetLoader
# from metadrive.policy.replay_policy import ReplayEgoCarPolicy
# from metadrive.envs.scenario_env import ScenarioEnv
# from metadrive.utils import generate_gif
# from IPython.display import Image, clear_output
# import cv2

# # turn on this to enable 3D render. It only works when you have a screen
# threeD_render=False
# # Use the built-in datasets with simulator
# nuscenes_data=AssetLoader.file_path(AssetLoader.asset_path, "nuscenes", unix_style=False) 

# env = ScenarioEnv(
#     {
#         "reactive_traffic": False,
#         "use_render": threeD_render,
#         "agent_policy": ReplayEgoCarPolicy,
#         "data_directory": nuscenes_data,
#         "num_scenarios": 3,
#     }
# )

# try:
#     scenarios={}
#     for seed in range(3):
#         print("\nSimulate Scenario: {}".format(seed))
#         o, _ = env.reset(seed=seed)
#         semantic_map = seed == 1
#         for i in range(1, 100000):
#             o, r, tm, tc, info = env.step([1.0, 0.])
#             env.render(mode="top_down", 
#                        window=True,
#                        screen_record=True,
#                        text={"Index": seed,
#                              "semantic_map": semantic_map},
#                        screen_size=(500, 500),
#                        semantic_map=semantic_map) # semantic topdown
#             if info["replay_done"]:
#                 break
#         scenarios[seed]=env.top_down_renderer.screen_frames
# finally:
#     env.close()

# # make gif for three scenarios
# frames=[]
# min_len=min([len(scenario) for scenario in scenarios.values()])
# for i in range(min_len):
#     frames.append(cv2.hconcat([scenarios[s][i] for s in range(3)]))
    
# clear_output()
# generate_gif(frames)
# Image(open("demo.gif", "rb").read())



# Reactive Traffic

import numpy as np
from metadrive.engine.asset_loader import AssetLoader
from metadrive.policy.replay_policy import ReplayEgoCarPolicy
from metadrive.envs.scenario_env import ScenarioEnv
from metadrive.utils import generate_gif
import cv2
from IPython.display import Image

nuscenes_data =  AssetLoader.file_path(AssetLoader.asset_path, "nuscenes", unix_style=False)

def run_real_env(reactive):
    env = ScenarioEnv(
        {
            "reactive_traffic": reactive,
            "data_directory": nuscenes_data,
            "start_scenario_index":6, # use scenario #6
            "num_scenarios": 1,
            "crash_vehicle_done": True,
            "log_level": 50,
        }
    )
    try:
        o, _ = env.reset(seed=6) # start simulation for senario #6
        for i in range(1, 150):
            o, r, tm, tc, info = env.step([.0, -1])
            env.render(mode="top_down", 
                       window=True,
                       screen_record=True, 
                       camera_position=(0,0),
                       screen_size=(500, 400))
        frames=env.top_down_renderer.screen_frames
    finally:
        env.close()
    return frames

# visualization
f_1=run_real_env(False)
f_2=run_real_env(True)
frames = []
for i in range(len(f_1)):
    frames.append(cv2.hconcat([f_1[i], f_2[i]]))
generate_gif(frames)

Image(open("demo.gif", "rb").read())
