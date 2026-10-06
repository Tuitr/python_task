from problems.jump_game_55 import canJump


def test_can_reach_end():
    assert canJump([2, 3, 1, 1, 4]) is True


def test_stuck_on_zero():
    assert canJump([3, 2, 1, 0, 4]) is False


def test_single_element():
    assert canJump([0]) is True