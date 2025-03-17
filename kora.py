from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.factory import Factory
from kivy.uix.label import Label
import time
import re
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.widget import Widget
from kivy.base import runTouchApp
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor=(100 ,100 ,100 ,150/255.0)
Window.size=(400, 630)

class Doda(Screen):
   nassw = ObjectProperty()
   passw = ObjectProperty(None)
   real_name = ObjectProperty()
   my_text = StringProperty('enter your name')
   def Click(self):
        passw = self.manager.get_screen('first').passw.text
        if any(char.isdigit()for char in passw): 
           self.real_name = 'please enter your real name'
        else:
           self.real_name = 'good name!'
           with open("C:\\Users\\Lenovo ThinkPad\\data_base.text", "r", encoding='utf-8') as old_file :
            lines = old_file.read()
            user = re.findall('\d', lines)
            try: 
               user = user[-1]
            except IndexError:
               user = 0
            user = int(user) + 1
           my_file = open("C:\\Users\\Lenovo ThinkPad\\data_base.text", "a")
           text = f'\nname_user {user} is: {passw}'
           my_file.write(text)
        self.my_text = self.real_name
   def hoha(self):
       text = self.manager.get_screen('first').passw.text
       self.nassw = f'Hello {text}'

class Ba3a(Screen):
    nassw = ObjectProperty()
    def hoha(self):
       text = self.manager.get_screen('first').passw.text
       self.nassw = f'Hello {text}'
           
class calcule(Screen):
   reg = ObjectProperty('enter your note in regional')
   nat = ObjectProperty('enter your note in national')
   semestre1 = ObjectProperty('enter your note in semestre1')
   sm2 = ObjectProperty('enter your note in semstre2')
   final = ObjectProperty()
   def verfie(self):
       errors = ['', '.', '-' '+']
       try:
          not_regional = self.manager.get_screen('maths').regional.text
          note_natioanl = self.manager.get_screen('maths').national.text
          not_semestre1 = self.manager.get_screen('maths').s1.text
          not_s2 = self.manager.get_screen('maths').s2.text
       except  Exception as e:
           pass
       if not_regional in errors:
           self.reg = 'Please enter your real note in regional'
       else:
           not_regional= float(not_regional)
           if not_regional > 20 :
              self.reg = 'your note is note in interval 0 betwin 20' 
           else:
               self.reg = 'Entered'
              
           if  note_natioanl in errors:
              self.nat = 'Please enter your real note in national'
           else: 
              note_natioanl = float(note_natioanl)
              if note_natioanl > 20 :
                 self.nat =  'your note is note in interval 0 betwin 20'
              else:
                  self.nat = 'Entered'
                  if not_semestre1 in errors:
                    self.semestre1 = 'Please enter your real note in semetre1'
                  else:
                    not_semestre1 = float(not_semestre1)
                    if not_semestre1 > 20 :
                       self.semestre1 =  'your note is note in interval 0 betwin 20'
                    else:
                        self.semestre1 = 'Entered'
                        if not_s2 in errors:
                          self.sm2 = 'Please enter your real note in semetre2'
                        else:
                           not_s2 = float(not_s2)
                           if not_s2 > 20 :
                              self.sm2 = 'your note is note in interval 0 betwin 20'
                           else:
                             self.sm2 = 'Entered'
                             if self.sm2 == 'Entered' and self.semestre1 == 'Entered' and self.nat == 'Entered' and self.reg == 'Entered' :
                                result = round(not_s2 * 0.125 + not_semestre1 * 0.125 + note_natioanl * 0.5 + not_regional * 0.25, 2)
                                if result >= 10 :
                                    self.final = f'your result is ' + str(result) + ' bravo!'
                                else:
                                    self.final = f'your result is ' + str(result) + ' stay hard'
                                self.popup = Factory.ResultPopup()
                                self.popup.final = self.final
                                time.sleep(0.3)
                                self.popup.open()
                                self.ids.regional.text = ''
                                self.ids.national.text = ''
                                self.ids.s1.text = ''
                                self.ids.s2.text = ''
                                self.reg = 'enter your note in regional'
                                self.nat = 'enter your note in national'
                                self.semestre1 = 'enter your note in semestre1'
                                self.sm2 = 'enter your note in semstre2'

class ecoles(Screen):
   name_ecoles = StringProperty('not available now')
   def ecole(self):
     errors = ['', '.', '+', '-']
     nationale = self.manager.get_screen('re_input').nationale.text
     regionale = self.manager.get_screen('re_input').regionale.text
     if nationale in errors or regionale in errors :
       self.name_ecoles = 'please enter you real result, and try again'
     else:
      nationale = float(nationale)
      regionale = float(regionale)
      result_final = round(nationale * 0.75 + regionale * 0.25, 2)
      float(result_final)
      if result_final in errors :
        self.name_ecoles = ''
      if result_final < 9.99 :
        self.name_ecoles = 'your result does not allow you to join any school'
      elif 10 <= result_final <= 12 :
         self.name_ecoles = 'est, fst, ofppt, bts, IAV, ISPIS, ISTP, IFMEFREE, la fac \n \n for information: \n \n  https://youtu.be/Zj6c1ZTHm0o?si=IC6FWUErfTDlNUE84 \n  \n https://youtu.be/rP_-cLHohho?si=nU-10ipDXP-2txEo  \n'
      elif 12 < result_final <= 14 :
        self.name_ecoles = 'est, fst, ofppt, bts, IAV, ISPITS, ISTP, IFMEFREE, la fac,\n \n ensa, encg, ENS, ISPITS, ISIC, ENSC \n \n for more information: \n  https://www.9rayti.com/'
      elif 14 < result_final <= 16 :
        self.name_ecoles = 'est, fst, ofppt, bts, IAV, ISPITS, ISTP, IFMEFREE, la fac,\n \n ensa, encg, ENS, ISPITS, ISIC, ENSC, ensam,  FMP, FMD \n \n enset, ensc, ens, isic, ena, enam \n \n for more information: \n https://www.9rayti.com/ '
      elif 16 < result_final <= 18 :
        self.name_ecoles = 'est, fst, ofppt, bts, IAV, ISPITS, ISTP, IFMEFREE, la fac,\n \n ensa, encg, ENS, ISPITS, ISIC, ENSC, ensam,  FMP, FMD \n \n enset, ensc, ens, isic, ena, enam, cpge some shcolls in france \n \n for more information: \n https://www.9rayti.com/ '
      elif 18 < result_final <= 20 :
        self.name_ecoles = 'bravo! you are accepted in almost all schools'
      else:
        self.name_ecoles = 'we detected an error please enter your result result'
     self.popup = Factory.EcolesPopup()
     self.popup.name_ecoles = self.name_ecoles
     self.popup.open()
     self.ids.regionale.text = ''
     self.ids.nationale.text = ''
class cible(Screen):
   final_bomba = StringProperty('please enter you real result, and try again ')
   def bomba(self):
      errors = ['', '.', '-', '+', ' ']
      try :
         result_desired = float(self.manager.get_screen('cible').result_desired.text)
         bac1 = float(self.manager.get_screen('cible').bac1.text)
         se1 = float(self.manager.get_screen('cible').se1.text)
         se2 = float(self.manager.get_screen('cible').se2.text)
         if result_desired in errors or bac1 in errors or se1 in errors or se2 in errors :
           self.final_bomba = 'please entre your result, and try again'
      except Exception as e:
         pass
          
      else :
           somme = round(se1 + se2, 2)
           r = round(somme * 0.125 + bac1 * 0.25, 2)
           m =  round(result_desired - r, 2)
           s = round(m / 0.5, 2)
           self.final_bomba = f'you must get {s} on examan national \n to get result general {result_desired}'
      self.popup = Factory.DesiredPopup()
      self.popup.final_bomba = self.final_bomba
      self.popup.open()
      self.ids.result_desired.text = ''
      self.ids.bac1.text = ''
      self.ids.se1.text = ''
      self.ids.se2.text = ''

class Test(ScreenManager):
    pass
class Best(AnchorLayout):
    pass
class Box(BoxLayout):
    pass
class Stack(StackLayout):
    pass
class Scroll(ScrollView):
    pass
   
kv = Builder.load_file('tv.kv')
class Test(App) :
    def build(self) :
        self.title='bac'
        return kv
        return calcule()

if __name__ == '__main__' :
    Test().run()
