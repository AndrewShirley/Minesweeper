from textual.widgets import Static, Button
#from textual.containers import Horizontal

class GameButtons(Static):

	DEFAULT_CSS = '''
		GameButtons {
			layout: horizontal
		}


	'''


	def compose(self):
		#with Horizontal():
		yield Button("SAVE", id="Button_Save")
		yield Button("LOAD", id="Button_Load")
		yield Button("NEW", id="Button_NewGame")