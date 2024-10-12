# ConsumptionManagementClient.ManagementGroupAggregatedCostProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureCharges** | **Number** | Azure Charges. | [optional] [readonly] 
**billingPeriodId** | **String** | The id of the billing period resource that the aggregated cost belongs to. | [optional] [readonly] 
**chargesBilledSeparately** | **Number** | Charges Billed Separately. | [optional] [readonly] 
**children** | [**[ManagementGroupAggregatedCostResult]**](ManagementGroupAggregatedCostResult.md) | Children of a management group | [optional] 
**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. | [optional] [readonly] 
**excludedSubscriptions** | **[String]** | List of subscription Guids excluded from the calculation of aggregated cost | [optional] 
**includedSubscriptions** | **[String]** | List of subscription Guids included in the calculation of aggregated cost | [optional] 
**marketplaceCharges** | **Number** | Marketplace Charges. | [optional] [readonly] 
**usageEnd** | **Date** | The end of the date time range covered by the aggregated cost. | [optional] [readonly] 
**usageStart** | **Date** | The start of the date time range covered by aggregated cost. | [optional] [readonly] 


