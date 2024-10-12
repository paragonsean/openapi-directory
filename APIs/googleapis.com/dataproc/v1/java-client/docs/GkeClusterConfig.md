

# GkeClusterConfig

The cluster's GKE config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gkeClusterTarget** | **String** | Optional. A target GKE cluster to deploy to. It must be in the same project and region as the Dataproc cluster (the GKE cluster can be zonal or regional). Format: &#39;projects/{project}/locations/{location}/clusters/{cluster_id}&#39; |  [optional] |
|**namespacedGkeDeploymentTarget** | [**NamespacedGkeDeploymentTarget**](NamespacedGkeDeploymentTarget.md) |  |  [optional] |
|**nodePoolTarget** | [**List&lt;GkeNodePoolTarget&gt;**](GkeNodePoolTarget.md) | Optional. GKE node pools where workloads will be scheduled. At least one node pool must be assigned the DEFAULT GkeNodePoolTarget.Role. If a GkeNodePoolTarget is not specified, Dataproc constructs a DEFAULT GkeNodePoolTarget. Each role can be given to only one GkeNodePoolTarget. All node pools must have the same location settings. |  [optional] |



