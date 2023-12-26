import pandas as pd

from app.pipeline.transform import contact_data_frame

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def testar_a_concatenacao_da_lista_de_dataframe():
    """use o arrange act e assert para testar a função contact_data_frame"""

    # arrange
    data_frame_list = [df_1, df_2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    # act
    df = contact_data_frame(data_frame_list)

    # assert
    assert df.shape == (4, 2)     # O corpo do dataframe é igual (4,2)
    assert data_frame.equals(df)   # Um data fica igual o outro
    assert df.shape != (5, 2)
