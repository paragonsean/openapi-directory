

# PlanQuantity

Represents the quantity a commitment plan provides of a metered resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowance** | **Double** | The quantity added to the commitment plan at an interval specified by its allowance frequency. |  [optional] [readonly] |
|**amount** | **Double** | The quantity available to the plan the last time usage was calculated. |  [optional] [readonly] |
|**includedQuantityMeter** | **String** | The Azure meter for usage against included quantities. |  [optional] [readonly] |
|**overageMeter** | **String** | The Azure meter for usage which exceeds included quantities. |  [optional] [readonly] |



