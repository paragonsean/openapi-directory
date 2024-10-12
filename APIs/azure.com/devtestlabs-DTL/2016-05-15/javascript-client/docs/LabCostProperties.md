# DevTestLabsClient.LabCostProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **Date** | The creation date of the cost. | [optional] 
**currencyCode** | **String** | The currency code of the cost. | [optional] 
**endDateTime** | **Date** | The end time of the cost data. | [optional] 
**labCostDetails** | [**[LabCostDetailsProperties]**](LabCostDetailsProperties.md) | The lab cost details component of the cost data. | [optional] [readonly] 
**labCostSummary** | [**LabCostSummaryProperties**](LabCostSummaryProperties.md) |  | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**resourceCosts** | [**[LabResourceCostProperties]**](LabResourceCostProperties.md) | The resource cost component of the cost data. | [optional] [readonly] 
**startDateTime** | **Date** | The start time of the cost data. | [optional] 
**targetCost** | [**TargetCostProperties**](TargetCostProperties.md) |  | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 


