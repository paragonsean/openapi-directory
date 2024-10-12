

# OperationalizationClusterProperties

Properties of an operationalization cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appInsights** | [**AppInsightsProperties**](AppInsightsProperties.md) |  |  [optional] |
|**clusterType** | [**ClusterTypeEnum**](#ClusterTypeEnum) | The cluster type. |  |
|**containerRegistry** | [**ContainerRegistryProperties**](ContainerRegistryProperties.md) |  |  [optional] |
|**containerService** | [**AcsClusterProperties**](AcsClusterProperties.md) |  |  [optional] |
|**createdOn** | **OffsetDateTime** | The date and time when the cluster was created. |  [optional] [readonly] |
|**description** | **String** | The description of the cluster. |  [optional] |
|**globalServiceConfiguration** | **GlobalServiceConfiguration** |  |  [optional] |
|**modifiedOn** | **OffsetDateTime** | The date and time when the cluster was last modified. |  [optional] [readonly] |
|**provisioningErrors** | [**List&lt;ErrorResponseWrapper&gt;**](ErrorResponseWrapper.md) | List of provisioning errors reported by the resource provider. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. |  [optional] [readonly] |
|**storageAccount** | [**StorageAccountProperties**](StorageAccountProperties.md) |  |  [optional] |



## Enum: ClusterTypeEnum

| Name | Value |
|---- | -----|
| ACS | &quot;ACS&quot; |
| LOCAL | &quot;Local&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UPDATING | &quot;Updating&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



