# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Champion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, armor: float=None, armor_per_level: float=None, attack: float=None, attack_damage: float=None, attack_damage_per_level: float=None, attack_range: float=None, attack_speed_offset: float=None, champion_id: int=None, defense: float=None, difficulty: float=None, hp: float=None, hp_regen: float=None, hp_regen_per_level: float=None, hp_up_per_level: float=None, magic: float=None, move_speed: float=None, mp: float=None, mp_regen: float=None, mp_regen_per_level: float=None, mp_up_per_level: float=None, name: str=None, spell_block: float=None, spell_block_per_level: float=None, title: str=None):
        """Champion - a model defined in OpenAPI

        :param armor: The armor of this Champion.
        :param armor_per_level: The armor_per_level of this Champion.
        :param attack: The attack of this Champion.
        :param attack_damage: The attack_damage of this Champion.
        :param attack_damage_per_level: The attack_damage_per_level of this Champion.
        :param attack_range: The attack_range of this Champion.
        :param attack_speed_offset: The attack_speed_offset of this Champion.
        :param champion_id: The champion_id of this Champion.
        :param defense: The defense of this Champion.
        :param difficulty: The difficulty of this Champion.
        :param hp: The hp of this Champion.
        :param hp_regen: The hp_regen of this Champion.
        :param hp_regen_per_level: The hp_regen_per_level of this Champion.
        :param hp_up_per_level: The hp_up_per_level of this Champion.
        :param magic: The magic of this Champion.
        :param move_speed: The move_speed of this Champion.
        :param mp: The mp of this Champion.
        :param mp_regen: The mp_regen of this Champion.
        :param mp_regen_per_level: The mp_regen_per_level of this Champion.
        :param mp_up_per_level: The mp_up_per_level of this Champion.
        :param name: The name of this Champion.
        :param spell_block: The spell_block of this Champion.
        :param spell_block_per_level: The spell_block_per_level of this Champion.
        :param title: The title of this Champion.
        """
        self.openapi_types = {
            'armor': float,
            'armor_per_level': float,
            'attack': float,
            'attack_damage': float,
            'attack_damage_per_level': float,
            'attack_range': float,
            'attack_speed_offset': float,
            'champion_id': int,
            'defense': float,
            'difficulty': float,
            'hp': float,
            'hp_regen': float,
            'hp_regen_per_level': float,
            'hp_up_per_level': float,
            'magic': float,
            'move_speed': float,
            'mp': float,
            'mp_regen': float,
            'mp_regen_per_level': float,
            'mp_up_per_level': float,
            'name': str,
            'spell_block': float,
            'spell_block_per_level': float,
            'title': str
        }

        self.attribute_map = {
            'armor': 'Armor',
            'armor_per_level': 'ArmorPerLevel',
            'attack': 'Attack',
            'attack_damage': 'AttackDamage',
            'attack_damage_per_level': 'AttackDamagePerLevel',
            'attack_range': 'AttackRange',
            'attack_speed_offset': 'AttackSpeedOffset',
            'champion_id': 'ChampionId',
            'defense': 'Defense',
            'difficulty': 'Difficulty',
            'hp': 'Hp',
            'hp_regen': 'HpRegen',
            'hp_regen_per_level': 'HpRegenPerLevel',
            'hp_up_per_level': 'HpUpPerLevel',
            'magic': 'Magic',
            'move_speed': 'MoveSpeed',
            'mp': 'Mp',
            'mp_regen': 'MpRegen',
            'mp_regen_per_level': 'MpRegenPerLevel',
            'mp_up_per_level': 'MpUpPerLevel',
            'name': 'Name',
            'spell_block': 'SpellBlock',
            'spell_block_per_level': 'SpellBlockPerLevel',
            'title': 'Title'
        }

        self._armor = armor
        self._armor_per_level = armor_per_level
        self._attack = attack
        self._attack_damage = attack_damage
        self._attack_damage_per_level = attack_damage_per_level
        self._attack_range = attack_range
        self._attack_speed_offset = attack_speed_offset
        self._champion_id = champion_id
        self._defense = defense
        self._difficulty = difficulty
        self._hp = hp
        self._hp_regen = hp_regen
        self._hp_regen_per_level = hp_regen_per_level
        self._hp_up_per_level = hp_up_per_level
        self._magic = magic
        self._move_speed = move_speed
        self._mp = mp
        self._mp_regen = mp_regen
        self._mp_regen_per_level = mp_regen_per_level
        self._mp_up_per_level = mp_up_per_level
        self._name = name
        self._spell_block = spell_block
        self._spell_block_per_level = spell_block_per_level
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Champion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Champion of this Champion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def armor(self):
        """Gets the armor of this Champion.


        :return: The armor of this Champion.
        :rtype: float
        """
        return self._armor

    @armor.setter
    def armor(self, armor):
        """Sets the armor of this Champion.


        :param armor: The armor of this Champion.
        :type armor: float
        """

        self._armor = armor

    @property
    def armor_per_level(self):
        """Gets the armor_per_level of this Champion.


        :return: The armor_per_level of this Champion.
        :rtype: float
        """
        return self._armor_per_level

    @armor_per_level.setter
    def armor_per_level(self, armor_per_level):
        """Sets the armor_per_level of this Champion.


        :param armor_per_level: The armor_per_level of this Champion.
        :type armor_per_level: float
        """

        self._armor_per_level = armor_per_level

    @property
    def attack(self):
        """Gets the attack of this Champion.


        :return: The attack of this Champion.
        :rtype: float
        """
        return self._attack

    @attack.setter
    def attack(self, attack):
        """Sets the attack of this Champion.


        :param attack: The attack of this Champion.
        :type attack: float
        """

        self._attack = attack

    @property
    def attack_damage(self):
        """Gets the attack_damage of this Champion.


        :return: The attack_damage of this Champion.
        :rtype: float
        """
        return self._attack_damage

    @attack_damage.setter
    def attack_damage(self, attack_damage):
        """Sets the attack_damage of this Champion.


        :param attack_damage: The attack_damage of this Champion.
        :type attack_damage: float
        """

        self._attack_damage = attack_damage

    @property
    def attack_damage_per_level(self):
        """Gets the attack_damage_per_level of this Champion.


        :return: The attack_damage_per_level of this Champion.
        :rtype: float
        """
        return self._attack_damage_per_level

    @attack_damage_per_level.setter
    def attack_damage_per_level(self, attack_damage_per_level):
        """Sets the attack_damage_per_level of this Champion.


        :param attack_damage_per_level: The attack_damage_per_level of this Champion.
        :type attack_damage_per_level: float
        """

        self._attack_damage_per_level = attack_damage_per_level

    @property
    def attack_range(self):
        """Gets the attack_range of this Champion.


        :return: The attack_range of this Champion.
        :rtype: float
        """
        return self._attack_range

    @attack_range.setter
    def attack_range(self, attack_range):
        """Sets the attack_range of this Champion.


        :param attack_range: The attack_range of this Champion.
        :type attack_range: float
        """

        self._attack_range = attack_range

    @property
    def attack_speed_offset(self):
        """Gets the attack_speed_offset of this Champion.


        :return: The attack_speed_offset of this Champion.
        :rtype: float
        """
        return self._attack_speed_offset

    @attack_speed_offset.setter
    def attack_speed_offset(self, attack_speed_offset):
        """Sets the attack_speed_offset of this Champion.


        :param attack_speed_offset: The attack_speed_offset of this Champion.
        :type attack_speed_offset: float
        """

        self._attack_speed_offset = attack_speed_offset

    @property
    def champion_id(self):
        """Gets the champion_id of this Champion.


        :return: The champion_id of this Champion.
        :rtype: int
        """
        return self._champion_id

    @champion_id.setter
    def champion_id(self, champion_id):
        """Sets the champion_id of this Champion.


        :param champion_id: The champion_id of this Champion.
        :type champion_id: int
        """

        self._champion_id = champion_id

    @property
    def defense(self):
        """Gets the defense of this Champion.


        :return: The defense of this Champion.
        :rtype: float
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this Champion.


        :param defense: The defense of this Champion.
        :type defense: float
        """

        self._defense = defense

    @property
    def difficulty(self):
        """Gets the difficulty of this Champion.


        :return: The difficulty of this Champion.
        :rtype: float
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        """Sets the difficulty of this Champion.


        :param difficulty: The difficulty of this Champion.
        :type difficulty: float
        """

        self._difficulty = difficulty

    @property
    def hp(self):
        """Gets the hp of this Champion.


        :return: The hp of this Champion.
        :rtype: float
        """
        return self._hp

    @hp.setter
    def hp(self, hp):
        """Sets the hp of this Champion.


        :param hp: The hp of this Champion.
        :type hp: float
        """

        self._hp = hp

    @property
    def hp_regen(self):
        """Gets the hp_regen of this Champion.


        :return: The hp_regen of this Champion.
        :rtype: float
        """
        return self._hp_regen

    @hp_regen.setter
    def hp_regen(self, hp_regen):
        """Sets the hp_regen of this Champion.


        :param hp_regen: The hp_regen of this Champion.
        :type hp_regen: float
        """

        self._hp_regen = hp_regen

    @property
    def hp_regen_per_level(self):
        """Gets the hp_regen_per_level of this Champion.


        :return: The hp_regen_per_level of this Champion.
        :rtype: float
        """
        return self._hp_regen_per_level

    @hp_regen_per_level.setter
    def hp_regen_per_level(self, hp_regen_per_level):
        """Sets the hp_regen_per_level of this Champion.


        :param hp_regen_per_level: The hp_regen_per_level of this Champion.
        :type hp_regen_per_level: float
        """

        self._hp_regen_per_level = hp_regen_per_level

    @property
    def hp_up_per_level(self):
        """Gets the hp_up_per_level of this Champion.


        :return: The hp_up_per_level of this Champion.
        :rtype: float
        """
        return self._hp_up_per_level

    @hp_up_per_level.setter
    def hp_up_per_level(self, hp_up_per_level):
        """Sets the hp_up_per_level of this Champion.


        :param hp_up_per_level: The hp_up_per_level of this Champion.
        :type hp_up_per_level: float
        """

        self._hp_up_per_level = hp_up_per_level

    @property
    def magic(self):
        """Gets the magic of this Champion.


        :return: The magic of this Champion.
        :rtype: float
        """
        return self._magic

    @magic.setter
    def magic(self, magic):
        """Sets the magic of this Champion.


        :param magic: The magic of this Champion.
        :type magic: float
        """

        self._magic = magic

    @property
    def move_speed(self):
        """Gets the move_speed of this Champion.


        :return: The move_speed of this Champion.
        :rtype: float
        """
        return self._move_speed

    @move_speed.setter
    def move_speed(self, move_speed):
        """Sets the move_speed of this Champion.


        :param move_speed: The move_speed of this Champion.
        :type move_speed: float
        """

        self._move_speed = move_speed

    @property
    def mp(self):
        """Gets the mp of this Champion.


        :return: The mp of this Champion.
        :rtype: float
        """
        return self._mp

    @mp.setter
    def mp(self, mp):
        """Sets the mp of this Champion.


        :param mp: The mp of this Champion.
        :type mp: float
        """

        self._mp = mp

    @property
    def mp_regen(self):
        """Gets the mp_regen of this Champion.


        :return: The mp_regen of this Champion.
        :rtype: float
        """
        return self._mp_regen

    @mp_regen.setter
    def mp_regen(self, mp_regen):
        """Sets the mp_regen of this Champion.


        :param mp_regen: The mp_regen of this Champion.
        :type mp_regen: float
        """

        self._mp_regen = mp_regen

    @property
    def mp_regen_per_level(self):
        """Gets the mp_regen_per_level of this Champion.


        :return: The mp_regen_per_level of this Champion.
        :rtype: float
        """
        return self._mp_regen_per_level

    @mp_regen_per_level.setter
    def mp_regen_per_level(self, mp_regen_per_level):
        """Sets the mp_regen_per_level of this Champion.


        :param mp_regen_per_level: The mp_regen_per_level of this Champion.
        :type mp_regen_per_level: float
        """

        self._mp_regen_per_level = mp_regen_per_level

    @property
    def mp_up_per_level(self):
        """Gets the mp_up_per_level of this Champion.


        :return: The mp_up_per_level of this Champion.
        :rtype: float
        """
        return self._mp_up_per_level

    @mp_up_per_level.setter
    def mp_up_per_level(self, mp_up_per_level):
        """Sets the mp_up_per_level of this Champion.


        :param mp_up_per_level: The mp_up_per_level of this Champion.
        :type mp_up_per_level: float
        """

        self._mp_up_per_level = mp_up_per_level

    @property
    def name(self):
        """Gets the name of this Champion.


        :return: The name of this Champion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Champion.


        :param name: The name of this Champion.
        :type name: str
        """

        self._name = name

    @property
    def spell_block(self):
        """Gets the spell_block of this Champion.


        :return: The spell_block of this Champion.
        :rtype: float
        """
        return self._spell_block

    @spell_block.setter
    def spell_block(self, spell_block):
        """Sets the spell_block of this Champion.


        :param spell_block: The spell_block of this Champion.
        :type spell_block: float
        """

        self._spell_block = spell_block

    @property
    def spell_block_per_level(self):
        """Gets the spell_block_per_level of this Champion.


        :return: The spell_block_per_level of this Champion.
        :rtype: float
        """
        return self._spell_block_per_level

    @spell_block_per_level.setter
    def spell_block_per_level(self, spell_block_per_level):
        """Sets the spell_block_per_level of this Champion.


        :param spell_block_per_level: The spell_block_per_level of this Champion.
        :type spell_block_per_level: float
        """

        self._spell_block_per_level = spell_block_per_level

    @property
    def title(self):
        """Gets the title of this Champion.


        :return: The title of this Champion.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Champion.


        :param title: The title of this Champion.
        :type title: str
        """

        self._title = title
