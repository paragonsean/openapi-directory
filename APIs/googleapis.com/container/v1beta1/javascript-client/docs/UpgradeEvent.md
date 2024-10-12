# KubernetesEngineApi.UpgradeEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentVersion** | **String** | The current version before the upgrade. | [optional] 
**operation** | **String** | The operation associated with this upgrade. | [optional] 
**operationStartTime** | **String** | The time when the operation was started. | [optional] 
**resource** | **String** | Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool. | [optional] 
**resourceType** | **String** | The resource type that is upgrading. | [optional] 
**targetVersion** | **String** | The target version for the upgrade. | [optional] 



## Enum: ResourceTypeEnum


* `UPGRADE_RESOURCE_TYPE_UNSPECIFIED` (value: `"UPGRADE_RESOURCE_TYPE_UNSPECIFIED"`)

* `MASTER` (value: `"MASTER"`)

* `NODE_POOL` (value: `"NODE_POOL"`)




