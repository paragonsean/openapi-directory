

# OfferRights

The base type for both Offer and Entitlement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryType** | [**DeliveryTypeEnum**](#DeliveryTypeEnum) |  |  |
|**exclusionRules** | [**List&lt;ExclusionRule&gt;**](ExclusionRule.md) | Any specific playback exclusion rules. |  [optional] |
|**maxDownloads** | **Integer** | The maximum number of allowed downloads. |  [optional] |
|**maxPlays** | **Integer** | The maximum number of allowed plays. |  [optional] |
|**ownership** | [**OwnershipEnum**](#OwnershipEnum) |  |  |
|**playPeriod** | **Integer** | The length of time in minutes which the rental will last once played for the first time. |  [optional] |
|**rentalPeriod** | **Integer** | The length of time in minutes which the rental will last once purchased. |  [optional] |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) |  |  |
|**scopes** | **List&lt;String&gt;** |  |  |



## Enum: DeliveryTypeEnum

| Name | Value |
|---- | -----|
| STREAM | &quot;Stream&quot; |
| DOWNLOAD | &quot;Download&quot; |
| STREAM_OR_DOWNLOAD | &quot;StreamOrDownload&quot; |
| PROGRESSIVE_DOWNLOAD | &quot;ProgressiveDownload&quot; |
| NONE | &quot;None&quot; |



## Enum: OwnershipEnum

| Name | Value |
|---- | -----|
| SUBSCRIPTION | &quot;Subscription&quot; |
| FREE | &quot;Free&quot; |
| RENT | &quot;Rent&quot; |
| OWN | &quot;Own&quot; |
| NONE | &quot;None&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| SD | &quot;SD&quot; |
| HD_720 | &quot;HD-720&quot; |
| HD_1080 | &quot;HD-1080&quot; |
| HD_4_K | &quot;HD-4K&quot; |
| EXTERNAL | &quot;External&quot; |
| UNKNOWN | &quot;Unknown&quot; |



