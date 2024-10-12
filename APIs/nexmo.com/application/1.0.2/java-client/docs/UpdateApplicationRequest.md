

# UpdateApplicationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerMethod** | **String** | The HTTP method used to make the request to &#x60;answer_url&#x60;. The default value is &#x60;GET&#x60;. |  [optional] |
|**answerUrl** | **String** | The URL where your webhook delivers the Nexmo Call Control Object that governs this call. As soon as your user answers a call Nexmo makes a request to &#x60;answer_url&#x60;. |  [optional] |
|**apiKey** | **String** | You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview) |  |
|**apiSecret** | **String** | You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview) |  |
|**eventMethod** | **String** | The HTTP method used to send event information to &#x60;event_url&#x60;. The default value is POST. |  [optional] |
|**eventUrl** | **String** | Nexmo sends event information asynchronously to this URL when status changes. |  [optional] |
|**name** | **String** | The name of your application. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The Nexmo product or products that you access with this application. Currently &#x60;voice&#x60; and &#x60;messages&#x60; application types are supported. You  can&#39;t change the type of application. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VOICE | &quot;voice&quot; |
| MESSAGES | &quot;messages&quot; |



