from textual import on
from enum import Enum
from textual.app import ComposeResult
from textual.widgets import Static
from textual.message import Message

class BlockCharacterTypes(Enum):
	Covered					= 1						# Blocks that are still UnRevealed
	Uncovered				= 2						# Blocks that are Revealed
	Marked					= 3

class BlockTypes(Enum):
	Safe					= 1						# This Block is a BOMB
	Bomb					= 2						# This Block is SAFE

class Block(Static):
	'''
		The Base-Block Class for Blocks that appear on the board
		Events:
			Click						The User Clicked the Block
	'''

	DEFAULT_CSS = '''
		Block { 
			width:  5;
			height: 3;
        	text-align: center;		
			background: #E0E0E0;
			color: black;
		}

	'''

	def __init__(self, *args,  CoveredChr:str = "?", UncoveredChr: str = "!", **kwargs) -> None:
		self._Uncovered					: bool		= False
		self.CoveredCharacter			: str		= CoveredChr				# "?" = Calculate Number based on number of adjacent bombs
		self.UnCoveredCharacter			: str		= UncoveredChr
		self.MarkedCharacter			: str		= r"\?"						# \? = ?, the "\" is an escape chr
		self.Adjacent_Bomb_Count		: int		= 0							# Number of Adjacent Bombs
		self.X							: int		= -1						# X Location of the Block
		self.Y							: int		= -1						# Y Location of the Block
		self.Marked						: bool		= False						# True when the Player Marks this tile as a bomb
		super().__init__(self.Get_Current_Character(), *args, **kwargs)

	class Click(Message):
		'''		The Message Class for Bubbling/Raising Click Events		'''
		def __init__(self, Control:"Block") -> None:
			super().__init__()
			self.Control = Control
			
	def on_click(self, event: Click) -> None:
		'''			Called when the User Clicks a Tile		'''
		self.Raise_Click()

	def Raise_Click(self):
		'''
			Raises a Click Message.
		'''
		Msg:Block.Click = Block.Click(Control=self)
		Msg.control
		self.post_message(message=Msg)

	@property
	def Uncovered(self) -> bool:
		return self._Uncovered


	@Uncovered.setter
	def Uncovered(self, Value: bool):
		self._Uncovered = Value
		self.update(self.Get_Current_Character(), layout=False)		# Layout won't change, always the same size


	def Get_Character(self, Which: BlockCharacterTypes) -> str:
		'''		Returns the Character to Represent this Block		'''
		match Which:
			case BlockCharacterTypes.Covered:
				return self.CoveredCharacter
			case BlockCharacterTypes.Uncovered:
				return self.UnCoveredCharacter
			case BlockCharacterTypes.Marked:
				return self.MarkedCharacter
			
		return "X"

	def Get_Current_Character(self) -> str:
		'''
			Returns the Current Character for the Block
			Rules:	If self.Marked, return self.MarkedCharacter
					Otherwise, return self.CoveredCharacter or self.UncoveredCharacter, dependent on
			   		self._Uncovered
			
		'''
		Which:BlockCharacterTypes = (BlockCharacterTypes.Marked if self.Marked  else (BlockCharacterTypes.Uncovered if self._Uncovered else BlockCharacterTypes.Covered))

		Chr: str = self.Get_Character(Which=Which)

		if Chr == "?":
			return str(self.Adjacent_Bomb_Count)

		if Chr == r"\?":
			return "?"
		
		return Chr

	def render(self):
		return self.Get_Current_Character()


class Block_Bomb(Block):
	DEFAULT_CSS = '''
		Block_Bomb {
        	text-align: center;
        	content-align: center middle;
			background: #C00000;
		}
	'''
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, CoveredChr = "?", UncoveredChr = "*", **kwargs)



class Block_Safe(Block):
	DEFAULT_CSS = '''
		Block_Safe {
        	text-align: center;		
        	content-align: center middle;

		}
	'''
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, CoveredChr = "?", UncoveredChr = "*", **kwargs)

