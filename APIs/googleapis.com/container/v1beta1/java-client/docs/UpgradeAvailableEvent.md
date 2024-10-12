

# UpgradeAvailableEvent

UpgradeAvailableEvent is a notification sent to customers when a new available version is released.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**releaseChannel** | [**ReleaseChannel**](ReleaseChannel.md) |  |  [optional] |
|**resource** | **String** | Optional relative path to the resource. For example, the relative path of the node pool. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The resource type of the release version. |  [optional] |
|**version** | **String** | The release version available for upgrade. |  [optional] |
|**windowsVersions** | [**WindowsVersions**](WindowsVersions.md) |  |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| UPGRADE_RESOURCE_TYPE_UNSPECIFIED | &quot;UPGRADE_RESOURCE_TYPE_UNSPECIFIED&quot; |
| MASTER | &quot;MASTER&quot; |
| NODE_POOL | &quot;NODE_POOL&quot; |



