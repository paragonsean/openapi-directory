# DriveActivityApi.ConsolidationStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy** | **Object** | A strategy that consolidates activities using the grouping rules from the legacy V1 Activity API. Similar actions occurring within a window of time can be grouped across multiple targets (such as moving a set of files at once) or multiple actors (such as several users editing the same item). Grouping rules for this strategy are specific to each type of action. | [optional] 
**none** | **Object** | A strategy that does no consolidation of individual activities. | [optional] 


