from metadrive.engine.core import main_camera
from metadrive.envs.metadrive_env import MetaDriveEnv
from metadrive.component.sensors.rgb_camera import RGBCamera
import cv2
from metadrive.policy.idm_policy import IDMPolicy
from IPython.display import Image
from metadrive.utils import generate_gif
import numpy as np
import os
# sensor_size = (84, 60) if os.getenv('TEST_DOC') else (200, 100)

# cfg=dict(image_observation=True, 
#          vehicle_config=dict(image_source="rgb_camera"),
#          sensors={"rgb_camera": (RGBCamera, *sensor_size)},
#          stack_size=3,
#          agent_policy=IDMPolicy # drive with IDM policy
#         )

# env=MetaDriveEnv(cfg)
# frames = []
# try:
#     env.reset()
#     for _ in range(1 if os.getenv('TEST_DOC') else 10000):
#         # simulation
#         o, r, d, _, _ = env.step([0,1])
#         # rendering, the last one is the current frame
#         ret=o["image"][..., -1]*255 # [0., 1.] to [0, 255]
#         ret=ret.astype(np.uint8)
#         frames.append(ret[..., ::-1])
#         if d:
#             break
#     generate_gif(frames if os.getenv('TEST_DOC') else frames[-300:-50])
#     Image(open("demo.gif", 'rb').read(), width=512, height=256)
# finally:
#     env.close()

# cfg=dict(image_observation=True, 
#          vehicle_config=dict(image_source="main_camera"),
#          norm_pixel=True,
#          agent_policy=IDMPolicy, # drive with IDM policy
#          show_terrain = not os.getenv('TEST_DOC'), # test
#          window_size=(84, 60) if os.getenv('TEST_DOC') else (200, 100))

# env=MetaDriveEnv(cfg)
# frames = []
# try:
#     env.reset()
#     for _ in range(1 if os.getenv('TEST_DOC') else 10000):
#         # simulation
#         o, r, d, _, _ = env.step([0,1])
#         # rendering, the last one is the current frame
#         ret=o["image"][..., -1]
#         frames.append(ret[..., ::-1])
#         if d:
#             break
#     generate_gif(frames if os.getenv('TEST_DOC') else frames[-300: -50])
# finally:
#     env.close()

# Image(open("demo.gif", 'rb').read(), width=512, height=256)


# # Using semantic camera as observation
# from metadrive.envs import MetaDriveEnv
# from metadrive.component.sensors.semantic_camera import SemanticCamera
# import matplotlib.pyplot as plt
# import os

# size = (256, 128) if not os.getenv('TEST_DOC') else (16, 16) # for github CI

# env = MetaDriveEnv(dict(
#     log_level=50, # suppress log
#     image_observation=True,
#     show_terrain=not os.getenv('TEST_DOC'),
#     sensors={"sementic_camera": [SemanticCamera, *size]},
#     vehicle_config={"image_source": "sementic_camera"},
#     stack_size=3,
# ))
# obs, info = env.reset()
# for _ in range(5):
#     obs, r, d, t, i = env.step((0, 1))

# env.close()

# print({k: v.shape for k, v in obs.items()})  # Image is in shape (H, W, C, num_stacks)

# plt.subplot(131)
# plt.imshow(obs["image"][:, :, :, 0])
# plt.subplot(132)
# plt.imshow(obs["image"][:, :, :, 1])
# plt.subplot(133)
# plt.imshow(obs["image"][:, :, :, 2])


# # TopDownObservation
# from metadrive import TopDownMetaDrive

# env = TopDownMetaDrive()
# try:
#     o,i = env.reset()
#     for s in range(1, 100000):
#         o, r, tm, tc, info = env.step([0, 1])
#         env.render(mode="top_down")
#         if tm or tc:
#             break
#             env.reset()
# finally:
#     env.close()



# # customise multi sensor --- gives error, will see later

# from metadrive.envs.metadrive_env import MetaDriveEnv
# from metadrive.component.sensors.rgb_camera import RGBCamera
# from metadrive.component.sensors.semantic_camera import SemanticCamera
# from metadrive.component.sensors.depth_camera import DepthCamera
# import cv2
# import gymnasium as gym
# import numpy as np
# from metadrive.policy.idm_policy import IDMPolicy
# from metadrive.obs.observation_base import BaseObservation
# from metadrive.obs.image_obs import ImageObservation
# from metadrive.obs.state_obs import StateObservation
# import os
# sensor_size = (84, 60) if os.getenv('TEST_DOC') else (200, 100)

# class MyObservation(BaseObservation):
#     def __init__(self, config):
#         super(MyObservation, self).__init__(config)
#         self.rgb = ImageObservation(config, "rgb", config["norm_pixel"])
#         self.depth = ImageObservation(config, "depth", config["norm_pixel"])
#         self.semantic = ImageObservation(config, "semantic", config["norm_pixel"])
#         self.state = StateObservation(config)

#     @property
#     def observation_space(self):
#         os={o: getattr(self, o).observation_space for o in ["rgb", "state", "depth", "semantic"]}
#         return gym.spaces.Dict(os)

#     def observe(self, vehicle):
#         os={o: getattr(self, o).observe() for o in ["rgb", "state", "depth", "semantic"]}
#         return os

# cfg=dict(agent_policy=IDMPolicy, # drive with IDM policy
#          agent_observation=MyObservation,
#          image_observation=True,
#          sensors={"rgb": (RGBCamera, *sensor_size),
#                   "depth": (DepthCamera, *sensor_size),
#                   "semantic": (SemanticCamera, *sensor_size)},
#          log_level=50) # turn off log

# from metadrive.utils import generate_gif
# from IPython.display import Image

# frames = []
# env=MetaDriveEnv(cfg)
# try:
#     env.reset()
#     print("Observation shape: \n", env.observation_space)
#     for step in range(1 if os.getenv('TEST_DOC') else 1000):
#         o, r, d, _, _ = env.step([0,1]) # simulation
        
#         # visualize image observation
#         o_1 = o["depth"][..., -1]
#         o_1 = np.concatenate([o_1, o_1, o_1], axis=-1) # align channel
#         o_2 = o["rgb"][..., -1]
#         o_3 = o["semantic"][..., -1]
#         ret = cv2.hconcat([o_1, o_2, o_3])*255
#         ret=ret.astype(np.uint8)
#         frames.append(ret[..., ::-1])
#         if d:
#             break
#     generate_gif(frames if os.getenv('TEST_DOC') else frames[-300:-50]) # only show 250 frames
# finally:
#     env.close()



# #Customization-MultiView -- gives error
# from metadrive.envs.metadrive_env import MetaDriveEnv
# import cv2
# import gymnasium as gym
# import numpy as np
# from metadrive.obs.observation_base import BaseObservation
# from metadrive.obs.image_obs import ImageObservation
# import os
# from metadrive.utils import generate_gif
# from IPython.display import Image
# sensor_size = (1, 1) if os.getenv('TEST_DOC') else (200, 200)

# class MyObservation(BaseObservation):
#     def __init__(self, config):
#         super(MyObservation, self).__init__(config)
#         self.rgb = ImageObservation(config, main_camera, config["norm_pixel"])

#     @property
#     def observation_space(self):
#         os = {"entry_{}".format(idx): self.rgb.observation_space for idx in range(4)}
#         os["top_down"] = self.rgb.observation_space
#         return gym.spaces.Dict(os)

#     def observe(self, vehicle):
#         ret = {}
#         # The first rendered image is the top-down view
#         ret["top_down"] = self.rgb.observe()
#         # The camera can be borrowed to render new images with new poses
#         for idx in range(4):
#             ret["entry_{}".format(idx)] = self.rgb.observe(self.engine.origin,
#                                                            position=[70, 8.75, 8],
#                                                            hpr=[idx * 90, -15, 0])
#         return ret


# env_cfg = dict(agent_observation=MyObservation,
#                image_observation=True,
#                window_size=sensor_size,
#                map="X",
#                show_terrain=not os.getenv('TEST_DOC'),
#                traffic_density=0.2,
#                show_interface=False,
#                show_fps=False,
#                traffic_mode="respawn",
#                log_level=50,  # no log message
#                vehicle_config=dict(image_source="main_camera"))


# def reset_sensors(self):
#     """
#     Put the main camera to the center of the intersection at the start of each episode
#     """
#     self.main_camera.stop_track()
#     self.main_camera.set_bird_view_pos([70, 8.75])
#     self.main_camera.top_down_camera_height = 50


# MetaDriveEnv.reset_sensors = reset_sensors
# frames = []
# env = MetaDriveEnv(env_cfg)
# try:
#     env.reset()
#     print("Observation shape: \n", env.observation_space)
#     for step in range(1 if os.getenv('TEST_DOC') else 500):
#         o, r, d, _, _ = env.step([0, -1])  # simulation

#         # visualize image observation
#         o_1 = o["entry_0"][..., -1]
#         o_2 = o["entry_1"][..., -1]
#         o_3 = o["entry_2"][..., -1]
#         o_4 = o["entry_3"][..., -1]
#         o_5 = o["top_down"][..., -1]
#         ret = cv2.hconcat([o_1, o_2, o_3, o_4, o_5]) * 255
#         ret = ret.astype(np.uint8)
#         frames.append(ret[::2, ::2, ::-1])
#     generate_gif(frames if os.getenv('TEST_DOC') else frames[-100:])  # only show -100 frames
# finally:
#     env.close()


# Can I use LidarState observation but also render the images at the same time?
from metadrive.envs.metadrive_env import MetaDriveEnv
from metadrive.obs.state_obs import LidarStateObservation
from metadrive.component.sensors.rgb_camera import RGBCamera

env = MetaDriveEnv(config=dict(
    use_render=False,
    agent_observation=LidarStateObservation,
    image_observation=True,
    norm_pixel=False,
    sensors=dict(rgb_camera=(RGBCamera, 512, 256)),
))

obs, info = env.reset()

print("Observation shape: ", obs.shape)

image = env.engine.get_sensor("rgb_camera").perceive(to_float=False)
image = image[..., [2, 1, 0]]

import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
