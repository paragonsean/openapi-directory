

# ContinueWatchingListData

List data for ContinueWatching List

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemInclusions** | [**Map&lt;String, ContinueWatchingListDataExpansion&gt;**](ContinueWatchingListDataExpansion.md) | Object where keys are itemIds for the items in the list and values are objects containing additional items (either episode/season/show) that were requested in the \&quot;include\&quot; query option.  For example if you request the ContinueWatching list with \&quot;season\&quot; items in the list, you can specify &#x60;include&#x3D;episode&#x60; and then the specific next episode will be returned in this object.  |  [optional] |



