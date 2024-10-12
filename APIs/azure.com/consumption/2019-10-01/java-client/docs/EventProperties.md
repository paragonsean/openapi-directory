

# EventProperties

The event properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustments** | [**Amount**](Amount.md) |  |  [optional] |
|**charges** | [**Amount**](Amount.md) |  |  [optional] |
|**closedBalance** | [**Amount**](Amount.md) |  |  [optional] |
|**creditExpired** | [**Amount**](Amount.md) |  |  [optional] |
|**description** | **String** | Transaction description. |  [optional] [readonly] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | The type of event. |  [optional] |
|**invoiceNumber** | **String** | Invoice number. |  [optional] [readonly] |
|**newCredit** | [**Amount**](Amount.md) |  |  [optional] |
|**transactionDate** | **OffsetDateTime** | Transaction date. |  [optional] [readonly] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| SETTLED_CHARGES | &quot;SettledCharges&quot; |
| PENDING_CHARGES | &quot;PendingCharges&quot; |
| PENDING_ADJUSTMENTS | &quot;PendingAdjustments&quot; |
| PENDING_NEW_CREDIT | &quot;PendingNewCredit&quot; |
| PENDING_EXPIRED_CREDIT | &quot;PendingExpiredCredit&quot; |
| UN_KNOWN | &quot;UnKnown&quot; |
| NEW_CREDIT | &quot;NewCredit&quot; |



