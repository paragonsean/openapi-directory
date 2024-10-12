from typing import List, Dict
from aiohttp import web

from openapi_server.models.atom import Atom
from openapi_server import util


async def brand_epg_atom_feed(request: web.Request, brand_web_safe_title, platform=None) -> web.Response:
    """Brand EPG Atom Feed

    This feed contains metadata about upcoming electronic programme guide (EPG)    information for a brand. The entry details upcoming transmission slots for    this brand.    http://api.channel4.com/pmlsd/brand-web-safe-title/epg.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-simpsons/epg.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: Title of the programme for which you seek EPG information
    :type brand_web_safe_title: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def call4o_d_feed(request: web.Request, brand_web_safe_title, platform=None) -> web.Response:
    """4oD Feed

    A feed containing all available on-demand long-form content for a specified    brand. The entries for the 4oD feed contain references to each long-form    asset for a brand, ordered by series number and episode number.    http://api.channel4.com/pmlsd/[brand-web-safe-title]/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: The title of the programme for which you seek on-demand content
    :type brand_web_safe_title: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def clip_detail_atom_feed(request: web.Request, brand_web_safe_title, clip_asset_id, platform=None) -> web.Response:
    """Clip Detail Atom Feed

    A feed containing metadata about a single short-form video (clip).    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/clip-asset-id.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/videos/TCGS_CLIP_0000001015.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: Title of the brand for which you seek a clip
    :type brand_web_safe_title: str
    :param clip_asset_id: Asset id for this clip
    :type clip_asset_id: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def clips_landing_feed_brand_series_and_episode_levels(request: web.Request, brand_web_safe_title, platform=None) -> web.Response:
    """Clips Landing Feed Brand Series and Episode Levels

    A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/all.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: Title of brand to which clips belong
    :type brand_web_safe_title: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def clips_landing_feed_brand_series_and_episode_levels2(request: web.Request, brand_web_safe_title, series_number, platform=None) -> web.Response:
    """Clips Landing Feed Brand Series and Episode Levels(2)

    A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/series-series_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: Title of brand to which clips belong
    :type brand_web_safe_title: str
    :param series_number: Unique identifier of series to which clips belong
    :type series_number: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def clips_landing_feed_brand_series_and_episode_levels3(request: web.Request, brand_web_safe_title, series_number, episode_number, platform=None) -> web.Response:
    """Clips Landing Feed Brand Series and Episode Levels(3)

    A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/series-series_number/episode-episode_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: Title of brand to which clips belong
    :type brand_web_safe_title: str
    :param series_number: Unique identifier of series to which clips belong
    :type series_number: str
    :param episode_number: Unique identifier of episode to which clips belong
    :type episode_number: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def coming_soon_feed(request: web.Request, platform=None) -> web.Response:
    """Coming Soon feed

    Coming Soon feed display a list of episodes coming soon to linear TV so that    I can promote new Channel 4 content.    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def coming_soon_feed2(request: web.Request, category, platform=None) -> web.Response:
    """Coming Soon feed(2)

    Coming Soon feed display a list of episodes coming soon to linear TV so that    I can promote new Channel 4 content.    http://api.channel4.com/pmlsd/coming-soon/[category].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param category: The category websafe_title to filter the coming soon programmes on TV.
    :type category: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def episode_guide_feed_episode_detail(request: web.Request, brand_web_safe_title, series_number, episode_number, platform=None) -> web.Response:
    """Episode Guide Feed Episode Detail

    A feed containing metadata about a specified episode. (This feed does not    contain any entries and only contains a feed element regarding this    episode.)    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide/series-series_number/episode-episode_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/episode-guide/series-1/episode-1.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: Title of the brand to which the episode belongs
    :type brand_web_safe_title: str
    :param series_number: Unique enumerated identifier of the series within its brand to which the episode belongs
    :type series_number: str
    :param episode_number: Unique enumerated identifier of the episode within its series
    :type episode_number: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def episode_guide_feed_series_detail(request: web.Request, brand_web_safe_title, series_number, platform=None) -> web.Response:
    """Episode Guide Feed Series Detail

    A feed containing metadata about all the episodes for a specific series. The    entries in this feed contain references to each of the episodes (where    metadata has been published), with some convenient links.    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide/series-series_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/chelmsford-123/episode-guide/series-1.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: The title of the programme for which you seek series-related information
    :type brand_web_safe_title: str
    :param series_number: Unique enumerated identifier of the series within its brand
    :type series_number: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def episode_guide_feed_series_landing(request: web.Request, brand_web_safe_title, platform=None) -> web.Response:
    """Episode Guide Feed Series Landing

    A feed containing metadata about all series for a specified brand. The    entries in this feed contain references to each of the series (where    metadata has been published), with some convenient links.    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/father-ted/episode-guide.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: The title of the programme for which you seek episode-guide information
    :type brand_web_safe_title: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def hub_feed(request: web.Request, brand_web_safe_title, platform=None) -> web.Response:
    """Hub Feed

    The basis for all brand information    http://api.channel4.com/pmlsd/brand-web-safe-title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param brand_web_safe_title: The title of the programme for which you seek associated data
    :type brand_web_safe_title: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)


async def programme_feed(request: web.Request, programme_id, platform=None) -> web.Response:
    """Programme Feed

    A feed containing all long-form content currently or previously available    for a specified Programme Id. The entries for the Programme feed contain    references to long-form assets for each platform.    http://api.channel4.com/pmlsd/programme/[programme-id].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/programme/33881-001/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

    :param programme_id: The websafe programme identifier for the episode for which you seek on-demand content
    :type programme_id: str
    :param platform: The platform to use for the query. Alias &#39;client&#39;.
    :type platform: str

    """
    return web.Response(status=200)
