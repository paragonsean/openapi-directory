

# RewardEarningResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**earnedAt** | **String** | Date at which the reward was earned. (Must be after the reward was allocated and before the reward program activation was deactivated or expired) |  |
|**earnedUnit** | **String** | Unit of the reward that has been earned. (Read-only property) |  [optional] [readonly] |
|**earnedValue** | **BigDecimal** | Value of the reward that has been earned. (Must not exceed the allocated value for the reward) |  |
|**fulfilledAt** | **String** | Date at which the reward earning was fulfilled. (Read-only property) |  [optional] [readonly] |
|**fulfilledValue** | **BigDecimal** | Value of the earned reward that has been fulfilled. (Read-only property) |  [optional] [readonly] |
|**readyForFulfillment** | **Boolean** | If true, the reward earning is ready to be fulfilled, either because the reward program activation was fulfill_as_earned or because the reward program activation has been deactivated. (Read-only property) |  [optional] [readonly] |



