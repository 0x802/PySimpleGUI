import PySimpleGUI as sg
import wikipedia

sg.change_look_and_feel('Reds')

def main_window():
    layout = [[sg.Text('wikipedia', justification='center', font=('Helvetica', '16'))],
        [sg.ML("", size=(40, 100), key='-text_ml1-', disabled=False), sg.Col(
            [
                [sg.Text('Search', background_color=sg.DEFAULT_BACKGROUND_COLOR, size=(10, 1))],
                [sg.In(key="-input1-", text_color="grey20")], [sg.Submit('OK'), sg.Exit()],
                [sg.Listbox([], size=(20, 50), key='-listbox1-', no_scrollbar=True)]
            ]
        )],
        [sg.)]
    ]
    window = sg.Window('wikipedia', layout=layout,font=('Helvetica', '13'), size=(700,700))
    return window

def wiki_get(data):
    search = wikipedia.search(data)
    try:
        get =  wikipedia.summary(data)
        return [get,search]
    except Exception as e:
        return [None,search]
    
def main():
    window = main_window()
    while True:
        a, v = window.Read()
        if a in (None, "Exit"):
            break
        else:
            get = wiki_get(v['-input1-'])
            if get[0] == None:
                sg.PopupError("Sorry Not Foind")
                window['-text_ml1-'].Update('')
                window['-input1-'].Update('')
                window['-listbox1-'].Update(get[1])
                continue
            else:
                window['-text_ml1-'].Update(get[0])
                window['-listbox1-'].Update(get[1])
                continue
                
    window.close()

if __name__ == "__main__":
    main()
