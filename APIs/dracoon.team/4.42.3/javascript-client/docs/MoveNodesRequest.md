# DracoonApi.MoveNodesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[MoveNode]**](MoveNode.md) | List of nodes to be moved | [optional] 
**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. | [optional] [default to false]
**nodeIds** | **[Number]** | &amp;#128679; Deprecated since v4.5.0  Node IDs  Please use &#x60;items&#x60; instead. | [optional] 
**resolutionStrategy** | **String** | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; | [optional] [default to &#39;autorename&#39;]



## Enum: ResolutionStrategyEnum


* `autorename` (value: `"autorename"`)

* `overwrite` (value: `"overwrite"`)

* `fail` (value: `"fail"`)




