

# EpisodeVersionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | [**ClipVersionsInnerAvailability**](ClipVersionsInnerAvailability.md) |  |  |
|**creditsStart** | **BigDecimal** |  |  [optional] |
|**download** | **Boolean** |  |  |
|**duration** | [**BroadcastDuration**](BroadcastDuration.md) |  |  |
|**events** | [**List&lt;ClipVersionsInnerEventsInner&gt;**](ClipVersionsInnerEventsInner.md) |  |  [optional] |
|**firstBroadcast** | **String** |  |  [optional] |
|**firstBroadcastDateTime** | **String** |  |  [optional] |
|**guidance** | [**ClipVersionsInnerGuidance**](ClipVersionsInnerGuidance.md) |  |  [optional] |
|**hd** | **Boolean** |  |  |
|**id** | **String** |  |  |
|**interactions** | [**List&lt;Interaction&gt;**](Interaction.md) |  |  [optional] |
|**kind** | **String** |  |  |
|**rrc** | [**ClipVersionsInnerRrc**](ClipVersionsInnerRrc.md) |  |  [optional] |
|**serviceId** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**uhd** | **Boolean** |  |  |
|**storeId** | **String** |  |  |
|**storeProfile** | **String** |  |  |
|**storeSession** | [**EpisodeVersionsInnerAnyOfStoreSession**](EpisodeVersionsInnerAnyOfStoreSession.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VERSION | &quot;version&quot; |
| VERSION_LARGE | &quot;version_large&quot; |
| STORE_VERSION | &quot;store_version&quot; |



