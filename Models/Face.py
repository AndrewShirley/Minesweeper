from textual.widgets import Static
from textual.reactive import reactive
from enum import Enum

class Face(Static):



    class FaceTypes(Enum):
        Happy               = 1
        Sad                 = 2
        Angry               = 3

    Faces:dict = {
        FaceTypes.Happy: "HAPPY HAPPY\nJOY JOY"
    }

    FaceStyle           : reactive[FaceTypes] = reactive(FaceTypes.Happy)           # This changes the displayed Face Style



    def render(self):
        return self.Faces[self.FaceStyle]
