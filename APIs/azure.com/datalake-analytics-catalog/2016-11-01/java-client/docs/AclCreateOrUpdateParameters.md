

# AclCreateOrUpdateParameters

The parameters used to create or update an access control list (ACL) entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aceType** | [**AceTypeEnum**](#AceTypeEnum) | the access control list (ACL) entry type. UserObj and GroupObj denote the owning user and group, respectively. |  |
|**permission** | [**PermissionEnum**](#PermissionEnum) | the permission type of the access control list (ACL) entry. |  |
|**principalId** | **UUID** | the Azure AD object ID of the user or group being specified in the access control list (ACL) entry. |  |



## Enum: AceTypeEnum

| Name | Value |
|---- | -----|
| USER_OBJ | &quot;UserObj&quot; |
| GROUP_OBJ | &quot;GroupObj&quot; |
| OTHER | &quot;Other&quot; |
| USER | &quot;User&quot; |
| GROUP | &quot;Group&quot; |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| USE | &quot;Use&quot; |
| CREATE | &quot;Create&quot; |
| DROP | &quot;Drop&quot; |
| ALTER | &quot;Alter&quot; |
| WRITE | &quot;Write&quot; |
| ALL | &quot;All&quot; |



