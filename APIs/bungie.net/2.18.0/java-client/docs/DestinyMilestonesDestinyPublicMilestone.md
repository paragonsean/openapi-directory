

# DestinyMilestonesDestinyPublicMilestone

Information about milestones, presented in a character state-agnostic manner. Combine this data with DestinyMilestoneDefinition to get a full picture of the milestone, which is basically a checklist of things to do in the game. Think of this as GetPublicAdvisors 3.0, for those who used the Destiny 1 API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activities** | [**List&lt;DestinyMilestonesDestinyPublicMilestoneChallengeActivity&gt;**](DestinyMilestonesDestinyPublicMilestoneChallengeActivity.md) |  |  [optional] |
|**availableQuests** | [**List&lt;DestinyMilestonesDestinyPublicMilestoneQuest&gt;**](DestinyMilestonesDestinyPublicMilestoneQuest.md) | A milestone not need have even a single quest, but if there are active quests they will be returned here. |  [optional] |
|**endDate** | **OffsetDateTime** | If known, this is the date when the Milestone will expire/recycle/end. |  [optional] |
|**milestoneHash** | **Integer** | The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone. |  [optional] |
|**order** | **Integer** | Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information. |  [optional] |
|**startDate** | **OffsetDateTime** | If known, this is the date when the Milestone started/became active. |  [optional] |
|**vendorHashes** | **List&lt;Integer&gt;** | Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant.  Deprecated, already, for the sake of the new \&quot;vendors\&quot; property that has more data. What was I thinking. |  [optional] |
|**vendors** | [**List&lt;DestinyMilestonesDestinyPublicMilestoneVendor&gt;**](DestinyMilestonesDestinyPublicMilestoneVendor.md) | This is why we can&#39;t have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data. |  [optional] |



