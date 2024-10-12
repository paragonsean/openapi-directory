# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_template import JobTemplate
from openapi_server.models.list_job_templates_response import ListJobTemplatesResponse
from openapi_server.models.list_jobs_response import ListJobsResponse


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_job_templates_create(client):
    """Test case for transcoder_projects_locations_job_templates_create

    
    """
    body = {"name":"name","config":{"output":{"uri":"uri"},"adBreaks":[{"startTimeOffset":"startTimeOffset"},{"startTimeOffset":"startTimeOffset"}],"editList":[{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"},{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"}],"spriteSheets":[{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":3,"rowCount":7,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":6,"spriteHeightPixels":0,"quality":3},{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":3,"rowCount":7,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":6,"spriteHeightPixels":0,"quality":3}],"muxStreams":[{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"encryption":{"aes128":{"keyUri":"keyUri"},"mpegCenc":{"scheme":"scheme","keyId":"keyId"},"sampleAes":{"keyUri":"keyUri"},"iv":"iv","key":"key"},"elementaryStreams":["elementaryStreams","elementaryStreams"],"key":"key"},{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"encryption":{"aes128":{"keyUri":"keyUri"},"mpegCenc":{"scheme":"scheme","keyId":"keyId"},"sampleAes":{"keyUri":"keyUri"},"iv":"iv","key":"key"},"elementaryStreams":["elementaryStreams","elementaryStreams"],"key":"key"}],"pubsubDestination":{"topic":"topic"},"inputs":[{"preprocessingConfig":{"pad":{"topPixels":6,"bottomPixels":6,"rightPixels":2,"leftPixels":1},"denoise":{"strength":3.5571952270680973,"tune":"tune"},"color":{"saturation":9.965781217890562,"brightness":4.965218492984954,"contrast":5.025004791520295},"audio":{"lufs":1.1730742509559433,"lowBoost":True,"highBoost":True},"deblock":{"strength":6.438423552598547,"enabled":True},"crop":{"topPixels":9,"bottomPixels":9,"rightPixels":8,"leftPixels":6}},"uri":"uri","key":"key"},{"preprocessingConfig":{"pad":{"topPixels":6,"bottomPixels":6,"rightPixels":2,"leftPixels":1},"denoise":{"strength":3.5571952270680973,"tune":"tune"},"color":{"saturation":9.965781217890562,"brightness":4.965218492984954,"contrast":5.025004791520295},"audio":{"lufs":1.1730742509559433,"lowBoost":True,"highBoost":True},"deblock":{"strength":6.438423552598547,"enabled":True},"crop":{"topPixels":9,"bottomPixels":9,"rightPixels":8,"leftPixels":6}},"uri":"uri","key":"key"}],"overlays":[{"image":{"alpha":6.704019297950036,"resolution":{"x":6.878052220127876,"y":5.944895607614016},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]},{"image":{"alpha":6.704019297950036,"resolution":{"x":6.878052220127876,"y":5.944895607614016},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]}],"manifests":[{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"type":"MANIFEST_TYPE_UNSPECIFIED"},{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"type":"MANIFEST_TYPE_UNSPECIFIED"}],"elementaryStreams":[{"videoStream":{"entropyCoder":"entropyCoder","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":4,"heightPixels":1,"preset":"preset","bitrateBps":2,"tune":"tune","widthPixels":7,"codec":"codec","frameRate":7.386281948385884,"vbvSizeBits":6,"bFrameCount":3,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":9.301444243932576,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":1,"rateControlMode":"rateControlMode"},"audioStream":{"sampleRateHertz":2,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"},{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"}],"bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"},{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"}],"languageCode":"languageCode"},"key":"key"},{"videoStream":{"entropyCoder":"entropyCoder","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":4,"heightPixels":1,"preset":"preset","bitrateBps":2,"tune":"tune","widthPixels":7,"codec":"codec","frameRate":7.386281948385884,"vbvSizeBits":6,"bFrameCount":3,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":9.301444243932576,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":1,"rateControlMode":"rateControlMode"},"audioStream":{"sampleRateHertz":2,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"},{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"}],"bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"},{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"}],"languageCode":"languageCode"},"key":"key"}]}}
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
                    ('uploadType', 'upload_type_example'),
                    ('jobTemplateId', 'job_template_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/jobTemplates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_job_templates_delete(client):
    """Test case for transcoder_projects_locations_job_templates_delete

    
    """
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_job_templates_get(client):
    """Test case for transcoder_projects_locations_job_templates_get

    
    """
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_job_templates_list(client):
    """Test case for transcoder_projects_locations_job_templates_list

    
    """
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
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/jobTemplates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_jobs_create(client):
    """Test case for transcoder_projects_locations_jobs_create

    
    """
    body = {"ttlAfterCompletionDays":2,"outputUri":"outputUri","inputUri":"inputUri","priority":0,"templateId":"templateId","createTime":"createTime","failureDetails":[{"description":"description"},{"description":"description"}],"failureReason":"failureReason","name":"name","originUri":{"dash":"dash","hls":"hls"},"progress":{"notified":5.962133916683182,"analyzed":6.027456183070403,"uploaded":5.637376656633329,"encoded":1.4658129805029452},"startTime":"startTime","endTime":"endTime","state":"PROCESSING_STATE_UNSPECIFIED","config":{"output":{"uri":"uri"},"adBreaks":[{"startTimeOffset":"startTimeOffset"},{"startTimeOffset":"startTimeOffset"}],"editList":[{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"},{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"}],"spriteSheets":[{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":3,"rowCount":7,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":6,"spriteHeightPixels":0,"quality":3},{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":3,"rowCount":7,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":6,"spriteHeightPixels":0,"quality":3}],"muxStreams":[{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"encryption":{"aes128":{"keyUri":"keyUri"},"mpegCenc":{"scheme":"scheme","keyId":"keyId"},"sampleAes":{"keyUri":"keyUri"},"iv":"iv","key":"key"},"elementaryStreams":["elementaryStreams","elementaryStreams"],"key":"key"},{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"encryption":{"aes128":{"keyUri":"keyUri"},"mpegCenc":{"scheme":"scheme","keyId":"keyId"},"sampleAes":{"keyUri":"keyUri"},"iv":"iv","key":"key"},"elementaryStreams":["elementaryStreams","elementaryStreams"],"key":"key"}],"pubsubDestination":{"topic":"topic"},"inputs":[{"preprocessingConfig":{"pad":{"topPixels":6,"bottomPixels":6,"rightPixels":2,"leftPixels":1},"denoise":{"strength":3.5571952270680973,"tune":"tune"},"color":{"saturation":9.965781217890562,"brightness":4.965218492984954,"contrast":5.025004791520295},"audio":{"lufs":1.1730742509559433,"lowBoost":True,"highBoost":True},"deblock":{"strength":6.438423552598547,"enabled":True},"crop":{"topPixels":9,"bottomPixels":9,"rightPixels":8,"leftPixels":6}},"uri":"uri","key":"key"},{"preprocessingConfig":{"pad":{"topPixels":6,"bottomPixels":6,"rightPixels":2,"leftPixels":1},"denoise":{"strength":3.5571952270680973,"tune":"tune"},"color":{"saturation":9.965781217890562,"brightness":4.965218492984954,"contrast":5.025004791520295},"audio":{"lufs":1.1730742509559433,"lowBoost":True,"highBoost":True},"deblock":{"strength":6.438423552598547,"enabled":True},"crop":{"topPixels":9,"bottomPixels":9,"rightPixels":8,"leftPixels":6}},"uri":"uri","key":"key"}],"overlays":[{"image":{"alpha":6.704019297950036,"resolution":{"x":6.878052220127876,"y":5.944895607614016},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]},{"image":{"alpha":6.704019297950036,"resolution":{"x":6.878052220127876,"y":5.944895607614016},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":6.878052220127876,"y":5.944895607614016},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]}],"manifests":[{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"type":"MANIFEST_TYPE_UNSPECIFIED"},{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"type":"MANIFEST_TYPE_UNSPECIFIED"}],"elementaryStreams":[{"videoStream":{"entropyCoder":"entropyCoder","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":4,"heightPixels":1,"preset":"preset","bitrateBps":2,"tune":"tune","widthPixels":7,"codec":"codec","frameRate":7.386281948385884,"vbvSizeBits":6,"bFrameCount":3,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":9.301444243932576,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":1,"rateControlMode":"rateControlMode"},"audioStream":{"sampleRateHertz":2,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"},{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"}],"bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"},{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"}],"languageCode":"languageCode"},"key":"key"},{"videoStream":{"entropyCoder":"entropyCoder","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":4,"heightPixels":1,"preset":"preset","bitrateBps":2,"tune":"tune","widthPixels":7,"codec":"codec","frameRate":7.386281948385884,"vbvSizeBits":6,"bFrameCount":3,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":9.301444243932576,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":1,"rateControlMode":"rateControlMode"},"audioStream":{"sampleRateHertz":2,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"},{"channels":[{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]},{"inputs":[{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"},{"gainDb":5.962133916683182,"channel":1,"track":5,"key":"key"}]}],"key":"key"}],"bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"},{"inputs":[{"track":7,"key":"key"},{"track":7,"key":"key"}],"key":"key"}],"languageCode":"languageCode"},"key":"key"}]}}
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
        path='/v1beta1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_jobs_list(client):
    """Test case for transcoder_projects_locations_jobs_list

    
    """
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
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

