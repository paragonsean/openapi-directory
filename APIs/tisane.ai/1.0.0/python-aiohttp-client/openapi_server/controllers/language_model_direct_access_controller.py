from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_family_details200_response import GetFamilyDetails200Response
from openapi_server.models.list_hypernyms200_response_inner_inner import ListHypernyms200ResponseInnerInner
from openapi_server.models.list_inflected_forms200_response_inner import ListInflectedForms200ResponseInner
from openapi_server.models.list_word_senses200_response_inner import ListWordSenses200ResponseInner
from openapi_server import util


async def get_family_details(request: web.Request, id=None, ocp_apim_subscription_key=None) -> web.Response:
    """Get family details

    Fetches and outputs metadata for a family from the Tisane language models.

    :param id: (Required) a numeric identifier of the family
    :type id: str
    :param ocp_apim_subscription_key: {{apiKeyDescription}}
    :type ocp_apim_subscription_key: str

    """
    return web.Response(status=200)


async def list_feature_values(request: web.Request, language=None, type=None, description=None, ocp_apim_subscription_key=None) -> web.Response:
    """List feature values

    Lists feature values for a particular category of features. This allows obtaining all the values such as entity types, subtypes, abuse types and tags, and more.  Returns the values as a JSON array of strings.

    :param language: (Required) Language code
    :type language: str
    :param type: (Required) Feature type
    :type type: str
    :param description: (Required) Feature list name (localized)
    :type description: str
    :param ocp_apim_subscription_key: {{apiKeyDescription}}
    :type ocp_apim_subscription_key: str

    """
    return web.Response(status=200)


async def list_hypernyms(request: web.Request, family=None, max_level=None, ocp_apim_subscription_key=None) -> web.Response:
    """List hypernyms

    Lists all hypernyms related to a family. A hypernym is a parent concent. E.g. \&quot;vehicle\&quot; is a hypernym of \&quot;truck\&quot;.

    :param family: (Required) a numeric identifier of the family
    :type family: str
    :param max_level: (Required) maximum distance from the family
    :type max_level: str
    :param ocp_apim_subscription_key: {{apiKeyDescription}}
    :type ocp_apim_subscription_key: str

    """
    return web.Response(status=200)


async def list_hyponyms(request: web.Request, family=None, max_level=None, ocp_apim_subscription_key=None) -> web.Response:
    """List hyponyms

    Lists all hyponyms related to a family. A hyponym is a child concent. E.g. \&quot;truck\&quot; is a hypernym of \&quot;vehicle\&quot;.

    :param family: (Required) a numeric identifier of the family
    :type family: str
    :param max_level: (Required) maximum distance from the family
    :type max_level: str
    :param ocp_apim_subscription_key: {{apiKeyDescription}}
    :type ocp_apim_subscription_key: str

    """
    return web.Response(status=200)


async def list_inflected_forms(request: web.Request, language=None, lexeme=None, family=None, ocp_apim_subscription_key=None) -> web.Response:
    """List inflected forms

    List inflected forms

    :param language: (Required) The language code
    :type language: str
    :param lexeme: (Required) The lexeme to inspect
    :type lexeme: str
    :param family: (Required) The family to inspect
    :type family: str
    :param ocp_apim_subscription_key: {{apiKeyDescription}}
    :type ocp_apim_subscription_key: str

    """
    return web.Response(status=200)


async def list_word_senses(request: web.Request, language=None, word=None, ocp_apim_subscription_key=None) -> web.Response:
    """List word senses

    Fetches and outputs all senses related to a word.

    :param language: (Required) a standard culture code (ISO-639 language code with an optional country extension)
    :type language: str
    :param word: (Required) the word to inspect
    :type word: str
    :param ocp_apim_subscription_key: {{apiKeyDescription}}
    :type ocp_apim_subscription_key: str

    """
    return web.Response(status=200)
