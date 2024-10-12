

# VoiceWebhooksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | &#x60;answer_url&#x60;: The URL where your webhook delivers the Nexmo Call Control Object that governs this call. As soon as your user answers a call Nexmo makes a request to answer_url. &#x60;event_url&#x60;: Nexmo sends event information asynchronously to this URL when status changes. |  |
|**endpointType** | [**EndpointTypeEnum**](#EndpointTypeEnum) |  |  |
|**httpMethod** | [**HttpMethodEnum**](#HttpMethodEnum) | The HTTP method used to send event information to the &#x60;event_url&#x60; or &#x60;answer_url&#x60;. |  |



## Enum: EndpointTypeEnum

| Name | Value |
|---- | -----|
| ANSWER_URL | &quot;answer_url&quot; |
| EVENT_URL | &quot;event_url&quot; |



## Enum: HttpMethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |



