# TwilioVideo.VideoV1CompositionHook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CompositionHook resource. | [optional] 
**audioSources** | **[String]** | The array of track names to include in the compositions created by the composition hook. A composition triggered by the composition hook includes all audio sources specified in &#x60;audio_sources&#x60; except those specified in &#x60;audio_sources_excluded&#x60;. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; includes tracks named &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request | [optional] 
**audioSourcesExcluded** | **[String]** | The array of track names to exclude from the compositions created by the composition hook. A composition triggered by the composition hook includes all audio sources specified in &#x60;audio_sources&#x60; except for those specified in &#x60;audio_sources_excluded&#x60;. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; excludes &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. This parameter can also be empty. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**enabled** | **Boolean** | Whether the CompositionHook is active. When &#x60;true&#x60;, the CompositionHook is triggered for every completed Group Room on the account. When &#x60;false&#x60;, the CompositionHook is never triggered. | [optional] 
**format** | [**CompositionHookEnumFormat**](CompositionHookEnumFormat.md) |  | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. Can be up to 100 characters long and must be unique within the account. | [optional] 
**resolution** | **String** | The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string&#39;s format is &#x60;{width}x{height}&#x60;, such as &#x60;640x480&#x60;. | [optional] 
**sid** | **String** | The unique string that we created to identify the CompositionHook resource. | [optional] 
**statusCallback** | **String** | The URL we call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
**statusCallbackMethod** | **String** | The HTTP method we should use to call &#x60;status_callback&#x60;. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
**trim** | **Boolean** | Whether intervals with no media are clipped, as specified in the POST request that created the CompositionHook resource. Compositions with &#x60;trim&#x60; enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 
**videoLayout** | **Object** | A JSON object that describes the video layout of the composition in terms of regions as specified in the HTTP POST request that created the CompositionHook resource. See [POST Parameters](https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters) for more information. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request | [optional] 



## Enum: StatusCallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




