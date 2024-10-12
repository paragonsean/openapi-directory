

# KubernetesMetadata

KubernetesMetadata provides informational metadata for Memberships representing Kubernetes clusters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kubernetesApiServerVersion** | **String** | Output only. Kubernetes API server version string as reported by &#x60;/version&#x60;. |  [optional] [readonly] |
|**memoryMb** | **Integer** | Output only. The total memory capacity as reported by the sum of all Kubernetes nodes resources, defined in MB. |  [optional] [readonly] |
|**nodeCount** | **Integer** | Output only. Node count as reported by Kubernetes nodes resources. |  [optional] [readonly] |
|**nodeProviderId** | **String** | Output only. Node providerID as reported by the first node in the list of nodes on the Kubernetes endpoint. On Kubernetes platforms that support zero-node clusters (like GKE-on-GCP), the node_count will be zero and the node_provider_id will be empty. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time at which these details were last updated. This update_time is different from the Membership-level update_time since EndpointDetails are updated internally for API consumers. |  [optional] [readonly] |
|**vcpuCount** | **Integer** | Output only. vCPU count as reported by Kubernetes nodes resources. |  [optional] [readonly] |



