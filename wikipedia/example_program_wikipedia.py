import PySimpleGUI as sg
import wikipedia

# look all window style
sg.change_look_and_feel('Reds')

def main_window():
    layout = \
    [
        # text title
        [sg.Text('wikipedia', justification='center', font=('Helvetica', '16'))],
        # Multiline the Output details
        [sg.ML("", size=(40, 100), key='-text_ml1-', disabled=False), sg.Col(
            [
                # Label
                [sg.Text('Search', background_color=sg.DEFAULT_BACKGROUND_COLOR, size=(10, 1))],
                # Input for search
                [sg.In(key="-input1-", text_color="grey20")],
                # Button Submit and exit
                [sg.Submit('OK'), sg.Exit()],
                # List Boxs for ==> like Did you mean these are wholesale 
                [sg.Listbox([], size=(20, 50), key='-listbox1-', no_scrollbar=True)]
            ]
        )],
    ]
    # window main
    window = sg.Window('wikipedia', layout=layout,font=('Helvetica', '13'), size=(700,700))
    return window

def wiki_get(data):
    # search for this data 
    search = wikipedia.search(data)
    try:
        # get details the target
        get =  wikipedia.summary(data)
        return [get,search]
    except Exception as e:
        return [None,search]
    
def main():
    window = main_window()
    while True:
        # run window and read the outbot
        a, v = window.Read()
        if a in (None, "Exit"):
            break
        else:
            # get data outpot wikipedia
            get = wiki_get(v['-input1-'])
            # if not find data target
            if get[0] == None:
                sg.PopupError("Sorry Not Foind")
                window['-text_ml1-'].Update('') # delete Multiline data in input
                window['-input1-'].Update('') # delete any data in input
                window['-listbox1-'].Update(get[1]) # put searchs words in list box 
                continue
            else:
                # if found data target
                window['-text_ml1-'].Update(get[0]) # put data in Multiline
                window['-listbox1-'].Update(get[1]) # put searchs words in list box 
                continue
        
    window.close()

if __name__ == "__main__":
    main()
