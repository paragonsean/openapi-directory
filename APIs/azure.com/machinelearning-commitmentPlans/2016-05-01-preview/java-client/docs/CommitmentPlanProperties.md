

# CommitmentPlanProperties

Properties of an Azure ML commitment plan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chargeForOverage** | **Boolean** | Indicates whether usage beyond the commitment plan&#39;s included quantities will be charged. |  [optional] [readonly] |
|**chargeForPlan** | **Boolean** | Indicates whether the commitment plan will incur a charge. |  [optional] [readonly] |
|**creationDate** | **OffsetDateTime** | The date at which this commitment plan was created, in ISO 8601 format. |  [optional] [readonly] |
|**includedQuantities** | [**Map&lt;String, PlanQuantity&gt;**](PlanQuantity.md) | The included resource quantities this plan gives you. |  [optional] [readonly] |
|**maxAssociationLimit** | **Integer** | The maximum number of commitment associations that can be children of this commitment plan. |  [optional] [readonly] |
|**maxCapacityLimit** | **Integer** | The maximum scale-out capacity for this commitment plan. |  [optional] [readonly] |
|**minCapacityLimit** | **Integer** | The minimum scale-out capacity for this commitment plan. |  [optional] [readonly] |
|**planMeter** | **String** | The Azure meter which will be used to charge for this commitment plan. |  [optional] [readonly] |
|**refillFrequencyInDays** | **Integer** | The frequency at which this commitment plan&#39;s included quantities are refilled. |  [optional] [readonly] |
|**suspendPlanOnOverage** | **Boolean** | Indicates whether this commitment plan will be moved into a suspended state if usage goes beyond the commitment plan&#39;s included quantities. |  [optional] [readonly] |



