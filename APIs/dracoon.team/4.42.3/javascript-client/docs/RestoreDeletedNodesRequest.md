# DracoonApi.RestoreDeletedNodesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedNodeIds** | **[Number]** | List of deleted node IDs | 
**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. | [optional] [default to false]
**parentId** | **Number** | Node parent ID  (default: previous parent ID) | [optional] 
**resolutionStrategy** | **String** | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; | [optional] [default to &#39;autorename&#39;]



## Enum: ResolutionStrategyEnum


* `autorename` (value: `"autorename"`)

* `overwrite` (value: `"overwrite"`)

* `fail` (value: `"fail"`)




