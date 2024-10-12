# VoiceApi.CreateCallRequestAnswerUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventMethod** | **String** | The HTTP method used to send event information to &#x60;event_url&#x60;. | [optional] [default to &#39;POST&#39;]
**eventUrl** | **[String]** | **Required** unless &#x60;event_url&#x60; is configured at the application level, see [Create an Application](/api/application.v2#createApplication)  The webhook endpoint where call progress events are sent to. For more information about the values sent, see [Event webhook](/voice/voice-api/webhook-reference#event-webhook).  | [optional] 
**from** | [**EndpointPhoneFrom**](EndpointPhoneFrom.md) |  | 
**lengthTimer** | **Number** | Set the number of seconds that elapse before Vonage hangs up after the call state changes to answered. | [optional] [default to 7200]
**machineDetection** | **String** | Configure the behavior when Vonage detects that the call is answered by voicemail. If &#x60;continue&#x60;, Vonage sends an HTTP request to &#x60;event_url&#x60; with the Call event machine. If &#x60;hangup&#x60;, Vonage ends the call. | [optional] 
**randomFromNumber** | **Boolean** | Set to &#x60;true&#x60; to use random phone number as &#x60;from&#x60;. The number will be selected from the list of the numbers assigned to the current application. &#x60;random_from_number: true&#x60; cannot be used together with &#x60;from&#x60;. | [optional] [default to false]
**ringingTimer** | **Number** | Set the number of seconds that elapse before Vonage hangs up after the call state changes to ‘ringing’. | [optional] [default to 60]
**to** | [**[CreateCallRequestBaseToInner]**](CreateCallRequestBaseToInner.md) |  | 
**answerMethod** | **String** | The HTTP method used to send event information to answer_url. | [optional] [default to &#39;GET&#39;]
**answerUrl** | **[String]** | The webhook endpoint where you provide the [Nexmo Call Control Object](/voice/voice-api/ncco-reference) that governs this call.  | 



## Enum: EventMethodEnum


* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)





## Enum: MachineDetectionEnum


* `continue` (value: `"continue"`)

* `hangup` (value: `"hangup"`)





## Enum: AnswerMethodEnum


* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)




