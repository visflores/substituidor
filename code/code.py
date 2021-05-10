__version__ = '0.2.0'

import pandas as pd
import re

def process_files(model, data):
    '''
        Function to process models and data.
    '''

    data = pd.read_csv(data, sep=',')

    data_index = data.to_dict('index')

    repeat_models = list()
    with open(model, 'r') as models:
        repeat_models.append(models.read())

    return repeat_models * len(data_index), data_index

def substitute_tags(repeat_model, index_data):
    '''
        Change tags from models
    '''

    filled_model = list()

    for model, index in zip(repeat_model, index_data):
        keys = index_data[index]
        to_change = model

        for key in keys:
            if model.find('<' + key + '>'):
                to_change = re.sub('<'+key+'>', keys[key], to_change)

        filled_model.append(to_change)

    return filled_model

def save_as_txt(filled_model):
    '''
        Save a list into a file
    '''
    with open('model_filled.txt', 'w') as save_model:
        save_model.writelines(filled + '\n\n' for filled in filled_model)


def save_as_xlsx(filled_model, data_path):
    '''
        Save a csv with our filled models
    '''
    df = pd.read_csv(data_path, sep=',')

    df['modelos'] = filled_model

    df.to_excel('filled_models.xlsx', index=False, engine='openpyxl')

if __name__ == '__main__':
    repeat_model, index_data = process_files('../data/modelo.txt', '../data/informacoes.csv')

    subs = substitute_tags(repeat_model, index_data)

    save_as_xlsx(subs, '../data/informacoes.csv')
