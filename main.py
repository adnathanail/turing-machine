from dataclasses import dataclass
from enum import Enum


class TapeMovement(Enum):
    LEFT = 0
    RIGHT = 1


@dataclass
class TransitionFunction:
    from_state: int
    current_value: str
    to_state: int | None
    action: TapeMovement | str


def turing_machine(transition_functions: list[TransitionFunction], tape: list[str]) -> list[str]:
    tfd: dict[int, dict[str, tuple[int | None, TapeMovement | str]]] = {}
    for tf in transition_functions:
        if tf.from_state not in tfd:
            tfd[tf.from_state] = {}
        tfd[tf.from_state][tf.current_value] = (tf.to_state, tf.action)

    tape_index = 0
    state = 0

    while state is not None:
        to_state, action = tfd[state][tape[tape_index]]

        if type(action) == str:
            tape[tape_index] = action
        elif action == TapeMovement.LEFT:
            tape_index -= 1
        elif action == TapeMovement.RIGHT:
            tape_index += 1
            if tape_index == len(tape):
                tape.append("")
        else:
            raise Exception("Invalid action")

        state = to_state

    return tape
