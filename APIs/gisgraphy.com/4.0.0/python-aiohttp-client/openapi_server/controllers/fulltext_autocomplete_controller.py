from typing import List, Dict
from aiohttp import web

from openapi_server.models.fulltext_results_dto import FulltextResultsDto
from openapi_server import util


async def fulltxtsearch(request: web.Request, q, allwordsrequired, spellchecking=None, lat=None, lng=None, radius=None, suggest=None, style=None, country=None, lang=None, format=None, _from=None, to=None, param_callback=None, indent=None) -> web.Response:
    """search for places by text around a GPS point

    The full text service allows you to search for features / places / street and do autocompletion . you can : Specify one or more words search on part of the name (auto completion / suggestion) Search for text or zip code Specify a GPS restriction (promote nearest, not sorted but has an impact on the score), Limit the results to a specific Language, Country, place type, Paginate the results, Specify the output verbosity, Tells if you want the output to be indented, Tells that all words are required or not, The search is case insensitive, use synonyms (Saint/st, ..), separator characters stripping, ...

    :param q: The searched text : The text for the query can be a zip code, a string or one or more strings
    :type q: str
    :param allwordsrequired: Whether the fulltext engine should considers all the words specified as required. Defaults to false (since v 4.0). possible values are true|false (or &#39;on&#39; when used with the rest service)
    :type allwordsrequired: bool
    :param spellchecking: The spellchecking (optional) : whether some suggestions should be provided if no results are found
    :type spellchecking: str
    :param lat: The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
    :type lat: float
    :param lng: TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
    :type lng: float
    :param radius: distance from the location point in meters we&#39;d like to search around. The value is a number &gt; 0 if it is not specify or incorrect.
    :type radius: float
    :param suggest: If this parameter is set then it will search in part of the names of the street, place,.... It allow you to do auto completion auto suggestion. See the Gisgraphy leaflet plugin for more details. The JSON format will be forced if this parameter is true. See auto completion / suggestions engine for more details
    :type suggest: bool
    :param style: The output style verbosity (optional) : Determines the output verbosity. 4 styles are available
    :type style: str
    :param country: limit the search to the specified ISO 3166 country code. Default : search in all countries
    :type country: str
    :param lang: The language code (optional) : The iso 639 Alpha2 or alpha3 Language Code. Some properties such as the AlternateName AdmNames and countryname belong to a certain language code. The language parameter can limit the output of those fields to a certain language (it only apply when style parameter&#x3D;&#39;style&#39;) : If the language code does not exists or is not specified, properties with all the languages are retrieved If it exists, the properties with the specified language code, are retrieved
    :type lang: str
    :param format: The output format.
    :type format: str
    :param _from: The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1
    :type _from: int
    :param to: The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed)
    :type to: int
    :param param_callback: The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
    :type param_callback: str
    :param indent: indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39;
    :type indent: bool

    """
    return web.Response(status=200)
