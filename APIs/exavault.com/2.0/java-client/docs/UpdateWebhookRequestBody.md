

# UpdateWebhookRequestBody



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointUrl** | **URI** | New endpoint URL to use for the webhook configuration |  [optional] |
|**resource** | **String** | Resource identifier of the top folder watched by this webhook. |  [optional] |
|**responseVersion** | [**ResponseVersionEnum**](#ResponseVersionEnum) | Version of the webhooks message to send to the endpoint |  [optional] |
|**triggers** | [**WebhookTriggers**](WebhookTriggers.md) |  |  [optional] |



## Enum: ResponseVersionEnum

| Name | Value |
|---- | -----|
| V2 | &quot;v2&quot; |
| V1 | &quot;v1&quot; |



