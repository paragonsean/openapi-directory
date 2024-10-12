# BillingManagementClient.BillingSubscriptionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingProfileId** | **String** | Billing Profile id to which this product belongs. | [optional] [readonly] 
**billingProfileName** | **String** | Billing Profile name to which this product belongs. | [optional] [readonly] 
**customerDisplayName** | **String** | Display name of customer to which this product belongs. | [optional] [readonly] 
**customerId** | **String** | Customer id to which this product belongs. | [optional] [readonly] 
**displayName** | **String** | display name. | [optional] [readonly] 
**invoiceSectionId** | **String** | Invoice section id to which this product belongs. | [optional] [readonly] 
**invoiceSectionName** | **String** | Invoice section name to which this product belongs. | [optional] [readonly] 
**lastMonthCharges** | [**Amount**](Amount.md) |  | [optional] 
**monthToDateCharges** | [**Amount**](Amount.md) |  | [optional] 
**reseller** | [**Reseller**](Reseller.md) |  | [optional] 
**skuDescription** | **String** | The sku description. | [optional] [readonly] 
**skuId** | **String** | The sku id. | [optional] 
**subscriptionBillingStatus** | **String** | Subscription billing status. | [optional] 
**subscriptionId** | **String** | Subscription Id. | [optional] [readonly] 



## Enum: SubscriptionBillingStatusEnum


* `Active` (value: `"Active"`)

* `Inactive` (value: `"Inactive"`)

* `Abandoned` (value: `"Abandoned"`)

* `Deleted` (value: `"Deleted"`)

* `Warning` (value: `"Warning"`)




