from textual.app import ComposeResult
from textual.widgets import Static, Digits
from textual.containers import Horizontal
from Models import Face

class ScoreBoard(Static):
	DEFAULT_CSS = '''
		ScoreBoard {
			height: 7;
    		layout: grid;
			grid-size: 3 1;
			grid-columns: 1fr 1fr 1fr;
		}

		Face {
			width: auto;
		}

		#BombsLeft {
			width: auto;
		}

		#Face {
			width: auto;
		}

		#ElapsedTime {
			width: auto;
		}

		#Container_BombsLeft {
			height: 100%;
			width: 1fr;
			border: round $border;
			align: center middle;
			border-title-align: center;
			border-title-color: $text-secondary;
		}

		#Container_StatusFace {
			height: 100%;
			width: 1fr;
			border: round $border;
			align: center middle;
			border-title-align: center;
		}

		#Container_ElapsedTime {
			height: 100%;
			width: 1fr;
			border: round $border;
			align: center middle;
			border-title-align: center;
			border-title-color: $text-secondary;
		}

	'''
	def compose(self):
		with Static(id="Container_BombsLeft") as S:
			S.border_title = "Bombs"
			yield Digits("022", id="BombsLeft")

		with Static(id="Container_StatusFace") as S:
			yield Face.Face()
			#yield Static(":)", id="Face")

		with Static(id="Container_ElapsedTime") as S:
			S.border_title = "Seconds"
			yield Digits("073", id="ElapsedTime")
	