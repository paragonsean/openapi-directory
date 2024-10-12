

# LoyaltyEventRedeemReward

Provides metadata when the event `type` is `REDEEM_REWARD`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loyaltyProgramId** | **String** | The ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram). |  |
|**orderId** | **String** | The ID of the [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that redeemed the reward. This field is returned only if the Orders API is used to process orders. |  [optional] |
|**rewardId** | **String** | The ID of the redeemed [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward). This field is returned only if the event source is &#x60;LOYALTY_API&#x60;. |  [optional] |



