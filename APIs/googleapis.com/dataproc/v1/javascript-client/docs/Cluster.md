# CloudDataprocApi.Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterName** | **String** | Required. The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused. | [optional] 
**clusterUuid** | **String** | Output only. A cluster UUID (Unique Universal Identifier). Dataproc generates this value when it creates the cluster. | [optional] [readonly] 
**config** | [**ClusterConfig**](ClusterConfig.md) |  | [optional] 
**labels** | **{String: String}** | Optional. The labels to associate with this cluster. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a cluster. | [optional] 
**metrics** | [**ClusterMetrics**](ClusterMetrics.md) |  | [optional] 
**projectId** | **String** | Required. The Google Cloud Platform project ID that the cluster belongs to. | [optional] 
**status** | [**ClusterStatus**](ClusterStatus.md) |  | [optional] 
**statusHistory** | [**[ClusterStatus]**](ClusterStatus.md) | Output only. The previous cluster status. | [optional] [readonly] 
**virtualClusterConfig** | [**VirtualClusterConfig**](VirtualClusterConfig.md) |  | [optional] 


