

# MessagesWebhooksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | &#x60;inbound_url&#x60;: The URL where inbound messages are delivered. &#x60;status_url&#x60;: The URL where message status is delivered. |  |
|**endpointType** | [**EndpointTypeEnum**](#EndpointTypeEnum) |  |  |
|**httpMethod** | [**HttpMethodEnum**](#HttpMethodEnum) | The HTTP method used to send data to the &#x60;inbound_url&#x60; or &#x60;status_url&#x60;. Default is POST. |  |



## Enum: EndpointTypeEnum

| Name | Value |
|---- | -----|
| INBOUND_URL | &quot;inbound_url&quot; |
| STATUS_URL | &quot;status_url&quot; |



## Enum: HttpMethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |



