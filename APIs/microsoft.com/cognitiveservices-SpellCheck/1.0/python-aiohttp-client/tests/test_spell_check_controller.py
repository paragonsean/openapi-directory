# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.spell_check import SpellCheck


pytestmark = pytest.mark.asyncio

async def test_spell_checker(client):
    """Test case for spell_checker

    The Bing Spell Check API lets you perform contextual grammar and spell checking. Bing has developed a web-based spell-checker that leverages machine learning and statistical machine translation to dynamically train a constantly evolving and highly contextual algorithm. The spell-checker is based on a massive corpus of web searches and documents.
    """
    params = [('ActionType', 'action_type_example'),
                    ('AppName', 'app_name_example'),
                    ('cc', 'cc_example'),
                    ('ClientMachineName', 'client_machine_name_example'),
                    ('DocId', 'doc_id_example'),
                    ('mkt', 'mkt_example'),
                    ('SessionId', 'session_id_example'),
                    ('SetLang', 'set_lang_example'),
                    ('UserId', 'user_id_example'),
                    ('Mode', 'mode_example'),
                    ('PreContextText', 'pre_context_text_example'),
                    ('PostContextText', 'post_context_text_example'),
                    ('Text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'x_bing_apis_sdk': 'x_bing_apis_sdk_example',
        'accept': 'accept_example',
        'accept_language': 'accept_language_example',
        'pragma': 'pragma_example',
        'user_agent': 'user_agent_example',
        'x_ms_edge_client_id': 'x_ms_edge_client_id_example',
        'x_ms_edge_client_ip': 'x_ms_edge_client_ip_example',
        'x_search_location': 'x_search_location_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bing/v7.0/spellcheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

