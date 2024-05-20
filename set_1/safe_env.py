""""
The syntax for safe driving is:  python -m metadrive.examples.drive_in_safe_metadrive_env

"""


# Accident Probability

# from metadrive import SafeMetaDriveEnv

# def run_env(density):
#     env=SafeMetaDriveEnv(dict(map="CCCCC", accident_prob = density, log_level=50))
#     env.reset(seed=0)
#     obj_num=len(env.engine.object_manager.spawned_objects)
#     print("There are {} traffic objects on the map with accident_prob={}".format(obj_num,density))
#     env.close()

# run_env(0.1)
# run_env(1)



# Termination and Cost

from metadrive import SafeMetaDriveEnv
from metadrive.component.static_object.traffic_object import TrafficCone
import os

try:
    env=SafeMetaDriveEnv(dict(crash_object_cost=-5, 
                              random_spawn_lane_index=False,
                              # use 3D renderer
                              use_render=not os.getenv('TEST_DOC'))) 
    env.reset(seed=0)
    cone=env.engine.spawn_object(TrafficCone, position=[20, 7], heading_theta=0)
    for _ in range(100):
        o,r,d,_,info = env.step([0, 1])
        if env.agent.crash_object:
            assert info["cost"] == -5
            break
    env.engine.clear_objects([cone.id])
finally:
    env.close()

    





