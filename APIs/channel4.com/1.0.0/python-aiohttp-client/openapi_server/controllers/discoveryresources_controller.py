from typing import List, Dict
from aiohttp import web

from openapi_server.models.atom import Atom
from openapi_server import util


async def a_to_z_landing_feed(request: web.Request, platform=None) -> web.Response:
    """A to Z Landing Feed

    Lists Channel 4 programmes alphabetically from A to Z, providing the same    functionality and information as is available in the A to Z section of the    Channel 4 Programmes page, http://www.channel4.com/programmes.    http://api.channel4.com/pmlsd/atoz.atom    http://api.channel4.com/pmlsd/atoz.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def a_to_z_letter_feed(request: web.Request, start_letter, platform=None) -> web.Response:
    """A to Z Letter Feed

    Lists Channel 4 programmes whose names begin with the associated letter.    http://api.channel4.com/pmlsd/atoz/start_letter.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/atoz/a.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param start_letter: The letter of the alphabet for which you seek associated Channel 4 programmes
    :type start_letter: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def a_to_z_letter_feed2(request: web.Request, start_letter, pageno, platform=None) -> web.Response:
    """A to Z Letter Feed(2)

    Lists Channel 4 programmes whose names begin with the associated letter.    http://api.channel4.com/pmlsd/atoz/start_letter/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/atoz/a.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param start_letter: The letter of the alphabet for which you seek associated Channel 4 programmes
    :type start_letter: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_title(request: web.Request, category, platform=None) -> web.Response:
    """All Programmes by Title

    Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_title2(request: web.Request, category, channel, platform=None) -> web.Response:
    """All Programmes by Title(2)

    Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_title3(request: web.Request, category, platform=None) -> web.Response:
    """All Programmes by Title(3)

    Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_title4(request: web.Request, category, pageno, platform=None) -> web.Response:
    """All Programmes by Title(4)

    Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_title5(request: web.Request, category, channel, pageno, platform=None) -> web.Response:
    """All Programmes by Title(5)

    Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_title6(request: web.Request, category, pageno, platform=None) -> web.Response:
    """All Programmes by Title(6)

    Lists all Channel 4 programmes associated with the specified category (tag),    alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/history/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_tx_date(request: web.Request, category, platform=None) -> web.Response:
    """All Programmes by TX Date

    Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_tx_date2(request: web.Request, category, channel, platform=None) -> web.Response:
    """All Programmes by TX Date(2)

    Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_tx_date3(request: web.Request, category, platform=None) -> web.Response:
    """All Programmes by TX Date(3)

    Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_tx_date4(request: web.Request, category, pageno, platform=None) -> web.Response:
    """All Programmes by TX Date(4)

    Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_tx_date5(request: web.Request, category, channel, pageno, platform=None) -> web.Response:
    """All Programmes by TX Date(5)

    Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def all_programmes_by_tx_date6(request: web.Request, category, pageno, platform=None) -> web.Response:
    """All Programmes by TX Date(6)

    Lists all Channel 4 programmes associated with the specified category (tag).     By default, the programmes are listed in order of Transmission (TX) Date,    with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_browse_by_date_feed(request: web.Request, yyyy, mm, dd, platform=None) -> web.Response:
    """4oD Browse by Date Feed

    Information of daily broadcast content available on 4oD, according to    broadcast date    http://api.channel4.com/pmlsd/4od/episode-list/date/[yyyy]/[mm]/[dd].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/4od/episode-list/date/2010/11/28.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param yyyy: The date for which you wish to see programming information
    :type yyyy: str
    :param mm: The date for which you wish to see programming information
    :type mm: str
    :param dd: The date for which you wish to see programming information
    :type dd: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_clips_catch_up_feed(request: web.Request, platform=None) -> web.Response:
    """4oD Clips Catch Up Feed

    A feed containing metadata about short-form content relating to 4oD Episodes    recently added to 4oD based on linear transmission. The entries for the    Clips Landing Feed contain references to each short-form asset. It will    return up to 20 entries.    http://api.channel4.com/pmlsd/4od/recently-added/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/4od/episode-list/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_most_popular_episodes_feed(request: web.Request, platform=None) -> web.Response:
    """4oD Most Popular Episodes Feed

    Information of the most popular content available on 4oD, according to user    data driven.    http://api.channel4.com/pmlsd/4od/episode-list/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/4od/episode-list/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_popular_all_brands_feed(request: web.Request, platform=None) -> web.Response:
    """4oD Popular All Brands Feed

    Lists all Channel 4 programmes available on 4oD by popularity considering    the data gathered within the last 7 days.    http://api.channel4.com/pmlsd/brands/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_popular_all_brands_feed2(request: web.Request, pageno, platform=None) -> web.Response:
    """4oD Popular All Brands Feed(2)

    Lists all Channel 4 programmes available on 4oD by popularity considering    the data gathered within the last 7 days.    http://api.channel4.com/pmlsd/brands/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_title(request: web.Request, category, platform=None) -> web.Response:
    """4oD Programmes by Title

    Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/4od/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_title2(request: web.Request, category, channel, platform=None) -> web.Response:
    """4oD Programmes by Title(2)

    Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_title3(request: web.Request, category, platform=None) -> web.Response:
    """4oD Programmes by Title(3)

    Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_title4(request: web.Request, category, pageno, platform=None) -> web.Response:
    """4oD Programmes by Title(4)

    Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/4od/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_title5(request: web.Request, category, channel, pageno, platform=None) -> web.Response:
    """4oD Programmes by Title(5)

    Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_title6(request: web.Request, category, pageno, platform=None) -> web.Response:
    """4oD Programmes by Title(6)

    Lists all Channel 4oD programmes associated with the specified category    (tag), alphanumerically in order of Title.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/title/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/religion-and-belief/4oD/title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_tx_date(request: web.Request, category, platform=None) -> web.Response:
    """4oD Programmes by TX Date

    Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_tx_date2(request: web.Request, category, channel, platform=None) -> web.Response:
    """4oD Programmes by TX Date(2)

    Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_tx_date3(request: web.Request, category, platform=None) -> web.Response:
    """4oD Programmes by TX Date(3)

    Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_tx_date4(request: web.Request, category, pageno, platform=None) -> web.Response:
    """4oD Programmes by TX Date(4)

    Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_tx_date5(request: web.Request, category, channel, pageno, platform=None) -> web.Response:
    """4oD Programmes by TX Date(5)

    Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_programmes_by_tx_date6(request: web.Request, category, pageno, platform=None) -> web.Response:
    """4oD Programmes by TX Date(6)

    Lists all Channel 4oD programmes associated with the specified category    (tag).By default, the programmes are listed in order of Transmission (TX)    Date, with the most-recently-transmitted programmes listed first.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/animals/4oD.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_title_all_brands_feed(request: web.Request, platform=None) -> web.Response:
    """4oD Title All Brands Feed

    Lists all Channel 4 programmes available on 4oD.  By default, the programmes    are listed by title in alphabetical order (case unsensitive).    http://api.channel4.com/pmlsd/brands/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_title_all_brands_feed2(request: web.Request, pageno, platform=None) -> web.Response:
    """4oD Title All Brands Feed(2)

    Lists all Channel 4 programmes available on 4oD.  By default, the programmes    are listed by title in alphabetical order (case unsensitive).    http://api.channel4.com/pmlsd/brands/4od/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def categories_landing_feed(request: web.Request, platform=None) -> web.Response:
    """Categories Landing Feed

    Lists Channel 4 programmes by category (/ tag).    http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def collections_feed(request: web.Request, collection_name, platform=None) -> web.Response:
    """Collections Feed

    Collections are editorially controlled groups of brands, series, episodes or    other collections used for promotion and discovery of content. A SIMPLE    collection can contain an assortment of Brands, Series, Episodes or Freeform    items. A GROUP collection contains other collections.    http://api.channel4.com/pmlsd/collections/collection_name/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param collection_name: Web safe title for the collection.
    :type collection_name: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def collections_feed2(request: web.Request, collection_name, platform=None) -> web.Response:
    """Collections Feed(2)

    Collections are editorially controlled groups of brands, series, episodes or    other collections used for promotion and discovery of content. A SIMPLE    collection can contain an assortment of Brands, Series, Episodes or Freeform    items. A GROUP collection contains other collections.    http://api.channel4.com/pmlsd/collections/collection_name.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param collection_name: Web safe title for the collection.
    :type collection_name: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def flattened_collection_feed(request: web.Request, collection_name, platform=None) -> web.Response:
    """Flattened Collection Feed

    The Flattened Collections Feed is only applicable for GROUP collections and    its purpose is mainly return 3 items (BRAND, SERIES or EPSIODE) of each of    the simple collections assigned to the GROUP.    http://api.channel4.com/pmlsd/collections/collection_name/flattened/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/flattened/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param collection_name: Web safe title for the collection.
    :type collection_name: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def flattened_collection_feed2(request: web.Request, collection_name, platform=None) -> web.Response:
    """Flattened Collection Feed(2)

    The Flattened Collections Feed is only applicable for GROUP collections and    its purpose is mainly return 3 items (BRAND, SERIES or EPSIODE) of each of    the simple collections assigned to the GROUP.    http://api.channel4.com/pmlsd/collections/collection_name/flattened.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/collections/4od-home-promo/flattened/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param collection_name: Web safe title for the collection.
    :type collection_name: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed(request: web.Request, category, platform=None) -> web.Response:
    """Most Popular Brands Feed

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed2(request: web.Request, category, platform=None) -> web.Response:
    """Most Popular Brands Feed(2)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed3(request: web.Request, category, channel, platform=None) -> web.Response:
    """Most Popular Brands Feed(3)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed4(request: web.Request, category, platform=None) -> web.Response:
    """Most Popular Brands Feed(4)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed5(request: web.Request, category, pageno, platform=None) -> web.Response:
    """Most Popular Brands Feed(5)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed6(request: web.Request, category, pageno, platform=None) -> web.Response:
    """Most Popular Brands Feed(6)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed7(request: web.Request, category, channel, pageno, platform=None) -> web.Response:
    """Most Popular Brands Feed(7)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/channel/[channel]/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param channel: The name of the channel for which you seek associated Channel 4oD programmes
    :type channel: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def most_popular_brands_feed8(request: web.Request, category, pageno, platform=None) -> web.Response:
    """Most Popular Brands Feed(8)

    Lists all Channel 4oD most popular brands for the given category within the    last 7 days, in order of popularity.    http://api.channel4.com/pmlsd/categories/category/derived/ad/4od/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/categories/comedy/4od/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The name of the category for which you seek associated Channel 4 programmes. (For a full list of categories, please see http://api.channel4.com/pmlsd/categories.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx)
    :type category: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def popular_brands_feed(request: web.Request, platform=None) -> web.Response:
    """Popular Brands Feed

    Lists all Channel 4 programmes by popularity considering the data gathered    within the last 7 days.    http://api.channel4.com/pmlsd/brands/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def popular_brands_feed2(request: web.Request, pageno, platform=None) -> web.Response:
    """Popular Brands Feed(2)

    Lists all Channel 4 programmes by popularity considering the data gathered    within the last 7 days.    http://api.channel4.com/pmlsd/brands/popular/page-{pageno}.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/brands/popular.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def search_feed(request: web.Request, q, platform=None) -> web.Response:
    """Search Feed

    Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search.atom?q&#x3D;search-term&amp;apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param q: The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    :type q: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def search_feed2(request: web.Request, q, platform=None) -> web.Response:
    """Search Feed(2)

    Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search/search-term.atom?apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param q: The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    :type q: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def search_feed3(request: web.Request, q, pageno, platform=None) -> web.Response:
    """Search Feed(3)

    Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search/page-{pageno}.atom?q&#x3D;search-term&amp;apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param q: The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    :type q: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def search_feed4(request: web.Request, q, pageno, platform=None) -> web.Response:
    """Search Feed(4)

    Lists all Channel 4 programmes where title (brand name) matching the search    term. Matches are made from the beginning of individual words in the title.    http://api.channel4.com/pmlsd/search/search-term/page-{pageno}.atom?apikey&#x3D;xxx    http://api.channel4.com/pmlsd/search.atom?q&#x3D;the+it+crowd&amp;apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param q: The programme name to look for, minimum length: 2 chars.Looking for programme names with special chars might be URL encoded.
    :type q: str
    :param pageno: Page number of results to return
    :type pageno: int
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def t_v_listings_feed(request: web.Request, yyyy, mm, dd, platform=None) -> web.Response:
    """TV Listings Feed

    EPG Information of daily broadcast content aired per channels, according to    broadcast date    http://api.channel4.com/pmlsd/tv-listings/daily/[yyyy]/[mm]/[dd].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/tv-listings/daily/2010/11/28.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param yyyy: The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    :type yyyy: str
    :param mm: The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    :type mm: str
    :param dd: The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    :type dd: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def t_v_listings_feed2(request: web.Request, yyyy, mm, dd, channel, platform=None) -> web.Response:
    """TV Listings Feed(2)

    EPG Information of daily broadcast content aired per channels, according to    broadcast date    http://api.channel4.com/pmlsd/tv-listings/daily/[yyyy]/[mm]/[dd]/[channel].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/tv-listings/daily/2010/11/28.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param yyyy: The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    :type yyyy: str
    :param mm: The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    :type mm: str
    :param dd: The date for which you wish to see programming information. Note the schedule days start from 6am and run until 6am on the next calendar day.
    :type dd: str
    :param channel: The EPG for a specific channel (c4, e4, m4, 4m, f4, 4s)
    :type channel: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)
