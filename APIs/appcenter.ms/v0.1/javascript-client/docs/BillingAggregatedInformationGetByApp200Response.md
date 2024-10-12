# AppCenterClient.BillingAggregatedInformationGetByApp200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureSubscriptionId** | **String** | Unique identifier for the Azure subscription used for billing | [optional] 
**azureSubscriptionState** | **String** | State of the Azure subscription used for billing | [optional] 
**billingPlans** | [**BillingAggregatedInformationGetByApp200ResponseBillingPlans**](BillingAggregatedInformationGetByApp200ResponseBillingPlans.md) |  | [optional] 
**id** | **String** | ID of the user or organization | [optional] 
**timestamp** | **String** | The ISO 8601 datetime of last modification | [optional] 
**usage** | [**BillingAggregatedInformationGetByApp200ResponseUsage**](BillingAggregatedInformationGetByApp200ResponseUsage.md) |  | [optional] 
**version** | **String** | Version of the Billing Information schema | [optional] 



## Enum: AzureSubscriptionStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)

* `NotSet` (value: `"NotSet"`)




