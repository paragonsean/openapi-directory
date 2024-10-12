

# AddWebhookRequestBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointUrl** | **URI** | The endpoint is where the webhook request will be sent. |  |
|**resource** | **String** | Resource identifier for the top folder this webhook is associated with |  [optional] |
|**responseVersion** | [**ResponseVersionEnum**](#ResponseVersionEnum) | What version of webhook request should be sent to the endpoint URL when messages are sent |  [optional] |
|**triggers** | [**WebhookTriggers**](WebhookTriggers.md) |  |  [optional] |



## Enum: ResponseVersionEnum

| Name | Value |
|---- | -----|
| V1 | &quot;v1&quot; |
| V2 | &quot;v2&quot; |



