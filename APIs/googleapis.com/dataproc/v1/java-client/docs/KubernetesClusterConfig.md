

# KubernetesClusterConfig

The configuration for running the Dataproc cluster on Kubernetes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gkeClusterConfig** | [**GkeClusterConfig**](GkeClusterConfig.md) |  |  [optional] |
|**kubernetesNamespace** | **String** | Optional. A namespace within the Kubernetes cluster to deploy into. If this namespace does not exist, it is created. If it exists, Dataproc verifies that another Dataproc VirtualCluster is not installed into it. If not specified, the name of the Dataproc Cluster is used. |  [optional] |
|**kubernetesSoftwareConfig** | [**KubernetesSoftwareConfig**](KubernetesSoftwareConfig.md) |  |  [optional] |



