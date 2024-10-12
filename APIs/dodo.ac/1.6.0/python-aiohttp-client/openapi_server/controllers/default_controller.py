from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error401 import Error401
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.nh_artwork import NHArtwork
from openapi_server.models.nh_bug import NHBug
from openapi_server.models.nh_clothing import NHClothing
from openapi_server.models.nh_event import NHEvent
from openapi_server.models.nh_fish import NHFish
from openapi_server.models.nh_fossil_group import NHFossilGroup
from openapi_server.models.nh_fossil_group_with_individual_fossils import NHFossilGroupWithIndividualFossils
from openapi_server.models.nh_fossil_group_with_individual_fossils_no_matched import NHFossilGroupWithIndividualFossilsNoMatched
from openapi_server.models.nh_furniture import NHFurniture
from openapi_server.models.nh_individual_fossil import NHIndividualFossil
from openapi_server.models.nh_interior import NHInterior
from openapi_server.models.nh_item import NHItem
from openapi_server.models.nh_photo import NHPhoto
from openapi_server.models.nh_recipe import NHRecipe
from openapi_server.models.nh_sea_creature import NHSeaCreature
from openapi_server.models.nh_tool import NHTool
from openapi_server.models.villager import Villager
from openapi_server import util


async def nh_art_artwork_get(request: web.Request, artwork, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons artwork

    Retrieve information about a specific artwork in *Animal Crossing: New Horizons*.

    :param artwork: The name of the artwork you wish to retrieve information about.
    :type artwork: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_art_get(request: web.Request, x_api_key, accept_version, hasfake=None, excludedetails=None, thumbsize=None) -> web.Response:
    """All New Horizons artwork

    Get a list of all artwork and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param hasfake: When set to &#x60;true&#x60;, only artwork that has a fake will be returned. When set to &#x60;false&#x60;, only artwork without fakes will be returned.
    :type hasfake: str
    :param excludedetails: When set to &#x60;true&#x60;, only artwork names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_bugs_bug_get(request: web.Request, bug, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons bug

    Retrieve information about a specific bug in *Animal Crossing: New Horizons*.

    :param bug: The name of the bug you wish to retrieve information about.
    :type bug: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_bugs_get(request: web.Request, x_api_key, accept_version, month=None, excludedetails=None, thumbsize=None) -> web.Response:
    """All New Horizons bugs

    Get a list of all bugs and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param month: Retrive only the bug that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the bug available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month.
    :type month: str
    :param excludedetails: When set to &#x60;true&#x60;, only bug names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of bugs in a given month but not all their respective details.
    :type excludedetails: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_clothing_clothing_get(request: web.Request, clothing, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons clothing

    Retrieve information about a specific clothing item in *Animal Crossing: New Horizons*.

    :param clothing: The name of the clothing you wish to retrieve information about.
    :type clothing: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_clothing_get(request: web.Request, x_api_key, accept_version, category=None, color=None, style=None, labeltheme=None, excludedetails=None) -> web.Response:
    """All New Horizons clothing

    Get a list of all clothing items and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param category: Specify the category of clothing to return.
    :type category: str
    :param color: Return clothing that matches the provided colors (may specify one or two colors). Colors are used for gifting villagers.
    :type color: List[str]
    :param style: Return clothing that matches the provided styles (may specify one or two styles). Styles are used for gifting villagers.
    :type style: List[str]
    :param labeltheme: Return clothing that have the specified Label theme. This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player&#39;s island.
    :type labeltheme: str
    :param excludedetails: When set to &#x60;true&#x60;, only clothing names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str

    """
    return web.Response(status=200)


async def nh_events_get(request: web.Request, x_api_key, accept_version, _date=None, year=None, month=None, day=None) -> web.Response:
    """All New Horizons events

    Get a list of events and dates in *Animal Crossing: New Horizons*, filterable to specific years, months, or days. Data is available for the current and next year.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param _date: Specify a specific date (in the current or next year) to retrieve events for. Accepts many date formats, such as &#x60;YYYY-MM-DD&#x60; or &#x60;Month Day, Year&#x60;, as well as &#x60;today&#x60; to retrieve the current day&#39;s events (UTC time).
    :type _date: str
    :param year: Specify the year to retrieve events for. Must be the current or next year.
    :type year: str
    :param month: Specify the month to retrieve events for (accepts multiple formats, such as &#x60;Oct&#x60;, &#x60;October&#x60;, or &#x60;10&#x60;). Most likely want to use alongside &#x60;year&#x60;, otherwise events in both the current and next year are returned.
    :type month: str
    :param day: Specify the day of the month to retrieve events for.
    :type day: int

    """
    return web.Response(status=200)


async def nh_fish_fish_get(request: web.Request, fish, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons fish

    Retrieve information about a specific fish in *Animal Crossing: New Horizons*.

    :param fish: The name of the fish you wish to retrieve information about.
    :type fish: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fish_get(request: web.Request, x_api_key, accept_version, month=None, excludedetails=None, thumbsize=None) -> web.Response:
    """All New Horizons fish

    Get a list of all fish and their details in *New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param month: Retrive only the fish that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the fish available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month.
    :type month: str
    :param excludedetails: When set to &#x60;true&#x60;, only fish names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of fish in a given month but not all their respective details.
    :type excludedetails: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fossils_all_fossil_get(request: web.Request, fossil, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons fossil group with individual fossils

    Retrieve information about a specific fossil group with their respective individual fossils in *Animal Crossing: New Horizons*.

    :param fossil: The name of the fossil OR fossil group you wish to retrieve information about. If a fossil is provided, a fossil group that the specified fossil belongs to will be returned.
    :type fossil: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fossils_all_get(request: web.Request, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """All New Horizons fossil groups or individual fossil

    Get a list of all the fossil groups with their respective individual fossils in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fossils_groups_fossil_group_get(request: web.Request, fossil_group, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons fossil group

    Retrieve information about a specific fossil group in *Animal Crossing: New Horizons*.

    :param fossil_group: The name of the fossil group you wish to retrieve information about.
    :type fossil_group: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fossils_groups_get(request: web.Request, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """All New Horizons fossil groups

    Get a list of all the fossil groups in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fossils_individuals_fossil_get(request: web.Request, fossil, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons fossil

    Retrieve information about a specific individual fossil in *Animal Crossing: New Horizons*.

    :param fossil: The name of the individual fossil you wish to retrieve fossil information about.
    :type fossil: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_fossils_individuals_get(request: web.Request, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """All New Horizons fossils

    Get a list of all the individual fossils in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_furniture_furniture_get(request: web.Request, furniture, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons furniture

    Retrieve information about a specific furniture in *Animal Crossing: New Horizons*.

    :param furniture: The name of the furniture you wish to retrieve information about.
    :type furniture: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_furniture_get(request: web.Request, x_api_key, accept_version, category=None, color=None, excludedetails=None) -> web.Response:
    """All New Horizons furniture

    Get a list of all furniture and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param category: Specify the category of furniture to return (houswares, miscellaneous, or wall-mounted).
    :type category: str
    :param color: Return furniture that matches the provided colors (may specify one or two colors).
    :type color: List[str]
    :param excludedetails: When set to &#x60;true&#x60;, only furniture names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str

    """
    return web.Response(status=200)


async def nh_interior_get(request: web.Request, x_api_key, accept_version, color=None, excludedetails=None) -> web.Response:
    """All New Horizons interior items

    Get a list of all interior items (flooring, wallpaper, and rugs) and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param color: Return furniture that matches the provided colors (may specify one or two colors).
    :type color: List[str]
    :param excludedetails: When set to &#x60;true&#x60;, only interior item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str

    """
    return web.Response(status=200)


async def nh_interior_item_get(request: web.Request, item, x_api_key, accept_version, color=None, thumbsize=None) -> web.Response:
    """Single New Horizons interior item

    Retrieve information about a specific interior item in *Animal Crossing: New Horizons*.

    :param item: The name of the interior item you wish to retrieve information about.
    :type item: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param color: Return furniture that matches the provided colors (may specify one or two colors).
    :type color: List[str]
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_items_get(request: web.Request, x_api_key, accept_version, excludedetails=None) -> web.Response:
    """Miscellaneous New Horizons items

    Get a list of all miscellaneous items (such as materials, star fragments, fruits, fences, and plants) and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param excludedetails: When set to &#x60;true&#x60;, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str

    """
    return web.Response(status=200)


async def nh_items_item_get(request: web.Request, item, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons miscellaneous item

    Retrieve information about a miscellaneous item (such as materials, star fragments, fruits, fences, and plants) in *Animal Crossing: New Horizons*.

    :param item: The name of the interior item you wish to retrieve information about.
    :type item: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_photos_get(request: web.Request, x_api_key, accept_version, excludedetails=None) -> web.Response:
    """All New Horizons photos and posters

    Get a list of all character photos+posters and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param excludedetails: When set to &#x60;true&#x60;, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str

    """
    return web.Response(status=200)


async def nh_photos_item_get(request: web.Request, item, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons photo or poster

    Retrieve information about a character photo or poster in *Animal Crossing: New Horizons*.

    :param item: The name of the photo or poster you wish to retrieve information about.
    :type item: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_recipes_get(request: web.Request, x_api_key, accept_version, material=None, excludedetails=None, thumbsize=None) -> web.Response:
    """All New Horizons recipes

    Get a list of all recipes and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param material: Specify a material to only get recipes that use that material. You can specify &#x60;material&#x60; up to six times (no recipe uses more than six materials).
    :type material: str
    :param excludedetails: When set to &#x60;true&#x60;, only recipe names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_recipes_item_get(request: web.Request, item, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons recipe

    Retrieve information about a specific recipe in *Animal Crossing: New Horizons*.

    :param item: The name of the item you wish to retrieve recipe information about.
    :type item: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_sea_get(request: web.Request, x_api_key, accept_version, month=None, excludedetails=None, thumbsize=None) -> web.Response:
    """All New Horizons sea creatures

    Get a list of all sea creatures and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param month: Retrive only the sea creature that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the sea creature available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month.
    :type month: str
    :param excludedetails: When set to &#x60;true&#x60;, only sea creature names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of sea creatures in a given month but not all their respective details.
    :type excludedetails: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_sea_sea_creature_get(request: web.Request, sea_creature, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons sea creature

    Retrieve information about a specific sea creature in *Animal Crossing: New Horizons*.

    :param sea_creature: The name of the sea creature you wish to retrieve information about.
    :type sea_creature: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def nh_tools_get(request: web.Request, x_api_key, accept_version, excludedetails=None) -> web.Response:
    """All New Horizons tools

    Get a list of all tools and their details in *Animal Crossing: New Horizons*.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param excludedetails: When set to &#x60;true&#x60;, only tool names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str

    """
    return web.Response(status=200)


async def nh_tools_tool_get(request: web.Request, tool, x_api_key, accept_version, thumbsize=None) -> web.Response:
    """Single New Horizons tool

    Retrieve information about a specific tool in *Animal Crossing: New Horizons*.

    :param tool: The name of the interior item you wish to retrieve information about.
    :type tool: str
    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
    :type thumbsize: int

    """
    return web.Response(status=200)


async def villagers_get(request: web.Request, x_api_key, accept_version, name=None, species=None, personality=None, game=None, birthmonth=None, birthday=None, nhdetails=None, excludedetails=None, thumbsize=None) -> web.Response:
    """Villagers

    This endpoint retrieves villager information from the entire *Animal Crossing* series, with the option to filter by species, personality, game, and/or birthday. Filters use the AND operator (e.g. asking for villagers who have species &#x60;frog&#x60; and personality &#x60;smug&#x60; will return all smug frogs). Note that villagers only include the animals that act as residents. Special characters, such as Tom Nook and Isabelle, are not accessed through this endpoint.

    :param x_api_key: Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
    :type x_api_key: str
    :type x_api_key: str
    :param accept_version: The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
    :type accept_version: str
    :param name: Villager name. For most names you will get back an array with one object, but note that names are not a unique identifier across the series, as there are 3 names that are shared by multiple villagers (Lulu, Petunia, Carmen). For those 3 names you will get back an array with 2 objects. How you disambiguate between these villagers is up to you.
    :type name: str
    :param species: Retrieve villagers of a certain species.
    :type species: str
    :param personality: Retrieve villagers with a certain personality. For &#39;sisterly&#39;, note that the community often also calls it &#39;uchi&#39; or &#39;big sister&#39;.
    :type personality: str
    :param game: Retrieve villagers that appear in all listed games. For example, if you want only villagers that appear in both *New Horizons* and *Pocket Camp*, you would send in &#x60;?game&#x3D;nh&amp;game&#x3D;pc&#x60;.
    :type game: List[str]
    :param birthmonth: Retrieve villagers born in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;) or the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;).
    :type birthmonth: str
    :param birthday: Use with &#x60;birthmonth&#x60; to get villager(s) born on a specific day. Value should be an int, 1 through 31.
    :type birthday: str
    :param nhdetails: When set to &#x60;true&#x60;, an &#x60;nh_details&#x60; object will be included that contains *New Horizons* details about the villager. If the villager does not appear in *New Horizons*, the returned &#x60;nh_details&#x60; field will be set to null.
    :type nhdetails: str
    :param excludedetails: When set to &#x60;true&#x60;, only villager names are returned. Instead of an array of objects with all details, the return will be an array of strings.
    :type excludedetails: str
    :param thumbsize: Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
    :type thumbsize: int

    """
    return web.Response(status=200)
