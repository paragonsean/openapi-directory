# AzureResourceGraph.ResourceChangeList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skipToken** | **Object** | Skip token that encodes the skip information while executing the current request | [optional] 
**changes** | [**[ResourceChangeData]**](ResourceChangeData.md) | The pageable value returned by the operation, i.e. a list of changes to the resource.  - The list is ordered from the most recent changes to the least recent changes. - This list will be empty if there were no changes during the requested interval. - The &#x60;Before&#x60; snapshot timestamp value of the oldest change can be outside of the specified time interval. | [optional] 


