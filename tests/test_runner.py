from unittest.mock import call, Mock

from psychopy_app.runner import runner


def test_stop_on_mouse_down_prevents_reentry():
    button = Mock()
    event = Mock()
    event.GetEventObject.return_value = button
    parent = Mock()
    ribbon = Mock()
    ribbon.GetParent.return_value = parent
    calls = Mock()
    calls.attach_mock(button, "button")
    calls.attach_mock(parent, "parent")

    runner.RunnerRibbon._stopOnMouseDown(ribbon, event)

    assert calls.mock_calls == [
        call.button.Disable(),
        call.parent.stopTask(event),
    ]
    event.Skip.assert_called_once_with()
