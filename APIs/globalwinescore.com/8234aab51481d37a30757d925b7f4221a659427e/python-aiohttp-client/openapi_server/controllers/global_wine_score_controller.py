from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def globalwinescores_latest_get(request: web.Request, authorization=None, wine_id=None, vintage=None, color=None, is_primeurs=None, lwin=None, lwin_11=None, limit=None, offset=None, ordering=None) -> web.Response:
    """List all latest GWS

    Returns the latest GWS available per wine/vintage.

    :param authorization: 
    :type authorization: str
    :param wine_id: The exact &#x60;id&#x60; of the wine. Can be used multiple times (e.g &#x60;?wine_id&#x3D;114959&amp;wine_id&#x3D;114952&#x60;) &lt;br/&gt; If you need to find the &#x60;wine_id&#x60; for your wines, use our &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;search page&lt;/a&gt; 
    :type wine_id: List[int]
    :param vintage: The vintage you want to search against.
    :type vintage: str
    :param color: The lowercase color of the wine.
    :type color: str
    :param is_primeurs: Only show the &lt;a href&#x3D;\&quot;See https://en.wikipedia.org/wiki/En_primeur\&quot;&gt;en primeur&lt;/a&gt; GlobalWineScores 
    :type is_primeurs: bool
    :param lwin: L-WIN wine identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;) 
    :type lwin: str
    :param lwin_11: L-WIN wine/vintage identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;) 
    :type lwin_11: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int
    :param ordering: Which field to use when ordering the results.
    :type ordering: str

    """
    return web.Response(status=200)


async def list_historical_gws(request: web.Request, authorization=None, wine_id=None, vintage=None, color=None, is_primeurs=None, lwin=None, lwin_11=None, limit=None, offset=None, ordering=None) -> web.Response:
    """List all historical GWS

    Returns all available GWS

    :param authorization: 
    :type authorization: str
    :param wine_id: The exact &#x60;id&#x60; of the wine. Can be used multiple times (e.g &#x60;?wine_id&#x3D;114959&amp;wine_id&#x3D;114952&#x60;) &lt;br/&gt; If you need to find the &#x60;wine_id&#x60; for your wines, use our &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;search page&lt;/a&gt; 
    :type wine_id: List[int]
    :param vintage: The vintage you want to search against.
    :type vintage: str
    :param color: The lowercase color of the wine.
    :type color: str
    :param is_primeurs: Only show the &lt;a href&#x3D;\&quot;See https://en.wikipedia.org/wiki/En_primeur\&quot;&gt;en primeur&lt;/a&gt; GlobalWineScores 
    :type is_primeurs: bool
    :param lwin: L-WIN wine identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;) 
    :type lwin: str
    :param lwin_11: L-WIN wine/vintage identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;) 
    :type lwin_11: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int
    :param ordering: Which field to use when ordering the results.
    :type ordering: str

    """
    return web.Response(status=200)
