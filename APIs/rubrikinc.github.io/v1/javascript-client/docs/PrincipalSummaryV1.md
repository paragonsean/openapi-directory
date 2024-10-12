# RubrikRestApi.PrincipalSummaryV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authDomainId** | **String** | ID of the authentication domain for a specified principal. | 
**authDomainType** | [**AuthDomainType**](AuthDomainType.md) |  | 
**description** | **String** | Short description for a principal of type group. For all other types the value is null.  | [optional] 
**emailAddress** | **String** | Email address associated with a principal. | [optional] 
**firstName** | **String** | First name of a principal of type user. For all other types the value is null.  | [optional] 
**id** | **String** | ID of a principal in an authentication domain. | 
**isAssignedRoles** | **Boolean** | A Boolean that specifies whether the principal has any roles assigned. When this value is &#39;true,&#39; the principal has one or more roles assigned.  | 
**isAssignedRolesOrIsLocal** | **Boolean** | A Boolean that specifies whether the principal is a local user or has any roles assigned. When this value is &#39;true,&#39; the principal either has one or more roles assigned or is a local user.  | 
**isLocked** | **Boolean** | Boolean value that shows the lock state of a user account. Value is true when the account is locked and false when the account is not locked.  | 
**isTotpEnabled** | **Boolean** | Indicates if the principal has TOTP authentication enabled. Returns true when TOTP is enabled, returns false when TOTP is not enabled.  | [optional] 
**isTotpEnforced** | **Boolean** | Indicates if the TOTP authentication is enforced. Returns true when TOTP is enforced, returns false when TOTP is not enforced.  | [optional] 
**lastName** | **String** | Last name of a principal of type user. For all other types the value is null.  | [optional] 
**mfaServerName** | **String** | Name of the MFA server assgined to the user.  | [optional] 
**name** | **String** | The name of a principal in an authentication domain. | 
**principalType** | [**PrincipalType**](PrincipalType.md) |  | 
**roles** | [**[RoleInfo]**](RoleInfo.md) | Roles assigned to this principal. | 


