

# CreateCallRequestNcco


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventMethod** | [**EventMethodEnum**](#EventMethodEnum) | The HTTP method used to send event information to &#x60;event_url&#x60;. |  [optional] |
|**eventUrl** | **List&lt;URI&gt;** | **Required** unless &#x60;event_url&#x60; is configured at the application level, see [Create an Application](/api/application.v2#createApplication)  The webhook endpoint where call progress events are sent to. For more information about the values sent, see [Event webhook](/voice/voice-api/webhook-reference#event-webhook).  |  [optional] |
|**from** | [**EndpointPhoneFrom**](EndpointPhoneFrom.md) |  |  |
|**lengthTimer** | **Integer** | Set the number of seconds that elapse before Vonage hangs up after the call state changes to answered. |  [optional] |
|**machineDetection** | [**MachineDetectionEnum**](#MachineDetectionEnum) | Configure the behavior when Vonage detects that the call is answered by voicemail. If &#x60;continue&#x60;, Vonage sends an HTTP request to &#x60;event_url&#x60; with the Call event machine. If &#x60;hangup&#x60;, Vonage ends the call. |  [optional] |
|**randomFromNumber** | **Boolean** | Set to &#x60;true&#x60; to use random phone number as &#x60;from&#x60;. The number will be selected from the list of the numbers assigned to the current application. &#x60;random_from_number: true&#x60; cannot be used together with &#x60;from&#x60;. |  [optional] |
|**ringingTimer** | **Integer** | Set the number of seconds that elapse before Vonage hangs up after the call state changes to ‘ringing’. |  [optional] |
|**to** | [**List&lt;CreateCallRequestBaseToInner&gt;**](CreateCallRequestBaseToInner.md) |  |  |
|**ncco** | **List&lt;Object&gt;** | The [Nexmo Call Control Object](/voice/voice-api/ncco-reference) to use for this call.  |  |



## Enum: EventMethodEnum

| Name | Value |
|---- | -----|
| POST | &quot;POST&quot; |
| GET | &quot;GET&quot; |



## Enum: MachineDetectionEnum

| Name | Value |
|---- | -----|
| CONTINUE | &quot;continue&quot; |
| HANGUP | &quot;hangup&quot; |



