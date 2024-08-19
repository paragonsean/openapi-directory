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
from openapi_server.models.feedback_loop_out import FeedbackLoopOut
from openapi_server.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_server.models.name_match_candidates_out import NameMatchCandidatesOut
from openapi_server.models.name_matched_out import NameMatchedOut
from openapi_server.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_server.models.personal_name_parsed_out import PersonalNameParsedOut
from openapi_server import util


async def gender_japanese_name_full(request: web.Request, japanese_name) -> web.Response:
    """Infer the likely gender of a Japanese full name ex. 王晓明

    

    :param japanese_name: 
    :type japanese_name: str

    """
    return web.Response(status=200)


async def gender_japanese_name_full_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 full names

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)


async def gender_japanese_name_pinyin(request: web.Request, japanese_surname, japanese_given_name) -> web.Response:
    """Infer the likely gender of a Japanese name in LATIN (Pinyin).

    

    :param japanese_surname: 
    :type japanese_surname: str
    :param japanese_given_name: 
    :type japanese_given_name: str

    """
    return web.Response(status=200)


async def gender_japanese_name_pinyin_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).

    

    :param body: A list of names, with country code.
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def japanese_name_gender_kanji_candidates_batch(request: web.Request, body=None) -> web.Response:
    """Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae

    

    :param body: A list of personal japanese names in LATIN, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname and known gender
    :type body: dict | bytes

    """
    body = BatchFirstLastNameGenderIn.from_dict(body)
    return web.Response(status=200)


async def japanese_name_kanji_candidates(request: web.Request, japanese_surname_latin, japanese_given_name_latin, known_gender) -> web.Response:
    """Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.

    

    :param japanese_surname_latin: 
    :type japanese_surname_latin: str
    :param japanese_given_name_latin: 
    :type japanese_given_name_latin: str
    :param known_gender: 
    :type known_gender: str

    """
    return web.Response(status=200)


async def japanese_name_kanji_candidates1(request: web.Request, japanese_surname_latin, japanese_given_name_latin) -> web.Response:
    """Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae

    

    :param japanese_surname_latin: 
    :type japanese_surname_latin: str
    :param japanese_given_name_latin: 
    :type japanese_given_name_latin: str

    """
    return web.Response(status=200)


async def japanese_name_kanji_candidates_batch(request: web.Request, body=None) -> web.Response:
    """Identify japanese name candidates in KANJI, based on the romanized name (firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname), ex. Yamamoto Sanae

    

    :param body: A list of personal japanese names in LATIN, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def japanese_name_latin_candidates(request: web.Request, japanese_surname_kanji, japanese_given_name_kanji) -> web.Response:
    """Romanize japanese name, based on the name in Kanji.

    

    :param japanese_surname_kanji: 
    :type japanese_surname_kanji: str
    :param japanese_given_name_kanji: 
    :type japanese_given_name_kanji: str

    """
    return web.Response(status=200)


async def japanese_name_latin_candidates_batch(request: web.Request, body=None) -> web.Response:
    """Romanize japanese names, based on the name in KANJI

    

    :param body: A list of personal japanese names in KANJI, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname
    :type body: dict | bytes

    """
    body = BatchFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def japanese_name_match(request: web.Request, japanese_surname_latin, japanese_given_name_latin, japanese_name) -> web.Response:
    """Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae

    

    :param japanese_surname_latin: 
    :type japanese_surname_latin: str
    :param japanese_given_name_latin: 
    :type japanese_given_name_latin: str
    :param japanese_name: 
    :type japanese_name: str

    """
    return web.Response(status=200)


async def japanese_name_match_batch(request: web.Request, body=None) -> web.Response:
    """Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae

    

    :param body: A list of personal Japanese names in LATIN, firstName &#x3D; japaneseGivenName; lastName&#x3D;japaneseSurname
    :type body: dict | bytes

    """
    body = BatchMatchPersonalFirstLastNameIn.from_dict(body)
    return web.Response(status=200)


async def japanese_name_match_feedback_loop(request: web.Request, japanese_surname_latin, japanese_given_name_latin, japanese_name) -> web.Response:
    """[CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae

    

    :param japanese_surname_latin: 
    :type japanese_surname_latin: str
    :param japanese_given_name_latin: 
    :type japanese_given_name_latin: str
    :param japanese_name: 
    :type japanese_name: str

    """
    return web.Response(status=200)


async def parse_japanese_name(request: web.Request, japanese_name) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae

    

    :param japanese_name: 
    :type japanese_name: str

    """
    return web.Response(status=200)


async def parse_japanese_name_batch(request: web.Request, body=None) -> web.Response:
    """Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 

    

    :param body: A list of personal names
    :type body: dict | bytes

    """
    body = BatchPersonalNameIn.from_dict(body)
    return web.Response(status=200)
