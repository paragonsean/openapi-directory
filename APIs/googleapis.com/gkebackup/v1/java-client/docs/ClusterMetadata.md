

# ClusterMetadata

Information about the GKE cluster from which this Backup was created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**anthosVersion** | **String** | Output only. Anthos version |  [optional] [readonly] |
|**backupCrdVersions** | **Map&lt;String, String&gt;** | Output only. A list of the Backup for GKE CRD versions found in the cluster. |  [optional] [readonly] |
|**cluster** | **String** | Output only. The source cluster from which this Backup was created. Valid formats: - &#x60;projects/_*_/locations/_*_/clusters/_*&#x60; - &#x60;projects/_*_/zones/_*_/clusters/_*&#x60; This is inherited from the parent BackupPlan&#39;s cluster field. |  [optional] [readonly] |
|**gkeVersion** | **String** | Output only. GKE version |  [optional] [readonly] |
|**k8sVersion** | **String** | Output only. The Kubernetes server version of the source cluster. |  [optional] [readonly] |



