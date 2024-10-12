

# LoyaltyEventDeleteReward

Provides metadata when the event `type` is `DELETE_REWARD`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loyaltyProgramId** | **String** | The ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram). |  |
|**points** | **Integer** | The number of points returned to the loyalty account. |  |
|**rewardId** | **String** | The ID of the deleted [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward). This field is returned only if the event source is &#x60;LOYALTY_API&#x60;. |  [optional] |



