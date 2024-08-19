# RocketServices.Offer

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
**availability** | **String** |  | 
**customFields** | **{String: Object}** | A map of custom fields defined by a curator for an offer. | [optional] 
**endDate** | **Date** |  | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**price** | **Number** |  | 
**startDate** | **Date** |  | [optional] 
**subscriptionCode** | **String** | The code of the subscription this offer is offered under, if any. | [optional] 



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





## Enum: AvailabilityEnum


* `Available` (value: `"Available"`)

* `ComingSoon` (value: `"ComingSoon"`)




