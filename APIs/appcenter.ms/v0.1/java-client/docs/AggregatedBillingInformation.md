

# AggregatedBillingInformation

Aggregated Billing Information for a user or an organization

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureSubscriptionId** | **String** | Unique identifier for the Azure subscription used for billing |  [optional] |
|**azureSubscriptionState** | [**AzureSubscriptionStateEnum**](#AzureSubscriptionStateEnum) | State of the Azure subscription used for billing |  [optional] |
|**billingPlans** | [**BillingAggregatedInformationGetByApp200ResponseBillingPlans**](BillingAggregatedInformationGetByApp200ResponseBillingPlans.md) |  |  [optional] |
|**id** | **String** | ID of the user or organization |  [optional] |
|**timestamp** | **String** | The ISO 8601 datetime of last modification |  [optional] |
|**usage** | [**BillingAggregatedInformationGetByApp200ResponseUsage**](BillingAggregatedInformationGetByApp200ResponseUsage.md) |  |  [optional] |
|**version** | **String** | Version of the Billing Information schema |  [optional] |



## Enum: AzureSubscriptionStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |
| NOT_SET | &quot;NotSet&quot; |



