# RocketServices.Entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveryType** | **String** |  | 
**exclusionRules** | [**[ExclusionRule]**](ExclusionRule.md) | Any specific playback exclusion rules. | [optional] 
**maxDownloads** | **Number** | The maximum number of allowed downloads. | [optional] 
**maxPlays** | **Number** | The maximum number of allowed plays. | [optional] 
**ownership** | **String** |  | 
**playPeriod** | **Number** | The length of time in minutes which the rental will last once played for the first time. | [optional] 
**rentalPeriod** | **Number** | The length of time in minutes which the rental will last once purchased. | [optional] 
**resolution** | **String** |  | 
**scopes** | **[String]** |  | 
**activationDate** | **Date** | The date of activation. If no date is defined the entitlement has not be activated. | [optional] 
**classification** | [**ClassificationSummary**](ClassificationSummary.md) |  | [optional] 
**creationDate** | **Date** | The date the entitlement was created. | [optional] 
**expirationDate** | **Date** | The date the entitlement expires. | [optional] 
**itemId** | **String** | The id of the item this entitlement is for. | [optional] 
**itemType** | **String** | The type of item this entitlement is for. | [optional] 
**mediaDuration** | **Number** | The duration of the entitled media. | [optional] 
**planId** | **String** | The id of the plan this entitlement is for. | [optional] 
**playCount** | **Number** | How many times the media has been played. | [optional] 
**remainingDownloads** | **Number** | How many more downloads of this media are available. | [optional] 



## Enum: DeliveryTypeEnum


* `Stream` (value: `"Stream"`)

* `Download` (value: `"Download"`)

* `StreamOrDownload` (value: `"StreamOrDownload"`)

* `ProgressiveDownload` (value: `"ProgressiveDownload"`)

* `None` (value: `"None"`)





## Enum: OwnershipEnum


* `Subscription` (value: `"Subscription"`)

* `Free` (value: `"Free"`)

* `Rent` (value: `"Rent"`)

* `Own` (value: `"Own"`)

* `None` (value: `"None"`)





## Enum: ResolutionEnum


* `SD` (value: `"SD"`)

* `HD-720` (value: `"HD-720"`)

* `HD-1080` (value: `"HD-1080"`)

* `HD-4K` (value: `"HD-4K"`)

* `External` (value: `"External"`)

* `Unknown` (value: `"Unknown"`)





## Enum: ItemTypeEnum


* `movie` (value: `"movie"`)

* `show` (value: `"show"`)

* `season` (value: `"season"`)

* `episode` (value: `"episode"`)

* `program` (value: `"program"`)

* `link` (value: `"link"`)

* `trailer` (value: `"trailer"`)

* `channel` (value: `"channel"`)

* `customAsset` (value: `"customAsset"`)




