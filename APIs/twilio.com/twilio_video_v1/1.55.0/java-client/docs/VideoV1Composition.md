

# VideoV1Composition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Composition resource. |  [optional] |
|**audioSources** | **List&lt;String&gt;** | The array of track names to include in the composition. The composition includes all audio sources specified in &#x60;audio_sources&#x60; except those specified in &#x60;audio_sources_excluded&#x60;. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; includes tracks named &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. |  [optional] |
|**audioSourcesExcluded** | **List&lt;String&gt;** | The array of track names to exclude from the composition. The composition includes all audio sources specified in &#x60;audio_sources&#x60; except for those specified in &#x60;audio_sources_excluded&#x60;. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, &#x60;student*&#x60; excludes &#x60;student&#x60; as well as &#x60;studentTeam&#x60;. This parameter can also be empty. |  [optional] |
|**bitrate** | **Integer** | The average bit rate of the composition&#39;s media. |  [optional] |
|**dateCompleted** | **OffsetDateTime** | The date and time in GMT when the composition&#39;s media processing task finished, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateDeleted** | **OffsetDateTime** | The date and time in GMT when the composition generated media was deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**duration** | **Integer** | The duration of the composition&#39;s media file in seconds. |  [optional] |
|**format** | **CompositionEnumFormat** |  |  [optional] |
|**links** | **Object** | The URL of the media file associated with the composition. |  [optional] |
|**mediaExternalLocation** | **URI** | The URL of the media file associated with the composition when stored externally. See [External S3 Compositions](/docs/video/api/external-s3-compositions) for more details. |  [optional] |
|**resolution** | **String** | The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string&#39;s format is &#x60;{width}x{height}&#x60;, such as &#x60;640x480&#x60;. |  [optional] |
|**roomSid** | **String** | The SID of the Group Room that generated the audio and video tracks used in the composition. All media sources included in a composition must belong to the same Group Room. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Composition resource. |  [optional] |
|**size** | **Long** | The size of the composed media file in bytes. |  [optional] |
|**status** | **CompositionEnumStatus** |  |  [optional] |
|**statusCallback** | **URI** | The URL called using the &#x60;status_callback_method&#x60; to send status information on every composition event. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | The HTTP method used to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60;, defaults to &#x60;POST&#x60;. |  [optional] |
|**trim** | **Boolean** | Whether to remove intervals with no media, as specified in the POST request that created the composition. Compositions with &#x60;trim&#x60; enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**videoLayout** | **Object** | An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. |  [optional] |



## Enum: StatusCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



