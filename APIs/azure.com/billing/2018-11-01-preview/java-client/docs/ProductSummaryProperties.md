

# ProductSummaryProperties

The properties of the product summary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityId** | **String** | Availability Id. |  [optional] [readonly] |
|**billingFrequency** | [**BillingFrequencyEnum**](#BillingFrequencyEnum) | Billing frequency. |  [optional] |
|**billingProfileId** | **String** | Billing Profile id to which this product belongs. |  [optional] [readonly] |
|**billingProfileName** | **String** | Billing Profile name to which this product belongs. |  [optional] [readonly] |
|**displayName** | **String** | The display name of the product. |  [optional] [readonly] |
|**endDate** | **OffsetDateTime** | end date. |  [optional] [readonly] |
|**invoiceSectionId** | **String** | Invoice section id to which this product belongs. |  [optional] [readonly] |
|**invoiceSectionName** | **String** | Invoice section name to which this product belongs. |  [optional] [readonly] |
|**lastCharge** | [**Amount**](Amount.md) |  |  [optional] |
|**lastChargeDate** | **OffsetDateTime** | The date of the last charge. |  [optional] [readonly] |
|**parentProductId** | **String** | Parent Product Id. |  [optional] [readonly] |
|**productType** | **String** | The type of product. |  [optional] [readonly] |
|**productTypeId** | **String** | The product type id. |  [optional] [readonly] |
|**purchaseDate** | **OffsetDateTime** | The date of purchase. |  [optional] [readonly] |
|**quantity** | **BigDecimal** | The purchased product quantity. |  [optional] [readonly] |
|**skuDescription** | **String** | Sku description. |  [optional] [readonly] |
|**skuId** | **String** | Sku Id. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Product status. |  [optional] |



## Enum: BillingFrequencyEnum

| Name | Value |
|---- | -----|
| ONE_TIME | &quot;OneTime&quot; |
| MONTHLY | &quot;Monthly&quot; |
| USAGE_BASED | &quot;UsageBased&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| INACTIVE | &quot;Inactive&quot; |
| PAST_DUE | &quot;PastDue&quot; |
| EXPIRING | &quot;Expiring&quot; |
| EXPIRED | &quot;Expired&quot; |
| DISABLED | &quot;Disabled&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| AUTO_RENEW | &quot;AutoRenew&quot; |



