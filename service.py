import requests
from cryptography.fernet import Fernet


WEB_APP_URL = "http://127.0.0.1:5000/"


def encrypt(key, data):
    '''
        Function to encrypt data and transform the encrypted elements from byte type to str.
    :param path_to_key: Path to file where the key is contained;
    :param data: Data about user that should be encrypted;
    :return: Returns the encrypted data in json format;
    '''

    f = Fernet(key)

    for idx_key, key in enumerate(data.keys()):
        new_data = [f.encrypt(element.encode('ascii')) for element in data[key]]
        data[key] = [str(element.decode("utf-8")) for element in new_data]

    return data

def send_user_info(data):
    
    requests.post(WEB_APP_URL, json=data)# .__dict__)

def send_user_info_to_server(name, last_name, email, speed):
    user_info = {
        'user_name': name,
        'last_name': last_name,
        'email': email,
        'speed': str(speed)
    }

    key = 'VUVgU6Hjr3OfYIjuihLymn1nuWxNOBkp498AjOu--DA='
    encrypted_info = encrypt(key, user_info)

    res = requests.post(WEB_APP_URL, json=encrypted_info)

    return res.ok 


#send_user_info()
# send_user_info({'user_name': ['gAAAAABh4vAVDi_iM0J4nVlVi9csANf4N7i_dMOb-5Uale6rLd25bSmBSmUZTzbSRUQWCz2cntz1Ogr4NhjNGndyz8QymzDNSQ==', 'gAAAAABh4vAVD9rPPe2QVL1fZWVuQ8ovB0UwAQuKRiiTNiWeOrs7CwN5HxNRVZVDs7bF5XNcItkJaFMEPhsvoZV00ugmyWR7UA==', 'gAAAAABh4vAVtelj-dQDuFQMzM0X9OVMjPMETmleTwl6YKs4ZM-7vTkYm0cZo58ndPNOhWZlzSfQ5veQkpdppFLNMJ1nRyUhSQ==', 'gAAAAABh4vAVNR6NI79JBG-ehSEXwoIS_npZz6kTn798v5r8ZbKsBObK-eWhQQHhCS3xRaWjeb9tK7XK1cF8i5Rao7jzre9QAg=='], 'last_name': ['gAAAAABh4vAVOIydF8AjOoTud2HUY6z8Pty7Eu1J1Xwvx6xxHz41bVbQLxdQZqos3cgLL20BdqT-mTNHGGQtMly7cc20hLx1aQ==', 'gAAAAABh4vAV6rd4LRwNwKFrgvYfZbnPSENXMF35XBw4hXSwDEpdtToSN-xNNSMinUKEjO7dCqGD2pWxrAdP1RLZX90HdUvN6A==', 'gAAAAABh4vAV91JzpWxsKAqHOpEqBCsuHlboR4oHwXtqf9iEqlLcRIB1CM2cDoBPZM8FmLHVa2j-BXmEVqLuVSGj2IvSH0bahg==', 'gAAAAABh4vAVYlD186Zt1eRKTG6GuMYaeQJtjAIaZIfALQr5g7D_dA6hz8bbkJb5sEX8BoVhyflopWW9Sq3kyAciirk9PFOZTQ==', 'gAAAAABh4vAVNF_wHggZDxt2nvmIA3Hn_rKJm04NWc_LqQUeYv7ypSu6QodW5w_-RtexTBgUYB03fT_aMdHLyP-awQ73Vj6uBg==', 'gAAAAABh4vAVFI7D2paiSxepUrsDdELpshwVRXHTlTIxz-f3wnIZMak76VymduJL64GLk2O5xWTDX0oa-SyPCM8CGTrZzqQkMg=='], 'email': ['gAAAAABh4vAVfBmEGzHXnsMU0FZVHZRIuxzPI4TUUlPkPPMJ2X95waEE4JBZlDZUAQPLOaH_el9csCShAxHRye_FKHInsZlLRg==', 'gAAAAABh4vAVK_h8n_QJff4DG4-OTKQu8tdZjlvkxdKdVZYkNzOUCGxCqcTxNqlMGSHDx3r9puU-x2smZqKQzHytptqW8SjQ8g==', 'gAAAAABh4vAVjnNc_cyzJPyArqJv2HhN_dAAaD6WZn8TawVo7aKNGd8-jf58_Zo_NbvNKL0jrifsi4CaqQbk4sgCmhtv1QVLyQ==', 'gAAAAABh4vAVaWHJ8IPbppwF_P3_9NcfimJKn8OZcemeXWKDn2tnS1JsEOaCAo2FkqaDuQJQwulT0iKjheeZCc3hb3qBMNVFVQ==', 'gAAAAABh4vAVopCutrV2WzZhGeaQ5lvBiVnPa2DLLmtvhvfnZINnceLAPdtHy3_qXdHEM61nuAEWNrnVckWLMkpBmLZfbPoNiw==', 'gAAAAABh4vAVcib3Ed__v_t_IPKbnEIgPWhpFcRDR27mnB2-a036kNfkcPctqiP4FDdbQrS45lcsQ05irtoQWUGwRziDni054g==', 'gAAAAABh4vAVhw-vH8vWOmHsx2qgyhyLbttI0hwACWW_6kVyVBtgvP-zJL17gBwC2hCuEeqPGfCDJNnUdjDNUeZ7a0-EKGQg5Q==', 'gAAAAABh4vAV54kpxTZWvArm4h56DO2zmmax3IGzNOl4g2dZarZzvi7rPMLFiywj75E7HB7ue8v2mXlpvIPXqFZy9Tsc5vjd5A==', 'gAAAAABh4vAVbfk0Xsif2H3CwoCqrxhYqqRQjmOmImM07cObEVVr36ZogrP7q6vwVjyiwVXsHc0GfW-67ku6Vt67O2Bo3Vto3A==', 'gAAAAABh4vAV6BN1FkSoATkbh9q_5qdtRlsknthzC6aG6pTBMAqjkT5Bstd4DNbYjSomMpStdffhyV7rbswIL4ivxoqwYJVjng==', 'gAAAAABh4vAVD8PCvD9oJ_rDWdkdBwXaqa4jmKQyltzZqORRkLTBRCK9nYvUXgtpqBUDWEoam2zFUzyIrkmzyW3BUCOwoKPajw==', 'gAAAAABh4vAVPUrCoWcBJSk9CF-OX1enEtxyh4QF2BOIiQgeR4lny20INwfoWmjYy64cvmtmcGJLZqoI8IjpVIZw3r-0yhJoeQ==', 'gAAAAABh4vAVq-DSZWeH1doQSVG6PEaw51hHhLveiA7wY6WRkpZlih8vzpsZlwsEigi1JBlRZ9-ZCS4UmUUTya8lGbT-GpOJhw==', 'gAAAAABh4vAVO75Ka5skMu3n481ArtN6qfmtECDM58P_aoBCOzw_63kik-Sh0T5bfv-q8WqhwHiPILwaTw8w7GYzss5W3FeACA==', 'gAAAAABh4vAVoRJQQub8TXwSPX2kgrCFU42mk7gcrgX0NUpE2wZlJUsNvlV8Snd6wZRQHWdkR0mwF9Of_zHSXXM1hGqHoNPuKA==', 'gAAAAABh4vAVv5aZO7KB_xZmUS4S5FYDo84eVn_F-TW1aFrxqhWIsSYi6G8m3LpsmSKcOzvRsBjAACdNcczZHfQOJXFLV9nneA==', 'gAAAAABh4vAVJ5dtJcM38TeL2Cf9gCdmhpc9-5LFQ0f8d9TneGMAThpYe--nZaaHGk0WaTUYSu0WYyvYXBiP2T6rLkUma_2qnw==', 'gAAAAABh4vAVXG6V9MFGbMHNMl65CC8ldZDpjMLK1qX6SVBEuBHeSZGWGYQWdawopOqWNsetJuYq4Icb2CUrX5jr5o-EdY7W1Q=='], 'speed': ['gAAAAABh4vAVL1ouyQmxdUEFEuFUQ3J6NenNWXy_CouwgmZ7ad7KOx-ca6sJqbshykXyWLDabXNG_nNN-geUuat9CC3mFFLpCg==', 'gAAAAABh4vAVYn0-a-ujp9UnOeYOkeC4sLqyZHN6Gfs_oLjw1l4ydrnK5sMVQb0fi00_uLLfRRRuOVa6UfN6klEB5xSta_OqOA==', 'gAAAAABh4vAVpD-XkUCjpDrTvMMV0MziPXOyEk3MKlSp2eDYBtiLdl5PrZTyVbUPbP2N39F2xWDGUi9nQoxWl3d1vPrGRgZ7Ww==']})