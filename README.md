# GTPylenium Testing Program | Test Automation Engineer Assessment

## Know Before You Go 
* Python 3.7 `python3`
* Selenium version 3.141.0
* Chromium versions 74 to 77, and Gecko versions 0.22 to 0.25.
* Determine browser version:
     - Open Chrome, select the menu (3 vertical dots, top right), select help, select 'About Google Chrome.'
     - Open Firefox, select the Firefox menu option, select 'About Firefox.'

## Which is which?
1. [1_BryanNonni_SeleniumTest.py](./1_BryanNonni_SeleniumTest.py) contains the adapted file without drivers included.
2. [2_BryanNonni_SeleniumTest_With_Drivers](./2_BryanNonni_SeleniumTest_With_Drivers) contains the same file from the 1_BryanNonni_SeleniumTest.py folder but also includes the drivers needed to run the program.
3. [3_BryanNonni_SeleniumTest](./3_BryanNonni_SeleniumTest) contains the originally written program that takes user inputs and adapts the test to those inputs. Also included are multiple versions of the drivers.

## Now You Know, Time to Go
### To execute the program in [1_BryanNonni_SeleniumTest.py](./1_BryanNonni_SeleniumTest.py/BryanNonni_SeleniumTest.py)
1. Change directories via terminal into this folder `cd 1_BryanNonni_SeleniumTest.py`
2. Execute script either using the python interpreter command `python3 BryanNonni_SeleniumTest.py` or simply using traditional bash execution `./BryanNonni_SeleniumTest.py`
3. Watch the console for test results.

### To execute the program in [2_BryanNonni_SeleniumTest_With_Drivers](./2_BryanNonni_SeleniumTest_With_Drivers/BryanNonni_SeleniumTest.py)
1. Change directories via terminal into this folder `cd 2_BryanNonni_SeleniumTest_With_Drivers`
2. Execute script either using the python interpreter command `python3 BryanNonni_SeleniumTest.py` or simply using traditional bash execution `./BryanNonni_SeleniumTest.py`
3. Watch the console for test results.

### To execute the program in [3_BryanNonni_SeleniumTest](./3_BryanNonni_SeleniumTest/BryanNonni_SeleniumTest)
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

### Report bugs to the [issues tab](https://github.com/bnonni/GTPylenium/issues)
