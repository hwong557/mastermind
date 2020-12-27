from mastermind_code import Code
import assistant

def test_constructor():
    assert Code(["blue", "green", "orange", "red"]) \
            == Code(["b", "g", "o", "r"]) \
            == Code("bgor") \
            == Code([0, 1, 2, 4]) \

round1 = [
        Code([0, 1, 2, 3], 1, 1),
        Code([1, 2, 3, 4], 0, 1),
        Code([2, 3, 4, 5], 0, 1),
        Code([3, 4, 5, 0], 0, 1),
        Code([4, 5, 0, 1], 1, 0),
        Code([5, 0, 1, 2], 2, 0),
        Code([0, 0, 0, 0], 3, 0),
        Code([1, 1, 1, 1], 0, 0),
        Code([2, 2, 2, 2], 1, 0),
        Code([3, 3, 3, 3], 0, 0),
        ]
real_code_1 = Code([0, 0, 0, 2])

# tests
round2 = [
        Code([0, 1, 2, 3], 0, 1),
        Code([1, 2, 3, 4], 1, 1),
        Code([2, 3, 4, 5], 1, 2),
        Code([3, 4, 5, 0], 1, 2),
        Code([4, 5, 0, 1], 1, 1),
        Code([5, 0, 1, 2], 0, 1),
        Code([0, 2, 4, 0], 1, 0),
        Code([1, 3, 5, 1], 0, 2),
        Code([2, 4, 0, 2], 0, 1),
        Code([4, 2, 0, 4], 1, 1),
        Code([3, 5, 4, 4], 4, 0),
        ]
real_code_2 = Code([3, 5, 4, 4])

round3 = [
        Code("bgop", 0, 2),
        Code("yggp", 0, 0),
        Code("bboo", 2, 1),
        Code("bbbb", 1, 0),
        Code("gpor", 0, 2),
        Code("orpy", 1, 1),
        Code("gyob", 0, 2),
        Code("pgrb", 1, 1),
        Code("gyor", 0, 2),
        Code("bbpr", 1, 1),
        ]
real_code_3 = Code("obro")

round4 = [
        Code("bgop", 0, 0),
        Code("yyyy", 2, 0),
        Code("yyrr", 2, 2),
        Code("ryry", 0, 4),
        Code("yryr", 4, 0),
        ]

real_code_4=Code("yryr", 4, 0)


data = [
        ( round1, real_code_1),
        ( round2, real_code_2),
        ( round3, real_code_3),
        ( round4, real_code_4),
        ]

def test_is_correct_compatible_with():
    for round, real_code in data:
        for guess in round:
            assert guess.is_correct_compatible_with(real_code)

def test_is_permute_compatible_with():
    for round, real_code in data:
        for guess in round:
            assert guess.is_permute_compatible_with(real_code)

def test_get_possible_codes():
    assert len(list(assistant.all_possible_codes(assistant.all_codes, [Code([1, 2, 3, 4], 3, 0)]))) == 4 * 5
    # In some 4th slot, the present color is wrong and should be one of the other 5 colors (6 colors total).
