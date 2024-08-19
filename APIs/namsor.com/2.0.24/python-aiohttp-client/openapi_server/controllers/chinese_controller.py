from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_first_last_name_gender_in import BatchFirstLastNameGenderIn
from openapi_server.models.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from openapi_server.models.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_server.models.batch_match_personal_first_last_name_in import BatchMatchPersonalFirstLastNameIn
from openapi_server.models.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from openapi_server.models.batch_name_matched_out import BatchNameMatchedOut
from openapi_server.models.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_server.models.batch_personal_name_in import BatchPersonalNameIn
from openapi_server.models.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_server.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_server.models.name_match_candidates_out import NameMatchCandidatesOut
from openapi_server.models.name_matched_out import NameMatchedOut
from openapi_server.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_server.models.personal_name_parsed_out import PersonalNameParsedOut
from openapi_server import util


async def chinese_name_candidates(request: web.Request, chinese_surname_latin, chinese_given_name_latin) -> web.Response:
    """Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming

    

    :param chinese_surname_latin: 
    :type chinese_surname_latin: str
    :param chinese_given_name_latin: 
    :type chinese_given_name_latin: str

    """
    return web.Response(status=200)


async def chinese_name_candidates_batch(request: web.Request, body=None) -> web.Response:
    """Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming

    

    :param body: A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def chinese_name_candidates_gender_batch(request: web.Request, body=None) -> web.Response:
    """Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname) ex. Wang Xiaoming.

    

    :param body: A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGenderIn.from_dict(body)
    return web.Response(status=200)


async def chinese_name_gender_candidates(request: web.Request, chinese_surname_latin, chinese_given_name_latin, known_gender) -> web.Response:
    """Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender (&#39;male&#39; or &#39;female&#39;)

    

    :param chinese_surname_latin: 
    :type chinese_surname_latin: str
    :param chinese_given_name_latin: 
    :type chinese_given_name_latin: str
    :param known_gender: 
    :type known_gender: str

    """
    return web.Response(status=200)


async def chinese_name_match(request: web.Request, chinese_surname_latin, chinese_given_name_latin, chinese_name) -> web.Response:
    """Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming

    

    :param chinese_surname_latin: 
    :type chinese_surname_latin: str
    :param chinese_given_name_latin: 
    :type chinese_given_name_latin: str
    :param chinese_name: 
    :type chinese_name: str

    """
    return web.Response(status=200)


async def chinese_name_match_batch(request: web.Request, body=None) -> web.Response:
    """Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming

    

    :param body: A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname
    :type body: dict | bytes

    """
    body = BatchMatchPersonalFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def gender_chinese_name(request: web.Request, chinese_name) -> web.Response:
    """Infer the likely gender of a Chinese full name ex. 王晓明

    

    :param chinese_name: 
    :type chinese_name: str

    """
    return web.Response(status=200)


async def gender_chinese_name_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 full names ex. 王晓明

    

    :param body: A list of personal names, with a country ISO2 code
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)


async def gender_chinese_name_pinyin(request: web.Request, chinese_surname_latin, chinese_given_name_latin) -> web.Response:
    """Infer the likely gender of a Chinese name in LATIN (Pinyin).

    

    :param chinese_surname_latin: 
    :type chinese_surname_latin: str
    :param chinese_given_name_latin: 
    :type chinese_given_name_latin: str

    """
    return web.Response(status=200)


async def gender_chinese_name_pinyin_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).

    

    :param body: A list of names, with country code.
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def parse_chinese_name(request: web.Request, chinese_name) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name)

    

    :param chinese_name: 
    :type chinese_name: str

    """
    return web.Response(status=200)


async def parse_chinese_name_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name).

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)


async def pinyin_chinese_name(request: web.Request, chinese_name) -> web.Response:
    """Romanize the Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name)

    

    :param chinese_name: 
    :type chinese_name: str

    """
    return web.Response(status=200)


async def pinyin_chinese_name_batch(request: web.Request, body=None) -> web.Response:
    """Romanize a list of Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name).

    

    :param body: A list of Chinese names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)
