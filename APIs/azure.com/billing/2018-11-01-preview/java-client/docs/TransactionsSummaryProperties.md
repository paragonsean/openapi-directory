

# TransactionsSummaryProperties

The properties of the reservation transaction summary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingProfileId** | **String** | Billing Profile id to which this product belongs. |  [optional] [readonly] |
|**billingProfileName** | **String** | Billing Profile name to which this product belongs. |  [optional] [readonly] |
|**customerDisplayName** | **String** | Display name of customer to which this product belongs. |  [optional] [readonly] |
|**customerId** | **String** | Customer id to which this product belongs. |  [optional] [readonly] |
|**date** | **OffsetDateTime** | The date of reservation transaction. |  [optional] [readonly] |
|**invoice** | **String** | Invoice number or &#39;pending&#39; if not invoiced. |  [optional] [readonly] |
|**invoiceSectionId** | **String** | Invoice section id to which this product belongs. |  [optional] [readonly] |
|**invoiceSectionName** | **String** | Invoice section name to which this product belongs. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | The kind of transaction. Choices are all and reservation. |  [optional] |
|**orderId** | **String** | The reservation order id. |  [optional] [readonly] |
|**orderName** | **String** | The reservation order name. |  [optional] [readonly] |
|**productDescription** | **String** | Product description. |  [optional] [readonly] |
|**productFamily** | **String** | The product family. |  [optional] [readonly] |
|**productType** | **String** | The type of product. |  [optional] [readonly] |
|**productTypeId** | **String** | The product type id. |  [optional] [readonly] |
|**quantity** | **Integer** | Purchase quantity. |  [optional] [readonly] |
|**subscriptionId** | **String** | The subscription id. |  [optional] [readonly] |
|**subscriptionName** | **String** | The subscription name. |  [optional] [readonly] |
|**transactionAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**transactionType** | [**TransactionTypeEnum**](#TransactionTypeEnum) | Transaction types. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| RESERVATION | &quot;reservation&quot; |



## Enum: TransactionTypeEnum

| Name | Value |
|---- | -----|
| PURCHASE | &quot;Purchase&quot; |
| USAGE_CHARGE | &quot;Usage Charge&quot; |



