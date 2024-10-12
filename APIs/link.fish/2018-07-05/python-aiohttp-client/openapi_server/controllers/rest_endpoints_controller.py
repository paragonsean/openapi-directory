from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_respons_error import ApiResponsError
from openapi_server.models.apps import Apps
from openapi_server.models.data_raw import DataRaw
from openapi_server.models.data_tabular import DataTabular
from openapi_server.models.geo_coordinates import GeoCoordinates
from openapi_server.models.social_media import SocialMedia
from openapi_server.models.url import Url
from openapi_server.models.url_browser import UrlBrowser
from openapi_server import util


async def urls_apps_get(request: web.Request, url, return_urls=None, browser_render=None) -> web.Response:
    """Get mobile apps

    Visits the URL and checks if there are mobile apps on them and returns the found ones.  Will by default return the app identifiers and not the full URL to the apps. To return URLs instead set the parameter \&quot;return_urls\&quot; to true.  The URLs can also be created manually like this:  | Property | URL                                                | | -------- | -------------------------------------------------- | | android  | https://play.google.com/store/apps/details?id&#x3D;{ID} | | ios      | https://itunes.apple.com/us/app/app-name/id{ID}    |  Properties only get set when a value for it has been found. That means that if no app has been found only the property \&quot;url\&quot; will be set. 

    :param url: The URL of the website to query
    :type url: str
    :param return_urls: Returns app URLs instead of the identifiers
    :type return_urls: bool
    :param browser_render: If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    :type browser_render: bool

    """
    return web.Response(status=200)


async def urls_browser_data_get(request: web.Request, url, item_format=None, simplify_special_types=None, include_raw_html=None, screenshot=None, screenshot_width=None, screenshot_file_format=None) -> web.Response:
    """Extract data (browser)

    Visits the URL with a full browser and extracts the data. This request costs 5 credits.

    :param url: The URL of the website to query
    :type url: str
    :param item_format: If the items should be return \&quot;normal\&quot; with multiple levels or \&quot;flat\&quot; with just one level and linked instead.
    :type item_format: str
    :param simplify_special_types: Some types like \&quot;PropertyValue\&quot; do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -&gt; value format.
    :type simplify_special_types: bool
    :param include_raw_html: Returns additionally also the raw HTML as property \&quot;rawHtml\&quot;.
    :type include_raw_html: bool
    :param screenshot: If and what kind of screenshot should be returned. Do only request screenshot generation when really needed because it will increase the response time significantly.
    :type screenshot: str
    :param screenshot_width: The widh of the screenshot in pixel.
    :type screenshot_width: int
    :param screenshot_file_format: The file format of the screenshot
    :type screenshot_file_format: str

    """
    return web.Response(status=200)


async def urls_browser_screenshot_get(request: web.Request, url, type=None, file_format=None, width=None) -> web.Response:
    """Generate screenshot (browser)

    Visits the URL with full browser and creates a screenshot. This request costs 5 credits.

    :param url: The URL of the website to create screenshot of
    :type url: str
    :param type: What kind of screenshot should be returned. If it should be a regular 16:9 screenshot or one with the full page height
    :type type: str
    :param file_format: The file format of the screenshot
    :type file_format: str
    :param width: The widh of the screenshot in pixel.
    :type width: int

    """
    return web.Response(status=200)


async def urls_data_get(request: web.Request, url, item_format=None, simplify_special_types=None, include_raw_html=None, browser_render=None) -> web.Response:
    """Extract data

    Visits the URL and extracts the data.

    :param url: The URL of the website to query
    :type url: str
    :param item_format: If the items should be return \&quot;normal\&quot; with multiple levels or \&quot;flat\&quot; with just one level and linked instead.
    :type item_format: str
    :param simplify_special_types: Some types like \&quot;PropertyValue\&quot; do save key and value in separate properties which makes the data harder to process. If this option gets set it converts them automatically into the regular key -&gt; value format.
    :type simplify_special_types: bool
    :param include_raw_html: Returns additionally also the raw HTML as property \&quot;rawHtml\&quot;.
    :type include_raw_html: bool
    :param browser_render: If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    :type browser_render: bool

    """
    return web.Response(status=200)


async def urls_data_raw_get(request: web.Request, url) -> web.Response:
    """Return data of JSON/XML

    Visits the URL and extracts the data.

    :param url: The URL to get the data of
    :type url: str

    """
    return web.Response(status=200)


async def urls_data_tabular_get(request: web.Request, url, selector=None, browser_render=None) -> web.Response:
    """Return tabular data

    Visits the URL and extracts tabular data.

    :param url: The URL to get the data of
    :type url: str
    :param selector: CSS selector to define tabular data which should get returned
    :type selector: str
    :param browser_render: If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    :type browser_render: bool

    """
    return web.Response(status=200)


async def urls_geo_coordinates_get(request: web.Request, url, browser_render=None) -> web.Response:
    """Get geo coordinates

    Visits the URL and checks if there are Geo Coordinates on them and returns the found ones.  Properties only get set when a value for both latitude and longitude have been found. That means that if no geo coordinates have been found only the property \&quot;url\&quot; will be set.

    :param url: The URL of the website to query
    :type url: str
    :param browser_render: If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    :type browser_render: bool

    """
    return web.Response(status=200)


async def urls_social_media_get(request: web.Request, url, return_urls=None, browser_render=None) -> web.Response:
    """Get social media accounts

    Visits the URL and checks if there are any social media accounts and returns the found ones.  Will by default return the account identifiers and not the full URL to the profiles. To return URLs instead set the parameter \&quot;return_urls\&quot; to true.  The URLs can also be created manually like this:  | Property        | URL                                    | | --------------- | -------------------------------------- | | facebookPage    | https://facebook.com/{ID}              | | githubUser      | https://github.com/{ID}                | | googlePlus      | https://plus.google.com/+{ID}          | | instagram       | https://instagram.com/{ID}             | | linkedInCompany | https://linkedin.com/company/{ID}      | | pinterest       | https://pinterest.com/{ID}             | | twitter         | https://twitter.com/{ID}               | | youTubeUser     | https://youtube.com/user/{ID}          |  Properties only get set when a value for it has been found. That means that if no social media account has been found only the property \&quot;url\&quot; will be set. 

    :param url: The URL of the website to query
    :type url: str
    :param return_urls: Returns profile URLs instead of the profile names/ids
    :type return_urls: bool
    :param browser_render: If the page should be fully rendered with a browser to extract data. The request will then cost 5 credits instead of 1!
    :type browser_render: bool

    """
    return web.Response(status=200)
