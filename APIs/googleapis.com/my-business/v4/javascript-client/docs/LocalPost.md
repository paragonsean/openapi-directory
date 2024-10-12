# GoogleMyBusinessApi.LocalPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertType** | **String** | The type of alert the post is created for. This field is only applicable for posts of topic_type Alert, and behaves as a sub-type of Alerts. | [optional] 
**callToAction** | [**CallToAction**](CallToAction.md) |  | [optional] 
**createTime** | **String** | Output only. Time of the creation of the post. | [optional] 
**event** | [**LocalPostEvent**](LocalPostEvent.md) |  | [optional] 
**languageCode** | **String** | The language of the local post. | [optional] 
**media** | [**[MediaItem]**](MediaItem.md) | The media associated with the post. source_url is the only supported data field for a LocalPost MediaItem. | [optional] 
**name** | **String** | Output only. Google identifier for this local post in the form: &#x60;accounts/{account_id}/locations/{location_id}/localPosts/{local_post_id}&#x60; | [optional] 
**offer** | [**LocalPostOffer**](LocalPostOffer.md) |  | [optional] 
**searchUrl** | **String** | Output only. The link to the local post in Google search. This link can be used to share the post via social media, email, text, etc. | [optional] 
**state** | **String** | Output only. The state of the post, indicating what part of its lifecycle it is in. | [optional] 
**summary** | **String** | Description/body of the local post. | [optional] 
**topicType** | **String** | Required. The topic type of the post: standard, event, offer, or alert. | [optional] 
**updateTime** | **String** | Output only. Time of the last modification of the post made by the user. | [optional] 



## Enum: AlertTypeEnum


* `ALERT_TYPE_UNSPECIFIED` (value: `"ALERT_TYPE_UNSPECIFIED"`)

* `COVID_19` (value: `"COVID_19"`)





## Enum: StateEnum


* `LOCAL_POST_STATE_UNSPECIFIED` (value: `"LOCAL_POST_STATE_UNSPECIFIED"`)

* `REJECTED` (value: `"REJECTED"`)

* `LIVE` (value: `"LIVE"`)

* `PROCESSING` (value: `"PROCESSING"`)





## Enum: TopicTypeEnum


* `LOCAL_POST_TOPIC_TYPE_UNSPECIFIED` (value: `"LOCAL_POST_TOPIC_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `EVENT` (value: `"EVENT"`)

* `OFFER` (value: `"OFFER"`)

* `ALERT` (value: `"ALERT"`)




