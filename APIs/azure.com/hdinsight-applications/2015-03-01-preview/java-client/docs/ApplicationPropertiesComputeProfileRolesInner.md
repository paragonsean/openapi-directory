

# ApplicationPropertiesComputeProfileRolesInner

Describes a role on the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoscale** | [**ApplicationPropertiesComputeProfileRolesInnerAutoscale**](ApplicationPropertiesComputeProfileRolesInnerAutoscale.md) |  |  [optional] |
|**dataDisksGroups** | [**List&lt;ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner&gt;**](ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner.md) | The data disks groups for the role. |  [optional] |
|**hardwareProfile** | [**ApplicationPropertiesComputeProfileRolesInnerHardwareProfile**](ApplicationPropertiesComputeProfileRolesInnerHardwareProfile.md) |  |  [optional] |
|**minInstanceCount** | **Integer** | The minimum instance count of the cluster. |  [optional] |
|**name** | **String** | The name of the role. |  [optional] |
|**osProfile** | [**ApplicationPropertiesComputeProfileRolesInnerOsProfile**](ApplicationPropertiesComputeProfileRolesInnerOsProfile.md) |  |  [optional] |
|**scriptActions** | [**List&lt;ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner&gt;**](ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner.md) | The list of script actions on the role. |  [optional] |
|**targetInstanceCount** | **Integer** | The instance count of the cluster. |  [optional] |
|**virtualNetworkProfile** | [**ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile**](ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile.md) |  |  [optional] |



