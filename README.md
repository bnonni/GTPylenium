# Pylenium Testing Suite | Web Testing Automation

## Know Before You Go 
1. Python 3.7 `python3`
2. Selenium version 3.141.0
3. Chromium versions 74 to 77, and Gecko versions 0.22 to 0.25.
4. Determine browser version:
     - Open Chrome, select the menu (3 vertical dots, top right), select help, select 'About Google Chrome.'
     - Open Firefox, select the Firefox menu option, select 'About Firefox.'
5. Download and install [Google Chrome](https://www.google.com/chrome/) and [Firefox](https://www.mozilla.org/firefox/download/thanks/).
6. Download [ChromeDriver v77.0.3865.10](https://chromedriver.storage.googleapis.com/index.html?path=77.0.3865.40/) and [GeckoDriver v0.25.0](https://github.com/mozilla/geckodriver/releases/tag/v0.25.0), and place them inside the Pylenium.py folder
* Note: If you're using windows, you'll need to download the .exe drivers and place them inside the Pylenium.py and Pylenium_With_Drivers folders.
7. If using Windows, change line 1 in all programs from `#!/usr/bin/env python3` to `#!/c/Python37/python`

## Which is which?
1. [Pylenium.py](./Pylenium.py) contains the adapted file without drivers included.
2. [Pylenium_With_Drivers](./Pylenium_With_Drivers) contains the same file from the 1_BryanNonni_SeleniumTest.py folder but also includes the drivers needed to run the program for a mac. If using windows, follow step 6 from the `Know Before You Go` section (also pay attention to the note below step 6). 
3. [Pylenium_Full_Suite](./Pylenium_Full_Suite) contains the originally written program that takes user inputs and adapts the test to those inputs. Also included are multiple versions of the drivers.

## Now You Know, Time to Go
### To execute the program in [Pylenium.py](./Pylenium.py/Pylenium.py)
* Note: If using a windows OS, change line 1 from `#!/usr/bin/env python3` to `#!/c/Python37/python`
1. Follow steps 5, 6 and 7 from the `Know Before You Go` section, if necessary.
2. Change directories via terminal into this folder `cd Pylenium.py`
3. Execute script either using the python interpreter command `python3 Pylenium.py` or using bash execution `./Pylenium.py`
4. Watch the console for test results.

### To execute the program in [Pylenium_With_Drivers](./Pylenium_With_Drivers/Pylenium.py)
* Note: If using a windows OS, change line 1 from `#!/usr/bin/env python3` to `#!/c/Python37/python`
1. Follow steps 5, 6 and 7 from the `Know Before You Go` section, if necessary.
2. Change directories via terminal into this folder `cd Pylenium_With_Drivers`
3. Execute script either using the python interpreter command `python3 Pylenium.py` or using bash execution `./Pylenium.py`
4. Watch the console for test results.

### To execute the program in [Pylenium_Full_Suite](./Pylenium_Full_Suite/Pylenium)
* Note: If using a windows OS, change line 1 from `#!/usr/bin/env python3` to `#!/c/Python37/python`
1. Change directories via terminal into this folder `cd Pylenium_Full_Suite`
1. Execute the start bash script `./start`
2. Wait for console prompts and input proper responses:
     - Select Y for headless and n for not headless.
     - Select environment OS (mac/win).
     - Select browser (chrome/firefox).
     - Select browser version (74/75/76/77) or (22/23/24/25).
3. Wait for console outputs and test results.
4. To restart test, wait for final prompt and input `Y` otherwise input `n`.
5. Upon restart, program prompts for headless/not headless, input `Y` or `n`, respectively.

### Report bugs to the [issues tab](https://github.com/bnonni/Pylenium/issues).
