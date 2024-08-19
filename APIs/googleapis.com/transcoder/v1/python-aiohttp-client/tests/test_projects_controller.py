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
    body = {"name":"name","config":{"output":{"uri":"uri"},"adBreaks":[{"startTimeOffset":"startTimeOffset"},{"startTimeOffset":"startTimeOffset"}],"editList":[{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"},{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"}],"spriteSheets":[{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":6,"rowCount":1,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":9,"spriteHeightPixels":4,"quality":4},{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":6,"rowCount":1,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":9,"spriteHeightPixels":4,"quality":4}],"muxStreams":[{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"elementaryStreams":["elementaryStreams","elementaryStreams"],"fmp4":{"codecTag":"codecTag"},"key":"key","encryptionId":"encryptionId"},{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"elementaryStreams":["elementaryStreams","elementaryStreams"],"fmp4":{"codecTag":"codecTag"},"key":"key","encryptionId":"encryptionId"}],"pubsubDestination":{"topic":"topic"},"inputs":[{"preprocessingConfig":{"pad":{"topPixels":5,"bottomPixels":3,"rightPixels":7,"leftPixels":3},"denoise":{"strength":7.740351818741173,"tune":"tune"},"color":{"saturation":0.8851374739011653,"brightness":3.0937452626664474,"contrast":7.143538047012306},"deinterlace":{"bwdif":{"mode":"mode","parity":"parity","deinterlaceAllFrames":True},"yadif":{"mode":"mode","disableSpatialInterlacing":True,"parity":"parity","deinterlaceAllFrames":True}},"audio":{"lufs":3.353193347011243,"lowBoost":True,"highBoost":True},"deblock":{"strength":8.969578798196912,"enabled":True},"crop":{"topPixels":4,"bottomPixels":7,"rightPixels":0,"leftPixels":6}},"uri":"uri","key":"key"},{"preprocessingConfig":{"pad":{"topPixels":5,"bottomPixels":3,"rightPixels":7,"leftPixels":3},"denoise":{"strength":7.740351818741173,"tune":"tune"},"color":{"saturation":0.8851374739011653,"brightness":3.0937452626664474,"contrast":7.143538047012306},"deinterlace":{"bwdif":{"mode":"mode","parity":"parity","deinterlaceAllFrames":True},"yadif":{"mode":"mode","disableSpatialInterlacing":True,"parity":"parity","deinterlaceAllFrames":True}},"audio":{"lufs":3.353193347011243,"lowBoost":True,"highBoost":True},"deblock":{"strength":8.969578798196912,"enabled":True},"crop":{"topPixels":4,"bottomPixels":7,"rightPixels":0,"leftPixels":6}},"uri":"uri","key":"key"}],"overlays":[{"image":{"alpha":0.2025324113236393,"resolution":{"x":3.2588565619047607,"y":4.078845849666752},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]},{"image":{"alpha":0.2025324113236393,"resolution":{"x":3.2588565619047607,"y":4.078845849666752},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]}],"manifests":[{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"dash":{"segmentReferenceScheme":"SEGMENT_REFERENCE_SCHEME_UNSPECIFIED"},"type":"MANIFEST_TYPE_UNSPECIFIED"},{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"dash":{"segmentReferenceScheme":"SEGMENT_REFERENCE_SCHEME_UNSPECIFIED"},"type":"MANIFEST_TYPE_UNSPECIFIED"}],"elementaryStreams":[{"videoStream":{"h264":{"sdr":"{}","entropyCoder":"entropyCoder","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":7,"heightPixels":1,"preset":"preset","bitrateBps":4,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":1,"frameRate":1.2315135367772556,"vbvSizeBits":7,"bFrameCount":2,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":3.616076749251911,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":6,"rateControlMode":"rateControlMode"},"h265":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":9,"heightPixels":9,"preset":"preset","bitrateBps":9,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":6,"frameRate":6.683562403749608,"vbvSizeBits":3,"bFrameCount":5,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":4.965218492984954,"bPyramid":True,"gopFrameCount":8,"vbvFullnessBits":6,"hdr10":"{}","rateControlMode":"rateControlMode"},"vp9":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","profile":"profile","crfLevel":2,"heightPixels":5,"bitrateBps":1,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","widthPixels":6,"frameRate":6.778324963048013,"gopDuration":"gopDuration","gopFrameCount":6,"rateControlMode":"rateControlMode"}},"audioStream":{"sampleRateHertz":7,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5},{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5}],"displayName":"displayName","languageCode":"languageCode","bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9},{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9}],"displayName":"displayName","languageCode":"languageCode"},"key":"key"},{"videoStream":{"h264":{"sdr":"{}","entropyCoder":"entropyCoder","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":7,"heightPixels":1,"preset":"preset","bitrateBps":4,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":1,"frameRate":1.2315135367772556,"vbvSizeBits":7,"bFrameCount":2,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":3.616076749251911,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":6,"rateControlMode":"rateControlMode"},"h265":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":9,"heightPixels":9,"preset":"preset","bitrateBps":9,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":6,"frameRate":6.683562403749608,"vbvSizeBits":3,"bFrameCount":5,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":4.965218492984954,"bPyramid":True,"gopFrameCount":8,"vbvFullnessBits":6,"hdr10":"{}","rateControlMode":"rateControlMode"},"vp9":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","profile":"profile","crfLevel":2,"heightPixels":5,"bitrateBps":1,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","widthPixels":6,"frameRate":6.778324963048013,"gopDuration":"gopDuration","gopFrameCount":6,"rateControlMode":"rateControlMode"}},"audioStream":{"sampleRateHertz":7,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5},{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5}],"displayName":"displayName","languageCode":"languageCode","bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9},{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9}],"displayName":"displayName","languageCode":"languageCode"},"key":"key"}],"encryptions":[{"drmSystems":{"playready":"{}","fairplay":"{}","widevine":"{}","clearkey":"{}"},"aes128":"{}","mpegCenc":{"scheme":"scheme"},"sampleAes":"{}","id":"id","secretManagerKeySource":{"secretVersion":"secretVersion"}},{"drmSystems":{"playready":"{}","fairplay":"{}","widevine":"{}","clearkey":"{}"},"aes128":"{}","mpegCenc":{"scheme":"scheme"},"sampleAes":"{}","id":"id","secretManagerKeySource":{"secretVersion":"secretVersion"}}]},"labels":{"key":"labels"}}
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
        path='/v1/{parent}/jobTemplates'.format(parent='parent_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('allowMissing', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/jobTemplates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transcoder_projects_locations_jobs_create(client):
    """Test case for transcoder_projects_locations_jobs_create

    
    """
    body = {"ttlAfterCompletionDays":1,"batchModePriority":0,"outputUri":"outputUri","error":{"code":6,"details":[{"key":""},{"key":""}],"message":"message"},"inputUri":"inputUri","templateId":"templateId","labels":{"key":"labels"},"mode":"PROCESSING_MODE_UNSPECIFIED","createTime":"createTime","optimization":"OPTIMIZATION_STRATEGY_UNSPECIFIED","name":"name","startTime":"startTime","endTime":"endTime","state":"PROCESSING_STATE_UNSPECIFIED","config":{"output":{"uri":"uri"},"adBreaks":[{"startTimeOffset":"startTimeOffset"},{"startTimeOffset":"startTimeOffset"}],"editList":[{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"},{"endTimeOffset":"endTimeOffset","inputs":["inputs","inputs"],"startTimeOffset":"startTimeOffset","key":"key"}],"spriteSheets":[{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":6,"rowCount":1,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":9,"spriteHeightPixels":4,"quality":4},{"endTimeOffset":"endTimeOffset","spriteWidthPixels":7,"format":"format","interval":"interval","columnCount":6,"rowCount":1,"filePrefix":"filePrefix","startTimeOffset":"startTimeOffset","totalCount":9,"spriteHeightPixels":4,"quality":4}],"muxStreams":[{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"elementaryStreams":["elementaryStreams","elementaryStreams"],"fmp4":{"codecTag":"codecTag"},"key":"key","encryptionId":"encryptionId"},{"container":"container","fileName":"fileName","segmentSettings":{"segmentDuration":"segmentDuration","individualSegments":True},"elementaryStreams":["elementaryStreams","elementaryStreams"],"fmp4":{"codecTag":"codecTag"},"key":"key","encryptionId":"encryptionId"}],"pubsubDestination":{"topic":"topic"},"inputs":[{"preprocessingConfig":{"pad":{"topPixels":5,"bottomPixels":3,"rightPixels":7,"leftPixels":3},"denoise":{"strength":7.740351818741173,"tune":"tune"},"color":{"saturation":0.8851374739011653,"brightness":3.0937452626664474,"contrast":7.143538047012306},"deinterlace":{"bwdif":{"mode":"mode","parity":"parity","deinterlaceAllFrames":True},"yadif":{"mode":"mode","disableSpatialInterlacing":True,"parity":"parity","deinterlaceAllFrames":True}},"audio":{"lufs":3.353193347011243,"lowBoost":True,"highBoost":True},"deblock":{"strength":8.969578798196912,"enabled":True},"crop":{"topPixels":4,"bottomPixels":7,"rightPixels":0,"leftPixels":6}},"uri":"uri","key":"key"},{"preprocessingConfig":{"pad":{"topPixels":5,"bottomPixels":3,"rightPixels":7,"leftPixels":3},"denoise":{"strength":7.740351818741173,"tune":"tune"},"color":{"saturation":0.8851374739011653,"brightness":3.0937452626664474,"contrast":7.143538047012306},"deinterlace":{"bwdif":{"mode":"mode","parity":"parity","deinterlaceAllFrames":True},"yadif":{"mode":"mode","disableSpatialInterlacing":True,"parity":"parity","deinterlaceAllFrames":True}},"audio":{"lufs":3.353193347011243,"lowBoost":True,"highBoost":True},"deblock":{"strength":8.969578798196912,"enabled":True},"crop":{"topPixels":4,"bottomPixels":7,"rightPixels":0,"leftPixels":6}},"uri":"uri","key":"key"}],"overlays":[{"image":{"alpha":0.2025324113236393,"resolution":{"x":3.2588565619047607,"y":4.078845849666752},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]},{"image":{"alpha":0.2025324113236393,"resolution":{"x":3.2588565619047607,"y":4.078845849666752},"uri":"uri"},"animations":[{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}},{"animationStatic":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"startTimeOffset":"startTimeOffset"},"animationFade":{"xy":{"x":3.2588565619047607,"y":4.078845849666752},"endTimeOffset":"endTimeOffset","fadeType":"FADE_TYPE_UNSPECIFIED","startTimeOffset":"startTimeOffset"},"animationEnd":{"startTimeOffset":"startTimeOffset"}}]}],"manifests":[{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"dash":{"segmentReferenceScheme":"SEGMENT_REFERENCE_SCHEME_UNSPECIFIED"},"type":"MANIFEST_TYPE_UNSPECIFIED"},{"fileName":"fileName","muxStreams":["muxStreams","muxStreams"],"dash":{"segmentReferenceScheme":"SEGMENT_REFERENCE_SCHEME_UNSPECIFIED"},"type":"MANIFEST_TYPE_UNSPECIFIED"}],"elementaryStreams":[{"videoStream":{"h264":{"sdr":"{}","entropyCoder":"entropyCoder","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":7,"heightPixels":1,"preset":"preset","bitrateBps":4,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":1,"frameRate":1.2315135367772556,"vbvSizeBits":7,"bFrameCount":2,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":3.616076749251911,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":6,"rateControlMode":"rateControlMode"},"h265":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":9,"heightPixels":9,"preset":"preset","bitrateBps":9,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":6,"frameRate":6.683562403749608,"vbvSizeBits":3,"bFrameCount":5,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":4.965218492984954,"bPyramid":True,"gopFrameCount":8,"vbvFullnessBits":6,"hdr10":"{}","rateControlMode":"rateControlMode"},"vp9":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","profile":"profile","crfLevel":2,"heightPixels":5,"bitrateBps":1,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","widthPixels":6,"frameRate":6.778324963048013,"gopDuration":"gopDuration","gopFrameCount":6,"rateControlMode":"rateControlMode"}},"audioStream":{"sampleRateHertz":7,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5},{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5}],"displayName":"displayName","languageCode":"languageCode","bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9},{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9}],"displayName":"displayName","languageCode":"languageCode"},"key":"key"},{"videoStream":{"h264":{"sdr":"{}","entropyCoder":"entropyCoder","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":7,"heightPixels":1,"preset":"preset","bitrateBps":4,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":1,"frameRate":1.2315135367772556,"vbvSizeBits":7,"bFrameCount":2,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":3.616076749251911,"bPyramid":True,"gopFrameCount":1,"vbvFullnessBits":6,"rateControlMode":"rateControlMode"},"h265":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","enableTwoPass":True,"profile":"profile","crfLevel":9,"heightPixels":9,"preset":"preset","bitrateBps":9,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","tune":"tune","widthPixels":6,"frameRate":6.683562403749608,"vbvSizeBits":3,"bFrameCount":5,"gopDuration":"gopDuration","allowOpenGop":True,"aqStrength":4.965218492984954,"bPyramid":True,"gopFrameCount":8,"vbvFullnessBits":6,"hdr10":"{}","rateControlMode":"rateControlMode"},"vp9":{"sdr":"{}","hlg":"{}","pixelFormat":"pixelFormat","profile":"profile","crfLevel":2,"heightPixels":5,"bitrateBps":1,"frameRateConversionStrategy":"FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED","widthPixels":6,"frameRate":6.778324963048013,"gopDuration":"gopDuration","gopFrameCount":6,"rateControlMode":"rateControlMode"}},"audioStream":{"sampleRateHertz":7,"channelCount":6,"channelLayout":["channelLayout","channelLayout"],"codec":"codec","mapping":[{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5},{"atomKey":"atomKey","outputChannel":2,"gainDb":1.4658129805029452,"inputKey":"inputKey","inputTrack":5,"inputChannel":5}],"displayName":"displayName","languageCode":"languageCode","bitrateBps":0},"textStream":{"codec":"codec","mapping":[{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9},{"atomKey":"atomKey","inputKey":"inputKey","inputTrack":9}],"displayName":"displayName","languageCode":"languageCode"},"key":"key"}],"encryptions":[{"drmSystems":{"playready":"{}","fairplay":"{}","widevine":"{}","clearkey":"{}"},"aes128":"{}","mpegCenc":{"scheme":"scheme"},"sampleAes":"{}","id":"id","secretManagerKeySource":{"secretVersion":"secretVersion"}},{"drmSystems":{"playready":"{}","fairplay":"{}","widevine":"{}","clearkey":"{}"},"aes128":"{}","mpegCenc":{"scheme":"scheme"},"sampleAes":"{}","id":"id","secretManagerKeySource":{"secretVersion":"secretVersion"}}]}}
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
        path='/v1/{parent}/jobs'.format(parent='parent_example'),
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
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

