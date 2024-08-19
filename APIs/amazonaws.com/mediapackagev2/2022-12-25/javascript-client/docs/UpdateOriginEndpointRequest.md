# AwsElementalMediaPackageV2.UpdateOriginEndpointRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerType** | **String** | The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file.  | 
**segment** | [**CreateOriginEndpointRequestSegment**](CreateOriginEndpointRequestSegment.md) |  | [optional] 
**description** | **String** | Any descriptive information that you want to add to the origin endpoint for future identification purposes. | [optional] 
**startoverWindowSeconds** | **Number** | The size of the window (in seconds) to create a window of the live stream that&#39;s available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days). | [optional] 
**hlsManifests** | [**[CreateHlsManifestConfiguration]**](CreateHlsManifestConfiguration.md) | An HTTP live streaming (HLS) manifest configuration. | [optional] 
**lowLatencyHlsManifests** | [**[CreateLowLatencyHlsManifestConfiguration]**](CreateLowLatencyHlsManifestConfiguration.md) | A low-latency HLS manifest configuration. | [optional] 



## Enum: ContainerTypeEnum


* `TS` (value: `"TS"`)

* `CMAF` (value: `"CMAF"`)




