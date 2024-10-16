# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MatchScoreBreakdown2020Alliance(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, adjust_points: int=None, auto_cell_points: int=None, auto_cells_bottom: int=None, auto_cells_inner: int=None, auto_cells_outer: int=None, auto_init_line_points: int=None, auto_points: int=None, control_panel_points: int=None, endgame_points: int=None, endgame_robot1: str=None, endgame_robot2: str=None, endgame_robot3: str=None, endgame_rung_is_level: str=None, foul_count: int=None, foul_points: int=None, init_line_robot1: str=None, init_line_robot2: str=None, init_line_robot3: str=None, rp: int=None, shield_energized_ranking_point: bool=None, shield_operational_ranking_point: bool=None, stage1_activated: bool=None, stage2_activated: bool=None, stage3_activated: bool=None, stage3_target_color: str=None, tba_num_robots_hanging: int=None, tba_shield_energized_ranking_point_from_foul: bool=None, tech_foul_count: int=None, teleop_cell_points: int=None, teleop_cells_bottom: int=None, teleop_cells_inner: int=None, teleop_cells_outer: int=None, teleop_points: int=None, total_points: int=None):
        """MatchScoreBreakdown2020Alliance - a model defined in OpenAPI

        :param adjust_points: The adjust_points of this MatchScoreBreakdown2020Alliance.
        :param auto_cell_points: The auto_cell_points of this MatchScoreBreakdown2020Alliance.
        :param auto_cells_bottom: The auto_cells_bottom of this MatchScoreBreakdown2020Alliance.
        :param auto_cells_inner: The auto_cells_inner of this MatchScoreBreakdown2020Alliance.
        :param auto_cells_outer: The auto_cells_outer of this MatchScoreBreakdown2020Alliance.
        :param auto_init_line_points: The auto_init_line_points of this MatchScoreBreakdown2020Alliance.
        :param auto_points: The auto_points of this MatchScoreBreakdown2020Alliance.
        :param control_panel_points: The control_panel_points of this MatchScoreBreakdown2020Alliance.
        :param endgame_points: The endgame_points of this MatchScoreBreakdown2020Alliance.
        :param endgame_robot1: The endgame_robot1 of this MatchScoreBreakdown2020Alliance.
        :param endgame_robot2: The endgame_robot2 of this MatchScoreBreakdown2020Alliance.
        :param endgame_robot3: The endgame_robot3 of this MatchScoreBreakdown2020Alliance.
        :param endgame_rung_is_level: The endgame_rung_is_level of this MatchScoreBreakdown2020Alliance.
        :param foul_count: The foul_count of this MatchScoreBreakdown2020Alliance.
        :param foul_points: The foul_points of this MatchScoreBreakdown2020Alliance.
        :param init_line_robot1: The init_line_robot1 of this MatchScoreBreakdown2020Alliance.
        :param init_line_robot2: The init_line_robot2 of this MatchScoreBreakdown2020Alliance.
        :param init_line_robot3: The init_line_robot3 of this MatchScoreBreakdown2020Alliance.
        :param rp: The rp of this MatchScoreBreakdown2020Alliance.
        :param shield_energized_ranking_point: The shield_energized_ranking_point of this MatchScoreBreakdown2020Alliance.
        :param shield_operational_ranking_point: The shield_operational_ranking_point of this MatchScoreBreakdown2020Alliance.
        :param stage1_activated: The stage1_activated of this MatchScoreBreakdown2020Alliance.
        :param stage2_activated: The stage2_activated of this MatchScoreBreakdown2020Alliance.
        :param stage3_activated: The stage3_activated of this MatchScoreBreakdown2020Alliance.
        :param stage3_target_color: The stage3_target_color of this MatchScoreBreakdown2020Alliance.
        :param tba_num_robots_hanging: The tba_num_robots_hanging of this MatchScoreBreakdown2020Alliance.
        :param tba_shield_energized_ranking_point_from_foul: The tba_shield_energized_ranking_point_from_foul of this MatchScoreBreakdown2020Alliance.
        :param tech_foul_count: The tech_foul_count of this MatchScoreBreakdown2020Alliance.
        :param teleop_cell_points: The teleop_cell_points of this MatchScoreBreakdown2020Alliance.
        :param teleop_cells_bottom: The teleop_cells_bottom of this MatchScoreBreakdown2020Alliance.
        :param teleop_cells_inner: The teleop_cells_inner of this MatchScoreBreakdown2020Alliance.
        :param teleop_cells_outer: The teleop_cells_outer of this MatchScoreBreakdown2020Alliance.
        :param teleop_points: The teleop_points of this MatchScoreBreakdown2020Alliance.
        :param total_points: The total_points of this MatchScoreBreakdown2020Alliance.
        """
        self.openapi_types = {
            'adjust_points': int,
            'auto_cell_points': int,
            'auto_cells_bottom': int,
            'auto_cells_inner': int,
            'auto_cells_outer': int,
            'auto_init_line_points': int,
            'auto_points': int,
            'control_panel_points': int,
            'endgame_points': int,
            'endgame_robot1': str,
            'endgame_robot2': str,
            'endgame_robot3': str,
            'endgame_rung_is_level': str,
            'foul_count': int,
            'foul_points': int,
            'init_line_robot1': str,
            'init_line_robot2': str,
            'init_line_robot3': str,
            'rp': int,
            'shield_energized_ranking_point': bool,
            'shield_operational_ranking_point': bool,
            'stage1_activated': bool,
            'stage2_activated': bool,
            'stage3_activated': bool,
            'stage3_target_color': str,
            'tba_num_robots_hanging': int,
            'tba_shield_energized_ranking_point_from_foul': bool,
            'tech_foul_count': int,
            'teleop_cell_points': int,
            'teleop_cells_bottom': int,
            'teleop_cells_inner': int,
            'teleop_cells_outer': int,
            'teleop_points': int,
            'total_points': int
        }

        self.attribute_map = {
            'adjust_points': 'adjustPoints',
            'auto_cell_points': 'autoCellPoints',
            'auto_cells_bottom': 'autoCellsBottom',
            'auto_cells_inner': 'autoCellsInner',
            'auto_cells_outer': 'autoCellsOuter',
            'auto_init_line_points': 'autoInitLinePoints',
            'auto_points': 'autoPoints',
            'control_panel_points': 'controlPanelPoints',
            'endgame_points': 'endgamePoints',
            'endgame_robot1': 'endgameRobot1',
            'endgame_robot2': 'endgameRobot2',
            'endgame_robot3': 'endgameRobot3',
            'endgame_rung_is_level': 'endgameRungIsLevel',
            'foul_count': 'foulCount',
            'foul_points': 'foulPoints',
            'init_line_robot1': 'initLineRobot1',
            'init_line_robot2': 'initLineRobot2',
            'init_line_robot3': 'initLineRobot3',
            'rp': 'rp',
            'shield_energized_ranking_point': 'shieldEnergizedRankingPoint',
            'shield_operational_ranking_point': 'shieldOperationalRankingPoint',
            'stage1_activated': 'stage1Activated',
            'stage2_activated': 'stage2Activated',
            'stage3_activated': 'stage3Activated',
            'stage3_target_color': 'stage3TargetColor',
            'tba_num_robots_hanging': 'tba_numRobotsHanging',
            'tba_shield_energized_ranking_point_from_foul': 'tba_shieldEnergizedRankingPointFromFoul',
            'tech_foul_count': 'techFoulCount',
            'teleop_cell_points': 'teleopCellPoints',
            'teleop_cells_bottom': 'teleopCellsBottom',
            'teleop_cells_inner': 'teleopCellsInner',
            'teleop_cells_outer': 'teleopCellsOuter',
            'teleop_points': 'teleopPoints',
            'total_points': 'totalPoints'
        }

        self._adjust_points = adjust_points
        self._auto_cell_points = auto_cell_points
        self._auto_cells_bottom = auto_cells_bottom
        self._auto_cells_inner = auto_cells_inner
        self._auto_cells_outer = auto_cells_outer
        self._auto_init_line_points = auto_init_line_points
        self._auto_points = auto_points
        self._control_panel_points = control_panel_points
        self._endgame_points = endgame_points
        self._endgame_robot1 = endgame_robot1
        self._endgame_robot2 = endgame_robot2
        self._endgame_robot3 = endgame_robot3
        self._endgame_rung_is_level = endgame_rung_is_level
        self._foul_count = foul_count
        self._foul_points = foul_points
        self._init_line_robot1 = init_line_robot1
        self._init_line_robot2 = init_line_robot2
        self._init_line_robot3 = init_line_robot3
        self._rp = rp
        self._shield_energized_ranking_point = shield_energized_ranking_point
        self._shield_operational_ranking_point = shield_operational_ranking_point
        self._stage1_activated = stage1_activated
        self._stage2_activated = stage2_activated
        self._stage3_activated = stage3_activated
        self._stage3_target_color = stage3_target_color
        self._tba_num_robots_hanging = tba_num_robots_hanging
        self._tba_shield_energized_ranking_point_from_foul = tba_shield_energized_ranking_point_from_foul
        self._tech_foul_count = tech_foul_count
        self._teleop_cell_points = teleop_cell_points
        self._teleop_cells_bottom = teleop_cells_bottom
        self._teleop_cells_inner = teleop_cells_inner
        self._teleop_cells_outer = teleop_cells_outer
        self._teleop_points = teleop_points
        self._total_points = total_points

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MatchScoreBreakdown2020Alliance':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Match_Score_Breakdown_2020_Alliance of this MatchScoreBreakdown2020Alliance.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def adjust_points(self):
        """Gets the adjust_points of this MatchScoreBreakdown2020Alliance.


        :return: The adjust_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._adjust_points

    @adjust_points.setter
    def adjust_points(self, adjust_points):
        """Sets the adjust_points of this MatchScoreBreakdown2020Alliance.


        :param adjust_points: The adjust_points of this MatchScoreBreakdown2020Alliance.
        :type adjust_points: int
        """

        self._adjust_points = adjust_points

    @property
    def auto_cell_points(self):
        """Gets the auto_cell_points of this MatchScoreBreakdown2020Alliance.


        :return: The auto_cell_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._auto_cell_points

    @auto_cell_points.setter
    def auto_cell_points(self, auto_cell_points):
        """Sets the auto_cell_points of this MatchScoreBreakdown2020Alliance.


        :param auto_cell_points: The auto_cell_points of this MatchScoreBreakdown2020Alliance.
        :type auto_cell_points: int
        """

        self._auto_cell_points = auto_cell_points

    @property
    def auto_cells_bottom(self):
        """Gets the auto_cells_bottom of this MatchScoreBreakdown2020Alliance.


        :return: The auto_cells_bottom of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._auto_cells_bottom

    @auto_cells_bottom.setter
    def auto_cells_bottom(self, auto_cells_bottom):
        """Sets the auto_cells_bottom of this MatchScoreBreakdown2020Alliance.


        :param auto_cells_bottom: The auto_cells_bottom of this MatchScoreBreakdown2020Alliance.
        :type auto_cells_bottom: int
        """

        self._auto_cells_bottom = auto_cells_bottom

    @property
    def auto_cells_inner(self):
        """Gets the auto_cells_inner of this MatchScoreBreakdown2020Alliance.


        :return: The auto_cells_inner of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._auto_cells_inner

    @auto_cells_inner.setter
    def auto_cells_inner(self, auto_cells_inner):
        """Sets the auto_cells_inner of this MatchScoreBreakdown2020Alliance.


        :param auto_cells_inner: The auto_cells_inner of this MatchScoreBreakdown2020Alliance.
        :type auto_cells_inner: int
        """

        self._auto_cells_inner = auto_cells_inner

    @property
    def auto_cells_outer(self):
        """Gets the auto_cells_outer of this MatchScoreBreakdown2020Alliance.


        :return: The auto_cells_outer of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._auto_cells_outer

    @auto_cells_outer.setter
    def auto_cells_outer(self, auto_cells_outer):
        """Sets the auto_cells_outer of this MatchScoreBreakdown2020Alliance.


        :param auto_cells_outer: The auto_cells_outer of this MatchScoreBreakdown2020Alliance.
        :type auto_cells_outer: int
        """

        self._auto_cells_outer = auto_cells_outer

    @property
    def auto_init_line_points(self):
        """Gets the auto_init_line_points of this MatchScoreBreakdown2020Alliance.


        :return: The auto_init_line_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._auto_init_line_points

    @auto_init_line_points.setter
    def auto_init_line_points(self, auto_init_line_points):
        """Sets the auto_init_line_points of this MatchScoreBreakdown2020Alliance.


        :param auto_init_line_points: The auto_init_line_points of this MatchScoreBreakdown2020Alliance.
        :type auto_init_line_points: int
        """

        self._auto_init_line_points = auto_init_line_points

    @property
    def auto_points(self):
        """Gets the auto_points of this MatchScoreBreakdown2020Alliance.


        :return: The auto_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._auto_points

    @auto_points.setter
    def auto_points(self, auto_points):
        """Sets the auto_points of this MatchScoreBreakdown2020Alliance.


        :param auto_points: The auto_points of this MatchScoreBreakdown2020Alliance.
        :type auto_points: int
        """

        self._auto_points = auto_points

    @property
    def control_panel_points(self):
        """Gets the control_panel_points of this MatchScoreBreakdown2020Alliance.


        :return: The control_panel_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._control_panel_points

    @control_panel_points.setter
    def control_panel_points(self, control_panel_points):
        """Sets the control_panel_points of this MatchScoreBreakdown2020Alliance.


        :param control_panel_points: The control_panel_points of this MatchScoreBreakdown2020Alliance.
        :type control_panel_points: int
        """

        self._control_panel_points = control_panel_points

    @property
    def endgame_points(self):
        """Gets the endgame_points of this MatchScoreBreakdown2020Alliance.


        :return: The endgame_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._endgame_points

    @endgame_points.setter
    def endgame_points(self, endgame_points):
        """Sets the endgame_points of this MatchScoreBreakdown2020Alliance.


        :param endgame_points: The endgame_points of this MatchScoreBreakdown2020Alliance.
        :type endgame_points: int
        """

        self._endgame_points = endgame_points

    @property
    def endgame_robot1(self):
        """Gets the endgame_robot1 of this MatchScoreBreakdown2020Alliance.


        :return: The endgame_robot1 of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._endgame_robot1

    @endgame_robot1.setter
    def endgame_robot1(self, endgame_robot1):
        """Sets the endgame_robot1 of this MatchScoreBreakdown2020Alliance.


        :param endgame_robot1: The endgame_robot1 of this MatchScoreBreakdown2020Alliance.
        :type endgame_robot1: str
        """

        self._endgame_robot1 = endgame_robot1

    @property
    def endgame_robot2(self):
        """Gets the endgame_robot2 of this MatchScoreBreakdown2020Alliance.


        :return: The endgame_robot2 of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._endgame_robot2

    @endgame_robot2.setter
    def endgame_robot2(self, endgame_robot2):
        """Sets the endgame_robot2 of this MatchScoreBreakdown2020Alliance.


        :param endgame_robot2: The endgame_robot2 of this MatchScoreBreakdown2020Alliance.
        :type endgame_robot2: str
        """

        self._endgame_robot2 = endgame_robot2

    @property
    def endgame_robot3(self):
        """Gets the endgame_robot3 of this MatchScoreBreakdown2020Alliance.


        :return: The endgame_robot3 of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._endgame_robot3

    @endgame_robot3.setter
    def endgame_robot3(self, endgame_robot3):
        """Sets the endgame_robot3 of this MatchScoreBreakdown2020Alliance.


        :param endgame_robot3: The endgame_robot3 of this MatchScoreBreakdown2020Alliance.
        :type endgame_robot3: str
        """

        self._endgame_robot3 = endgame_robot3

    @property
    def endgame_rung_is_level(self):
        """Gets the endgame_rung_is_level of this MatchScoreBreakdown2020Alliance.


        :return: The endgame_rung_is_level of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._endgame_rung_is_level

    @endgame_rung_is_level.setter
    def endgame_rung_is_level(self, endgame_rung_is_level):
        """Sets the endgame_rung_is_level of this MatchScoreBreakdown2020Alliance.


        :param endgame_rung_is_level: The endgame_rung_is_level of this MatchScoreBreakdown2020Alliance.
        :type endgame_rung_is_level: str
        """

        self._endgame_rung_is_level = endgame_rung_is_level

    @property
    def foul_count(self):
        """Gets the foul_count of this MatchScoreBreakdown2020Alliance.


        :return: The foul_count of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._foul_count

    @foul_count.setter
    def foul_count(self, foul_count):
        """Sets the foul_count of this MatchScoreBreakdown2020Alliance.


        :param foul_count: The foul_count of this MatchScoreBreakdown2020Alliance.
        :type foul_count: int
        """

        self._foul_count = foul_count

    @property
    def foul_points(self):
        """Gets the foul_points of this MatchScoreBreakdown2020Alliance.


        :return: The foul_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._foul_points

    @foul_points.setter
    def foul_points(self, foul_points):
        """Sets the foul_points of this MatchScoreBreakdown2020Alliance.


        :param foul_points: The foul_points of this MatchScoreBreakdown2020Alliance.
        :type foul_points: int
        """

        self._foul_points = foul_points

    @property
    def init_line_robot1(self):
        """Gets the init_line_robot1 of this MatchScoreBreakdown2020Alliance.


        :return: The init_line_robot1 of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._init_line_robot1

    @init_line_robot1.setter
    def init_line_robot1(self, init_line_robot1):
        """Sets the init_line_robot1 of this MatchScoreBreakdown2020Alliance.


        :param init_line_robot1: The init_line_robot1 of this MatchScoreBreakdown2020Alliance.
        :type init_line_robot1: str
        """

        self._init_line_robot1 = init_line_robot1

    @property
    def init_line_robot2(self):
        """Gets the init_line_robot2 of this MatchScoreBreakdown2020Alliance.


        :return: The init_line_robot2 of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._init_line_robot2

    @init_line_robot2.setter
    def init_line_robot2(self, init_line_robot2):
        """Sets the init_line_robot2 of this MatchScoreBreakdown2020Alliance.


        :param init_line_robot2: The init_line_robot2 of this MatchScoreBreakdown2020Alliance.
        :type init_line_robot2: str
        """

        self._init_line_robot2 = init_line_robot2

    @property
    def init_line_robot3(self):
        """Gets the init_line_robot3 of this MatchScoreBreakdown2020Alliance.


        :return: The init_line_robot3 of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._init_line_robot3

    @init_line_robot3.setter
    def init_line_robot3(self, init_line_robot3):
        """Sets the init_line_robot3 of this MatchScoreBreakdown2020Alliance.


        :param init_line_robot3: The init_line_robot3 of this MatchScoreBreakdown2020Alliance.
        :type init_line_robot3: str
        """

        self._init_line_robot3 = init_line_robot3

    @property
    def rp(self):
        """Gets the rp of this MatchScoreBreakdown2020Alliance.


        :return: The rp of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Sets the rp of this MatchScoreBreakdown2020Alliance.


        :param rp: The rp of this MatchScoreBreakdown2020Alliance.
        :type rp: int
        """

        self._rp = rp

    @property
    def shield_energized_ranking_point(self):
        """Gets the shield_energized_ranking_point of this MatchScoreBreakdown2020Alliance.


        :return: The shield_energized_ranking_point of this MatchScoreBreakdown2020Alliance.
        :rtype: bool
        """
        return self._shield_energized_ranking_point

    @shield_energized_ranking_point.setter
    def shield_energized_ranking_point(self, shield_energized_ranking_point):
        """Sets the shield_energized_ranking_point of this MatchScoreBreakdown2020Alliance.


        :param shield_energized_ranking_point: The shield_energized_ranking_point of this MatchScoreBreakdown2020Alliance.
        :type shield_energized_ranking_point: bool
        """

        self._shield_energized_ranking_point = shield_energized_ranking_point

    @property
    def shield_operational_ranking_point(self):
        """Gets the shield_operational_ranking_point of this MatchScoreBreakdown2020Alliance.


        :return: The shield_operational_ranking_point of this MatchScoreBreakdown2020Alliance.
        :rtype: bool
        """
        return self._shield_operational_ranking_point

    @shield_operational_ranking_point.setter
    def shield_operational_ranking_point(self, shield_operational_ranking_point):
        """Sets the shield_operational_ranking_point of this MatchScoreBreakdown2020Alliance.


        :param shield_operational_ranking_point: The shield_operational_ranking_point of this MatchScoreBreakdown2020Alliance.
        :type shield_operational_ranking_point: bool
        """

        self._shield_operational_ranking_point = shield_operational_ranking_point

    @property
    def stage1_activated(self):
        """Gets the stage1_activated of this MatchScoreBreakdown2020Alliance.


        :return: The stage1_activated of this MatchScoreBreakdown2020Alliance.
        :rtype: bool
        """
        return self._stage1_activated

    @stage1_activated.setter
    def stage1_activated(self, stage1_activated):
        """Sets the stage1_activated of this MatchScoreBreakdown2020Alliance.


        :param stage1_activated: The stage1_activated of this MatchScoreBreakdown2020Alliance.
        :type stage1_activated: bool
        """

        self._stage1_activated = stage1_activated

    @property
    def stage2_activated(self):
        """Gets the stage2_activated of this MatchScoreBreakdown2020Alliance.


        :return: The stage2_activated of this MatchScoreBreakdown2020Alliance.
        :rtype: bool
        """
        return self._stage2_activated

    @stage2_activated.setter
    def stage2_activated(self, stage2_activated):
        """Sets the stage2_activated of this MatchScoreBreakdown2020Alliance.


        :param stage2_activated: The stage2_activated of this MatchScoreBreakdown2020Alliance.
        :type stage2_activated: bool
        """

        self._stage2_activated = stage2_activated

    @property
    def stage3_activated(self):
        """Gets the stage3_activated of this MatchScoreBreakdown2020Alliance.


        :return: The stage3_activated of this MatchScoreBreakdown2020Alliance.
        :rtype: bool
        """
        return self._stage3_activated

    @stage3_activated.setter
    def stage3_activated(self, stage3_activated):
        """Sets the stage3_activated of this MatchScoreBreakdown2020Alliance.


        :param stage3_activated: The stage3_activated of this MatchScoreBreakdown2020Alliance.
        :type stage3_activated: bool
        """

        self._stage3_activated = stage3_activated

    @property
    def stage3_target_color(self):
        """Gets the stage3_target_color of this MatchScoreBreakdown2020Alliance.


        :return: The stage3_target_color of this MatchScoreBreakdown2020Alliance.
        :rtype: str
        """
        return self._stage3_target_color

    @stage3_target_color.setter
    def stage3_target_color(self, stage3_target_color):
        """Sets the stage3_target_color of this MatchScoreBreakdown2020Alliance.


        :param stage3_target_color: The stage3_target_color of this MatchScoreBreakdown2020Alliance.
        :type stage3_target_color: str
        """

        self._stage3_target_color = stage3_target_color

    @property
    def tba_num_robots_hanging(self):
        """Gets the tba_num_robots_hanging of this MatchScoreBreakdown2020Alliance.

        Unofficial TBA-computed value that counts the number of robots who were hanging at the end of the match.

        :return: The tba_num_robots_hanging of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._tba_num_robots_hanging

    @tba_num_robots_hanging.setter
    def tba_num_robots_hanging(self, tba_num_robots_hanging):
        """Sets the tba_num_robots_hanging of this MatchScoreBreakdown2020Alliance.

        Unofficial TBA-computed value that counts the number of robots who were hanging at the end of the match.

        :param tba_num_robots_hanging: The tba_num_robots_hanging of this MatchScoreBreakdown2020Alliance.
        :type tba_num_robots_hanging: int
        """

        self._tba_num_robots_hanging = tba_num_robots_hanging

    @property
    def tba_shield_energized_ranking_point_from_foul(self):
        """Gets the tba_shield_energized_ranking_point_from_foul of this MatchScoreBreakdown2020Alliance.

        Unofficial TBA-computed value that indicates whether the shieldEnergizedRankingPoint was earned normally or awarded due to a foul.

        :return: The tba_shield_energized_ranking_point_from_foul of this MatchScoreBreakdown2020Alliance.
        :rtype: bool
        """
        return self._tba_shield_energized_ranking_point_from_foul

    @tba_shield_energized_ranking_point_from_foul.setter
    def tba_shield_energized_ranking_point_from_foul(self, tba_shield_energized_ranking_point_from_foul):
        """Sets the tba_shield_energized_ranking_point_from_foul of this MatchScoreBreakdown2020Alliance.

        Unofficial TBA-computed value that indicates whether the shieldEnergizedRankingPoint was earned normally or awarded due to a foul.

        :param tba_shield_energized_ranking_point_from_foul: The tba_shield_energized_ranking_point_from_foul of this MatchScoreBreakdown2020Alliance.
        :type tba_shield_energized_ranking_point_from_foul: bool
        """

        self._tba_shield_energized_ranking_point_from_foul = tba_shield_energized_ranking_point_from_foul

    @property
    def tech_foul_count(self):
        """Gets the tech_foul_count of this MatchScoreBreakdown2020Alliance.


        :return: The tech_foul_count of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._tech_foul_count

    @tech_foul_count.setter
    def tech_foul_count(self, tech_foul_count):
        """Sets the tech_foul_count of this MatchScoreBreakdown2020Alliance.


        :param tech_foul_count: The tech_foul_count of this MatchScoreBreakdown2020Alliance.
        :type tech_foul_count: int
        """

        self._tech_foul_count = tech_foul_count

    @property
    def teleop_cell_points(self):
        """Gets the teleop_cell_points of this MatchScoreBreakdown2020Alliance.


        :return: The teleop_cell_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._teleop_cell_points

    @teleop_cell_points.setter
    def teleop_cell_points(self, teleop_cell_points):
        """Sets the teleop_cell_points of this MatchScoreBreakdown2020Alliance.


        :param teleop_cell_points: The teleop_cell_points of this MatchScoreBreakdown2020Alliance.
        :type teleop_cell_points: int
        """

        self._teleop_cell_points = teleop_cell_points

    @property
    def teleop_cells_bottom(self):
        """Gets the teleop_cells_bottom of this MatchScoreBreakdown2020Alliance.


        :return: The teleop_cells_bottom of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._teleop_cells_bottom

    @teleop_cells_bottom.setter
    def teleop_cells_bottom(self, teleop_cells_bottom):
        """Sets the teleop_cells_bottom of this MatchScoreBreakdown2020Alliance.


        :param teleop_cells_bottom: The teleop_cells_bottom of this MatchScoreBreakdown2020Alliance.
        :type teleop_cells_bottom: int
        """

        self._teleop_cells_bottom = teleop_cells_bottom

    @property
    def teleop_cells_inner(self):
        """Gets the teleop_cells_inner of this MatchScoreBreakdown2020Alliance.


        :return: The teleop_cells_inner of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._teleop_cells_inner

    @teleop_cells_inner.setter
    def teleop_cells_inner(self, teleop_cells_inner):
        """Sets the teleop_cells_inner of this MatchScoreBreakdown2020Alliance.


        :param teleop_cells_inner: The teleop_cells_inner of this MatchScoreBreakdown2020Alliance.
        :type teleop_cells_inner: int
        """

        self._teleop_cells_inner = teleop_cells_inner

    @property
    def teleop_cells_outer(self):
        """Gets the teleop_cells_outer of this MatchScoreBreakdown2020Alliance.


        :return: The teleop_cells_outer of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._teleop_cells_outer

    @teleop_cells_outer.setter
    def teleop_cells_outer(self, teleop_cells_outer):
        """Sets the teleop_cells_outer of this MatchScoreBreakdown2020Alliance.


        :param teleop_cells_outer: The teleop_cells_outer of this MatchScoreBreakdown2020Alliance.
        :type teleop_cells_outer: int
        """

        self._teleop_cells_outer = teleop_cells_outer

    @property
    def teleop_points(self):
        """Gets the teleop_points of this MatchScoreBreakdown2020Alliance.


        :return: The teleop_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._teleop_points

    @teleop_points.setter
    def teleop_points(self, teleop_points):
        """Sets the teleop_points of this MatchScoreBreakdown2020Alliance.


        :param teleop_points: The teleop_points of this MatchScoreBreakdown2020Alliance.
        :type teleop_points: int
        """

        self._teleop_points = teleop_points

    @property
    def total_points(self):
        """Gets the total_points of this MatchScoreBreakdown2020Alliance.


        :return: The total_points of this MatchScoreBreakdown2020Alliance.
        :rtype: int
        """
        return self._total_points

    @total_points.setter
    def total_points(self, total_points):
        """Sets the total_points of this MatchScoreBreakdown2020Alliance.


        :param total_points: The total_points of this MatchScoreBreakdown2020Alliance.
        :type total_points: int
        """

        self._total_points = total_points
