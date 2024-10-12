

# RestoreDeletedNodesRequest

Request model for restoring deleted nodes

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedNodeIds** | **List&lt;Long&gt;** | List of deleted node IDs |  |
|**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. |  [optional] |
|**parentId** | **Long** | Node parent ID  (default: previous parent ID) |  [optional] |
|**resolutionStrategy** | [**ResolutionStrategyEnum**](#ResolutionStrategyEnum) | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; |  [optional] |



## Enum: ResolutionStrategyEnum

| Name | Value |
|---- | -----|
| AUTORENAME | &quot;autorename&quot; |
| OVERWRITE | &quot;overwrite&quot; |
| FAIL | &quot;fail&quot; |



