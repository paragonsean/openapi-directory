# RocketServices.ExclusionRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** |  | [optional] 
**device** | **String** | The device type that the exclusion rules apply to. | [optional] 
**excludeAirplay** | **Boolean** | Prevent airplay from an apple device. | [optional] 
**excludeChromecast** | **Boolean** | Prevent chromecasting. | [optional] 
**excludeDelivery** | **String** |  | [optional] 
**excludeMinResolution** | **String** |  | [optional] 



## Enum: ExcludeDeliveryEnum


* `Stream` (value: `"Stream"`)

* `Download` (value: `"Download"`)

* `StreamOrDownload` (value: `"StreamOrDownload"`)

* `ProgressiveDownload` (value: `"ProgressiveDownload"`)

* `None` (value: `"None"`)





## Enum: ExcludeMinResolutionEnum


* `SD` (value: `"SD"`)

* `HD-720` (value: `"HD-720"`)

* `HD-1080` (value: `"HD-1080"`)

* `HD-4K` (value: `"HD-4K"`)

* `External` (value: `"External"`)

* `Unknown` (value: `"Unknown"`)




