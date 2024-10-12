

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
|**invoiceNumber** | **String** | Invoice Number. |  [optional] [readonly] |
|**newCredit** | [**Amount**](Amount.md) |  |  [optional] |
|**transactionDate** | **OffsetDateTime** | Transaction Date. |  [optional] [readonly] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| NEW_CREDIT | &quot;NewCredit&quot; |
| EXPIRED_CREDIT | &quot;ExpiredCredit&quot; |
| SETTLED_CHARGES | &quot;SettledCharges&quot; |



