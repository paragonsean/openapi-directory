

# NodeGroupOperationMetadata

Metadata describing the node group operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterUuid** | **String** | Output only. Cluster UUID associated with the node group operation. |  [optional] [readonly] |
|**description** | **String** | Output only. Short description of operation. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Output only. Labels associated with the operation. |  [optional] [readonly] |
|**nodeGroupId** | **String** | Output only. Node group ID for the operation. |  [optional] [readonly] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |
|**status** | [**ClusterOperationStatus**](ClusterOperationStatus.md) |  |  [optional] |
|**statusHistory** | [**List&lt;ClusterOperationStatus&gt;**](ClusterOperationStatus.md) | Output only. The previous operation status. |  [optional] [readonly] |
|**warnings** | **List&lt;String&gt;** | Output only. Errors encountered during operation execution. |  [optional] [readonly] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| NODE_GROUP_OPERATION_TYPE_UNSPECIFIED | &quot;NODE_GROUP_OPERATION_TYPE_UNSPECIFIED&quot; |
| CREATE | &quot;CREATE&quot; |
| UPDATE | &quot;UPDATE&quot; |
| DELETE | &quot;DELETE&quot; |
| RESIZE | &quot;RESIZE&quot; |
| REPAIR | &quot;REPAIR&quot; |
| UPDATE_LABELS | &quot;UPDATE_LABELS&quot; |



