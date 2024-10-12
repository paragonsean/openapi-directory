

# UpgradeEvent

UpgradeEvent is a notification sent to customers by the cluster server when a resource is upgrading.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentVersion** | **String** | The current version before the upgrade. |  [optional] |
|**operation** | **String** | The operation associated with this upgrade. |  [optional] |
|**operationStartTime** | **String** | The time when the operation was started. |  [optional] |
|**resource** | **String** | Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The resource type that is upgrading. |  [optional] |
|**targetVersion** | **String** | The target version for the upgrade. |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| UPGRADE_RESOURCE_TYPE_UNSPECIFIED | &quot;UPGRADE_RESOURCE_TYPE_UNSPECIFIED&quot; |
| MASTER | &quot;MASTER&quot; |
| NODE_POOL | &quot;NODE_POOL&quot; |



