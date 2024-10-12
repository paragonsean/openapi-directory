

# LabCostProperties

Properties of a cost item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **OffsetDateTime** | The creation date of the cost. |  [optional] |
|**currencyCode** | **String** | The currency code of the cost. |  [optional] |
|**endDateTime** | **OffsetDateTime** | The end time of the cost data. |  [optional] |
|**labCostDetails** | [**List&lt;LabCostDetailsProperties&gt;**](LabCostDetailsProperties.md) | The lab cost details component of the cost data. |  [optional] [readonly] |
|**labCostSummary** | [**LabCostSummaryProperties**](LabCostSummaryProperties.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**resourceCosts** | [**List&lt;LabResourceCostProperties&gt;**](LabResourceCostProperties.md) | The resource cost component of the cost data. |  [optional] [readonly] |
|**startDateTime** | **OffsetDateTime** | The start time of the cost data. |  [optional] |
|**targetCost** | [**TargetCostProperties**](TargetCostProperties.md) |  |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] |



