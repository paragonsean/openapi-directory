

# WebhookAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Timestamp when webhook configuration was added to system. |  [optional] |
|**endpointUrl** | **URI** | The endpoint is where the webhook request will be sent. |  [optional] |
|**failed** | **Boolean** | Whether webhook has been disabled for too many consecutive failures |  [optional] |
|**modified** | **OffsetDateTime** | Timestamp when webhook configuration was last modified |  [optional] |
|**responseVersion** | [**ResponseVersionEnum**](#ResponseVersionEnum) | The version of webhook request to send to the endpoint URL |  [optional] |
|**triggers** | [**WebhookTriggers**](WebhookTriggers.md) |  |  [optional] |
|**verificationToken** | **String** | Token for verifying sender is ExaVault |  [optional] |



## Enum: ResponseVersionEnum

| Name | Value |
|---- | -----|
| V1 | &quot;v1&quot; |
| V2 | &quot;v2&quot; |



