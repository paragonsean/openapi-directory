

# RewardResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**thread** | **String** | Unique string identifying the health action with which the reward is associated. |  [optional] |
|**allocatedAt** | **String** | Date at which the reward was allocated. (Must be after the reward program is activated and before it is deactivated or expires) |  |
|**allocatedUnit** | **String** | Unit of the reward program. (Read-only property) |  [optional] [readonly] |
|**allocatedValue** | **BigDecimal** | Value of the reward program budget allocated for the reward. (Must not exceed the remaining budget for the reward program activation) |  |
|**description** | **String** | Description of the reward. |  |
|**earnedAt** | **String** | Date at which the reward was earned. (Read-only property) |  [optional] [readonly] |
|**earnedValue** | **BigDecimal** | Value of the reward that has been earned. (Read-only property) |  [optional] [readonly] |
|**fulfilledAt** | **String** | Date at which the reward earning was fulfilled. (Read-only property) |  [optional] [readonly] |
|**fulfilledValue** | **BigDecimal** | Value of the earned reward that has been fulfilled. (Read-only property) |  [optional] [readonly] |
|**targetAt** | **String** | Date at which the patient aspires to achieve the reward. (Must be the same or after the allocated_at date) |  [optional] |



