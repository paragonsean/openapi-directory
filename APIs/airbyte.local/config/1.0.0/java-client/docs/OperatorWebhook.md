

# OperatorWebhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbtCloud** | [**OperatorWebhookDbtCloud**](OperatorWebhookDbtCloud.md) |  |  [optional] |
|**executionBody** | **String** | DEPRECATED. Populate dbtCloud instead. |  [optional] |
|**executionUrl** | **String** | DEPRECATED. Populate dbtCloud instead. |  [optional] |
|**webhookConfigId** | **UUID** | The id of the webhook configs to use from the workspace. |  [optional] |
|**webhookType** | [**WebhookTypeEnum**](#WebhookTypeEnum) |  |  [optional] |



## Enum: WebhookTypeEnum

| Name | Value |
|---- | -----|
| DBT_CLOUD | &quot;dbtCloud&quot; |



