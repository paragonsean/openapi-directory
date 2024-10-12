

# ChannelGrouping

A channel grouping defines a set of rules that can be used to categorize events in a path report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fallbackName** | **String** | The name to apply to an event that does not match any of the rules in the channel grouping. |  [optional] |
|**name** | **String** | Channel Grouping name. |  [optional] |
|**rules** | [**List&lt;Rule&gt;**](Rule.md) | Rules within Channel Grouping. There is a limit of 100 rules that can be set per channel grouping. |  [optional] |



