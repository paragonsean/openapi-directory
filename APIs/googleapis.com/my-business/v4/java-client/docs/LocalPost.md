

# LocalPost

Represents a [local post](https://support.google.com/business/answer/7662907) for a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertType** | [**AlertTypeEnum**](#AlertTypeEnum) | The type of alert the post is created for. This field is only applicable for posts of topic_type Alert, and behaves as a sub-type of Alerts. |  [optional] |
|**callToAction** | [**CallToAction**](CallToAction.md) |  |  [optional] |
|**createTime** | **String** | Output only. Time of the creation of the post. |  [optional] |
|**event** | [**LocalPostEvent**](LocalPostEvent.md) |  |  [optional] |
|**languageCode** | **String** | The language of the local post. |  [optional] |
|**media** | [**List&lt;MediaItem&gt;**](MediaItem.md) | The media associated with the post. source_url is the only supported data field for a LocalPost MediaItem. |  [optional] |
|**name** | **String** | Output only. Google identifier for this local post in the form: &#x60;accounts/{account_id}/locations/{location_id}/localPosts/{local_post_id}&#x60; |  [optional] |
|**offer** | [**LocalPostOffer**](LocalPostOffer.md) |  |  [optional] |
|**searchUrl** | **String** | Output only. The link to the local post in Google search. This link can be used to share the post via social media, email, text, etc. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the post, indicating what part of its lifecycle it is in. |  [optional] |
|**summary** | **String** | Description/body of the local post. |  [optional] |
|**topicType** | [**TopicTypeEnum**](#TopicTypeEnum) | Required. The topic type of the post: standard, event, offer, or alert. |  [optional] |
|**updateTime** | **String** | Output only. Time of the last modification of the post made by the user. |  [optional] |



## Enum: AlertTypeEnum

| Name | Value |
|---- | -----|
| ALERT_TYPE_UNSPECIFIED | &quot;ALERT_TYPE_UNSPECIFIED&quot; |
| COVID_19 | &quot;COVID_19&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| LOCAL_POST_STATE_UNSPECIFIED | &quot;LOCAL_POST_STATE_UNSPECIFIED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| LIVE | &quot;LIVE&quot; |
| PROCESSING | &quot;PROCESSING&quot; |



## Enum: TopicTypeEnum

| Name | Value |
|---- | -----|
| LOCAL_POST_TOPIC_TYPE_UNSPECIFIED | &quot;LOCAL_POST_TOPIC_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| EVENT | &quot;EVENT&quot; |
| OFFER | &quot;OFFER&quot; |
| ALERT | &quot;ALERT&quot; |



