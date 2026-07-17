from game import roll_dice_and_check_win, roll_dice
import pytest


def test_win_when_roll_is_six(mocker):

    mocker.patch('game.random.randint', return_value=6)
    result = roll_dice_and_check_win()
    assert result == "You win!"


def test_lose_when_roll_is_not_6(mocker):
    mocker.patch('game.random.randint', return_value=3)

    result = roll_dice_and_check_win()
    assert result == "You lose!"


def test_lose_when_roll_is_1(mocker):
    mocker.patch('game.random.randint', return_value=1)
    result = roll_dice_and_check_win()
    assert result == "You lose!"


def test_roll_dice_calls_randnt(mocker):
    mock_randint = mocker.patch("game.random.randint")

    roll_dice()

    mock_randint.assert_called_once()
    mock_randint.assert_called_once_with(1, 6)


def test_multiple_rolls(mocker):
    mocker.patch("game.random.randint", side_effect=[3, 5, 6])

    assert roll_dice() == 3
    assert roll_dice() == 5
    assert roll_dice() == 6


def test_random_failure(mocker):

    mocker.patch("game.random.randint", side_effect=RuntimeError("error!"))

    with pytest.raises(RuntimeError, match="error!"):
        roll_dice()
