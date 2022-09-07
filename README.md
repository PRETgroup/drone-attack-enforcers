# Drone Simulator with Attack Enforcers
For the development of drone simulation with attacker modelling using runtime enforcers.

# Setup
Requirements:
* Python (it is expected that you have an understanding of python too)
* ArduPilot
* Dronekit

Note: this was all done on a Windows 10 PC

## MAVLink and AdruPilot
_[ArduPilot](https://github.com/ardupilot/ardupilot) is the most advanced, full-featured, and reliable open source autopilot software available._ (Quote from the ArduPilot project repo)

We will be using ArduPilot Copter. [Wiki link.](https://ardupilot.org/copter/index.html)

Follow these [instructions to setup ArduPilot.](https://ardupilot.org/dev/docs/SITL-setup-landingpage.html).

I installed on Windows 10, _it was a hassle, I do not recommend._ The [provided powershell script](https://github.com/ArduPilot/ardupilot/tree/master/Tools/environment_install/install-prereqs-windows.ps1) was what got it running in the end. **Running random scripts people tell you to is always bad.** Read it first, it isn't long.

Then I needed to:
* Clone ArduPilot repo 
    * ```git clone https://github.com/ardupilot/ardupilot```
* (Must be Cygwin from here) Update and clone dependencies
    * ```git submodule update --init --recursive```
* Navigate to ardupilot/ArduCopter directory.
* Run ```../Tools/autotest/sim_vehicle.py --map --console```
    * At first this complained about some missing python dependencies. Install these ```pip install XYZ```
    * Eventually it started this huge build which took quite a while
    * Once complete, the quad-copter simulator opened up
<!--
* Navigate to the ArduCopter directory
    * ```cd ArduCopter```
* Required python package empy (maybe others too, this was the only one I was missing)
    * ```pip install empy```
* Required installation of [MAVProxy](https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html) manually too
    * Lots of python dependencies, check here [MAVProxy: Download and Installation](https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html)
    * Clone ```git clone https://github.com/ArduPilot/MAVProxy.git```
    * Build/install ```python setup.py build install --user```
* Required something to create XWindows Displays (so you can use a GUI from WSL)
    * VcXsrv was suggested in ArduoPilot docs [here](https://ardupilot.org/dev/docs/building-setup-windows10.html#building-setup-windows10)
    * I found a built binary [here](https://github.com/ArcticaProject/vcxsrv). Note some differences
    * Once installed, run xlaunch.exe to configure... you should only need to change "Disable access control" which is on the third page
    * Then run vcxsrv.exe
* Run the ArduPilot SITL (Software in the loop) 
    * ```../Tools/autotest/sim_vehicle.py -console -map```
    * _this will take 15-20 min the first time as it builds everything..._ -->

## Dronekit
_[Dronekit-Python](https://github.com/dronekit/dronekit-python) helps you create powerful apps for UAVs._ (Quote from the ArduPilot project repo)

* Can be installed with ```pip install dronekit```
    * I needed to install ```wheel``` first ```pip install wheel``` (there was an ungraceful fail without it)

In our context it is used to communicate with MAVLink and ArduCopter and abstracts a level of detail away for us.

# Examples
## Simple take off and land (tests your simulator!)
1. Open Cygwin terminal. Navigate to ardupilot/ArduCopter directory.
2. Run ```../Tools/autotest/sim_vehicle.py --map --console```
3. Open CMD. Navigate to the directory of this repo.
4. Run ```python dronekit/missions/simple-test.py```
5. Watch as dronekit controls the simulated drone through a simple take off and land!

## Take off and land with base station
_Very similar behaviour to the above take off and land but with much more control via simulation of asynch comms._
1. Open Cygwin terminal. Navigate to ardupilot/ArduCopter directory.
2. Run ```../Tools/autotest/sim_vehicle.py --map --console```
3. Open CMD. Navigate to the directory of this repo.3. Run ```python test-base-TOAL.py```
    * Base station (```test-base-TOAL.py```) communicates with on drone controller (```missions/take_off_and_land.py```) which interacts via dronekit with the drone. 

# Enforcer Attacks 
Placed between the environment (drone) and controller (base station) the attack enforcers can execute a number of attacks.

![Attack enforcer placed between environment and controller](/images/enf-attack.png)

Policies in this work are defined as Timed Automata and synthesised into enforcers using [easy-rte](https://github.com/PRETgroup/easy-rte). Below is an example of an injection attack which inserts the **ABORT** signal after a specified time (T *subscript* A).

![Policy describing an injection attack (of the abort signal)](/images/abort-attack.png)

To demonstrate attack enforcers and the attack manager see the below examples. 

## Examples: Drone Attack Enforcers
*Commands assume you have the simulator running*
* Mission: take off and land - ```python test-base-TOAL.py```
* Mission: fly from A to B - ```python test-base-A2B.py```
* Mission: fly from A to B to A -```python test-base-A2B2A.py```

# Enforcer Interchange
Adds an attack manager to perform enforcer interchange, which dynamically enables and disables (through the use of activate signals) appropriate enforcers to perform more complex attacks.

![Attack manager policy for drones example with three missions](/images/RI-Manager.png)

## Example: Drone Attack Manager 
Uses enforcer interchange to dynamically enable appropriate attack enforcers across a mission that combines the three examples above. 

* Combined Missions: all of the above - ```python test-base-combined.py``` - *Assumes you have the simulator running*

The policy below illustrates the attack manager policy for the three basic drone attacks used earlier.

![Attack manager policy for drones example with three missions](/images/ei-policy.png)

