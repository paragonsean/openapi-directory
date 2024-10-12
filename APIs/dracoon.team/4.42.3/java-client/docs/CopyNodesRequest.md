

# CopyNodesRequest

Request model for copying nodes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;CopyNode&gt;**](CopyNode.md) | List of nodes to be copied |  [optional] |
|**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. |  [optional] |
|**nodeIds** | **List&lt;Long&gt;** | &amp;#128679; Deprecated since v4.5.0  Node IDs  Please use &#x60;items&#x60; instead. |  [optional] |
|**resolutionStrategy** | [**ResolutionStrategyEnum**](#ResolutionStrategyEnum) | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; |  [optional] |



## Enum: ResolutionStrategyEnum

| Name | Value |
|---- | -----|
| AUTORENAME | &quot;autorename&quot; |
| OVERWRITE | &quot;overwrite&quot; |
| FAIL | &quot;fail&quot; |



