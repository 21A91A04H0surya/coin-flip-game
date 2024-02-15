import random
import time
from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    alert("Choose Head or Tails")

    # Any code you write here will run before the form opens.
  def choose_change(self, **event_args):
    my_change=self.choose_change.selected_value
  
  def button_1_click(self, **event_args):
  
    self.image_1.source = None
    coins = ['http://re-bol.com/heads.jpg','http://re-bol.com/tails.jpg'] 
    coin = random.choice(coins)
    time.sleep(1)
    self.image_1.source = URLMedia(coin)
    time.sleep(1)
    if coin==coins[0] and self.choose_change.selected_value=='Heads':   
      alert("You Won")
    elif coin==coins[1] and self.choose_change.selected_value=='Tails':
      alert("You Won")
    else:
      alert("You Lost")