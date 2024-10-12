# BillingManagementClient.TransactionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingProfileDisplayName** | **String** | Billing Profile display name to which this product belongs. | [optional] [readonly] 
**billingProfileId** | **String** | Billing Profile id to which this product belongs. | [optional] [readonly] 
**customerDisplayName** | **String** | Display name of customer to which this product belongs. | [optional] [readonly] 
**customerId** | **String** | Customer id to which this product belongs. | [optional] [readonly] 
**date** | **Date** | The date of reservation transaction. | [optional] [readonly] 
**invoice** | **String** | Invoice number or &#39;pending&#39; if not invoiced. | [optional] [readonly] 
**invoiceSectionDisplayName** | **String** | Invoice section display name to which this product belongs. | [optional] [readonly] 
**invoiceSectionId** | **String** | Invoice section id to which this product belongs. | [optional] [readonly] 
**kind** | **String** | The kind of transaction. Choices are all and reservation. | [optional] 
**orderId** | **String** | The reservation order id. | [optional] [readonly] 
**orderName** | **String** | The reservation order name. | [optional] [readonly] 
**productDescription** | **String** | Product description. | [optional] [readonly] 
**productFamily** | **String** | The product family. | [optional] [readonly] 
**productType** | **String** | The type of product. | [optional] [readonly] 
**productTypeId** | **String** | The product type id. | [optional] [readonly] 
**quantity** | **Number** | Purchase quantity. | [optional] [readonly] 
**subscriptionId** | **String** | The subscription id. | [optional] [readonly] 
**subscriptionName** | **String** | The subscription name. | [optional] [readonly] 
**transactionAmount** | [**Amount**](Amount.md) |  | [optional] 
**transactionType** | **String** | Transaction types. | [optional] 



## Enum: KindEnum


* `all` (value: `"all"`)

* `reservation` (value: `"reservation"`)





## Enum: TransactionTypeEnum


* `Purchase` (value: `"Purchase"`)

* `Usage Charge` (value: `"Usage Charge"`)




