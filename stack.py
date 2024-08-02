import os
import subprocess
import platform
import time
import shutil


# things

cmds = ['help','ping', 'clear', 'cd', 'rd', 'rmdir', 'del', 'run', 'color', 'copy', 'move', 'mkdir', 'md', 'rename', 'ren', 'shutdown', 'reboot', 'exit']
programs = {'Discord': {'id': 'ds', 'path': 'C:\\Users\\nalart11\\AppData\\Local\\Discord\\app-1.0.9152\\Discord.exe'},
            'Telegram': {'id': 'tg', 'path': 'C:\\Users\\nalart11\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe'},
            'Chrome': {'id': 'chr', 'path': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'},
            'Steam': {'id': 'st', 'path': 'C:\\Program Files (x86)\\Steam\\steam.exe'},
            'Modrinth': {'id': 'mr', 'path': 'C:\\Program Files\\Modrinth App\\Modrinth App.exe'},
            'HoYoPlay': {'id': 'hyp', 'path': 'C:\\Program Files\\HoYoPlay\\launcher.exe'},
            'Nekoray': {'id': 'nr', 'path': 'D:\\nekoray\\nekoray.exe'},
            'VS Code': {'id': 'vsc', 'path': 'C:\\Users\\nalart11\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'},
            'Smpl': {'id': 'smpl', 'path': 'C:\\Users\\nalart11\\Documents\\Smpl\\dist\\Smpl.exe'},
            'Taskmgr': {'id': 'tsm', 'path': 'C:\\WINDOWS\\system32\\Taskmgr.exe'},
            'Explorer': {'id': 'ex', 'path': 'C:\\Windows\\explorer.exe'}
            }
stack = ['STACK', 'Stack', 'stack', 'st']
folder = ['']
fld = ''
path = ['C:\\']
fldc = 'C:'
current_color = ''
colors = {
    '0': {"code": "\033[30m", "name": "Black"},
    '1': {"code": "\033[34m", "name": "Blue"},
    '2': {"code": "\033[32m", "name": "Green"},
    '3': {"code": "\033[36m", "name": "Cyan"},
    '4': {"code": "\033[31m", "name": "Red"},
    '5': {"code": "\033[35m", "name": "Magenta"},
    '6': {"code": "\033[33m", "name": "Yellow"},
    '7': {"code": "\033[37m", "name": "White"},
    '8': {"code": "\033[90m", "name": "Bright Black"},
    '9': {"code": "\033[94m", "name": "Bright Blue"},
    'a': {"code": "\033[92m", "name": "Bright Green"},
    'b': {"code": "\033[96m", "name": "Bright Cyan"},
    'c': {"code": "\033[91m", "name": "Bright Red"},
    'd': {"code": "\033[95m", "name": "Bright Magenta"},
    'e': {"code": "\033[93m", "name": "Bright Yellow"},
    'f': {"code": "\033[97m", "name": "Bright White"},
    'reset': {"code": "\033[0m", "name": "Reset"}
}

# help function

def help(cmd):
    global cmds
    commands = {
        'clear': ('Clears screen contents.', 'Usage: clear'),
        'ping': ('Tests the connection to the specified IP address.', 'Usage: ping <ip>'),
        'cd': ('Changes the current directory.', 'Usage: cd <directory>'),
        'rmdir': ('Removing a directory', 'Usage: rmdir <directory> or rd <directory>'),
        'rd': ('Removing a directory', 'Usage: rmdir <directory> or rd <directory>'),
        'del': ('Deleting one or more files.', 'Usage: del <file>'),
        'run': ('Launch a file or application.', 'Usage: run <file> or run <application>'),
        'color': ('Set default colors for text in the console.', 'Usage: color <code>'),
        'copy': ('Copy one or more files to another location.', 'Usage: copy <source> <destination>'),
        'move': ('Moving folder files.', 'Usage: move <source> <destination>'),
        'mkdir': ('Creating directory', 'Usage: mkdir <directory> or md <directory>'),
        'md': ('Creating directory', 'Usage: mkdir <directory> or md <directory>'),
        'rename': ('Renaming file or folder.', 'Usage: rename <source> <result> or ren <source> <result>'),
        'ren': ('Renaming file or folder.', 'Usage: rename <source> <result> or ren <source> <result>'),
        'shutdown': ('Shutdown system.', 'Usage: shutdown'),
        'reboot': ('Reboot system.', 'Usage: reboot'),
        'exit': ('Exit from Stack.', 'Usage: exit')
    }

    if cmd in commands:
        description, usage = commands[cmd]
        print(description)
        print('')
        print(usage)
    elif cmd is None:
        print('Commands list:')
        print('')
        for command, (description, usage) in commands.items():
            print(f'STACK\\{fld}:> {command}')
            print(description)
            print('')
            print(usage)
            print('')
    else:
        print(f'STACK\\{fld}:> Wrong usage. Try again.')


# main functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ping(host):
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', host]
    print(f'STACK\\{fld}:> ping...')
    return subprocess.run(command, stdout=subprocess.PIPE).returncode == 0

def cd(f):
    global path, folder, fld, fldc
    if os.path.exists(fldc + '\\' + f) or f in path or f in stack:
        if f in path:
            index = path.index(f)
            path = path[:index + 1]
        elif f in stack:
            path = path[:1]
        else:
            path.append(f)
    else:
        print(f'STACK\\{fld}:> Path does not exists.')

    folder = path[1:]
    fld = '\\'.join(folder)
    fldc = '\\'.join(path)

def rmdir(f):
    global fldc
    try:
        full_path = os.path.join(fldc, f)
        if os.path.exists(full_path):
            folder_name = os.path.basename(f)
            shutil.rmtree(full_path)
            print(f'STACK\\{fld}:> Folder "{folder_name}" successfully deleted.')
        else:
            print(f'STACK\\{fld}:> Folder "{f}" does not exists.')
    except PermissionError as e:
        print(f'STACK\\{fld}:> Permission error: {e}. Cannot delete folder "{f}".')
    except Exception as e:
        print(f'STACK\\{fld}:> Error: {e}. Cannot delete folder "{f}".')

def delete(f):
    global fldc
    try:
        full_path = os.path.join(fldc, f)
        if os.path.exists(full_path):
            file_name = os.path.basename(f)
            os.remove(full_path)
            print(f'STACK\\{fld}:> File "{file_name}" successfully deleted.')
        else:
            print(f'STACK\\{fld}:> File "{f}" does not exist.')
    except PermissionError as e:
        print(f'STACK\\{fld}:> Permission error: {e}. Cannot delete file "{f}".')
    except Exception as e:
        print(f'STACK\\{fld}:> Error: {e}. Cannot delete file "{f}".')

def run(p):
    global fldc, programs
    try:
        full_path = os.path.join(fldc, p)
        if p in programs:
            os.startfile(programs[p]['path'])
            print(f'STACK\\{fld}:> Running "{p}"')
        elif os.path.exists(full_path):
            os.startfile(full_path)
            print(f'STACK\\{fld}:> Running "{p}"')
        else:
            print(f'STACK\\{fld}:> File "{p}" does not exist.')
    except PermissionError as e:
        print(f'STACK\\{fld}:> Permission error: {e}. Cannot open file "{p}".')
    except Exception as e:
        print(f'STACK\\{fld}:> Error: {e}. Cannot open file "{p}".')

def color(c):
    global current_color, colors
    if c in colors:
        current_color = colors[c]["code"]
        color_name = colors[c]["name"]
        print(f'{current_color}STACK\\{fld}:> Color changed to {color_name}')
    else:
        print(f'STACK\\{fld}:> Invalid color code')

def copy(f):
    global fldc
    try:
        doppo = f.split(' ')
        if len(doppo) != 2:
            print(f'STACK\\{fld}:> Invalid input. Usage: copy <source> <destination>')
            return

        source_path = os.path.join(fldc, doppo[0])
        dest_path = os.path.join(fldc, doppo[1])

        if not os.path.exists(source_path):
            print(f'STACK\\{fld}:> Source "{doppo[0]}" does not exist.')
            return

        if os.path.isdir(dest_path):
            dest_path = os.path.join(dest_path, os.path.basename(source_path))

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f'STACK\\{fld}:> File "{doppo[0]}" successfully copied to "{doppo[1]}".')
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path)
            print(f'STACK\\{fld}:> Folder "{doppo[0]}" successfully copied to "{doppo[1]}".')
        else:
            print(f'STACK\\{fld}:> "{doppo[0]}" is neither a file nor a folder.')

    except shutil.Error as e:
        print(f'STACK\\{fld}:> Error during copy: {e}')
    except Exception as e:
        print(f'STACK\\{fld}:> Unexpected error: {e}')

def move(f):
    global fldc
    try:
        doppo = f.split(' ')
        if len(doppo) != 2:
            print(f'STACK\\{fld}:> Invalid input. Usage: moved <source> <destination>')
            return

        source_path = os.path.join(fldc, doppo[0])
        dest_path = os.path.join(fldc, doppo[1])

        if not os.path.exists(source_path):
            print(f'STACK\\{fld}:> Source "{doppo[0]}" does not exist.')
            return

        if os.path.isdir(dest_path):
            dest_path = os.path.join(dest_path, os.path.basename(source_path))

        if os.path.isfile(source_path):
            shutil.move(source_path, dest_path)
            print(f'STACK\\{fld}:> File "{doppo[0]}" successfully moved to "{doppo[1]}".')
        elif os.path.isdir(source_path):
            shutil.move(source_path, dest_path)
            print(f'STACK\\{fld}:> Folder "{doppo[0]}" successfully moved to "{doppo[1]}".')
        else:
            print(f'STACK\\{fld}:> "{doppo[0]}" is neither a file nor a folder.')

    except shutil.Error as e:
        print(f'STACK\\{fld}:> Error during copy: {e}')
    except Exception as e:
        print(f'STACK\\{fld}:> Unexpected error: {e}')

def shutdown():
    if os.name == 'nt':
        os.system("shutdown /s /t 0")
    else:
        os.system("shutdown now")

def reboot():
    if os.name == 'nt':
        os.system("shutdown /r /t 0")
    else:
        os.system("reboot")

def mkdir(f):
    global fldc
    full_path = os.path.join(fldc, f)
    if os.path.exists(full_path):
        print(f'STACK\\{fld}:> Folder "{f}" exists.')
    else:
        folder_name = os.path.basename(f)
        os.mkdir(full_path)
        print(f'STACK\\{fld}:> Folder "{folder_name}" successfully created.')

def rename(f):
    global fldc
    doppo = f.split(' ')
    if len(doppo) != 2:
        print(f'STACK\\{fld}:> Invalid input. Usage: moved <source> <destination>')
        return

    source_path = os.path.join(fldc, doppo[0])
    dest_path = os.path.join(fldc, doppo[1])

    source_index = source_path.rfind('\\')
    dest_index = dest_path.rfind('\\')

    sp = source_path[:source_index]
    dp = dest_path[:dest_index]

    if not os.path.exists(source_path):
            print(f'STACK\\{fld}:> File "{doppo[0]}" does not exist.')
            return
    
    if sp == dp:
        os.rename(source_path, dest_path)
        print(f'STACK\\{fld}:> {source_path[dest_index+1:]} succesfully renamed to {dest_path[dest_index+1:]}.')


# working on


# other functions

def print_with_delay(characters, delay=0.25):
    for char in characters:
        print(char, flush=True)
        time.sleep(delay)
        time.sleep(delay)

def clean_up():
    print(f'{colors["reset"]["code"]}Bye!')


# visualisation

# WELCOME to STACK!

'''
message1 = "WELCOME "
message2 = "to "
message3 = "STACK!\n"
message4 = "first python-based terminal\n"

clear()

print_with_delay(message1)
print_with_delay(message2, delay=0.00)
time.sleep(1.00)
print_with_delay(message3, delay=0.00)
time.sleep(1.00)
print(message4, ='', flush=True)
time.sleep(1.00)
'''

# terminalself

while True:
    print(f'STACK\\{fld}:> ', end = '')
    user_input = input()
    
    if not user_input:
        print(f'No command entered. Try again.')
        continue

    parts = user_input.split(' ', 1)
    cmd = parts[0]
    atr = parts[1] if len(parts) > 1 else None


    if cmd in cmds:
        if cmd == 'help':
            if atr:
                help(atr)
            else:
                help(None)
        elif cmd == 'clear':
            clear()
        elif cmd == 'ping':
            if atr:
                result = ping(atr)
                if result:
                    print(f'STACK\\{fld}:> Successfully pinged {atr}')
                else:
                    print(f'STACK\\{fld}:> Failed to ping {atr}')
            else:
                print(f'STACK\\{fld}:> No IP address entered for ping. Try again.')
        elif cmd == 'cd':
            if atr:
                cd(atr)
            else:
                print(f'STACK\\{fld}:> No path entered. Try again.')
        elif cmd == 'rmdir' or cmd == 'rd':
            if atr:
                rmdir(atr)
            else:
                print(f'STACK\\{fld}:> No directory entered. Try again.')
        elif cmd == 'del':
            if atr:
                delete(atr)
            else:
                print(f'STACK\\{fld}:> No file path entered. Try again.')
        elif cmd == 'run':
            if atr:
                run(atr)
            else:
                print(f'STACK\\{fld}:> No file name entered. Try again.')
        elif cmd == 'color':
            if atr:
                color(atr)
            else:
                print(f'STACK\\{fld}:> No color entered. Try again.')
        elif cmd == 'copy':
            if atr:
                copy(atr)
            else:
                print(f'STACK\\{fld}:> No file path entered. Try again.')
        elif cmd == 'move':
            if atr:
                move(atr)
            else:
                print(f'STACK\\{fld}:> No file path entered. Try again.')
        elif cmd == 'mkdir' or cmd in 'md':
            if atr:
                mkdir(atr)
            else:
                print(f'STACK\\{fld}:> No folder path entered. Try again.')
        elif cmd == 'rename' or cmd == 'ren':
            if atr:
                rename(atr)
            else:
                print(f'STACK\\{fld}:> No folder or file path entered. Try again.')
        elif cmd == 'shutdown':
            shutdown()
        elif cmd == 'reboot':
            reboot()
        elif cmd == 'exit':
            clean_up()
            break
    else:
        print(f'STACK\\{fld}:> Wrong command. Try again.')