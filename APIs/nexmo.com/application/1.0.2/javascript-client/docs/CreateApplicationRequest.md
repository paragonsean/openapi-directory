# NexmoApplicationApi.CreateApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answerMethod** | **String** | The HTTP method used to make the request to &#x60;answer_url&#x60;. The default value is &#x60;GET&#x60;. | [optional] 
**answerUrl** | **String** | The URL where your webhook delivers the Nexmo Call Control Object that governs this call. As soon as your user answers a call Nexmo makes a request to &#x60;answer_url&#x60;. Required for inbound calls only. | [optional] 
**apiKey** | **String** | You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview) | 
**apiSecret** | **String** | You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview) | 
**eventMethod** | **String** | The HTTP method used to send event information to &#x60;event_url&#x60;. The default value is &#x60;POST&#x60;. For &#x60;voice&#x60; type applications only. | [optional] 
**eventUrl** | **String** | Nexmo sends event information asynchronously to this URL when status changes for &#x60;voice&#x60; applications. Always required for &#x60;voice&#x60; applications. | [optional] 
**inboundMethod** | **String** | The HTTP method used to send event information to &#x60;inbound_url&#x60;. The default value is &#x60;POST&#x60;. For &#x60;messages&#x60; type applications only. | [optional] 
**inboundUrl** | **String** | Nexmo sends a request to this URL when an inbound message is received. Required for &#x60;messages&#x60; type applications only. | [optional] 
**name** | **String** | The name of your application. | 
**statusMethod** | **String** | The HTTP method used to send event information to &#x60;status_url&#x60;. The default value is &#x60;POST&#x60;. For &#x60;messages&#x60; type applications only. | [optional] 
**statusUrl** | **String** | Nexmo sends event information asynchronously to this URL when status changes. Required for &#x60;messages&#x60; type applications only. | [optional] 
**type** | **String** | The Nexmo product or products that you access with this application. Currently &#x60;voice&#x60; and &#x60;messages&#x60; application types are supported. | 



## Enum: TypeEnum


* `voice` (value: `"voice"`)

* `messages` (value: `"messages"`)




