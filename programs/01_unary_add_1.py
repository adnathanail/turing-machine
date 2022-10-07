from main import TransitionFunction, TapeMovement, turing_machine

transition_functions = [
    TransitionFunction(0, "", 1, TapeMovement.RIGHT),
    TransitionFunction(0, "1", 1, TapeMovement.RIGHT),
    TransitionFunction(1, "", 2, "1"),
    TransitionFunction(1, "1", 1, TapeMovement.RIGHT),
    TransitionFunction(2, "", None, ""),
    TransitionFunction(2, "1", 2, TapeMovement.LEFT),
]
tape: list[str] = ["", "1", "1", ""]
print(tape)
print(turing_machine(transition_functions, tape))
