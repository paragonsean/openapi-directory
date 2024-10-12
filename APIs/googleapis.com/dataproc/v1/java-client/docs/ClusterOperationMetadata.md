

# ClusterOperationMetadata

Metadata describing the operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childOperationIds** | **List&lt;String&gt;** | Output only. Child operation ids |  [optional] [readonly] |
|**clusterName** | **String** | Output only. Name of the cluster for the operation. |  [optional] [readonly] |
|**clusterUuid** | **String** | Output only. Cluster UUID for the operation. |  [optional] [readonly] |
|**description** | **String** | Output only. Short description of operation. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Output only. Labels associated with the operation |  [optional] [readonly] |
|**operationType** | **String** | Output only. The operation type. |  [optional] [readonly] |
|**status** | [**ClusterOperationStatus**](ClusterOperationStatus.md) |  |  [optional] |
|**statusHistory** | [**List&lt;ClusterOperationStatus&gt;**](ClusterOperationStatus.md) | Output only. The previous operation status. |  [optional] [readonly] |
|**warnings** | **List&lt;String&gt;** | Output only. Errors encountered during operation execution. |  [optional] [readonly] |



