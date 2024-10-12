

# LabPropertiesFragment

Properties of a Lab.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxUsersInLab** | **Integer** | Maximum number of users allowed in the lab. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] |
|**usageQuota** | **String** | Maximum duration a user can use an environment for in the lab. |  [optional] |
|**userAccessMode** | [**UserAccessModeEnum**](#UserAccessModeEnum) | Lab user access mode (open to all vs. restricted to those listed on the lab). |  [optional] |



## Enum: UserAccessModeEnum

| Name | Value |
|---- | -----|
| RESTRICTED | &quot;Restricted&quot; |
| OPEN | &quot;Open&quot; |



