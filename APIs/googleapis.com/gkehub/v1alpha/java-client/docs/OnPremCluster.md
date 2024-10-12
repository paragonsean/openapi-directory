

# OnPremCluster

OnPremCluster contains information specific to GKE On-Prem clusters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminCluster** | **Boolean** | Immutable. Whether the cluster is an admin cluster. |  [optional] |
|**clusterMissing** | **Boolean** | Output only. If cluster_missing is set then it denotes that API(gkeonprem.googleapis.com) resource for this GKE On-Prem cluster no longer exists. |  [optional] [readonly] |
|**clusterType** | [**ClusterTypeEnum**](#ClusterTypeEnum) | Immutable. The on prem cluster&#39;s type. |  [optional] |
|**resourceLink** | **String** | Immutable. Self-link of the Google Cloud resource for the GKE On-Prem cluster. For example: //gkeonprem.googleapis.com/projects/my-project/locations/us-west1-a/vmwareClusters/my-cluster //gkeonprem.googleapis.com/projects/my-project/locations/us-west1-a/bareMetalClusters/my-cluster |  [optional] |



## Enum: ClusterTypeEnum

| Name | Value |
|---- | -----|
| CLUSTERTYPE_UNSPECIFIED | &quot;CLUSTERTYPE_UNSPECIFIED&quot; |
| BOOTSTRAP | &quot;BOOTSTRAP&quot; |
| HYBRID | &quot;HYBRID&quot; |
| STANDALONE | &quot;STANDALONE&quot; |
| USER | &quot;USER&quot; |



