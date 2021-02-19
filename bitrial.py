# -*- coding: utf-8 -*-
#Coded By Ashkan Rafiee https://github.com/AshkanRafiee/BitRial/
################Libraries################
import PySimpleGUI as sg
import webbrowser
import threading
import requests
import bs4
import lxml
################Libraries################

################GUI################
sg.theme('DarkGreen2')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Calculate The Bitcoin Exchange Values!')],
	  [sg.Text('Sarmaye(Rials): ', size=(25,1)),sg.Input(size=(65,1), key='rials_buy')],
          [sg.Text('Bitcoin price(Rials): ', size=(25,1)),sg.Input(size=(45,1), key='bitcoin_be_rial')],
          [sg.Text('Dollar price(Rials): ', size=(25,1)),sg.Input(size=(45,1), key='dollar_be_rial')],
          [sg.Text('Euro price(Rials): ', size=(25,1)),sg.Input(size=(45,1), key='euro_be_rial')],
          [sg.Text('Bitcoin price(Dollars): ', size=(25,1)),sg.Input(size=(45,1), key='bitcoin_be_dollar')],
          [sg.Text('Bitcoin price(Euros): ', size=(25,1)),sg.Input(size=(45,1), key='bitcoin_be_euro'), sg.Button('Get Ratio', size=(15,1))],
          [sg.Text('Satooshi', size=(25,1)), sg.Text('',key='ghsbt',size=(15,1)), sg.Text('Bitcoin'), sg.Text('',key='ghbbt',size=(15,1)), sg.Text('(Buy With rials)')],
          [sg.Text('Satooshi', size=(25,1)), sg.Text('',key='ghsbd',size=(15,1)), sg.Text('Bitcoin'), sg.Text('',key='ghbbd',size=(15,1)), sg.Text('(Buy With Dollars)')],
          [sg.Text('Satooshi', size=(25,1)), sg.Text('',key='ghsbe',size=(15,1)), sg.Text('Bitcoin'), sg.Text('',key='ghbbe',size=(15,1)), sg.Text('(Buy With Euros)')],
          [sg.Text('Bitcoin', size=(25,1)), sg.Input(size=(45,1), key='bite_man_be_rial'), sg.Text('Darayi be rial'), sg.Text('',key='bite_man',size=(10,1)) ],
          [sg.Button('Calculate', size=(45,1)), sg.Button('Website'), sg.Button('Exit'), sg.Text('Made By Ashkan Rafiee')]]
# Create the Window
window = sg.Window('Exchange Calculator - Calculate The Bitcoin Exchange Values!', layout)
# Event Loop to process "events" and get the "values" of the inputs
################GUI################

################Functions################
def get_ratio():
	#Disable Buttons
    window['Calculate'].update(disabled=True)
    window['Get Ratio'].update(disabled=True)

    #Bitcoin to Dollar & Euro
    window['bitcoin_be_dollar'].update(disabled=True)
    window['bitcoin_be_euro'].update(disabled=True)
    resp = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    mydict = resp.json()
    bitratedol = mydict['bpi']['USD']['rate']
    bitratedol = bitratedol.replace(',','')
    bitrateur = mydict['bpi']['EUR']['rate']
    bitrateur = bitrateur.replace(',','')
    window.Element('bitcoin_be_dollar').Update(value=bitratedol)
    window.Element('bitcoin_be_euro').Update(value=bitrateur)
    window['bitcoin_be_dollar'].update(disabled=False)
    window['bitcoin_be_euro'].update(disabled=False)

    #Dollar & Euro to Rials
    window['dollar_be_rial'].update(disabled=True)
    window['euro_be_rial'].update(disabled=True)
    resp = requests.get('https://www.tgju.org/')
    soup = bs4.BeautifulSoup(resp.text,'lxml')
    table = soup.select('.nf')
    dolrate = table[4].getText()
    dolrate = dolrate.replace(',','')
    eurate = table[70].getText()
    eurate = eurate.replace(',','')
    window.Element('euro_be_rial').Update(value=eurate)
    window.Element('dollar_be_rial').Update(value=dolrate)
    window['dollar_be_rial'].update(disabled=False)
    window['euro_be_rial'].update(disabled=False)

    #Bitcoin to Rials
    window['bitcoin_be_rial'].update(disabled=True)
    resp = requests.get('https://www.tgju.org/profile/crypto-bitcoin')
    soup = bs4.BeautifulSoup(resp.text,'lxml')
    table = soup.select('.text-left')
    bitratetom = table[2].getText()
    bitratetom = bitratetom.replace(',','')
    window.Element('bitcoin_be_rial').Update(value=bitratetom)
    window['bitcoin_be_rial'].update(disabled=False)
    
    #Enable Buttons
    window['Calculate'].update(disabled=False)
    window['Get Ratio'].update(disabled=False)
    

def bitget():
    #rials
    satooshi_be_rial = (bitcoin_be_rial/100000000)
    valuet = (rials_buy/satooshi_be_rial)
    valuet = int(round(valuet,0))
    bit_gett = (valuet/100000000)
    window.Element('ghsbt').Update(value=valuet)
    window.Element('ghbbt').Update(value='{0:.10f}'.format(bit_gett))
    #Dollar
    satooshi_be_dollar = (bitcoin_be_dollar/100000000)
    dollars_buy = (rials_buy/dollar_be_rial)
    valued = (dollars_buy/satooshi_be_dollar)
    valued = int(round(valued,0))
    bit_getd = (valued/100000000)
    window.Element('ghsbd').Update(value=valued)
    window.Element('ghbbd').Update(value='{0:.10f}'.format(bit_getd))
    #Euro
    satooshi_be_euro = (bitcoin_be_euro/100000000)
    euros_buy = (rials_buy/euro_be_rial)
    valuee = (euros_buy/satooshi_be_euro)
    valuee = int(round(valuee,0))
    bit_gete = (valuee/100000000)
    window.Element('ghsbe').Update(value=valuee)
    window.Element('ghbbe').Update(value='{0:.10f}'.format(bit_gete))
    #bit e man be rial
    my_bit_to_rials = round(bitcoin_be_rial*bite_man,0)
    window.Element('bite_man').Update(value=str(my_bit_to_rials))
################Functions################

################GUI Events################
while True:
    event, values = window.read()
    

    if event == 'Calculate':
        try:
            window['Calculate'].update(disabled=True)
            rials_buy = float(values['rials_buy'])
            bitcoin_be_rial = float(values['bitcoin_be_rial'])
            bitcoin_be_dollar = float(values['bitcoin_be_dollar'])
            dollar_be_rial = float(values['dollar_be_rial'])
            bitcoin_be_euro = float(values['bitcoin_be_euro'])
            euro_be_rial = float(values['euro_be_rial'])
            bite_man = float(values['bite_man_be_rial'])
            threading.Thread(target=bitget, daemon=True).start()
            window['Calculate'].update(disabled=False)
        except ValueError:
            sg.Popup('Some Values are missing or in the wrong shape!', keep_on_top=True)
            window['Calculate'].update(disabled=False)

    if event == 'Get Ratio':
        threading.Thread(target=get_ratio, daemon=True).start()

    if event == 'Website':
        webbrowser.open_new('https://ashkanrafiee.ir/exchanger')

    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
################GUI Events################
