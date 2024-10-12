

# CacheProperties

Properties of the Cache.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cacheSizeGB** | **Integer** | The size of this Cache, in GB. |  [optional] |
|**health** | [**CacheHealth**](CacheHealth.md) |  |  [optional] |
|**mountAddresses** | **List&lt;String&gt;** | Array of IP addresses that can be used by clients mounting this Cache. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | ARM provisioning state, see https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property |  [optional] |
|**subnet** | **String** | A fully qualified URL. |  [optional] |
|**upgradeStatus** | [**CacheUpgradeStatus**](CacheUpgradeStatus.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| UPDATING | &quot;Updating&quot; |



