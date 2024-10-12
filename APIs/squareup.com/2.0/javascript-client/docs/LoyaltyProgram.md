# SquareConnectApi.LoyaltyProgram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrualRules** | [**[LoyaltyProgramAccrualRule]**](LoyaltyProgramAccrualRule.md) | Defines how buyers can earn loyalty points. | 
**createdAt** | **String** | The timestamp when the program was created, in RFC 3339 format. | 
**expirationPolicy** | [**LoyaltyProgramExpirationPolicy**](LoyaltyProgramExpirationPolicy.md) |  | [optional] 
**id** | **String** | The Square-assigned ID of the loyalty program. Updates to  the loyalty program do not modify the identifier. | 
**locationIds** | **[String]** | The [locations](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) at which the program is active. | 
**rewardTiers** | [**[LoyaltyProgramRewardTier]**](LoyaltyProgramRewardTier.md) | The list of rewards for buyers, sorted by ascending points. | 
**status** | **String** | Whether the program is currently active. | 
**terminology** | [**LoyaltyProgramTerminology**](LoyaltyProgramTerminology.md) |  | 
**updatedAt** | **String** | The timestamp when the reward was last updated, in RFC 3339 format. | 


