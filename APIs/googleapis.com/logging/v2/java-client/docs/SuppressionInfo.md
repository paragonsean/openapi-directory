

# SuppressionInfo

Information about entries that were omitted from the session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason that entries were omitted from the session. |  [optional] |
|**suppressedCount** | **Integer** | A lower bound on the count of entries omitted due to reason. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| REASON_UNSPECIFIED | &quot;REASON_UNSPECIFIED&quot; |
| RATE_LIMIT | &quot;RATE_LIMIT&quot; |
| NOT_CONSUMED | &quot;NOT_CONSUMED&quot; |



