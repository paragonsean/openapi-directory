

# AudioItemData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**album** | **String** | Album information associated with the media |  [optional] |
|**artist** | **String** | The artist associated with the media |  [optional] |
|**audioTitle** | **String** | For first-party client use only |  [optional] |
|**bingeAggId** | **String** | Indicates which aggregration ID this recommendation was binged from |  [optional] |
|**button** | **String** | The text contents of an action button displayed on the client |  [optional] |
|**date** | **OffsetDateTime** | The publication date in ISO-8601 format |  [optional] |
|**description** | **String** | A short description or teaser |  [optional] |
|**duration** | **Integer** | The length of the audio content in seconds |  [optional] |
|**expires** | **OffsetDateTime** | The media&#39;s expiration date in ISO-8601 format |  [optional] |
|**geofence** | [**Geofence**](Geofence.md) |  |  [optional] |
|**inFlow** | **Boolean** | Indicates the likelihood of being within a flow, useful for stateful playback buttons |  [optional] |
|**label** | **String** | The record label associated with the media |  [optional] |
|**organization** | [**RecommendationOrganization**](RecommendationOrganization.md) |  |  [optional] |
|**primary** | **Boolean** | Whether the audio is the primary audio of the story to which it is associated |  [optional] |
|**program** | **String** | The program associated with this media |  [optional] |
|**provider** | **String** | The name of the organization providing this media |  [optional] |
|**rating** | [**RatingData**](RatingData.md) |  |  |
|**rationale** | **String** | A short summary of why this content was recommended |  |
|**skippable** | **Boolean** | Whether the client should allow this content to be skipped |  |
|**slug** | **String** | A tag or category for this media |  [optional] |
|**song** | **String** | The song title associated with the media |  [optional] |
|**streamGuid** | **String** | The full GUID of the live stream returned within the recommendation |  [optional] |
|**title** | **String** | The title of this media |  |
|**type** | [**TypeEnum**](#TypeEnum) | Help determine how content is displayed; for more information, see &lt;a href&#x3D;&#39;https://dev.npr.org/design/general-specifications/playing-audio/&#39;&gt;our design guidelines&lt;/a&gt; |  |
|**uid** | **String** | The media ID (for use in ratings objects) |  |
|**unavailableText** | **String** | The text contents to be displayed on the client if no media URLs are available |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUDIO | &quot;audio&quot; |
| SPONSORSHIP | &quot;sponsorship&quot; |
| STATION_ID | &quot;stationId&quot; |
| INTRO | &quot;intro&quot; |
| DONATE | &quot;donate&quot; |
| FEATURE_CARD_INFORMATIONAL | &quot;featureCardInformational&quot; |
| FEATURE_CARD_NOTIFICATION | &quot;featureCardNotification&quot; |
| FEATURE_CARD_PROMOTION | &quot;featureCardPromotion&quot; |
| FEATURE_CARD_EXTERNAL_LINK | &quot;featureCardExternalLink&quot; |
| FEATURE_CARD_ASYNC_REQUEST | &quot;featureCardAsyncRequest&quot; |



