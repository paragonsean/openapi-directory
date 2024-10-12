

# MountPointMap

The share mount point.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mountPoint** | **String** | Mount point for the share. |  [optional] [readonly] |
|**roleId** | **String** | ID of the role to which share is mounted. |  [optional] [readonly] |
|**roleType** | [**RoleTypeEnum**](#RoleTypeEnum) | Role type. |  [optional] [readonly] |
|**shareId** | **String** | ID of the share mounted to the role VM. |  |



## Enum: RoleTypeEnum

| Name | Value |
|---- | -----|
| IOT | &quot;IOT&quot; |
| ASA | &quot;ASA&quot; |
| FUNCTIONS | &quot;Functions&quot; |
| COGNITIVE | &quot;Cognitive&quot; |



