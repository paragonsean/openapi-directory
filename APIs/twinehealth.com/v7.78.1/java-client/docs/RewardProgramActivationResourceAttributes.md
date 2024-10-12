

# RewardProgramActivationResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activatedAt** | **String** | Date at which the reward program was activated for the patient. (Must be between the start_at and end_at dates for the reward program) |  |
|**active** | **Boolean** | If true, the reward program is currently active. |  [optional] |
|**allocatedCount** | **BigDecimal** | Number of rewards allocated. (Read-only property) |  [optional] [readonly] |
|**budgetUnit** | **String** | Unit of the reward program budget. (Read-only property) |  [optional] [readonly] |
|**deactivatedAt** | **String** | Date at which the reward program was deactivated. (Must be after the activated_at date) |  [optional] |
|**earnedCount** | **BigDecimal** | Number of reward earnings. (Read-only property) |  [optional] [readonly] |
|**expiresAt** | **String** | Date at which the reward program activation expires. (Read-only property set by adding the days_active from the reward program to the activated_at date) |  [optional] [readonly] |
|**fulfillAsEarned** | **Boolean** | If true, the rewards created for a patient for the program can be fulfulled as they are earned. If false, the rewards should only be fulfilled when the program is deactivated. (Read-only property denormalized from the reward program) |  [optional] [readonly] |
|**totalAllocatedValue** | **BigDecimal** | Total value of reward allocated. (Read-only property) |  [optional] [readonly] |
|**totalEarnedValue** | **BigDecimal** | Total value of reward earnings. (Read-only property) |  [optional] [readonly] |



