

# HierarchiesSortParameter

Definition of sorting of hierarchy nodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**by** | [**ByEnum**](#ByEnum) | Value to use for hierarchy node sorting. When it is set to &#39;CumulativeInstanceCount&#39;, the returned hierarchies are sorted based on the total instances belonging to the hierarchy node and its child hierarchy nodes. When it is set to &#39;Name&#39;, the returned hierarchies are sorted based on the hierarchy name. Optional, default is &#39;CumulativeInstanceCount&#39;. |  [optional] |



## Enum: ByEnum

| Name | Value |
|---- | -----|
| CUMULATIVE_INSTANCE_COUNT | &quot;CumulativeInstanceCount&quot; |
| NAME | &quot;Name&quot; |



