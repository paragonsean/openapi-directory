

# Role

Describes a role on the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoscale** | [**Autoscale**](Autoscale.md) |  |  [optional] |
|**dataDisksGroups** | [**List&lt;DataDisksGroups&gt;**](DataDisksGroups.md) | The data disks groups for the role. |  [optional] |
|**hardwareProfile** | [**HardwareProfile**](HardwareProfile.md) |  |  [optional] |
|**minInstanceCount** | **Integer** | The minimum instance count of the cluster. |  [optional] |
|**name** | **String** | The name of the role. |  [optional] |
|**osProfile** | [**OsProfile**](OsProfile.md) |  |  [optional] |
|**scriptActions** | [**List&lt;RoleScriptActionsInner&gt;**](RoleScriptActionsInner.md) | The list of script actions on the role. |  [optional] |
|**targetInstanceCount** | **Integer** | The instance count of the cluster. |  [optional] |
|**virtualNetworkProfile** | [**VirtualNetworkProfile**](VirtualNetworkProfile.md) |  |  [optional] |



