# NexmoApplicationApi.MessagesWebhooksInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **String** | &#x60;inbound_url&#x60;: The URL where inbound messages are delivered. &#x60;status_url&#x60;: The URL where message status is delivered. | 
**endpointType** | **String** |  | 
**httpMethod** | **String** | The HTTP method used to send data to the &#x60;inbound_url&#x60; or &#x60;status_url&#x60;. Default is POST. | 



## Enum: EndpointTypeEnum


* `inbound_url` (value: `"inbound_url"`)

* `status_url` (value: `"status_url"`)





## Enum: HttpMethodEnum


* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)




