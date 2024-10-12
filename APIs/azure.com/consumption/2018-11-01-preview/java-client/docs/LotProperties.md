

# LotProperties

The lot properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedBalance** | [**Amount**](Amount.md) |  |  [optional] |
|**expirationDate** | **OffsetDateTime** | Expiration Date. |  [optional] [readonly] |
|**originalAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**poNumber** | **String** | PO Number. |  [optional] [readonly] |
|**source** | [**SourceEnum**](#SourceEnum) | Lot source. |  [optional] [readonly] |
|**startDate** | **OffsetDateTime** | Start Date. |  [optional] [readonly] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| PURCHASED_CREDIT | &quot;PurchasedCredit&quot; |
| PROMOTIONAL_CREDIT | &quot;PromotionalCredit&quot; |



