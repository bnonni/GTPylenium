# GTPylenium Testing Program | Test Automation Engineer Assessment

## Know Before You Go 
1. Python 3.7 `python3`
2. Selenium version 3.141.0
3. Chromium versions 74 to 77, and Gecko versions 0.22 to 0.25.
4. Determine browser version:
     - Open Chrome, select the menu (3 vertical dots, top right), select help, select 'About Google Chrome.'
     - Open Firefox, select the Firefox menu option, select 'About Firefox.'
5. Download and install [Google Chrome](https://www.google.com/chrome/) and [Firefox](https://www.mozilla.org/firefox/download/thanks/).
6. Download [ChromeDriver v77.0.3865.10](https://chromedriver.storage.googleapis.com/index.html?path=77.0.3865.40/) and [GeckoDriver v0.25.0](https://github.com/mozilla/geckodriver/releases/tag/v0.25.0), and place them inside the 1_BryanNonni_SeleniumTest.py folder
* Note: If you're using windows, you'll need to download the .exe drivers and place them inside the 1_BryanNonni_SeleniumTest.py and 2_BryanNonni_SeleniumTest_With_Drivers folders.
7. If using Windows, change line 1 in all programs from `#!/usr/bin/env python3` to `#!/c/Python37/python`

## Which is which?
1. [1_BryanNonni_SeleniumTest.py](./1_BryanNonni_SeleniumTest.py) contains the adapted file without drivers included.
2. [2_BryanNonni_SeleniumTest_With_Drivers](./2_BryanNonni_SeleniumTest_With_Drivers) contains the same file from the 1_BryanNonni_SeleniumTest.py folder but also includes the drivers needed to run the program for a mac. If using windows, follow step 
3. [3_BryanNonni_SeleniumTest](./3_BryanNonni_SeleniumTest) contains the originally written program that takes user inputs and adapts the test to those inputs. Also included are multiple versions of the drivers.

## Now You Know, Time to Go
### To execute the program in [1_BryanNonni_SeleniumTest.py](./1_BryanNonni_SeleniumTest.py/BryanNonni_SeleniumTest.py)
* Note: If using a windows OS, change line 1 from `#!/usr/bin/env python3` to `#!/c/Python37/python`
1. Follow steps 5, 6 and 7 from the `Know Before You Go` section, if necessary.
2. Change directories via terminal into this folder `cd 1_BryanNonni_SeleniumTest.py`
3. Execute script either using the python interpreter command `python3 BryanNonni_SeleniumTest.py` or simply using traditional bash execution `./BryanNonni_SeleniumTest.py`
4. Watch the console for test results.

### To execute the program in [2_BryanNonni_SeleniumTest_With_Drivers](./2_BryanNonni_SeleniumTest_With_Drivers/BryanNonni_SeleniumTest.py)
* Note: If using a windows OS, change line 1 from `#!/usr/bin/env python3` to `#!/c/Python37/python`
1. Follow steps 5, 6 and 7 from the `Know Before You Go` section, if necessary.
2. Change directories via terminal into this folder `cd 2_BryanNonni_SeleniumTest_With_Drivers`
3. Execute script either using the python interpreter command `python3 BryanNonni_SeleniumTest.py` or simply using traditional bash execution `./BryanNonni_SeleniumTest.py`
4. Watch the console for test results.

### To execute the program in [3_BryanNonni_SeleniumTest](./3_BryanNonni_SeleniumTest/BryanNonni_SeleniumTest)
* Note: If using a windows OS, change line 1 from `#!/usr/bin/env python3` to `#!/c/Python37/python`
1. Change directories via terminal into this folder `cd 3_BryanNonni_SeleniumTest`
1. Execute the start bash script `./start`
2. Wait for console prompts and input proper responses:
     - Select Y for headless and n for not headless.
     - Select environment OS (mac/win).
     - Select browser (chrome/firefox).
     - Select browser version (74/75/76/77) or (22/23/24/25).
3. Wait for console outputs and test results.
4. To restart test, wait for final prompt and input `Y` otherwise input `n`.
5. Upon restart, program prompts for headless/not headless, input `Y` or `n`, respectively.

### Report bugs to the [issues tab](https://github.com/bnonni/GTPylenium/issues).
