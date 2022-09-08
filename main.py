#importar o app, builder (GUI)

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('tela.kv')

#Criar o aplicativo
#Criar a função build

class MeuAplicativo(App):
    def build(self):
        return GUI








