

# MediaV1PlayerStreamer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PlayerStreamer resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**endedReason** | **PlayerStreamerEnumEndedReason** |  |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**maxDuration** | **Integer** | The maximum time, in seconds, that the PlayerStreamer is active (&#x60;created&#x60; or &#x60;started&#x60;) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming. |  [optional] |
|**sid** | **String** | The unique string generated to identify the PlayerStreamer resource. |  [optional] |
|**status** | **PlayerStreamerEnumStatus** |  |  [optional] |
|**statusCallback** | **URI** | The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**video** | **Boolean** | Specifies whether the PlayerStreamer is configured to stream video. Defaults to &#x60;true&#x60;. |  [optional] |



## Enum: StatusCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



