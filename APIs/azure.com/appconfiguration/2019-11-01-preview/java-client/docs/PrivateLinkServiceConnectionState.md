

# PrivateLinkServiceConnectionState

The state of a private link service connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionsRequired** | [**ActionsRequiredEnum**](#ActionsRequiredEnum) | Any action that is required beyond basic workflow (approve/ reject/ disconnect) |  [optional] [readonly] |
|**description** | **String** | The private link service connection description. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The private link service connection status. |  [optional] |



## Enum: ActionsRequiredEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| RECREATE | &quot;Recreate&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| APPROVED | &quot;Approved&quot; |
| REJECTED | &quot;Rejected&quot; |
| DISCONNECTED | &quot;Disconnected&quot; |



