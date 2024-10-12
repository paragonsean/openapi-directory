# GraphRbacManagementClient.ServicePrincipal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountEnabled** | **Boolean** | whether or not the service principal account is enabled | [optional] 
**alternativeNames** | **[String]** | alternative names | [optional] 
**appDisplayName** | **String** | The display name exposed by the associated application. | [optional] [readonly] 
**appId** | **String** | The application ID. | [optional] 
**appOwnerTenantId** | **String** |  | [optional] [readonly] 
**appRoleAssignmentRequired** | **Boolean** | Specifies whether an AppRoleAssignment to a user or group is required before Azure AD will issue a user or access token to the application. | [optional] 
**appRoles** | [**[AppRole]**](AppRole.md) | The collection of application roles that an application may declare. These roles can be assigned to users, groups or service principals. | [optional] 
**displayName** | **String** | The display name of the service principal. | [optional] 
**errorUrl** | **String** | A URL provided by the author of the associated application to report errors when using the application. | [optional] 
**homepage** | **String** | The URL to the homepage of the associated application. | [optional] 
**keyCredentials** | [**[KeyCredential]**](KeyCredential.md) | The collection of key credentials associated with the service principal. | [optional] 
**logoutUrl** | **String** | A URL provided by the author of the associated application to logout | [optional] 
**oauth2Permissions** | [**[OAuth2Permission]**](OAuth2Permission.md) | The OAuth 2.0 permissions exposed by the associated application. | [optional] [readonly] 
**passwordCredentials** | [**[PasswordCredential]**](PasswordCredential.md) | The collection of password credentials associated with the service principal. | [optional] 
**preferredTokenSigningKeyThumbprint** | **String** | The thumbprint of preferred certificate to sign the token | [optional] 
**publisherName** | **String** | The publisher&#39;s name of the associated application | [optional] 
**replyUrls** | **[String]** | The URLs that user tokens are sent to for sign in with the associated application.  The redirect URIs that the oAuth 2.0 authorization code and access tokens are sent to for the associated application. | [optional] 
**samlMetadataUrl** | **String** | The URL to the SAML metadata of the associated application | [optional] 
**servicePrincipalNames** | **[String]** | A collection of service principal names. | [optional] 
**servicePrincipalType** | **String** | the type of the service principal | [optional] 
**tags** | **[String]** | Optional list of tags that you can apply to your service principals. Not nullable. | [optional] 


