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


transition_functions = [
    TransitionFunction(0, "", 1, TapeMovement.RIGHT),
    TransitionFunction(0, "1", 1, TapeMovement.RIGHT),
    TransitionFunction(1, "", 2, "1"),
    TransitionFunction(1, "1", 1, TapeMovement.RIGHT),
    TransitionFunction(2, "", None, ""),
    TransitionFunction(2, "1", 2, TapeMovement.LEFT),
]

tfd: dict[int, dict[str, tuple[int | None, TapeMovement | str]]] = {}
for tf in transition_functions:
    if tf.from_state not in tfd:
        tfd[tf.from_state] = {}
    tfd[tf.from_state][tf.current_value] = (tf.to_state, tf.action)

tape: list[str] = ["", "1", "1", ""]
tape_index = 0
state = 0

print(tape)

while state is not None:
    to_state, action = tfd[state][tape[tape_index]]

    # print(tape)
    # print(to_state, action)
    # print()

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

print(tape)
