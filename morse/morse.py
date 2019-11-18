import PySimpleGUI as sg

sg.change_look_and_feel('DarkBlue')

# English To Morse 
string_to_mors = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', ',': '--..--', '1': '.----', '.': '.-.-.-', '2': '..---', '?': '..--..', '3': '...--', ';': '-.-.-.', '4': '....-', ':': '---...', '5': '.....', "'": '.----.', '6': '-....', '-': '-....-', '7': '--...', '/': '-..-.', '8': '---..', '(': '-.--.-', '9': '----.', ')': '-.--.-', '_': '..--.-', ' ': ' ',    }

# Morse To English 
morse_to_string = { m:o for o, m in string_to_mors.items()}


       
# Encode To Mores Code 
def encode(*args, **kwargs):
    some = str()
    text = args[0]

    for tap in text.split():
        for string in tap:
            try:some += ' ' + string_to_mors[string]
            except: return None
                
        if tap[-1] == string:
            some += '  '

    return some

# Decode To English Language  
def decode(*args, **kwargs):
    some = str()    
    morses = args[0]

    for morse in morses.split():
        try:some += morse_to_string[morse] + ' '
        except:return None

    return some

# Run audio
def go_play(text):
    try:
        from playsound import playsound
    except ImportError or Exception:
        return

    for Play in text.split():
            try:
                playsound(f'./ogg/{morse_to_string[Play]}.mp3')
            except Exception as e:
                continue

def main_window():
    layout =\
    [
        [sg.Text(" "*20+"Input"),sg.Text(" "*45+"Output") ],
        [sg.Multiline( size=(25, 10), key='-in-', do_not_clear=False,enter_submits=True, text_color="white"),sg.Text(">>"), sg.Output(size=(25, 10), key='-out-',text_color="white")],
        [sg.Text(" "* 30), sg.Col(
                [
                    [sg.Combo(('Encrypt', 'Decrypt'), size=(10, 1),text_color="black",readonly=True, key='-deOren-'),sg.CBox('Play', default=False, key='-play-')],
                    [sg.Text(" ")],
                    [sg.Text(" "* 3), sg.Submit('OK', size=(3, 1)), sg.Submit('Clear')],
                    [sg.Text(" "*10),sg.Exit()]
                ]
            )
        ]
        
    ]
    
    return layout

def main():
    window = sg.Window('wikipedia', layout=main_window(), font=('Helvetica', '13'), size=(600,400))
    en = str()
    de = str()

    while True:

        a, b = window.read()

        data = b['-in-'].replace("\n", ' ')
        
        if a in (None, 'Exit'):
            break

        elif a in (None, 'Clear'):
            window['-out-'].Update('')
            continue

        ########### encode #############
        if b['-deOren-'] == 'Encrypt':
            en = encode(data)
            if en == None:
                sg.PopupError("Error For Encoding")
            else:
                b['-in-'].rstrip()
                print(en)

                if b['-play-'] == True:
                    go_play(en)
            
        ########### decode #############
        elif b['-deOren-'] == 'Decrypt':
            de = decode(data)
            if de == None:
                sg.PopupError("Error For Decoding")
            else:
                b['-in-'].rstrip()
                print(de)

                if b['-play-'] == True:
                    go_play(data)
        
if __name__ == "__main__":
    main()
