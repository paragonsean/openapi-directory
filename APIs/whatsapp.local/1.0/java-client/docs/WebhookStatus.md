

# WebhookStatus



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | [**List&lt;Error&gt;**](Error.md) |  |  [optional] |
|**id** | **String** | Message ID |  [optional] |
|**recipientId** | **String** | WhatsApp ID of recipient |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of message |  [optional] |
|**timestamp** | **String** | Timestamp of the status message |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |
| FAILED | &quot;failed&quot; |
| DELETED | &quot;deleted&quot; |



