# gpbb-anna
General-purpose bot boilerplate "Anna" (to honor Basshunter's track "Boten Anna") is a boilerplate (or bare minimum) for a web browser bot. This script is compatible with Gecko driver (Mozilla Firefox).


### Overview
The stript is divided into four main sections:
**Essential libraries** include all libraries required by the boilerplate. It would help if you didn't modify them. Instead, you can provide additional libraries in the _Bot body_ sections.

**Framework's functions** contain all functions necessary to run a bot (with additional configuration). You can modify functions' behavior in a config file.

**Bot body** is where your code goes. It contains three default (and necessary!) scripts: loading the config file, preparing the environment, and running a browser. It is strongly recommended not to modify those actions and write bot tasks below them.

**Config file** - a stand-alone json file - contains basic and default settings. You can modify the config file according to your needs.

### Installing Gecko driver with bash:
1. Download the last release from: `https://github.com/mozilla/geckodriver/releases`
2. Unpack the file and, if necessary, move it according to your needs
3. Export patch in terminal: `export PATH=$PATH:/path/to/geckodriver/folder`