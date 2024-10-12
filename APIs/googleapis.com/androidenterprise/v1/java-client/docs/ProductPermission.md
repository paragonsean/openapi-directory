

# ProductPermission

A product permissions resource represents the set of permissions required by a specific app and whether or not they have been accepted by an enterprise admin. The API can be used to read the set of permissions, and also to update the set to indicate that permissions have been accepted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permissionId** | **String** | An opaque string uniquely identifying the permission. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Whether the permission has been accepted or not. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;required&quot; |
| ACCEPTED | &quot;accepted&quot; |



