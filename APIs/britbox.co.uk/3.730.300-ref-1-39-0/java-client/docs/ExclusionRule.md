

# ExclusionRule

Defines playback exclusion rules for an Offer or Entitlement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  [optional] |
|**device** | **String** | The device type that the exclusion rules apply to. |  [optional] |
|**excludeAirplay** | **Boolean** | Prevent airplay from an apple device. |  [optional] |
|**excludeChromecast** | **Boolean** | Prevent chromecasting. |  [optional] |
|**excludeDelivery** | [**ExcludeDeliveryEnum**](#ExcludeDeliveryEnum) |  |  [optional] |
|**excludeMinResolution** | [**ExcludeMinResolutionEnum**](#ExcludeMinResolutionEnum) |  |  [optional] |



## Enum: ExcludeDeliveryEnum

| Name | Value |
|---- | -----|
| STREAM | &quot;Stream&quot; |
| DOWNLOAD | &quot;Download&quot; |
| STREAM_OR_DOWNLOAD | &quot;StreamOrDownload&quot; |
| PROGRESSIVE_DOWNLOAD | &quot;ProgressiveDownload&quot; |
| NONE | &quot;None&quot; |



## Enum: ExcludeMinResolutionEnum

| Name | Value |
|---- | -----|
| SD | &quot;SD&quot; |
| HD_720 | &quot;HD-720&quot; |
| HD_1080 | &quot;HD-1080&quot; |
| HD_4_K | &quot;HD-4K&quot; |
| EXTERNAL | &quot;External&quot; |
| UNKNOWN | &quot;Unknown&quot; |



