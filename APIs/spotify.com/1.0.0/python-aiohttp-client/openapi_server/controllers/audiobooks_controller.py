from typing import List, Dict
from aiohttp import web

from openapi_server.models.audiobook_object import AudiobookObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_audiobooks200_response import GetMultipleAudiobooks200Response
from openapi_server.models.paging_simplified_audiobook_object import PagingSimplifiedAudiobookObject
from openapi_server.models.paging_simplified_chapter_object import PagingSimplifiedChapterObject
from openapi_server import util


async def check_users_saved_audiobooks(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Audiobooks 

    Check if one or more audiobooks are already saved in the current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def get_an_audiobook(request: web.Request, id, market=None) -> web.Response:
    """Get an Audiobook 

    Get Spotify catalog information for a single audiobook.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_audiobook_chapters(request: web.Request, id, market=None, limit=None, offset=None) -> web.Response:
    """Get Audiobook Chapters 

    Get Spotify catalog information about an audiobook&#39;s chapters.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

    :param id: 
    :type id: str
    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_multiple_audiobooks(request: web.Request, ids, market=None) -> web.Response:
    """Get Several Audiobooks 

    Get Spotify catalog information for several audiobooks identified by their Spotify IDs.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_users_saved_audiobooks(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Audiobooks 

    Get a list of the audiobooks saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def remove_audiobooks_user(request: web.Request, ids) -> web.Response:
    """Remove User&#39;s Saved Audiobooks 

    Remove one or more audiobooks from the Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def save_audiobooks_user(request: web.Request, ids) -> web.Response:
    """Save Audiobooks for Current User 

    Save one or more audiobooks to the current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)
