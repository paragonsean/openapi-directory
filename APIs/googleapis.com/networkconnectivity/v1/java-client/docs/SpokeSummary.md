

# SpokeSummary

Summarizes information about the spokes associated with a hub. The summary includes a count of spokes according to type and according to state. If any spokes are inactive, the summary also lists the reasons they are inactive, including a count for each reason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spokeStateCounts** | [**List&lt;SpokeStateCount&gt;**](SpokeStateCount.md) | Output only. Counts the number of spokes that are in each state and associated with a given hub. |  [optional] [readonly] |
|**spokeStateReasonCounts** | [**List&lt;SpokeStateReasonCount&gt;**](SpokeStateReasonCount.md) | Output only. Counts the number of spokes that are inactive for each possible reason and associated with a given hub. |  [optional] [readonly] |
|**spokeTypeCounts** | [**List&lt;SpokeTypeCount&gt;**](SpokeTypeCount.md) | Output only. Counts the number of spokes of each type that are associated with a specific hub. |  [optional] [readonly] |



