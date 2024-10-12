from typing import List, Dict
from aiohttp import web

from openapi_server.models.chapter_object import ChapterObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_several_chapters200_response import GetSeveralChapters200Response
from openapi_server.models.paging_simplified_chapter_object import PagingSimplifiedChapterObject
from openapi_server import util


async def get_a_chapter(request: web.Request, id, market=None) -> web.Response:
    """Get a Chapter 

    Get Spotify catalog information for a single chapter.&lt;br /&gt; **Note: Chapters are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_audiobook_chapters_0(request: web.Request, id, market=None, limit=None, offset=None) -> web.Response:
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


async def get_several_chapters(request: web.Request, ids, market=None) -> web.Response:
    """Get Several Chapters 

    Get Spotify catalog information for several chapters identified by their Spotify IDs.&lt;br /&gt; **Note: Chapters are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)
