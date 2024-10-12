from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_config import AppConfig
from openapi_server.models.page import Page
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def get_app_config(request: web.Request, include=None, system=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_app_config

    Get the global configuration for an application. Should be called during app statup.  This includes things like device and playback rules, classifications, sitemap and subscriptions.  You have the option to select specific configuration objects using the &#39;include&#39; parameter, or if unspecified, getting all configuration. 

    :param include: A comma delimited list of config objects to return. If none specified then all configuration is returned. 
    :type include: List[str]
    :param system: Classification system to load in case include &#x3D; classification. 
    :type system: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_itv_page(request: web.Request, path, list_page_size=None, list_page_size_large=None, max_list_prefetch=None, item_detail_expand=None, item_detail_select_season=None, text_entry_format=None, max_rating=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_itv_page

    Returns a page with the specified id.  This is a cut down version for low memory devices.123  If targeting the search page you must url encode the search term as a parameter using the &#x60;q&#x60; key. For example if your browser path looks like &#x60;/search?q&#x3D;the&#x60; then what you pass to this endpoint would look like &#x60;/itv/page?path&#x3D;/search%3Fq%3Dthe&#x60;. 

    :param path: The path of the page to load, e.g. &#39;/movies&#39;.
    :type path: str
    :param list_page_size: The number of items to load when prefetching and paging each list in the page row.
    :type list_page_size: int
    :param list_page_size_large: The number of items to load when prefetching a continuous scroll list entry in a page.  By default any list page entry with template pattern &#x60;/^CS\\d+$/&#x60; will be considered a continuous scroll list. 
    :type list_page_size_large: int
    :param max_list_prefetch: The maximum number of lists to prefetch in the page.
    :type max_list_prefetch: int
    :param item_detail_expand: Only relevant when loading item detail pages as these embed a detailed item in the main page entry.  If no value is specified no item dependencies are expanded.  If &#39;children&#39; is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If &#39;all&#39; is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season&#39;s episode list. The season will have its show expanded and the show will have its season list expanded.  The &#39;all&#39; options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If &#39;ancestors&#39; is specified then only the parent chain is included  If an expand is specified which is not relevant to the item type, it will be ignored. 
    :type item_detail_expand: str
    :param item_detail_select_season: Only relevant when loading show detail pages as these embed a detailed item in the main page entry.  Since the introduction of the D1,2,3 templates this parameter is now somewhat redundant, or less likely to have any effect. While it may still be useful in some cases, most of the time the season selection will be dictated by the configuration of the rows scheduled on the show detail page. This parameter will only take effect if there are rows used to schedule episodes of a season, like D1,2,3, or if no rows have a value set for their &#x60;seasonOrder&#x60; custom field.  Given a targeted show page, it can be useful to get the details of a child season. This option provides a means to return the &#x60;first&#x60; or &#x60;latest&#x60; season of a show embedded in the page.  The &#x60;expand&#x60; parameter also works here so for example you could land on a show page and request the &#x60;item_detail_select_season&#x3D;latest&#x60; along with &#x60;item_detail_expand&#x3D;all&#x60;. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries. 
    :type item_detail_select_season: str
    :param text_entry_format: Only relevant to page entries of type &#x60;TextEntry&#x60;.  Converts the value of a text page entry to the specified format. 
    :type text_entry_format: str
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_page(request: web.Request, path, list_page_size=None, list_page_size_large=None, max_list_prefetch=None, item_detail_expand=None, item_detail_select_season=None, text_entry_format=None, max_rating=None, device=None, sub=None, segments=None, ff=None, lang=None) -> web.Response:
    """get_page

    Returns a page with the specified id.  If targeting the search page you must url encode the search term as a parameter using the &#x60;q&#x60; key. For example if your browser path looks like &#x60;/search?q&#x3D;the&#x60; then what you pass to this endpoint would look like &#x60;/page?path&#x3D;/search%3Fq%3Dthe&#x60;. 

    :param path: The path of the page to load, e.g. &#39;/movies&#39;.
    :type path: str
    :param list_page_size: The number of items to load when prefetching and paging each list in the page row.
    :type list_page_size: int
    :param list_page_size_large: The number of items to load when prefetching a continuous scroll list entry in a page.  By default any list page entry with template pattern &#x60;/^CS\\d+$/&#x60; will be considered a continuous scroll list. 
    :type list_page_size_large: int
    :param max_list_prefetch: The maximum number of lists to prefetch in the page.
    :type max_list_prefetch: int
    :param item_detail_expand: Only relevant when loading item detail pages as these embed a detailed item in the main page entry.  If no value is specified no item dependencies are expanded.  If &#39;children&#39; is specified then the list of any direct children will be expanded. For example seasons of a show or episodes of a season.  If &#39;all&#39; is specified then the parent chain will be expanded along with any child list at each level. For example if an episode is specified then its season will be expanded and that season&#39;s episode list. The season will have its show expanded and the show will have its season list expanded.  The &#39;all&#39; options is useful when you deep link into a show/season/episode for the first time as it provides full context for navigating around the show page. Subsequent navigation around children of the show should only need to request expand of children.  If &#39;ancestors&#39; is specified then only the parent chain is included  If an expand is specified which is not relevant to the item type, it will be ignored. 
    :type item_detail_expand: str
    :param item_detail_select_season: Only relevant when loading show detail pages as these embed a detailed item in the main page entry.  Since the introduction of the D1,2,3 templates this parameter is now somewhat redundant, or less likely to have any effect. While it may still be useful in some cases, most of the time the season selection will be dictated by the configuration of the rows scheduled on the show detail page. This parameter will only take effect if there are rows used to schedule episodes of a season, like D1,2,3, or if no rows have a value set for their &#x60;seasonOrder&#x60; custom field.  Given a targeted show page, it can be useful to get the details of a child season. This option provides a means to return the &#x60;first&#x60; or &#x60;latest&#x60; season of a show embedded in the page.  The &#x60;expand&#x60; parameter also works here so for example you could land on a show page and request the &#x60;item_detail_select_season&#x3D;latest&#x60; along with &#x60;item_detail_expand&#x3D;all&#x60;. This would then return the detail of the latest season with its list of child episode summaries, and also expand the detail of the show with its list of seasons summaries. 
    :type item_detail_select_season: str
    :param text_entry_format: Only relevant to page entries of type &#x60;TextEntry&#x60;.  Converts the value of a text page entry to the specified format. 
    :type text_entry_format: str
    :param max_rating: The maximum rating (inclusive) of items returned, e.g. &#39;auoflc-pg&#39;.
    :type max_rating: str
    :param device: The type of device the content is targeting.
    :type device: str
    :param sub: The active subscription code.
    :type sub: str
    :param segments: The list of segments to filter the response by.
    :type segments: List[str]
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)
