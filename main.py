# NoisyKey
import json
from pynput import keyboard
from playsound import playsound

# exit
from pynput.keyboard import KeyCode

EXIT_HOT_KEY = '<ctrl>+<alt>+h'
file_map = {}


def on_press(key: keyboard.KeyCode):
    if type(key) == KeyCode and key.char in [chr(x) for x in range(97, 123)]:
        print(file_map[key.char][:-3])
        playsound('./sound/' + file_map[key.char], False)


def on_release(key):
    pass
    # print('{0} released'.format(key))


def on_activate_h():
    print('bye~')
    exit(0)


# music_map : KeyCode with music file's map
def start():
    listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
    listener.start()

    with keyboard.GlobalHotKeys({
            EXIT_HOT_KEY: on_activate_h,}) as h:
        h.join()


def get_key_list():
    return "qwertyuiopasdfghjklzxcvbnm"


if __name__ == '__main__':
    print("=====================================")
    print("= NoisyKey start to run! get ready! =")
    print("=====================================")
    # key_list = get_key_list()
    # music_list = os.listdir('./sound')[0:26]
    # file_map = dict(zip(key_list, music_list))
    # json = json.dumps(file_map, indent=2)
    with open('music.json', 'r') as f:
        file_map = json.loads(f.read())
    start()
