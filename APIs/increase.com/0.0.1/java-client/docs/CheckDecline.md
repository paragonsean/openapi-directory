

# CheckDecline

A Check Decline object. This field will be present in the JSON response if and only if `category` is equal to `check_decline`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**auxiliaryOnUs** | **String** |  |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Why the check was declined. |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ACH_ROUTE_CANCELED | &quot;ach_route_canceled&quot; |
| ACH_ROUTE_DISABLED | &quot;ach_route_disabled&quot; |
| BREACHES_LIMIT | &quot;breaches_limit&quot; |
| ENTITY_NOT_ACTIVE | &quot;entity_not_active&quot; |
| GROUP_LOCKED | &quot;group_locked&quot; |
| INSUFFICIENT_FUNDS | &quot;insufficient_funds&quot; |
| UNABLE_TO_LOCATE_ACCOUNT | &quot;unable_to_locate_account&quot; |
| UNABLE_TO_PROCESS | &quot;unable_to_process&quot; |
| REFER_TO_IMAGE | &quot;refer_to_image&quot; |
| STOP_PAYMENT_REQUESTED | &quot;stop_payment_requested&quot; |
| RETURNED | &quot;returned&quot; |
| DUPLICATE_PRESENTMENT | &quot;duplicate_presentment&quot; |
| NOT_AUTHORIZED | &quot;not_authorized&quot; |



