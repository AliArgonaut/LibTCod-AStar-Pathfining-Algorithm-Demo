from typing import Optional
import tcod.event
import actions

class EventHandler(tcod.event.EventDispatch[actions.Action]):

    def ev_quit(self, event: tcod.event.Quit) -> Optional[actions.Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[actions.Action]:
        action: Optional[actions.Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = actions.MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = actions.MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = actions.MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = actions.MovementAction(dx=1, dy=0)
        
        elif key == tcod.event.K_ESCAPE:
            action = actions.EscapeAction
        
        return action

