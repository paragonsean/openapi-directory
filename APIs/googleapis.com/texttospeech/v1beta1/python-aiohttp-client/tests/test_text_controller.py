# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.synthesize_speech_request import SynthesizeSpeechRequest
from openapi_server.models.synthesize_speech_response import SynthesizeSpeechResponse


pytestmark = pytest.mark.asyncio

async def test_texttospeech_text_synthesize(client):
    """Test case for texttospeech_text_synthesize

    
    """
    body = {"voice":{"ssmlGender":"SSML_VOICE_GENDER_UNSPECIFIED","name":"name","customVoice":{"model":"model","reportedUsage":"REPORTED_USAGE_UNSPECIFIED"},"languageCode":"languageCode"},"input":{"ssml":"ssml","text":"text"},"enableTimePointing":["TIMEPOINT_TYPE_UNSPECIFIED","TIMEPOINT_TYPE_UNSPECIFIED"],"audioConfig":{"sampleRateHertz":6,"volumeGainDb":5.962133916683182,"speakingRate":1.4658129805029452,"audioEncoding":"AUDIO_ENCODING_UNSPECIFIED","pitch":0.8008281904610115,"effectsProfileId":["effectsProfileId","effectsProfileId"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/text:synthesize',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

