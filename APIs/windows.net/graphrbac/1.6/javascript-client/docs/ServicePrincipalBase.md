# GraphRbacManagementClient.ServicePrincipalBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountEnabled** | **Boolean** | whether or not the service principal account is enabled | [optional] 
**appRoleAssignmentRequired** | **Boolean** | Specifies whether an AppRoleAssignment to a user or group is required before Azure AD will issue a user or access token to the application. | [optional] 
**keyCredentials** | [**[KeyCredential]**](KeyCredential.md) | The collection of key credentials associated with the service principal. | [optional] 
**passwordCredentials** | [**[PasswordCredential]**](PasswordCredential.md) | The collection of password credentials associated with the service principal. | [optional] 
**servicePrincipalType** | **String** | the type of the service principal | [optional] 
**tags** | **[String]** | Optional list of tags that you can apply to your service principals. Not nullable. | [optional] 


