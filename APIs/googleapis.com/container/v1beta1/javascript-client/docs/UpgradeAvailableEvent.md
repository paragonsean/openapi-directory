# KubernetesEngineApi.UpgradeAvailableEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**releaseChannel** | [**ReleaseChannel**](ReleaseChannel.md) |  | [optional] 
**resource** | **String** | Optional relative path to the resource. For example, the relative path of the node pool. | [optional] 
**resourceType** | **String** | The resource type of the release version. | [optional] 
**version** | **String** | The release version available for upgrade. | [optional] 
**windowsVersions** | [**WindowsVersions**](WindowsVersions.md) |  | [optional] 



## Enum: ResourceTypeEnum


* `UPGRADE_RESOURCE_TYPE_UNSPECIFIED` (value: `"UPGRADE_RESOURCE_TYPE_UNSPECIFIED"`)

* `MASTER` (value: `"MASTER"`)

* `NODE_POOL` (value: `"NODE_POOL"`)




