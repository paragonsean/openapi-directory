# CloudDataprocApi.NodeGroupOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterUuid** | **String** | Output only. Cluster UUID associated with the node group operation. | [optional] [readonly] 
**description** | **String** | Output only. Short description of operation. | [optional] [readonly] 
**labels** | **{String: String}** | Output only. Labels associated with the operation. | [optional] [readonly] 
**nodeGroupId** | **String** | Output only. Node group ID for the operation. | [optional] [readonly] 
**operationType** | **String** | The operation type. | [optional] 
**status** | [**ClusterOperationStatus**](ClusterOperationStatus.md) |  | [optional] 
**statusHistory** | [**[ClusterOperationStatus]**](ClusterOperationStatus.md) | Output only. The previous operation status. | [optional] [readonly] 
**warnings** | **[String]** | Output only. Errors encountered during operation execution. | [optional] [readonly] 



## Enum: OperationTypeEnum


* `NODE_GROUP_OPERATION_TYPE_UNSPECIFIED` (value: `"NODE_GROUP_OPERATION_TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `UPDATE` (value: `"UPDATE"`)

* `DELETE` (value: `"DELETE"`)

* `RESIZE` (value: `"RESIZE"`)

* `REPAIR` (value: `"REPAIR"`)

* `UPDATE_LABELS` (value: `"UPDATE_LABELS"`)




