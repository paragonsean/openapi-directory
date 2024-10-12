

# ClientAccessRight

The mapping between a particular client IP and the type of access client has on the NFS share.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPermission** | [**AccessPermissionEnum**](#AccessPermissionEnum) | Type of access to be allowed for the client. |  |
|**client** | **String** | IP of the client. |  |



## Enum: AccessPermissionEnum

| Name | Value |
|---- | -----|
| NO_ACCESS | &quot;NoAccess&quot; |
| READ_ONLY | &quot;ReadOnly&quot; |
| READ_WRITE | &quot;ReadWrite&quot; |



