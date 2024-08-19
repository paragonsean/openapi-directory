

# Entitlement


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
|**activationDate** | **OffsetDateTime** | The date of activation. If no date is defined the entitlement has not be activated. |  [optional] |
|**classification** | [**ClassificationSummary**](ClassificationSummary.md) |  |  [optional] |
|**creationDate** | **OffsetDateTime** | The date the entitlement was created. |  [optional] |
|**expirationDate** | **OffsetDateTime** | The date the entitlement expires. |  [optional] |
|**itemId** | **String** | The id of the item this entitlement is for. |  [optional] |
|**itemType** | [**ItemTypeEnum**](#ItemTypeEnum) | The type of item this entitlement is for. |  [optional] |
|**mediaDuration** | **Integer** | The duration of the entitled media. |  [optional] |
|**planId** | **String** | The id of the plan this entitlement is for. |  [optional] |
|**playCount** | **Integer** | How many times the media has been played. |  [optional] |
|**remainingDownloads** | **Integer** | How many more downloads of this media are available. |  [optional] |



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



## Enum: ItemTypeEnum

| Name | Value |
|---- | -----|
| MOVIE | &quot;movie&quot; |
| SHOW | &quot;show&quot; |
| SEASON | &quot;season&quot; |
| EPISODE | &quot;episode&quot; |
| PROGRAM | &quot;program&quot; |
| LINK | &quot;link&quot; |
| TRAILER | &quot;trailer&quot; |
| CHANNEL | &quot;channel&quot; |
| CUSTOM_ASSET | &quot;customAsset&quot; |



