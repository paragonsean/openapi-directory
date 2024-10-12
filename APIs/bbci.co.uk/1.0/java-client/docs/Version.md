

# Version


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
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**rrc** | [**ClipVersionsInnerRrc**](ClipVersionsInnerRrc.md) |  |  [optional] |
|**serviceId** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**uhd** | **Boolean** |  |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| LEGAL | &quot;legal&quot; |
| EDITORIAL | &quot;editorial&quot; |
| TECHNICAL_REPLACEMENT | &quot;technical-replacement&quot; |
| ORIGINAL | &quot;original&quot; |
| IPLAYER_VERSION | &quot;iplayer-version&quot; |
| LENGTHENED | &quot;lengthened&quot; |
| SHORTENED | &quot;shortened&quot; |
| PRE_WATERSHED | &quot;pre-watershed&quot; |
| POST_WATERSHED | &quot;post-watershed&quot; |
| WARNINGS_HIGHER | &quot;warnings-higher&quot; |
| WARNINGS_LOWER | &quot;warnings-lower&quot; |
| WARNINGS_NONE | &quot;warnings-none&quot; |
| DUPLICATION | &quot;duplication&quot; |
| OPEN_SUBTITLED | &quot;open-subtitled&quot; |
| OTHER | &quot;other&quot; |
| AUDIO_DESCRIBED | &quot;audio-described&quot; |
| SIGNED | &quot;signed&quot; |
| WEBCAST | &quot;webcast&quot; |
| SIMULCAST | &quot;simulcast&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VERSION | &quot;version&quot; |
| VERSION_LARGE | &quot;version_large&quot; |



