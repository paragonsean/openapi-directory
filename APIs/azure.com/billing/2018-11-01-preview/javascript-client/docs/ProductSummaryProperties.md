# BillingManagementClient.ProductSummaryProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityId** | **String** | Availability Id. | [optional] [readonly] 
**billingFrequency** | **String** | Billing frequency. | [optional] 
**billingProfileId** | **String** | Billing Profile id to which this product belongs. | [optional] [readonly] 
**billingProfileName** | **String** | Billing Profile name to which this product belongs. | [optional] [readonly] 
**displayName** | **String** | The display name of the product. | [optional] [readonly] 
**endDate** | **Date** | end date. | [optional] [readonly] 
**invoiceSectionId** | **String** | Invoice section id to which this product belongs. | [optional] [readonly] 
**invoiceSectionName** | **String** | Invoice section name to which this product belongs. | [optional] [readonly] 
**lastCharge** | [**Amount**](Amount.md) |  | [optional] 
**lastChargeDate** | **Date** | The date of the last charge. | [optional] [readonly] 
**parentProductId** | **String** | Parent Product Id. | [optional] [readonly] 
**productType** | **String** | The type of product. | [optional] [readonly] 
**productTypeId** | **String** | The product type id. | [optional] [readonly] 
**purchaseDate** | **Date** | The date of purchase. | [optional] [readonly] 
**quantity** | **Number** | The purchased product quantity. | [optional] [readonly] 
**skuDescription** | **String** | Sku description. | [optional] [readonly] 
**skuId** | **String** | Sku Id. | [optional] [readonly] 
**status** | **String** | Product status. | [optional] 



## Enum: BillingFrequencyEnum


* `OneTime` (value: `"OneTime"`)

* `Monthly` (value: `"Monthly"`)

* `UsageBased` (value: `"UsageBased"`)





## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)

* `PastDue` (value: `"PastDue"`)

* `Expiring` (value: `"Expiring"`)

* `Expired` (value: `"Expired"`)

* `Disabled` (value: `"Disabled"`)

* `Cancelled` (value: `"Cancelled"`)

* `AutoRenew` (value: `"AutoRenew"`)




