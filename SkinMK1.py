from _Framework.Skin import Skin
from .ColorsMK1 import Rgb
from _Framework.ButtonElement import Color

class Colors:
	
	class DefaultButton:
		On = Rgb.GREEN
		Off = Rgb.GREEN_THIRD
		Disabled = Rgb.BLACK

	class Mode: #mode buttons colour
		class Session:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Note:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Drum:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Device:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class StepSequencer:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class StepSequencer2:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class User:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class User2:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class Mixer:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
	
	class Session:
		#scene
		SceneTriggered = Rgb.AMBER_BLINK
		Scene = Rgb.AMBER_THIRD
		NoScene = Rgb.BLACK
		#clip states
		ClipStarted = Rgb.GREEN
		ClipStopped = Rgb.AMBER
		ClipRecording = Rgb.RED
		ClipEmpty = Rgb.BLACK
		#trigs
		ClipTriggeredPlay = Rgb.GREEN_BLINK
		ClipTriggeredRecord = Rgb.RED_BLINK
		RecordButton = Rgb.RED_THIRD
		#stop button
		StopClip = Rgb.RED
		StopClipTriggered = Rgb.RED_BLINK
		#Enabled = Rgb.GREEN
		#Off = Rgb.GREEN_THIRD

	class Zooming:#session zoomin
		Selected = Rgb.AMBER
		Stopped = Rgb.RED
		Playing = Rgb.GREEN
		Empty = Rgb.BLACK

	class Mixer:
		class Arm:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Solo:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Mute:
			On = Rgb.AMBER_THIRD
			Off = Rgb.AMBER
		class Stop:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Selected:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Volume:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class VolumeSlider:
			On = Rgb.GREEN
			Off = Rgb.BLACK
		class Pan:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class PanSlider:
			On = Rgb.GREEN
			Off = Rgb.BLACK
		class Sends:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class SendsSlider:
			On = Rgb.AMBER
			Off = Rgb.BLACK

	class Sends:#not used yet on legacy launchpad
		A = Rgb.RED
		AAvail = Rgb.RED_THIRD
		B = Rgb.RED
		BAvail = Rgb.RED_THIRD
		C = Rgb.RED
		CAvail = Rgb.RED_THIRD
		D = Rgb.RED
		DAvail = Rgb.RED_THIRD
		E = Rgb.RED
		EAvail = Rgb.RED_THIRD
		F = Rgb.RED
		FAvail = Rgb.RED_THIRD
		G = Rgb.RED
		GAvail = Rgb.RED_THIRD
		H = Rgb.RED
		HAvail = Rgb.RED_THIRD

	class Device:#device mode colours
		class Bank:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class Lock:
			Empty = Rgb.AMBER_THIRD
			Set = Rgb.RED_THIRD
			Locked = Rgb.RED
		class Slider:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class PrecisionSlider:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Enum:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class BigEnum:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Toggle:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
	
	class StepSequencer:
		class Scale:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Octave:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Mute:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Mode:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Lock:
			class ToTrack:
				On = Rgb.RED
				Off =  Rgb.RED_THIRD
			class ToClip:
				On =  Rgb.AMBER
				Off = Rgb.AMBER_THIRD
		class LoopSelector:
			SelectedPlaying = Rgb.RED
			Playing = Rgb.RED_THIRD
			Selected = Rgb.GREEN
			InLoop = Rgb.AMBER_THIRD
		class Quantization:
			One=Rgb.BLACK
			Two=Rgb.GREEN_HALF
			Three=Rgb.GREEN_THIRD
			Four=Rgb.GREEN
		class NoteSelector:
			class Octave:
				On = Rgb.GREEN
				Off = Rgb.GREEN_THIRD
			Selected = Rgb.AMBER
			Playing = Rgb.RED
		class NoteEditor:
			class VelocityShifted:
				On = Rgb.AMBER
				Off = Rgb.AMBER_THIRD
			Velocity0 = Rgb.GREEN_THIRD
			Velocity1 = Rgb.GREEN_HALF
			Velocity2 = Rgb.GREEN
			Velocity3 = Rgb.GREEN_THIRD
			Muted = Rgb.RED_THIRD
			Playing = Rgb.RED
			Metronome = Rgb.AMBER
			NoteMarker = Rgb.AMBER
			PageMarker = Rgb.AMBER_THIRD
				
	class StepSequencer2:
		class Pitch:
			On = Rgb.GREEN
			Dim = Rgb.GREEN_THIRD
			Off = Rgb.BLACK
		class Octave:
			On = Rgb.RED
			Dim = Rgb.RED_THIRD
			Off = Rgb.BLACK
		class Velocity:
			On = Rgb.AMBER
			Dim = Rgb.AMBER_THIRD
			Off = Rgb.BLACK
		class Length:
			On = Rgb.AMBER
			Dim = Rgb.AMBER_THIRD
			Off = Rgb.BLACK
		class Random:
			On = Rgb.RED
			Off = Rgb.RED
		class NoteEditor:
			MetronomeInPage = Rgb.AMBER
			MetronomeInOtherPage = Rgb.AMBER_THIRD
			PlayInPage = Rgb.RED
			PlayInOtherPage = Rgb.RED_THIRD
			
	class Recording:
		On = Rgb.RED
		Off = Rgb.RED_THIRD
		Transition = Rgb.RED_BLINK
		
	class TrackController:
		class Recording:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class ImplicitRecording:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Play:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Stop:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Mute:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Undo:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Solo:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
				
	class DrumGroup:
		PadEmpty = Rgb.BLACK
		PadFilled = Rgb.GREEN_THIRD
		PadSelected = Rgb.GREEN
		PadSelectedNotSoloed = Rgb.AMBER
		PadMuted = Rgb.AMBER
		PadMutedSelected = Rgb.AMBER
		PadSoloed = Rgb.AMBER
		PadSoloedSelected = Rgb.AMBER
		PadInvisible = Rgb.BLACK
		PadAction = Rgb.RED
		class Mute:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Solo:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
			
	class Note:
		FeedbackRecord = Rgb.RED
		Feedback = Rgb.AMBER
		class Octave:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class Scale:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Pads:
			Root = Rgb.AMBER_THIRD
			InScale = Rgb.GREEN_THIRD
			Highlight = Rgb.GREEN
			OutOfScale = Rgb.BLACK
			Invalid = Rgb.BLACK
					
	class Scale:#scale edition
		class AbsoluteRoot:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Mode:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Key:		
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		CircleOfFifths = Rgb.RED
		RelativeScale = Rgb.RED
		class Octave:
			On = Rgb.RED
			Off = Rgb.RED_THIRD
		class Modus:
			On = Rgb.GREEN
			Off = Rgb.GREEN_THIRD
		class QuickScale:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		
	class QuickScale:#quick scale on top of instrument mode
		class Modus:
			On = Rgb.AMBER
			Off = Rgb.AMBER_THIRD
		class Major: # quick scale while in major mode
			class Key:
				On = Rgb.AMBER
				Off = Rgb.AMBER_THIRD
			CircleOfFifths = Rgb.RED
			RelativeScale = Rgb.RED
			Mode = Rgb.GREEN
		class Minor:
			class Key:
				On = Rgb.RED
				Off = Rgb.RED_THIRD
			CircleOfFifths = Rgb.AMBER
			RelativeScale = Rgb.AMBER
			Mode = Rgb.GREEN
		class Other:
			class Key:
				On = Rgb.GREEN
				Off = Rgb.GREEN_THIRD
			CircleOfFifths = Rgb.RED
			RelativeScale = Rgb.RED
			Mode = Rgb.GREEN
		

def make_skin():
	return Skin(Colors)