

# ServiceMeshMembershipState

**Service Mesh**: State for a single Membership, as analyzed by the Service Mesh Hub Controller.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisMessages** | [**List&lt;ServiceMeshAnalysisMessage&gt;**](ServiceMeshAnalysisMessage.md) | Output only. Results of running Service Mesh analyzers. |  [optional] [readonly] |
|**configApiVersion** | **String** | The API version (i.e. Istio CRD version) for configuring service mesh in this cluster. This version is influenced by the &#x60;default_channel&#x60; field. |  [optional] |
|**controlPlaneManagement** | [**ServiceMeshControlPlaneManagement**](ServiceMeshControlPlaneManagement.md) |  |  [optional] |
|**dataPlaneManagement** | [**ServiceMeshDataPlaneManagement**](ServiceMeshDataPlaneManagement.md) |  |  [optional] |



