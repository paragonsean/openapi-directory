

# CreateNetworkWebhooksWebhookTest201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Webhook delivery identifier |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the webhook delivery |  [optional] |
|**url** | **String** | URL where the webhook was delivered |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;abandoned&quot; |
| DELIVERED | &quot;delivered&quot; |
| ENQUEUED | &quot;enqueued&quot; |
| PROCESSING | &quot;processing&quot; |
| RETRYING | &quot;retrying&quot; |



