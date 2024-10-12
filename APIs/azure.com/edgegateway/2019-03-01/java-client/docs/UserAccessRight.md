

# UserAccessRight

The mapping between a particular user and the access type on the SMB share.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessType** | [**AccessTypeEnum**](#AccessTypeEnum) | Type of access to be allowed for the user. |  |
|**userId** | **String** | User ID (already existing in the device). |  |



## Enum: AccessTypeEnum

| Name | Value |
|---- | -----|
| CHANGE | &quot;Change&quot; |
| READ | &quot;Read&quot; |
| CUSTOM | &quot;Custom&quot; |



