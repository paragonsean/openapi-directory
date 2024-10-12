# BungieNetApi.DestinyMilestonesDestinyPublicMilestone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**[DestinyMilestonesDestinyPublicMilestoneChallengeActivity]**](DestinyMilestonesDestinyPublicMilestoneChallengeActivity.md) |  | [optional] 
**availableQuests** | [**[DestinyMilestonesDestinyPublicMilestoneQuest]**](DestinyMilestonesDestinyPublicMilestoneQuest.md) | A milestone not need have even a single quest, but if there are active quests they will be returned here. | [optional] 
**endDate** | **Date** | If known, this is the date when the Milestone will expire/recycle/end. | [optional] 
**milestoneHash** | **Number** | The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone. | [optional] 
**order** | **Number** | Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information. | [optional] 
**startDate** | **Date** | If known, this is the date when the Milestone started/became active. | [optional] 
**vendorHashes** | **[Number]** | Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.  Deprecated, already, for the sake of the new \&quot;vendors\&quot; property that has more data. What was I thinking. | [optional] 
**vendors** | [**[DestinyMilestonesDestinyPublicMilestoneVendor]**](DestinyMilestonesDestinyPublicMilestoneVendor.md) | This is why we can&#39;t have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data. | [optional] 


