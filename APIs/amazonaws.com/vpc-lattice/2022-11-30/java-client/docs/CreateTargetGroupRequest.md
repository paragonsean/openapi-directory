

# CreateTargetGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. |  [optional] |
|**config** | [**CreateTargetGroupRequestConfig**](CreateTargetGroupRequestConfig.md) |  |  [optional] |
|**name** | **String** | The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can&#39;t use a hyphen as the first or last character, or immediately after another hyphen. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags for the target group. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of target group. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IP | &quot;IP&quot; |
| LAMBDA | &quot;LAMBDA&quot; |
| INSTANCE | &quot;INSTANCE&quot; |
| ALB | &quot;ALB&quot; |



