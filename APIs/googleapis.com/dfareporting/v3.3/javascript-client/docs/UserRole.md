# CampaignManager360Api.UserRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this user role. This is a read-only field that can be left blank. | [optional] 
**defaultUserRole** | **Boolean** | Whether this is a default user role. Default user roles are created by the system for the account/subaccount and cannot be modified or deleted. Each default user role comes with a basic set of preassigned permissions. | [optional] 
**id** | **String** | ID of this user role. This is a read-only, auto-generated field. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#userRole\&quot;. | [optional] 
**name** | **String** | Name of this user role. This is a required field. Must be less than 256 characters long. If this user role is under a subaccount, the name must be unique among sites of the same subaccount. Otherwise, this user role is a top-level user role, and the name must be unique among top-level user roles of the same account. | [optional] 
**parentUserRoleId** | **String** | ID of the user role that this user role is based on or copied from. This is a required field. | [optional] 
**permissions** | [**[UserRolePermission]**](UserRolePermission.md) | List of permissions associated with this user role. | [optional] 
**subaccountId** | **String** | Subaccount ID of this user role. This is a read-only field that can be left blank. | [optional] 


