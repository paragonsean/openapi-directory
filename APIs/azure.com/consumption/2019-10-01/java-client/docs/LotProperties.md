

# LotProperties

The lot properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedBalance** | [**Amount**](Amount.md) |  |  [optional] |
|**expirationDate** | **OffsetDateTime** | Expiration date. |  [optional] [readonly] |
|**originalAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**poNumber** | **String** | PO number. |  [optional] [readonly] |
|**source** | [**SourceEnum**](#SourceEnum) | Lot source. |  [optional] [readonly] |
|**startDate** | **OffsetDateTime** | Start date. |  [optional] [readonly] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PURCHASED_CREDIT | &quot;PurchasedCredit&quot; |
| PROMOTIONAL_CREDIT | &quot;PromotionalCredit&quot; |



