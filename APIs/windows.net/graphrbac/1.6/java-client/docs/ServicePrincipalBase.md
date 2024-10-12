

# ServicePrincipalBase

Active Directory service principal common properties shared among GET, POST and PATCH

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountEnabled** | **Boolean** | whether or not the service principal account is enabled |  [optional] |
|**appRoleAssignmentRequired** | **Boolean** | Specifies whether an AppRoleAssignment to a user or group is required before Azure AD will issue a user or access token to the application. |  [optional] |
|**keyCredentials** | **List&lt;KeyCredential&gt;** | The collection of key credentials associated with the service principal. |  [optional] |
|**passwordCredentials** | **List&lt;PasswordCredential&gt;** | The collection of password credentials associated with the service principal. |  [optional] |
|**servicePrincipalType** | **String** | the type of the service principal |  [optional] |
|**tags** | **List&lt;String&gt;** | Optional list of tags that you can apply to your service principals. Not nullable. |  [optional] |



