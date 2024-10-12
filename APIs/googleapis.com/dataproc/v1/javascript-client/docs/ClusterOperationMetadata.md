# CloudDataprocApi.ClusterOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childOperationIds** | **[String]** | Output only. Child operation ids | [optional] [readonly] 
**clusterName** | **String** | Output only. Name of the cluster for the operation. | [optional] [readonly] 
**clusterUuid** | **String** | Output only. Cluster UUID for the operation. | [optional] [readonly] 
**description** | **String** | Output only. Short description of operation. | [optional] [readonly] 
**labels** | **{String: String}** | Output only. Labels associated with the operation | [optional] [readonly] 
**operationType** | **String** | Output only. The operation type. | [optional] [readonly] 
**status** | [**ClusterOperationStatus**](ClusterOperationStatus.md) |  | [optional] 
**statusHistory** | [**[ClusterOperationStatus]**](ClusterOperationStatus.md) | Output only. The previous operation status. | [optional] [readonly] 
**warnings** | **[String]** | Output only. Errors encountered during operation execution. | [optional] [readonly] 


