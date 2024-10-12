

# MembershipEndpoint

MembershipEndpoint contains information needed to contact a Kubernetes API, endpoint and any additional Kubernetes metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applianceCluster** | [**ApplianceCluster**](ApplianceCluster.md) |  |  [optional] |
|**edgeCluster** | [**EdgeCluster**](EdgeCluster.md) |  |  [optional] |
|**gkeCluster** | [**GkeCluster**](GkeCluster.md) |  |  [optional] |
|**googleManaged** | **Boolean** | Output only. Whether the lifecycle of this membership is managed by a google cluster platform service. |  [optional] [readonly] |
|**kubernetesMetadata** | [**KubernetesMetadata**](KubernetesMetadata.md) |  |  [optional] |
|**kubernetesResource** | [**KubernetesResource**](KubernetesResource.md) |  |  [optional] |
|**multiCloudCluster** | [**MultiCloudCluster**](MultiCloudCluster.md) |  |  [optional] |
|**onPremCluster** | [**OnPremCluster**](OnPremCluster.md) |  |  [optional] |



