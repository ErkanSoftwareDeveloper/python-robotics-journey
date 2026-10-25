
import math
import time
from pathlib import Path

import mujoco
import mujoco.viewer

model_path = Path(__file__).with_name("robot.xml")

model = mujoco.MjModel.from_xml_path(str(model_path))
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:

    with viewer.lock():
        viewer.cam.distance = 2.0
        viewer.cam.lookat[:] = [0.15, 0, 0.2]

    while viewer.is_running():

        start = time.time()

        data.ctrl[0] = math.sin(data.time) * 0.8

        mujoco.mj_step(model, data)

        viewer.sync()

        time.sleep(max(0, model.opt.timestep - (time.time() - start)))
