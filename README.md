# Party Pooper
## A Bluetooth Control Script for All your BT-DoS needs.

This is a Python Toolkit with a set of functions for controlling Bluetooth devices on a Linux system. 
It allows the user to scan for (annoying) nearby devices, perform "L2Ping of Death" tests, 
and also allows to send thousands of beacons to connect to BT devices via RFCOMM. 
It is your perfect sidekick when neighbours keep playing "Despacito" ad finitum during Sunday mornings!

## Requirements

- Python 3.x
- xterm command-line terminal emulator
- hcitool command-line tool for Bluetooth device scanning
- l2ping command-line tool for Bluetooth device testing
- rfcomm command-line tool for Bluetooth device connection

## Usage

- Open a terminal window and navigate to the directory containing the Party-Pooper.py script.
- Run the script by typing python3 Party-Pooper.py and pressing Enter.
- The script will display a menu with the following options:


                
   	        ░ ░░..░░..░ ░.░ .░ ░.░ .░.░..░░ .░ .░.░░░░░..░ ░.░ ░░░░..░ ░.░ .░ ░░..░ ░░.
		   ░░░..░ ░.░ _________________________________________________________.░  ░░ ░..░ 
		   ░..░ ░ ░ .|.....................................................    | ░░.░░..   
		   ...░  .░  |       .........................................         | ..░.,.  . 
		   ░..░ ░    |   0          0               ╓N            o      0     |  ░░. ░ .░ 
		      .    ░░|                              ▓≡wφ╩        o             |░░░.. .    
		  . ~.. ░.. ░|                            ▓▀µ        .                 |░.  ░-  ░░ 
		   ░ ░  .. . |               O          ▄▒▒▒▓                          |  ].  -    
		   :░.  :.. ¬|        o                ▓▓▓╫▒╫µ           .     0       |░-   ,  ░\ 
		      .      |                        ▓▓▒▒▒▒▒▒▓         .  .           |:  .░░.    
		   ░. ░░ .:  |           o         ▓▓▓▒▒╫▒▒▓╫▒╫▓▓▓                     |  .    . ░ 
		  ░..░ ░.░ .░|                 ▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▒▓▓▓▒µ                  | . : ░ ░.  
		   .░ .:..░¬░|     o              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              O      |  ░░ ░░    
		    ░.  ...  |          0       J▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▓▓▓          o         |   ░.. ░ ░ 
		  ░ . .   -. |                 ▓▓▀    ▓▓▓▓▓▓▓      ▓                   |  . ░. ░░: 
		     ░ .░.░ ░|     o           ▓▓ ▄███  ▓▓▓▓▌ ████ █                   |.. ...  .  
		  ...  .  ░ .|                ▓▓▓ █   █ █▓▓▓▌ █  ▓ ▓▓▄        o        |░░░░░..░ ░ 
		    .. ░  ░~░|                ▓▓▓   ▀  ▄▓▓▓▓▓  ▀   ▓▓▓▌                |  -   .░░  
		  .     :░..░|             ╓▄▄▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╖      O      |: ~~    .. 
		   :..   ░   |           ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▒▓▓▓▓▓▓▓▓▓▓▓▓µ            |.  .░ :  ░ 
		  ░░. . ░  : |           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            |░  .░░. ░  
		   ~....     |           ╨▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╛            |░.:.░.   . 
		    . ..░.░ .|              ╙▀▀▀▀▀▀▀▀╙╨╙╙╙╙╨▀╙╙╙╨╨╨▀▀╨╙└               | . ░ ..░░░ 
		   ...░  .░: |          P A R T Y     ------      P O O P E R          |..░.,.: .. 
		  ░░: ░.░░ ░:|      _____________________________________________      |:.░:░    . 
		     .. ░ ░ .|                                                         |░.░ . ...  
		  :.   .░ : :|            ...Let*s  Make this Party... over.           |   .: ¬░:. 
		    .   . ..░|_________________________________________________________|░ ░...░:░: 
    
				--- Scan for nearby devices
				--- L2Ping of Death
				--- RFCOMM Beacon Flood
				--- Quit

-Select an option by typing the corresponding number and pressing Enter.

-Follow the prompts to enter any required information, such as a Bluetooth device address.
-An xterm window will be launched to run the selected command. The user must manually close the window to return to the script menu.

## Limitations

- This script assumes that the Bluetooth service is already running on the system. If it is not running, the user must start it manually before running the script.
- This script does not include any error handling or error messages. If any of the subprocess commands fail, they will simply fail silently.
- This script has only been tested on Linux systems with the xterm, hcitool, l2ping, and rfcomm commands installed. It may not work on other systems or configurations.

## Disclaimer
- Attack devices without prior consentment is ugly, rude and also illegal, also, is probable that the use of this tool will prevent people to invte you to parties, 
  and most of the times leads to your (ex) friends to described you as "bad vibes".
- Tool designed for Educatonal purposes, do not complain if you suddenly discover yourself alone and without any friends (in case you had).
