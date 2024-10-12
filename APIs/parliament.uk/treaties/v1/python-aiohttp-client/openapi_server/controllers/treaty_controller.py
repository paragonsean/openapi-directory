from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_item_resource_collection import BusinessItemResourceCollection
from openapi_server.models.house import House
from openapi_server.models.parliamentary_process import ParliamentaryProcess
from openapi_server.models.series_membership_type import SeriesMembershipType
from openapi_server.models.treaty_resource import TreatyResource
from openapi_server.models.treaty_resource_collection import TreatyResourceCollection
from openapi_server import util


async def get_business_items_by_treaty_id(request: web.Request, id) -> web.Response:
    """Returns business items belonging to the treaty with ID.

    

    :param id: Business items belonging to treaty with the ID specified
    :type id: str

    """
    return web.Response(status=200)


async def get_treaties(request: web.Request, search_text=None, government_organisation_id=None, series=None, parliamentary_process=None, debate_scheduled=None, motion_to_not_ratify=None, recommended_not_ratify=None, house=None, skip=None, take=None) -> web.Response:
    """Returns a list of treaties.

    

    :param search_text: Treaties which contains the search text specified
    :type search_text: str
    :param government_organisation_id: Treaties with the government organisation id specified
    :type government_organisation_id: int
    :param series: Treaties with the series membership type specified
    :type series: dict | bytes
    :param parliamentary_process: Treaties where the parliamentary process is concluded or notconcluded
    :type parliamentary_process: dict | bytes
    :param debate_scheduled: Treaties which contain a scheduled debate
    :type debate_scheduled: bool
    :param motion_to_not_ratify: Treaties which contain a motion to not ratify
    :type motion_to_not_ratify: bool
    :param recommended_not_ratify: Treaties which are recommended to not ratify
    :type recommended_not_ratify: bool
    :param house: Treaties which are laid in the specified house
    :type house: dict | bytes
    :param skip: The number of records to skip from the first, default is 0
    :type skip: int
    :param take: The number of records to return, default is 20
    :type take: int

    """
    series = .from_dict(series)
    parliamentary_process = .from_dict(parliamentary_process)
    house = .from_dict(house)
    return web.Response(status=200)


async def get_treaty_by_id(request: web.Request, id) -> web.Response:
    """Returns a treaty by ID.

    

    :param id: Treaty with ID specified
    :type id: str

    """
    return web.Response(status=200)
