# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.long_running_recognize_request import LongRunningRecognizeRequest
from openapi_server.models.operation import Operation
from openapi_server.models.recognize_request import RecognizeRequest
from openapi_server.models.recognize_response import RecognizeResponse


pytestmark = pytest.mark.asyncio

async def test_speech_speech_longrunningrecognize(client):
    """Test case for speech_speech_longrunningrecognize

    
    """
    body = {"outputConfig":{"gcsUri":"gcsUri"},"audio":{"uri":"uri","content":"content"},"config":{"enableWordConfidence":True,"diarizationConfig":{"enableSpeakerDiarization":True,"speakerTag":2,"maxSpeakerCount":5,"minSpeakerCount":5},"maxAlternatives":7,"metadata":{"audioTopic":"audioTopic","interactionType":"INTERACTION_TYPE_UNSPECIFIED","originalMimeType":"originalMimeType","recordingDeviceName":"recordingDeviceName","industryNaicsCodeOfAudio":9,"microphoneDistance":"MICROPHONE_DISTANCE_UNSPECIFIED","originalMediaType":"ORIGINAL_MEDIA_TYPE_UNSPECIFIED","recordingDeviceType":"RECORDING_DEVICE_TYPE_UNSPECIFIED"},"speechContexts":[{"boost":2.027123,"phrases":["phrases","phrases"]},{"boost":2.027123,"phrases":["phrases","phrases"]}],"adaptation":{"customClasses":[{"displayName":"displayName","customClassId":"customClassId","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","items":[{"value":"value"},{"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"},{"displayName":"displayName","customClassId":"customClassId","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","items":[{"value":"value"},{"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"}],"phraseSetReferences":["phraseSetReferences","phraseSetReferences"],"phraseSets":[{"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","boost":0.8008282,"etag":"etag","state":"STATE_UNSPECIFIED","phrases":[{"boost":6.0274563,"value":"value"},{"boost":6.0274563,"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"},{"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","boost":0.8008282,"etag":"etag","state":"STATE_UNSPECIFIED","phrases":[{"boost":6.0274563,"value":"value"},{"boost":6.0274563,"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"}],"abnfGrammar":{"abnfStrings":["abnfStrings","abnfStrings"]}},"profanityFilter":True,"encoding":"ENCODING_UNSPECIFIED","languageCode":"languageCode","enableWordTimeOffsets":True,"audioChannelCount":1,"sampleRateHertz":3,"transcriptNormalization":{"entries":[{"search":"search","caseSensitive":True,"replace":"replace"},{"search":"search","caseSensitive":True,"replace":"replace"}]},"alternativeLanguageCodes":["alternativeLanguageCodes","alternativeLanguageCodes"],"enableSpokenEmojis":True,"enableSeparateRecognitionPerChannel":True,"enableSpokenPunctuation":True,"useEnhanced":True,"enableAutomaticPunctuation":True,"model":"model"}}
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
        path='/v1/speech:longrunningrecognize',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_speech_speech_recognize(client):
    """Test case for speech_speech_recognize

    
    """
    body = {"audio":{"uri":"uri","content":"content"},"config":{"enableWordConfidence":True,"diarizationConfig":{"enableSpeakerDiarization":True,"speakerTag":2,"maxSpeakerCount":5,"minSpeakerCount":5},"maxAlternatives":7,"metadata":{"audioTopic":"audioTopic","interactionType":"INTERACTION_TYPE_UNSPECIFIED","originalMimeType":"originalMimeType","recordingDeviceName":"recordingDeviceName","industryNaicsCodeOfAudio":9,"microphoneDistance":"MICROPHONE_DISTANCE_UNSPECIFIED","originalMediaType":"ORIGINAL_MEDIA_TYPE_UNSPECIFIED","recordingDeviceType":"RECORDING_DEVICE_TYPE_UNSPECIFIED"},"speechContexts":[{"boost":2.027123,"phrases":["phrases","phrases"]},{"boost":2.027123,"phrases":["phrases","phrases"]}],"adaptation":{"customClasses":[{"displayName":"displayName","customClassId":"customClassId","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","items":[{"value":"value"},{"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"},{"displayName":"displayName","customClassId":"customClassId","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","items":[{"value":"value"},{"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"}],"phraseSetReferences":["phraseSetReferences","phraseSetReferences"],"phraseSets":[{"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","boost":0.8008282,"etag":"etag","state":"STATE_UNSPECIFIED","phrases":[{"boost":6.0274563,"value":"value"},{"boost":6.0274563,"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"},{"displayName":"displayName","annotations":{"key":"annotations"},"reconciling":True,"kmsKeyName":"kmsKeyName","uid":"uid","expireTime":"expireTime","deleteTime":"deleteTime","name":"name","boost":0.8008282,"etag":"etag","state":"STATE_UNSPECIFIED","phrases":[{"boost":6.0274563,"value":"value"},{"boost":6.0274563,"value":"value"}],"kmsKeyVersionName":"kmsKeyVersionName"}],"abnfGrammar":{"abnfStrings":["abnfStrings","abnfStrings"]}},"profanityFilter":True,"encoding":"ENCODING_UNSPECIFIED","languageCode":"languageCode","enableWordTimeOffsets":True,"audioChannelCount":1,"sampleRateHertz":3,"transcriptNormalization":{"entries":[{"search":"search","caseSensitive":True,"replace":"replace"},{"search":"search","caseSensitive":True,"replace":"replace"}]},"alternativeLanguageCodes":["alternativeLanguageCodes","alternativeLanguageCodes"],"enableSpokenEmojis":True,"enableSeparateRecognitionPerChannel":True,"enableSpokenPunctuation":True,"useEnhanced":True,"enableAutomaticPunctuation":True,"model":"model"}}
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
        path='/v1/speech:recognize',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

