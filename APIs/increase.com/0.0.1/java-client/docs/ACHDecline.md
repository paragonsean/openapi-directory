

# ACHDecline

A ACH Decline object. This field will be present in the JSON response if and only if `category` is equal to `ach_decline`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The declined amount in the minor unit of the destination account currency. For dollars, for example, this is cents. |  |
|**originatorCompanyDescriptiveDate** | **String** |  |  |
|**originatorCompanyDiscretionaryData** | **String** |  |  |
|**originatorCompanyId** | **String** |  |  |
|**originatorCompanyName** | **String** |  |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Why the ACH transfer was declined. |  |
|**receiverIdNumber** | **String** |  |  |
|**receiverName** | **String** |  |  |
|**traceNumber** | **String** |  |  |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ACH_ROUTE_CANCELED | &quot;ach_route_canceled&quot; |
| ACH_ROUTE_DISABLED | &quot;ach_route_disabled&quot; |
| BREACHES_LIMIT | &quot;breaches_limit&quot; |
| CREDIT_ENTRY_REFUSED_BY_RECEIVER | &quot;credit_entry_refused_by_receiver&quot; |
| DUPLICATE_RETURN | &quot;duplicate_return&quot; |
| ENTITY_NOT_ACTIVE | &quot;entity_not_active&quot; |
| GROUP_LOCKED | &quot;group_locked&quot; |
| INSUFFICIENT_FUNDS | &quot;insufficient_funds&quot; |
| MISROUTED_RETURN | &quot;misrouted_return&quot; |
| NO_ACH_ROUTE | &quot;no_ach_route&quot; |
| ORIGINATOR_REQUEST | &quot;originator_request&quot; |
| TRANSACTION_NOT_ALLOWED | &quot;transaction_not_allowed&quot; |



