

# LoyaltyEventCreateReward

Provides metadata when the event `type` is `CREATE_REWARD`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loyaltyProgramId** | **String** | The ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram). |  |
|**points** | **Integer** | The loyalty points used to create the reward. |  |
|**rewardId** | **String** | The Square-assigned ID of the created [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward). This field is returned only if the event source is &#x60;LOYALTY_API&#x60;. |  [optional] |



