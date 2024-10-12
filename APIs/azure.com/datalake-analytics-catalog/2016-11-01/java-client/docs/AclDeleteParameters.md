

# AclDeleteParameters

The parameters used to delete an access control list (ACL) entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aceType** | [**AceTypeEnum**](#AceTypeEnum) | the access control list (ACL) entry type. UserObj and GroupObj denote the owning user and group, respectively. |  |
|**principalId** | **UUID** | the Azure AD object ID of the user or group being specified in the access control list (ACL) entry. |  |



## Enum: AceTypeEnum

| Name | Value |
|---- | -----|
| USER_OBJ | &quot;UserObj&quot; |
| GROUP_OBJ | &quot;GroupObj&quot; |
| OTHER | &quot;Other&quot; |
| USER | &quot;User&quot; |
| GROUP | &quot;Group&quot; |



