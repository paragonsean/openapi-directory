# RealTimeBiddingApi.VideoMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **String** | The duration of the ad. Can be used to filter the response of the creatives.list method. | [optional] 
**isValidVast** | **Boolean** | Is this a valid VAST ad? Can be used to filter the response of the creatives.list method. | [optional] 
**isVpaid** | **Boolean** | Is this a VPAID ad? Can be used to filter the response of the creatives.list method. | [optional] 
**mediaFiles** | [**[MediaFile]**](MediaFile.md) | The list of all media files declared in the VAST. If there are multiple VASTs in a wrapper chain, this includes the media files from the deepest one in the chain. | [optional] 
**skipOffset** | **String** | The minimum duration that the user has to watch before being able to skip this ad. If the field is not set, the ad is not skippable. If the field is set, the ad is skippable. Can be used to filter the response of the creatives.list method. | [optional] 
**vastVersion** | **String** | The maximum VAST version across all wrapped VAST documents. Can be used to filter the response of the creatives.list method. | [optional] 



## Enum: VastVersionEnum


* `UNSPECIFIED` (value: `"VAST_VERSION_UNSPECIFIED"`)

* `1_0` (value: `"VAST_VERSION_1_0"`)

* `2_0` (value: `"VAST_VERSION_2_0"`)

* `3_0` (value: `"VAST_VERSION_3_0"`)

* `4_0` (value: `"VAST_VERSION_4_0"`)




