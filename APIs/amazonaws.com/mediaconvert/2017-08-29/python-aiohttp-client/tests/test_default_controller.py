# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.associate_certificate_request import AssociateCertificateRequest
from openapi_server.models.create_job_request import CreateJobRequest
from openapi_server.models.create_job_response import CreateJobResponse
from openapi_server.models.create_job_template_request import CreateJobTemplateRequest
from openapi_server.models.create_job_template_response import CreateJobTemplateResponse
from openapi_server.models.create_preset_request import CreatePresetRequest
from openapi_server.models.create_preset_response import CreatePresetResponse
from openapi_server.models.create_queue_request import CreateQueueRequest
from openapi_server.models.create_queue_response import CreateQueueResponse
from openapi_server.models.describe_endpoints_request import DescribeEndpointsRequest
from openapi_server.models.describe_endpoints_response import DescribeEndpointsResponse
from openapi_server.models.get_job_response import GetJobResponse
from openapi_server.models.get_job_template_response import GetJobTemplateResponse
from openapi_server.models.get_policy_response import GetPolicyResponse
from openapi_server.models.get_preset_response import GetPresetResponse
from openapi_server.models.get_queue_response import GetQueueResponse
from openapi_server.models.list_job_templates_response import ListJobTemplatesResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_presets_response import ListPresetsResponse
from openapi_server.models.list_queues_response import ListQueuesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_policy_request import PutPolicyRequest
from openapi_server.models.put_policy_response import PutPolicyResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_job_template_request import UpdateJobTemplateRequest
from openapi_server.models.update_job_template_response import UpdateJobTemplateResponse
from openapi_server.models.update_preset_request import UpdatePresetRequest
from openapi_server.models.update_preset_response import UpdatePresetResponse
from openapi_server.models.update_queue_request import UpdateQueueRequest
from openapi_server.models.update_queue_response import UpdateQueueResponse


pytestmark = pytest.mark.asyncio

async def test_associate_certificate(client):
    """Test case for associate_certificate

    
    """
    body = {"Arn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/certificates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_job(client):
    """Test case for cancel_job

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-08-29/jobs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_job(client):
    """Test case for create_job

    
    """
    body = {"Priority":"","UserMetadata":"","StatusUpdateInterval":"","JobTemplate":"","HopDestinations":"","Role":"","ClientRequestToken":"","AccelerationSettings":{"Mode":""},"BillingTagsSource":"","Queue":"","Settings":{"AdAvailOffset":"","NielsenNonLinearWatermark":{"CbetSourceId":"","UniqueTicPerAudioTrack":"","TicServerUrl":"","MetadataDestination":"","SourceId":"","ActiveWatermarkProcess":"","EpisodeId":"","AdiFilename":"","AssetId":"","AssetName":"","SourceWatermarkStatus":""},"KantarWatermark":{"KantarLicenseId":"","Metadata3":"","Metadata4":"","Metadata5":"","ChannelName":"","Metadata6":"","CredentialsSecretName":"","FileOffset":"","ContentReference":"","KantarServerUrl":"","LogDestination":"","Metadata7":"","Metadata8":""},"TimedMetadataInsertion":{"Id3Insertions":""},"Esam":{"ResponseSignalPreroll":"","SignalProcessingNotification":{"SccXml":""},"ManifestConfirmConditionNotification":{"MccXml":""}},"ExtendedDataServices":{"CopyProtectionAction":"","VchipAction":""},"OutputGroups":"","AvailBlanking":{"AvailBlankingImage":""},"NielsenConfiguration":{"DistributorId":"","BreakoutCode":""},"Inputs":"","MotionImageInserter":{"Framerate":{"FramerateDenominator":"","FramerateNumerator":""},"Input":"","InsertionMode":"","Playback":"","StartTime":"","Offset":{"ImageY":"","ImageX":""}},"TimecodeConfig":{"Anchor":"","Start":"","TimestampOffset":"","Source":""}},"Tags":"","SimulateReservedQueue":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/jobs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_job_template(client):
    """Test case for create_job_template

    
    """
    body = {"Category":"","Description":"","AccelerationSettings":{"Mode":""},"Priority":"","StatusUpdateInterval":"","Queue":"","HopDestinations":"","Settings":{"AdAvailOffset":"","NielsenNonLinearWatermark":{"CbetSourceId":"","UniqueTicPerAudioTrack":"","TicServerUrl":"","MetadataDestination":"","SourceId":"","ActiveWatermarkProcess":"","EpisodeId":"","AdiFilename":"","AssetId":"","AssetName":"","SourceWatermarkStatus":""},"KantarWatermark":{"KantarLicenseId":"","Metadata3":"","Metadata4":"","Metadata5":"","ChannelName":"","Metadata6":"","CredentialsSecretName":"","FileOffset":"","ContentReference":"","KantarServerUrl":"","LogDestination":"","Metadata7":"","Metadata8":""},"TimedMetadataInsertion":{"Id3Insertions":""},"Esam":{"ResponseSignalPreroll":"","SignalProcessingNotification":{"SccXml":""},"ManifestConfirmConditionNotification":{"MccXml":""}},"ExtendedDataServices":{"CopyProtectionAction":"","VchipAction":""},"OutputGroups":"","AvailBlanking":{"AvailBlankingImage":""},"NielsenConfiguration":{"DistributorId":"","BreakoutCode":""},"Inputs":"","MotionImageInserter":{"Framerate":{"FramerateDenominator":"","FramerateNumerator":""},"Input":"","InsertionMode":"","Playback":"","StartTime":"","Offset":{"ImageY":"","ImageX":""}},"TimecodeConfig":{"Anchor":"","Start":"","TimestampOffset":"","Source":""}},"Tags":"","Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/jobTemplates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_preset(client):
    """Test case for create_preset

    
    """
    body = {"Category":"","Description":"","Settings":{"AudioDescriptions":"","ContainerSettings":{"Container":"","MxfSettings":{"XavcProfileSettings":{"MaxAncDataSize":"","DurationMode":""},"AfdSignaling":"","Profile":""},"F4vSettings":{"MoovPlacement":""},"MpdSettings":{"CaptionContainerType":"","TimedMetadata":"","Scte35Source":"","TimedMetadataValue":"","Scte35Esam":"","KlvMetadata":"","ManifestMetadataSignaling":"","TimedMetadataBoxVersion":"","AccessibilityCaptionHints":"","AudioDuration":"","TimedMetadataSchemeIdUri":""},"M3u8Settings":{"PatInterval":"","PmtInterval":"","PcrPid":"","VideoPid":"","AudioFramesPerPes":"","TransportStreamId":"","PmtPid":"","Scte35Pid":"","TimedMetadata":"","MaxPcrInterval":"","Scte35Source":"","PrivateMetadataPid":"","DataPTSControl":"","NielsenId3":"","TimedMetadataPid":"","AudioPids":"","ProgramNumber":"","PcrControl":"","AudioDuration":""},"Mp4Settings":{"CttsVersion":"","Mp4MajorBrand":"","FreeSpaceBox":"","CslgAtom":"","AudioDuration":"","MoovPlacement":""},"M2tsSettings":{"PatInterval":"","RateMode":"","NullPacketBitrate":"","PmtInterval":"","EsRateInPes":"","Scte35Esam":{"Scte35EsamPid":""},"VideoPid":"","TransportStreamId":"","EbpPlacement":"","DvbSubPids":"","SegmentationStyle":"","Scte35Pid":"","MinEbpInterval":"","DataPTSControl":"","NielsenId3":"","ProgramNumber":"","DvbTdtSettings":{"TdtInterval":""},"AudioDuration":"","EbpAudioInterval":"","FragmentTime":"","DvbTeletextPid":"","PcrPid":"","SegmentationTime":"","AudioFramesPerPes":"","KlvMetadata":"","Bitrate":"","PmtPid":"","SegmentationMarkers":"","DvbNitSettings":{"NetworkName":"","NitInterval":"","NetworkId":""},"MaxPcrInterval":"","Scte35Source":"","DvbSdtSettings":{"ServiceProviderName":"","OutputSdt":"","ServiceName":"","SdtInterval":""},"PrivateMetadataPid":"","BufferModel":"","TimedMetadataPid":"","AudioPids":"","AudioBufferModel":"","PcrControl":"","ForceTsVideoEbpOrder":""},"MovSettings":{"PaddingControl":"","ClapAtom":"","Reference":"","CslgAtom":"","Mpeg2FourCCControl":""},"CmfcSettings":{"AudioTrackType":"","DescriptiveVideoServiceFlag":"","Scte35Esam":"","KlvMetadata":"","IFrameOnlyManifest":"","ManifestMetadataSignaling":"","TimedMetadata":"","Scte35Source":"","AudioRenditionSets":"","TimedMetadataValue":"","TimedMetadataBoxVersion":"","AudioGroupId":"","AudioDuration":"","TimedMetadataSchemeIdUri":""}},"VideoDescription":{"Position":{"X":"","Y":"","Height":"","Width":""},"FixedAfd":"","AntiAlias":"","AfdSignaling":"","CodecSettings":{"AvcIntraSettings":{"AvcIntraClass":"","FramerateConversionAlgorithm":"","AvcIntraUhdSettings":{"QualityTuningLevel":""},"InterlaceMode":"","FramerateControl":"","ScanTypeConversionMode":"","Telecine":"","FramerateDenominator":"","FramerateNumerator":"","SlowPal":""},"Codec":"","Mpeg2Settings":{"HrdBufferSize":"","DynamicSubGop":"","FramerateControl":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","ParControl":"","GopClosedCadence":"","HrdBufferFinalFillPercentage":"","SpatialAdaptiveQuantization":"","CodecLevel":"","MinIInterval":"","SceneChangeDetect":"","FramerateDenominator":"","Softness":"","GopSize":"","AdaptiveQuantization":"","CodecProfile":"","FramerateConversionAlgorithm":"","TemporalAdaptiveQuantization":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","GopSizeUnits":"","QualityTuningLevel":"","Bitrate":"","ParNumerator":"","RateControlMode":"","HrdBufferInitialFillPercentage":"","InterlaceMode":"","IntraDcPrecision":"","MaxBitrate":"","Syntax":"","SlowPal":""},"Vc3Settings":{"FramerateConversionAlgorithm":"","InterlaceMode":"","FramerateControl":"","ScanTypeConversionMode":"","Vc3Class":"","Telecine":"","FramerateDenominator":"","FramerateNumerator":"","SlowPal":""},"FrameCaptureSettings":{"MaxCaptures":"","Quality":"","FramerateDenominator":"","FramerateNumerator":""},"H264Settings":{"HrdBufferSize":"","DynamicSubGop":"","Slices":"","FramerateControl":"","FlickerAdaptiveQuantization":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","ParControl":"","QvbrSettings":{"QvbrQualityLevelFineTune":"","QvbrQualityLevel":"","MaxAverageBitrate":""},"GopClosedCadence":"","HrdBufferFinalFillPercentage":"","SpatialAdaptiveQuantization":"","CodecLevel":"","BandwidthReductionFilter":{"Sharpening":"","Strength":""},"MinIInterval":"","SceneChangeDetect":"","FramerateDenominator":"","Softness":"","RepeatPps":"","GopSize":"","AdaptiveQuantization":"","CodecProfile":"","FramerateConversionAlgorithm":"","EntropyEncoding":"","NumberReferenceFrames":"","TemporalAdaptiveQuantization":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","GopSizeUnits":"","QualityTuningLevel":"","UnregisteredSeiTimecode":"","Bitrate":"","ParNumerator":"","RateControlMode":"","HrdBufferInitialFillPercentage":"","InterlaceMode":"","FieldEncoding":"","GopBReference":"","MaxBitrate":"","Syntax":"","SlowPal":""},"H265Settings":{"HrdBufferSize":"","DynamicSubGop":"","SampleAdaptiveOffsetFilterMode":"","Slices":"","FramerateControl":"","FlickerAdaptiveQuantization":"","TemporalIds":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","ParControl":"","QvbrSettings":{"QvbrQualityLevelFineTune":"","QvbrQualityLevel":"","MaxAverageBitrate":""},"GopClosedCadence":"","HrdBufferFinalFillPercentage":"","SpatialAdaptiveQuantization":"","CodecLevel":"","BandwidthReductionFilter":{"Sharpening":"","Strength":""},"AlternateTransferFunctionSei":"","MinIInterval":"","SceneChangeDetect":"","FramerateDenominator":"","WriteMp4PackagingType":"","GopSize":"","AdaptiveQuantization":"","CodecProfile":"","FramerateConversionAlgorithm":"","NumberReferenceFrames":"","TemporalAdaptiveQuantization":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","GopSizeUnits":"","QualityTuningLevel":"","UnregisteredSeiTimecode":"","Bitrate":"","ParNumerator":"","RateControlMode":"","HrdBufferInitialFillPercentage":"","InterlaceMode":"","Tiles":"","GopBReference":"","MaxBitrate":"","SlowPal":""},"Vp8Settings":{"HrdBufferSize":"","FramerateConversionAlgorithm":"","FramerateControl":"","ParDenominator":"","FramerateNumerator":"","ParControl":"","QualityTuningLevel":"","Bitrate":"","ParNumerator":"","RateControlMode":"","FramerateDenominator":"","MaxBitrate":"","GopSize":""},"ProresSettings":{"CodecProfile":"","FramerateConversionAlgorithm":"","ChromaSampling":"","FramerateControl":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","FramerateNumerator":"","ParControl":"","ParNumerator":"","InterlaceMode":"","FramerateDenominator":"","SlowPal":""},"Vp9Settings":{"HrdBufferSize":"","FramerateConversionAlgorithm":"","FramerateControl":"","ParDenominator":"","FramerateNumerator":"","ParControl":"","QualityTuningLevel":"","Bitrate":"","ParNumerator":"","RateControlMode":"","FramerateDenominator":"","MaxBitrate":"","GopSize":""},"Av1Settings":{"FramerateConversionAlgorithm":"","Slices":"","FramerateControl":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","QvbrSettings":{"QvbrQualityLevelFineTune":"","QvbrQualityLevel":""},"BitDepth":"","SpatialAdaptiveQuantization":"","RateControlMode":"","FramerateDenominator":"","MaxBitrate":"","GopSize":"","AdaptiveQuantization":""},"XavcSettings":{"FramerateConversionAlgorithm":"","EntropyEncoding":"","TemporalAdaptiveQuantization":"","FramerateControl":"","FramerateNumerator":"","Profile":"","SpatialAdaptiveQuantization":"","Xavc4kIntraVbrProfileSettings":{"XavcClass":""},"FramerateDenominator":"","XavcHdIntraCbgProfileSettings":{"XavcClass":""},"XavcHdProfileSettings":{"BitrateClass":"","HrdBufferSize":"","InterlaceMode":"","Slices":"","FlickerAdaptiveQuantization":"","Telecine":"","GopBReference":"","GopClosedCadence":"","QualityTuningLevel":""},"Softness":"","Xavc4kIntraCbgProfileSettings":{"XavcClass":""},"Xavc4kProfileSettings":{"BitrateClass":"","CodecProfile":"","HrdBufferSize":"","Slices":"","FlickerAdaptiveQuantization":"","GopBReference":"","GopClosedCadence":"","QualityTuningLevel":""},"AdaptiveQuantization":"","SlowPal":""}},"Sharpness":"","Crop":{"X":"","Y":"","Height":"","Width":""},"DropFrameTimecode":"","TimecodeInsertion":"","ColorMetadata":"","ScalingBehavior":"","RespondToAfd":"","Height":"","Width":"","VideoPreprocessors":{"Deinterlacer":{"Control":"","Mode":"","Algorithm":""},"ImageInserter":{"InsertableImages":"","SdrReferenceWhiteLevel":""},"ColorCorrector":{"SampleRangeConversion":"","Brightness":"","ColorSpaceConversion":"","Hdr10Metadata":{"MaxContentLightLevel":"","RedPrimaryX":"","MinLuminance":"","GreenPrimaryX":"","BluePrimaryY":"","BluePrimaryX":"","GreenPrimaryY":"","MaxFrameAverageLightLevel":"","MaxLuminance":"","RedPrimaryY":"","WhitePointY":"","WhitePointX":""},"Saturation":"","HdrToSdrToneMapper":"","SdrReferenceWhiteLevel":"","Hue":"","Contrast":"","ClipLimits":{"MinimumYUV":"","MaximumRGBTolerance":"","MinimumRGBTolerance":"","MaximumYUV":""}},"DolbyVision":{"L6Mode":"","Mapping":"","L6Metadata":{"MaxCll":"","MaxFall":""},"Profile":""},"PartnerWatermarking":{"NexguardFileMarkerSettings":{"Preset":"","License":"","Payload":"","Strength":""}},"TimecodeBurnin":{"FontSize":"","Position":"","Prefix":""},"Hdr10Plus":{"TargetMonitorNits":"","MasteringMonitorNits":""},"NoiseReducer":{"TemporalFilterSettings":{"Speed":"","AggressiveMode":"","PostTemporalSharpening":"","PostTemporalSharpeningStrength":"","Strength":""},"Filter":"","SpatialFilterSettings":{"PostFilterSharpenStrength":"","Speed":"","Strength":""},"FilterSettings":{"Strength":""}}}},"CaptionDescriptions":""},"Tags":"","Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/presets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_queue(client):
    """Test case for create_queue

    
    """
    body = {"Status":"","Description":"","PricingPlan":"","ReservationPlanSettings":{"Commitment":"","ReservedSlots":"","RenewalType":""},"Tags":"","Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/queues',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_job_template(client):
    """Test case for delete_job_template

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-08-29/jobTemplates/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_policy(client):
    """Test case for delete_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-08-29/policy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_preset(client):
    """Test case for delete_preset

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-08-29/presets/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_queue(client):
    """Test case for delete_queue

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-08-29/queues/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_endpoints(client):
    """Test case for describe_endpoints

    
    """
    body = {"NextToken":"","MaxResults":"","Mode":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/endpoints',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_certificate(client):
    """Test case for disassociate_certificate

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-08-29/certificates/{arn}'.format(arn='arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job(client):
    """Test case for get_job

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/jobs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_template(client):
    """Test case for get_job_template

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/jobTemplates/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_policy(client):
    """Test case for get_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/policy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_preset(client):
    """Test case for get_preset

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/presets/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_queue(client):
    """Test case for get_queue

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/queues/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_job_templates(client):
    """Test case for list_job_templates

    
    """
    params = [('category', 'category_example'),
                    ('listBy', 'list_by_example'),
                    ('maxResults', 56),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/jobTemplates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_jobs(client):
    """Test case for list_jobs

    
    """
    params = [('maxResults', 56),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('queue', 'queue_example'),
                    ('status', 'status_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_presets(client):
    """Test case for list_presets

    
    """
    params = [('category', 'category_example'),
                    ('listBy', 'list_by_example'),
                    ('maxResults', 56),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/presets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_queues(client):
    """Test case for list_queues

    
    """
    params = [('listBy', 'list_by_example'),
                    ('maxResults', 56),
                    ('nextToken', 'next_token_example'),
                    ('order', 'order_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/queues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2017-08-29/tags/{arn}'.format(arn='arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_policy(client):
    """Test case for put_policy

    
    """
    body = {"Policy":{"HttpInputs":"","HttpsInputs":"","S3Inputs":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-08-29/policy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"Arn":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2017-08-29/tags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"TagKeys":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-08-29/tags/{arn}'.format(arn='arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_job_template(client):
    """Test case for update_job_template

    
    """
    body = {"Category":"","Description":"","AccelerationSettings":{"Mode":""},"Priority":"","StatusUpdateInterval":"","Queue":"","HopDestinations":"","Settings":{"AdAvailOffset":"","NielsenNonLinearWatermark":{"CbetSourceId":"","UniqueTicPerAudioTrack":"","TicServerUrl":"","MetadataDestination":"","SourceId":"","ActiveWatermarkProcess":"","EpisodeId":"","AdiFilename":"","AssetId":"","AssetName":"","SourceWatermarkStatus":""},"KantarWatermark":{"KantarLicenseId":"","Metadata3":"","Metadata4":"","Metadata5":"","ChannelName":"","Metadata6":"","CredentialsSecretName":"","FileOffset":"","ContentReference":"","KantarServerUrl":"","LogDestination":"","Metadata7":"","Metadata8":""},"TimedMetadataInsertion":{"Id3Insertions":""},"Esam":{"ResponseSignalPreroll":"","SignalProcessingNotification":{"SccXml":""},"ManifestConfirmConditionNotification":{"MccXml":""}},"ExtendedDataServices":{"CopyProtectionAction":"","VchipAction":""},"OutputGroups":"","AvailBlanking":{"AvailBlankingImage":""},"NielsenConfiguration":{"DistributorId":"","BreakoutCode":""},"Inputs":"","MotionImageInserter":{"Framerate":{"FramerateDenominator":"","FramerateNumerator":""},"Input":"","InsertionMode":"","Playback":"","StartTime":"","Offset":{"ImageY":"","ImageX":""}},"TimecodeConfig":{"Anchor":"","Start":"","TimestampOffset":"","Source":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-08-29/jobTemplates/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_preset(client):
    """Test case for update_preset

    
    """
    body = {"Category":"","Description":"","Settings":{"AudioDescriptions":"","ContainerSettings":{"Container":"","MxfSettings":{"XavcProfileSettings":{"MaxAncDataSize":"","DurationMode":""},"AfdSignaling":"","Profile":""},"F4vSettings":{"MoovPlacement":""},"MpdSettings":{"CaptionContainerType":"","TimedMetadata":"","Scte35Source":"","TimedMetadataValue":"","Scte35Esam":"","KlvMetadata":"","ManifestMetadataSignaling":"","TimedMetadataBoxVersion":"","AccessibilityCaptionHints":"","AudioDuration":"","TimedMetadataSchemeIdUri":""},"M3u8Settings":{"PatInterval":"","PmtInterval":"","PcrPid":"","VideoPid":"","AudioFramesPerPes":"","TransportStreamId":"","PmtPid":"","Scte35Pid":"","TimedMetadata":"","MaxPcrInterval":"","Scte35Source":"","PrivateMetadataPid":"","DataPTSControl":"","NielsenId3":"","TimedMetadataPid":"","AudioPids":"","ProgramNumber":"","PcrControl":"","AudioDuration":""},"Mp4Settings":{"CttsVersion":"","Mp4MajorBrand":"","FreeSpaceBox":"","CslgAtom":"","AudioDuration":"","MoovPlacement":""},"M2tsSettings":{"PatInterval":"","RateMode":"","NullPacketBitrate":"","PmtInterval":"","EsRateInPes":"","Scte35Esam":{"Scte35EsamPid":""},"VideoPid":"","TransportStreamId":"","EbpPlacement":"","DvbSubPids":"","SegmentationStyle":"","Scte35Pid":"","MinEbpInterval":"","DataPTSControl":"","NielsenId3":"","ProgramNumber":"","DvbTdtSettings":{"TdtInterval":""},"AudioDuration":"","EbpAudioInterval":"","FragmentTime":"","DvbTeletextPid":"","PcrPid":"","SegmentationTime":"","AudioFramesPerPes":"","KlvMetadata":"","Bitrate":"","PmtPid":"","SegmentationMarkers":"","DvbNitSettings":{"NetworkName":"","NitInterval":"","NetworkId":""},"MaxPcrInterval":"","Scte35Source":"","DvbSdtSettings":{"ServiceProviderName":"","OutputSdt":"","ServiceName":"","SdtInterval":""},"PrivateMetadataPid":"","BufferModel":"","TimedMetadataPid":"","AudioPids":"","AudioBufferModel":"","PcrControl":"","ForceTsVideoEbpOrder":""},"MovSettings":{"PaddingControl":"","ClapAtom":"","Reference":"","CslgAtom":"","Mpeg2FourCCControl":""},"CmfcSettings":{"AudioTrackType":"","DescriptiveVideoServiceFlag":"","Scte35Esam":"","KlvMetadata":"","IFrameOnlyManifest":"","ManifestMetadataSignaling":"","TimedMetadata":"","Scte35Source":"","AudioRenditionSets":"","TimedMetadataValue":"","TimedMetadataBoxVersion":"","AudioGroupId":"","AudioDuration":"","TimedMetadataSchemeIdUri":""}},"VideoDescription":{"Position":{"X":"","Y":"","Height":"","Width":""},"FixedAfd":"","AntiAlias":"","AfdSignaling":"","CodecSettings":{"AvcIntraSettings":{"AvcIntraClass":"","FramerateConversionAlgorithm":"","AvcIntraUhdSettings":{"QualityTuningLevel":""},"InterlaceMode":"","FramerateControl":"","ScanTypeConversionMode":"","Telecine":"","FramerateDenominator":"","FramerateNumerator":"","SlowPal":""},"Codec":"","Mpeg2Settings":{"HrdBufferSize":"","DynamicSubGop":"","FramerateControl":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","ParControl":"","GopClosedCadence":"","HrdBufferFinalFillPercentage":"","SpatialAdaptiveQuantization":"","CodecLevel":"","MinIInterval":"","SceneChangeDetect":"","FramerateDenominator":"","Softness":"","GopSize":"","AdaptiveQuantization":"","CodecProfile":"","FramerateConversionAlgorithm":"","TemporalAdaptiveQuantization":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","GopSizeUnits":"","QualityTuningLevel":"","Bitrate":"","ParNumerator":"","RateControlMode":"","HrdBufferInitialFillPercentage":"","InterlaceMode":"","IntraDcPrecision":"","MaxBitrate":"","Syntax":"","SlowPal":""},"Vc3Settings":{"FramerateConversionAlgorithm":"","InterlaceMode":"","FramerateControl":"","ScanTypeConversionMode":"","Vc3Class":"","Telecine":"","FramerateDenominator":"","FramerateNumerator":"","SlowPal":""},"FrameCaptureSettings":{"MaxCaptures":"","Quality":"","FramerateDenominator":"","FramerateNumerator":""},"H264Settings":{"HrdBufferSize":"","DynamicSubGop":"","Slices":"","FramerateControl":"","FlickerAdaptiveQuantization":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","ParControl":"","QvbrSettings":{"QvbrQualityLevelFineTune":"","QvbrQualityLevel":"","MaxAverageBitrate":""},"GopClosedCadence":"","HrdBufferFinalFillPercentage":"","SpatialAdaptiveQuantization":"","CodecLevel":"","BandwidthReductionFilter":{"Sharpening":"","Strength":""},"MinIInterval":"","SceneChangeDetect":"","FramerateDenominator":"","Softness":"","RepeatPps":"","GopSize":"","AdaptiveQuantization":"","CodecProfile":"","FramerateConversionAlgorithm":"","EntropyEncoding":"","NumberReferenceFrames":"","TemporalAdaptiveQuantization":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","GopSizeUnits":"","QualityTuningLevel":"","UnregisteredSeiTimecode":"","Bitrate":"","ParNumerator":"","RateControlMode":"","HrdBufferInitialFillPercentage":"","InterlaceMode":"","FieldEncoding":"","GopBReference":"","MaxBitrate":"","Syntax":"","SlowPal":""},"H265Settings":{"HrdBufferSize":"","DynamicSubGop":"","SampleAdaptiveOffsetFilterMode":"","Slices":"","FramerateControl":"","FlickerAdaptiveQuantization":"","TemporalIds":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","ParControl":"","QvbrSettings":{"QvbrQualityLevelFineTune":"","QvbrQualityLevel":"","MaxAverageBitrate":""},"GopClosedCadence":"","HrdBufferFinalFillPercentage":"","SpatialAdaptiveQuantization":"","CodecLevel":"","BandwidthReductionFilter":{"Sharpening":"","Strength":""},"AlternateTransferFunctionSei":"","MinIInterval":"","SceneChangeDetect":"","FramerateDenominator":"","WriteMp4PackagingType":"","GopSize":"","AdaptiveQuantization":"","CodecProfile":"","FramerateConversionAlgorithm":"","NumberReferenceFrames":"","TemporalAdaptiveQuantization":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","GopSizeUnits":"","QualityTuningLevel":"","UnregisteredSeiTimecode":"","Bitrate":"","ParNumerator":"","RateControlMode":"","HrdBufferInitialFillPercentage":"","InterlaceMode":"","Tiles":"","GopBReference":"","MaxBitrate":"","SlowPal":""},"Vp8Settings":{"HrdBufferSize":"","FramerateConversionAlgorithm":"","FramerateControl":"","ParDenominator":"","FramerateNumerator":"","ParControl":"","QualityTuningLevel":"","Bitrate":"","ParNumerator":"","RateControlMode":"","FramerateDenominator":"","MaxBitrate":"","GopSize":""},"ProresSettings":{"CodecProfile":"","FramerateConversionAlgorithm":"","ChromaSampling":"","FramerateControl":"","ScanTypeConversionMode":"","ParDenominator":"","Telecine":"","FramerateNumerator":"","ParControl":"","ParNumerator":"","InterlaceMode":"","FramerateDenominator":"","SlowPal":""},"Vp9Settings":{"HrdBufferSize":"","FramerateConversionAlgorithm":"","FramerateControl":"","ParDenominator":"","FramerateNumerator":"","ParControl":"","QualityTuningLevel":"","Bitrate":"","ParNumerator":"","RateControlMode":"","FramerateDenominator":"","MaxBitrate":"","GopSize":""},"Av1Settings":{"FramerateConversionAlgorithm":"","Slices":"","FramerateControl":"","NumberBFramesBetweenReferenceFrames":"","FramerateNumerator":"","QvbrSettings":{"QvbrQualityLevelFineTune":"","QvbrQualityLevel":""},"BitDepth":"","SpatialAdaptiveQuantization":"","RateControlMode":"","FramerateDenominator":"","MaxBitrate":"","GopSize":"","AdaptiveQuantization":""},"XavcSettings":{"FramerateConversionAlgorithm":"","EntropyEncoding":"","TemporalAdaptiveQuantization":"","FramerateControl":"","FramerateNumerator":"","Profile":"","SpatialAdaptiveQuantization":"","Xavc4kIntraVbrProfileSettings":{"XavcClass":""},"FramerateDenominator":"","XavcHdIntraCbgProfileSettings":{"XavcClass":""},"XavcHdProfileSettings":{"BitrateClass":"","HrdBufferSize":"","InterlaceMode":"","Slices":"","FlickerAdaptiveQuantization":"","Telecine":"","GopBReference":"","GopClosedCadence":"","QualityTuningLevel":""},"Softness":"","Xavc4kIntraCbgProfileSettings":{"XavcClass":""},"Xavc4kProfileSettings":{"BitrateClass":"","CodecProfile":"","HrdBufferSize":"","Slices":"","FlickerAdaptiveQuantization":"","GopBReference":"","GopClosedCadence":"","QualityTuningLevel":""},"AdaptiveQuantization":"","SlowPal":""}},"Sharpness":"","Crop":{"X":"","Y":"","Height":"","Width":""},"DropFrameTimecode":"","TimecodeInsertion":"","ColorMetadata":"","ScalingBehavior":"","RespondToAfd":"","Height":"","Width":"","VideoPreprocessors":{"Deinterlacer":{"Control":"","Mode":"","Algorithm":""},"ImageInserter":{"InsertableImages":"","SdrReferenceWhiteLevel":""},"ColorCorrector":{"SampleRangeConversion":"","Brightness":"","ColorSpaceConversion":"","Hdr10Metadata":{"MaxContentLightLevel":"","RedPrimaryX":"","MinLuminance":"","GreenPrimaryX":"","BluePrimaryY":"","BluePrimaryX":"","GreenPrimaryY":"","MaxFrameAverageLightLevel":"","MaxLuminance":"","RedPrimaryY":"","WhitePointY":"","WhitePointX":""},"Saturation":"","HdrToSdrToneMapper":"","SdrReferenceWhiteLevel":"","Hue":"","Contrast":"","ClipLimits":{"MinimumYUV":"","MaximumRGBTolerance":"","MinimumRGBTolerance":"","MaximumYUV":""}},"DolbyVision":{"L6Mode":"","Mapping":"","L6Metadata":{"MaxCll":"","MaxFall":""},"Profile":""},"PartnerWatermarking":{"NexguardFileMarkerSettings":{"Preset":"","License":"","Payload":"","Strength":""}},"TimecodeBurnin":{"FontSize":"","Position":"","Prefix":""},"Hdr10Plus":{"TargetMonitorNits":"","MasteringMonitorNits":""},"NoiseReducer":{"TemporalFilterSettings":{"Speed":"","AggressiveMode":"","PostTemporalSharpening":"","PostTemporalSharpeningStrength":"","Strength":""},"Filter":"","SpatialFilterSettings":{"PostFilterSharpenStrength":"","Speed":"","Strength":""},"FilterSettings":{"Strength":""}}}},"CaptionDescriptions":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-08-29/presets/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_queue(client):
    """Test case for update_queue

    
    """
    body = {"Status":"","Description":"","ReservationPlanSettings":{"Commitment":"","ReservedSlots":"","RenewalType":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-08-29/queues/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

