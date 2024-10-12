# AzureMachineLearningComputeManagementClient.OperationalizationClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appInsights** | [**AppInsightsCredentials**](AppInsightsCredentials.md) |  | [optional] 
**clusterType** | **String** | The cluster type. | 
**containerRegistry** | [**ContainerRegistryProperties**](ContainerRegistryProperties.md) |  | [optional] 
**containerService** | [**AcsClusterProperties**](AcsClusterProperties.md) |  | 
**createdOn** | **Date** | The date and time when the cluster was created. | [optional] [readonly] 
**description** | **String** | The description of the cluster. | [optional] 
**globalServiceConfiguration** | [**GlobalServiceConfiguration**](GlobalServiceConfiguration.md) |  | [optional] 
**modifiedOn** | **Date** | The date and time when the cluster was last modified. | [optional] [readonly] 
**provisioningState** | **String** | The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. | [optional] [readonly] 
**storageAccount** | [**StorageAccountProperties**](StorageAccountProperties.md) |  | [optional] 



## Enum: ClusterTypeEnum


* `ACS` (value: `"ACS"`)





## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




