

# UpcomingInvoiceItem

Line item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | Date-time when the item was added to the subscription. |  [optional] [readonly] |
|**description** | **String** | Description of line item. |  [optional] |
|**periodEndTime** | **OffsetDateTime** | Date-time when the period ends for this item. |  [optional] |
|**periodStartTime** | **OffsetDateTime** | Date-time when the period begins for this item. |  [optional] |
|**quantity** | **Integer** | Quantity of line item. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of line item. |  |
|**unitPriceAmount** | **Double** | Unit price of the line item. |  |
|**unitPriceCurrency** | **String** | ISO 4217 alphabetic currency code. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEBIT | &quot;debit&quot; |
| CREDIT | &quot;credit&quot; |



