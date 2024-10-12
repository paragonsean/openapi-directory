

# LoyaltyProgram

Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for rewards.  Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.  For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accrualRules** | [**List&lt;LoyaltyProgramAccrualRule&gt;**](LoyaltyProgramAccrualRule.md) | Defines how buyers can earn loyalty points. |  |
|**createdAt** | **String** | The timestamp when the program was created, in RFC 3339 format. |  |
|**expirationPolicy** | [**LoyaltyProgramExpirationPolicy**](LoyaltyProgramExpirationPolicy.md) |  |  [optional] |
|**id** | **String** | The Square-assigned ID of the loyalty program. Updates to  the loyalty program do not modify the identifier. |  |
|**locationIds** | **List&lt;String&gt;** | The [locations](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) at which the program is active. |  |
|**rewardTiers** | [**List&lt;LoyaltyProgramRewardTier&gt;**](LoyaltyProgramRewardTier.md) | The list of rewards for buyers, sorted by ascending points. |  |
|**status** | **String** | Whether the program is currently active. |  |
|**terminology** | [**LoyaltyProgramTerminology**](LoyaltyProgramTerminology.md) |  |  |
|**updatedAt** | **String** | The timestamp when the reward was last updated, in RFC 3339 format. |  |



