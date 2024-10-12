# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.click import Click
from openapi_server.models.double_click import DoubleClick
from openapi_server.models.execute import Execute
from openapi_server.models.getcontent import Getcontent
from openapi_server.models.input import Input
from openapi_server.models.jsclick import Jsclick
from openapi_server.models.loop_times import LoopTimes
from openapi_server.models.pause import Pause
from openapi_server.models.scroll import Scroll
from openapi_server.models.send_keys import SendKeys
from openapi_server.models.submit import Submit
from openapi_server.models.wait_not_visible import WaitNotVisible
from openapi_server.models.wait_visible import WaitVisible
from openapi_server import util


class Action(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ignore_if_not_present: bool=None, selector: str=None, value: str=None, skip_last_iteration: bool=None, wait_delay: str=None, script: str=None, actions: List[Action]=[], times: int=None, scroll_by_pixels: float=None, scrolling_element_selector: str=None):
        """Action - a model defined in OpenAPI

        :param ignore_if_not_present: The ignore_if_not_present of this Action.
        :param selector: The selector of this Action.
        :param value: The value of this Action.
        :param skip_last_iteration: The skip_last_iteration of this Action.
        :param wait_delay: The wait_delay of this Action.
        :param script: The script of this Action.
        :param actions: The actions of this Action.
        :param times: The times of this Action.
        :param scroll_by_pixels: The scroll_by_pixels of this Action.
        :param scrolling_element_selector: The scrolling_element_selector of this Action.
        """
        self.openapi_types = {
            'ignore_if_not_present': bool,
            'selector': str,
            'value': str,
            'skip_last_iteration': bool,
            'wait_delay': str,
            'script': str,
            'actions': List[Action],
            'times': int,
            'scroll_by_pixels': float,
            'scrolling_element_selector': str
        }

        self.attribute_map = {
            'ignore_if_not_present': 'ignoreIfNotPresent',
            'selector': 'selector',
            'value': 'value',
            'skip_last_iteration': 'skipLastIteration',
            'wait_delay': 'waitDelay',
            'script': 'script',
            'actions': 'actions',
            'times': 'times',
            'scroll_by_pixels': 'scrollByPixels',
            'scrolling_element_selector': 'scrollingElementSelector'
        }

        self._ignore_if_not_present = ignore_if_not_present
        self._selector = selector
        self._value = value
        self._skip_last_iteration = skip_last_iteration
        self._wait_delay = wait_delay
        self._script = script
        self._actions = actions
        self._times = times
        self._scroll_by_pixels = scroll_by_pixels
        self._scrolling_element_selector = scrolling_element_selector

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Action':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The action of this Action.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ignore_if_not_present(self):
        """Gets the ignore_if_not_present of this Action.

        This optional parameter is useful when the target element occasionally may not be present in the DOM.

        :return: The ignore_if_not_present of this Action.
        :rtype: bool
        """
        return self._ignore_if_not_present

    @ignore_if_not_present.setter
    def ignore_if_not_present(self, ignore_if_not_present):
        """Sets the ignore_if_not_present of this Action.

        This optional parameter is useful when the target element occasionally may not be present in the DOM.

        :param ignore_if_not_present: The ignore_if_not_present of this Action.
        :type ignore_if_not_present: bool
        """

        self._ignore_if_not_present = ignore_if_not_present

    @property
    def selector(self):
        """Gets the selector of this Action.

        Some websites require clicking 'More' button while scrolling a page. Put here 'More' button valid CSS Selector.

        :return: The selector of this Action.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this Action.

        Some websites require clicking 'More' button while scrolling a page. Put here 'More' button valid CSS Selector.

        :param selector: The selector of this Action.
        :type selector: str
        """

        self._selector = selector

    @property
    def value(self):
        """Gets the value of this Action.

        Sequence of keys to send. Keys can include keystrokes such as ALT+A, ENTER, BACKSPACE, etc.

        :return: The value of this Action.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Action.

        Sequence of keys to send. Keys can include keystrokes such as ALT+A, ENTER, BACKSPACE, etc.

        :param value: The value of this Action.
        :type value: str
        """

        self._value = value

    @property
    def skip_last_iteration(self):
        """Gets the skip_last_iteration of this Action.

        It is only used for loop actions only. Skips the last iteration.

        :return: The skip_last_iteration of this Action.
        :rtype: bool
        """
        return self._skip_last_iteration

    @skip_last_iteration.setter
    def skip_last_iteration(self, skip_last_iteration):
        """Sets the skip_last_iteration of this Action.

        It is only used for loop actions only. Skips the last iteration.

        :param skip_last_iteration: The skip_last_iteration of this Action.
        :type skip_last_iteration: bool
        """

        self._skip_last_iteration = skip_last_iteration

    @property
    def wait_delay(self):
        """Gets the wait_delay of this Action.

        Wait time (in milliseconds).

        :return: The wait_delay of this Action.
        :rtype: str
        """
        return self._wait_delay

    @wait_delay.setter
    def wait_delay(self, wait_delay):
        """Sets the wait_delay of this Action.

        Wait time (in milliseconds).

        :param wait_delay: The wait_delay of this Action.
        :type wait_delay: str
        """

        self._wait_delay = wait_delay

    @property
    def script(self):
        """Gets the script of this Action.

        The JavaScript snippet to run

        :return: The script of this Action.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Action.

        The JavaScript snippet to run

        :param script: The script of this Action.
        :type script: str
        """

        self._script = script

    @property
    def actions(self):
        """Gets the actions of this Action.

        list of actions combined in the loop are executed step-by-step

        :return: The actions of this Action.
        :rtype: List[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Action.

        list of actions combined in the loop are executed step-by-step

        :param actions: The actions of this Action.
        :type actions: List[Action]
        """

        self._actions = actions

    @property
    def times(self):
        """Gets the times of this Action.

        The number of times to scroll down a web page.

        :return: The times of this Action.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this Action.

        The number of times to scroll down a web page.

        :param times: The times of this Action.
        :type times: int
        """

        self._times = times

    @property
    def scroll_by_pixels(self):
        """Gets the scroll_by_pixels of this Action.

        Scrolls a web page by the number of pixels specified by 'scrollByPixels' parameter.

        :return: The scroll_by_pixels of this Action.
        :rtype: float
        """
        return self._scroll_by_pixels

    @scroll_by_pixels.setter
    def scroll_by_pixels(self, scroll_by_pixels):
        """Sets the scroll_by_pixels of this Action.

        Scrolls a web page by the number of pixels specified by 'scrollByPixels' parameter.

        :param scroll_by_pixels: The scroll_by_pixels of this Action.
        :type scroll_by_pixels: float
        """

        self._scroll_by_pixels = scroll_by_pixels

    @property
    def scrolling_element_selector(self):
        """Gets the scrolling_element_selector of this Action.

        Optionally specify here a valid CSS Selector of scrolling element.

        :return: The scrolling_element_selector of this Action.
        :rtype: str
        """
        return self._scrolling_element_selector

    @scrolling_element_selector.setter
    def scrolling_element_selector(self, scrolling_element_selector):
        """Sets the scrolling_element_selector of this Action.

        Optionally specify here a valid CSS Selector of scrolling element.

        :param scrolling_element_selector: The scrolling_element_selector of this Action.
        :type scrolling_element_selector: str
        """

        self._scrolling_element_selector = scrolling_element_selector
