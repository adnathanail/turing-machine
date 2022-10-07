from main import TransitionFunction, TapeMovement, turing_machine

transition_functions = [
    TransitionFunction(0, "", 1, TapeMovement.RIGHT),
    TransitionFunction(1, "1", 1, TapeMovement.RIGHT),
    TransitionFunction(1, "*", 2, "1"),
    TransitionFunction(2, "1", 2, TapeMovement.RIGHT),
    TransitionFunction(2, "", 3, TapeMovement.LEFT),
    TransitionFunction(3, "1", 3, ""),
    TransitionFunction(3, "", 4, TapeMovement.RIGHT),
    TransitionFunction(4, "1", 4, TapeMovement.LEFT),
    TransitionFunction(4, "", None, ""),
]
tape: list[str] = ["", "1", "1", "*", "1", "1", "1"]
print(tape)
print(turing_machine(transition_functions, tape))
