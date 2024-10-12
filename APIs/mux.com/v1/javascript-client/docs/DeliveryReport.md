# MuxApi.DeliveryReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetDuration** | **Number** | The duration of the asset in seconds. | [optional] 
**assetId** | **String** | Unique identifier for the asset. | [optional] 
**assetResolutionTier** | **String** | The resolution tier that the asset was ingested at, affecting billing for ingest &amp; storage | [optional] 
**assetState** | **String** | The state of the asset. | [optional] 
**createdAt** | **String** | Time at which the asset was created. Measured in seconds since the Unix epoch. | [optional] 
**deletedAt** | **String** | If exists, time at which the asset was deleted. Measured in seconds since the Unix epoch. | [optional] 
**deliveredSeconds** | **Number** | Total number of delivered seconds during this time window. | [optional] 
**deliveredSecondsByResolution** | [**DeliveryReportDeliveredSecondsByResolution**](DeliveryReportDeliveredSecondsByResolution.md) |  | [optional] 
**liveStreamId** | **String** | Unique identifier for the live stream that created the asset. | [optional] 
**passthrough** | **String** | The &#x60;passthrough&#x60; value for the asset. | [optional] 



## Enum: AssetResolutionTierEnum


* `audio-only` (value: `"audio-only"`)

* `720p` (value: `"720p"`)

* `1080p` (value: `"1080p"`)

* `1440p` (value: `"1440p"`)

* `2160p` (value: `"2160p"`)





## Enum: AssetStateEnum


* `ready` (value: `"ready"`)

* `errored` (value: `"errored"`)

* `deleted` (value: `"deleted"`)




