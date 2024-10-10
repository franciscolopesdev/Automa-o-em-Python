# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=925, y=470)
pyautogui.write('Bealinda@gmail.com')
pyautogui.press('tab')
pyautogui.write('chataprakrlh')
pyautogui.press('tab')
pyautogui.press('enter')


#importa dados

tabela = pd.read_csv('produtos.csv')
print(tabela)

#Primeiro click

for linha in tabela.index:
    time.sleep(4)
    # clicar no campo de código
    pyautogui.click(x=839, y=325)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    # pegar da tabela o valor do campo que a gente quer preencher
    # codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press('enter')
    pyautogui.scroll(5000)