from metadrive import MetaDriveEnv
import tqdm

# Randomization


# training_env = MetaDriveEnv(dict(
#     num_scenarios=1000,
#     start_seed=1000,
#     random_lane_width=True,
#     random_agent_model=True,
#     random_lane_num=True
# ))


# test_env = MetaDriveEnv(dict(
#     num_scenarios=200,
#     start_seed=0,
#     random_lane_width=True,
#     random_agent_model=True,
#     random_lane_num=True
# ))


# for training_epoch in range(2):
#     # training
#     training_env.reset()
#     print("\nStart fake training epoch {}...".format(training_epoch))
#     for _ in range(10):
#         # execute 10 step
#         training_env.step(training_env.action_space.sample())
#     training_env.close()

#     # evaluation
#     print("Evaluate checkpoint for training epoch {}...\n".format(training_epoch))
#     test_env.reset()
#     for _ in range(10):
#         # execute 10 evaluation step
#         test_env.step(test_env.action_space.sample())
#     test_env.close()

# assert test_env.config is not training_env.config



from metadrive.component.vehicle.vehicle_type import vehicle_type

# container
# env_seed=1000
# lane_nums = set()
# lane_widths = set()
# vehicle_models = set()
# traffic_vehicle_models = set()

# # collect statistics
# maps_to_sample = 50
# end_seed = training_env.config["start_seed"] + maps_to_sample
# for env_seed in tqdm.tqdm(range(training_env.config["start_seed"], end_seed)):
    
#     # use `seed` argument to choose which scenario to run
#     training_env.reset(seed=env_seed)
#     lane_nums.add(training_env.current_map.config["lane_num"]) 
#     lane_widths.add(training_env.current_map.config["lane_width"])
#     vehicle_models.add(training_env.agent.__class__.__name__)
#     traffic_models = set([obj.__class__ for obj in training_env.engine.traffic_manager.spawned_objects.values()])
#     traffic_vehicle_models = traffic_vehicle_models.union(traffic_models)
#     assert vehicle_type[training_env.agent.config["vehicle_model"]] is training_env.agent.__class__
    
# training_env.close()

# # show information
# print("Number of lanes in {} maps are: {}".format(maps_to_sample, lane_nums))
# print("{} maps have {} different widths".format(maps_to_sample, len(lane_widths)))
# print("The policy is learning to drive {} types of vehicles".format(len(vehicle_models)))
# print("There are {} types of traffic vehicles".format(len(traffic_vehicle_models)))

# # check
# assert lane_nums == {2, 3}
# assert len(lane_widths) == 50
# assert len(vehicle_models) == 5
# assert len(traffic_vehicle_models) == len(vehicle_models) - 1



# Traffic

import logging

# # Default, traffic density=0.1
# simple_env = MetaDriveEnv(dict(num_scenarios=10, 
#                                start_seed=0, 
#                                log_level=logging.WARNING))
# # traffic density=0.5
# complex_env = MetaDriveEnv(dict(num_scenarios=10, 
#                                 start_seed=0, 
#                                 traffic_density=0.5,
#                                 log_level=50)) # 50 == logging.WARNING

# def calculate_traffic_vehicles(env, name):
#     num_v = 0
#     for seed in range(10):
#         env.reset(seed=seed)
#         num_v += len(env.engine.traffic_manager.spawned_objects)
#     print("There are averagely {} vehicles in {}".format(num_v/10, name))
#     env.close()

# calculate_traffic_vehicles(simple_env, "environment with 0.1 density")
# calculate_traffic_vehicles(complex_env, "environment with 0.5 density")



from metadrive.policy.idm_policy import IDMPolicy
from IPython.display import Image, clear_output

# env = MetaDriveEnv(dict(traffic_mode="trigger", map="O"))
# env.reset(seed=0)
# try:
#     for i in range(600):
#         o,r,d,_,_ = env.step([0,-0.2] if i < 100 or i> 150 else [0, 0.2])
#         env.render(mode="topdown", 
#                    scaling=2, 
#                    camera_position=(100, 0), 
#                    screen_size=(500, 500),
#                    screen_record=True,
#                    window=True,
#                    text={"episode_step": env.engine.episode_step,
#                          "mode": "Trigger"})
#     env.top_down_renderer.generate_gif()
# finally:
#     env.close()
#     clear_output()


# env = MetaDriveEnv(dict(traffic_mode="respawn", map="O", traffic_density=0.05))
# env.reset(seed=0)
# try:
#     for _ in range(600):
#         o,r,d,_,_ = env.step([0,0.0])
#         env.render(mode="topdown", 
#                    scaling=2,
#                    screen_size=(500, 500),
#                    screen_record=True,
#                    window=True,
#                    camera_position=(100, 0),
#                    text={"episode_step": env.engine.episode_step,
#                          "mode": "Respawn"})
#     env.top_down_renderer.generate_gif()
# finally:
#     env.close()
#     clear_output()


# Image(open("demo.gif", "rb").read())



# Maps 

# generate map with 3 blocks, 5 blocks and 5 blocks with 4 lanes

from metadrive import MetaDriveEnv
from metadrive.component.map.base_map import BaseMap
from metadrive.policy.idm_policy import IDMPolicy
from metadrive.component.map.pg_map import MapGenerateMethod
import matplotlib.pyplot as plt
from metadrive import MetaDriveEnv
from metadrive.utils.draw_top_down_map import draw_top_down_map
import logging


# map_config={BaseMap.GENERATE_TYPE: MapGenerateMethod.BIG_BLOCK_NUM, 
#             BaseMap.GENERATE_CONFIG: 3,  # 3 block
#             BaseMap.LANE_WIDTH: 3.5,
#             BaseMap.LANE_NUM: 2}

# fig, axs = plt.subplots(3, 3, figsize=(10, 10), dpi=200)
# plt.tight_layout(pad=-3)

# for i in range(3):
#     if i==0:
#         map_config["config"]=3
#         env = MetaDriveEnv(dict(num_scenarios=10, map_config=map_config, log_level=logging.WARNING))
#     elif i==1:
#         map_config["config"]=5
#         env = MetaDriveEnv(dict(num_scenarios=10, map_config=map_config, log_level=logging.WARNING))
#     elif i==2:
#         map_config["config"]=5
#         map_config["lane_num"]=4
#         env = MetaDriveEnv(dict(num_scenarios=10, map_config=map_config, log_level=logging.WARNING))
#     for j in range(3):
#         env.reset(seed=j)
#         m = draw_top_down_map(env.current_map)
#         ax = axs[i][j]
#         ax.imshow(m, cmap="bone")
#         ax.set_xticks([])
#         ax.set_yticks([])
#     env.close()
# plt.show()



map_config={BaseMap.GENERATE_TYPE: MapGenerateMethod.BIG_BLOCK_SEQUENCE, 
            BaseMap.GENERATE_CONFIG: "XOS",  # 3 block
            BaseMap.LANE_WIDTH: 3.5,
            BaseMap.LANE_NUM: 2}

# fig, axs = plt.subplots(3, 3, figsize=(10, 10), dpi=200)
# plt.tight_layout(pad=-3)

# for i in range(3):
#     if i==0:
#         map_config["config"]="ST"
#         env = MetaDriveEnv(dict(num_scenarios=10, map_config=map_config, log_level=logging.WARNING))
#     elif i==1:
#         map_config["config"]="XCO"
#         env = MetaDriveEnv(dict(num_scenarios=10, map_config=map_config, log_level=logging.WARNING))
#     elif i==2:
#         map_config["config"]="rCR"
#         map_config["lane_num"]=4
#         env = MetaDriveEnv(dict(num_scenarios=10, map_config=map_config, log_level=logging.CRITICAL))
#     for j in range(3):
#         env.reset(seed=j)
#         m = draw_top_down_map(env.current_map)
#         ax = axs[i][j]
#         ax.imshow(m, cmap="bone")
#         ax.set_xticks([])
#         ax.set_yticks([])
#     env.close()
# plt.show()


fig, axs = plt.subplots(2, 3, figsize=(10, 6.5), dpi=200)
plt.tight_layout(pad=-3)

for i in range(2):
    if i==0:
        env = MetaDriveEnv(dict(num_scenarios=10, map=5, log_level=logging.WARNING))
    elif i==1:
        map_config["config"]="XCO"
        env = MetaDriveEnv(dict(num_scenarios=10, map="OC", log_level=logging.WARNING))
    for j in range(3):
        env.reset(seed=j)
        m = draw_top_down_map(env.current_map)
        ax = axs[i][j]
        ax.imshow(m, cmap="bone")
        ax.set_xticks([])
        ax.set_yticks([])
    env.close()
plt.show()



