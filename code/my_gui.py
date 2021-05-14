import PySimpleGUI as sg
import code


def my_gui():
    '''
        Function to execute program user interface.
    '''

    sg.theme("LightGreen")

    # Create layout for our window
    layout = [
                [
                sg.In(default_text='Modelo', size=(25,1), enable_events=True, key="-MODEL-"),
                    sg.FilesBrowse(button_text='Buscar'),
                ],

                [
                    sg.In(default_text='Dados', size=(25,1), enable_events=True, key="-DATA-"),
                    sg.FilesBrowse(button_text='Buscar'),
             ],

                [
                    sg.Button("Preencher"),
                ]
         ]

    # Instatiate window

    window = sg.Window("Substituidor de Tags", layout)

    # GUI loop event

    while True:
        event, values = window.read()

        if event == "Preencher":
            model_path = values["-MODEL-"]
            data_path = values["-DATA-"]

            if model_path == '' or data_path == '':
                sg.popup_error("Por favor, preencha os campos obrigatórios!", title="Erro!")
            else:
                repeat_model, index_data = code.process_files(model_path, data_path)

                subs = code.substitute_tags(repeat_model, index_data)

                code.save_as_xlsx(subs, data_path)

                sg.popup_ok("Finalizado com sucesso!", title="Sucesso!", auto_close=True ,auto_close_duration=5)


        if event == sg.WIN_CLOSED:
            break

    window.close()
