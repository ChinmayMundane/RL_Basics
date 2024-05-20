
# Action
from metadrive.component.vehicle.base_vehicle import BaseVehicle
# from metadrive.utils import print_source
# print_source(BaseVehicle._set_action)
# print_source(BaseVehicle._apply_throttle_brake)

# def _set_action(self, action):
#     if action is None:
#         return
#     steering = action[0]
#     self.throttle_brake = action[1]
#     self.steering = steering
#     self.system.setSteeringValue(self.steering * self.max_steering, 0)
#     self.system.setSteeringValue(self.steering * self.max_steering, 1)
#     self._apply_throttle_brake(action[1])

# def _apply_throttle_brake(self, throttle_brake):
#     max_engine_force = self.config["max_engine_force"]
#     max_brake_force = self.config["max_brake_force"]
#     for wheel_index in range(4):
#         if throttle_brake >= 0:
#             self.system.setBrake(2.0, wheel_index)
#             if self.speed_km_h > self.max_speed_km_h:
#                 self.system.applyEngineForce(0.0, wheel_index)
#             else:
#                 self.system.applyEngineForce(max_engine_force * throttle_brake, wheel_index)
#         else:
#             if self.enable_reverse:
#                 self.system.applyEngineForce(max_engine_force * throttle_brake, wheel_index)
#                 self.system.setBrake(0, wheel_index)
#             else:
#                 self.system.applyEngineForce(0.0, wheel_index)
#                 self.system.setBrake(abs(throttle_brake) * max_brake_force, wheel_index)

# from metadrive.envs.metadrive_env import MetaDriveEnv
# from metadrive.component.vehicle.vehicle_type import DefaultVehicle
# from metadrive.utils import generate_gif

# env=MetaDriveEnv(dict(map="S", traffic_density=0))
# frames = []
# try:
#     env.reset()
#     cfg=env.config["vehicle_config"]
#     cfg["navigation"]=None # it doesn't need navigation system
#     v = env.engine.spawn_object(DefaultVehicle, 
#                                 vehicle_config=cfg, 
#                                 position=[30,0], 
#                                 heading=0)
#     for _ in range(100):
#         v.before_step([0, 0.5])
#         env.step([0,0])
#         frame=env.render(mode="topdown", 
#                          window=True,
#                          screen_size=(800, 200),
#                          camera_position=(60, 7))
#         frames.append(frame)
#     generate_gif(frames, gif_name="demo.gif")
# finally:
#     env.close()


from IPython.display import Image
# Image(open("demo.gif", "rb").read())



# # Policy
# from metadrive.envs.metadrive_env import MetaDriveEnv
# from metadrive.utils import generate_gif

# env=MetaDriveEnv(dict(map="S",
#                       log_level=50,
#                       traffic_density=0))
# try:
#     frames = []
#     # run several episodes
#     env.reset()
#     for step in range(300):
#         # simulation
#         _,_,_,_,info = env.step([3,3])
#         frame = env.render(mode="topdown", 
#                            window=True,
#                            screen_size=(800, 200),
#                            camera_position=(60, 15))
#         frames.append(frame)
#     generate_gif(frames)
# finally:
#     env.close()

# Image(open("demo.gif", "rb").read())


# Lane  change policy 
from metadrive.envs.metadrive_env import MetaDriveEnv
from metadrive.policy.lange_change_policy import LaneChangePolicy
from metadrive.utils import generate_gif

env=MetaDriveEnv(dict(map="C",
                      discrete_action=True,
                      use_multi_discrete=True,
                      agent_policy=LaneChangePolicy,
                      log_level=50,
                      traffic_density=0))
frames=[]
try:
    # run several episodes
    env.reset()
    for step in range(300):
        # change command
        if step<90:
            steering = 1
            command = "lane keeping"
        elif step<100:
            steering = 0
            command = "right lane changing"
        elif step<140:
            steering = 1
            command = "lane keeping"
        elif step<160:
            steering = 0
            command = "right lane changing"
        elif step<200:
            steering = 2
            command = "left lane changing"
        else:
            steering = 1
            command = "lane keeping"
        # simulation
        _,_,_,_,info = env.step([steering, 3])
        frame= env.render(mode="topdown", 
                          window=True,
                          text={"command": command},
                          screen_size=(700, 900),
                          camera_position=(60,-54))
        frames.append(frame)
        if info["arrive_dest"]:
            break
    generate_gif(frames)
finally:
    env.close()

Image(open("demo.gif", "rb").read())

