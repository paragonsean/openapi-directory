

# DestinyMilestonesDestinyMilestoneRewardEntry

The character-specific data for a milestone's reward entry. See DestinyMilestoneDefinition for more information about Reward Entries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**earned** | **Boolean** | If TRUE, the player has earned this reward. |  [optional] |
|**redeemed** | **Boolean** | If TRUE, the player has redeemed/picked up/obtained this reward. Feel free to alias this to \&quot;gotTheShinyBauble\&quot; in your own codebase. |  [optional] |
|**rewardEntryHash** | **Integer** | The identifier for the reward entry in question. It is important to look up the related DestinyMilestoneRewardEntryDefinition to get the static details about the reward, which you can do by looking up the milestone&#39;s DestinyMilestoneDefinition and examining the DestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data. |  [optional] |



