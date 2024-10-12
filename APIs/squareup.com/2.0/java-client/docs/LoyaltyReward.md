

# LoyaltyReward

Represents a contract to redeem loyalty points for a [reward tier](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgramRewardTier) discount. Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state. For more information, see [Redeem loyalty rewards](https://developer.squareup.com/docs/loyalty-api/overview#redeem-loyalty-rewards).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | The timestamp when the reward was created, in RFC 3339 format. |  [optional] |
|**id** | **String** | The Square-assigned ID of the loyalty reward. |  [optional] |
|**loyaltyAccountId** | **String** | The Square-assigned ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to which the reward belongs. |  |
|**orderId** | **String** | The Square-assigned ID of the [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) to which the reward is attached. |  [optional] |
|**points** | **Integer** | The number of loyalty points used for the reward. |  [optional] |
|**redeemedAt** | **String** | The timestamp when the reward was redeemed, in RFC 3339 format. |  [optional] |
|**rewardTierId** | **String** | The Square-assigned ID of the [reward tier](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgramRewardTier) used to create the reward. |  |
|**status** | **String** | The status of a loyalty reward. |  [optional] |
|**updatedAt** | **String** | The timestamp when the reward was last updated, in RFC 3339 format. |  [optional] |



