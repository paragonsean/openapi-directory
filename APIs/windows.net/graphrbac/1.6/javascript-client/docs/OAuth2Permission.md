# GraphRbacManagementClient.OAuth2Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminConsentDescription** | **String** | Permission help text that appears in the admin consent and app assignment experiences. | [optional] 
**adminConsentDisplayName** | **String** | Display name for the permission that appears in the admin consent and app assignment experiences. | [optional] 
**id** | **String** | Unique scope permission identifier inside the oauth2Permissions collection. | [optional] 
**isEnabled** | **Boolean** | When creating or updating a permission, this property must be set to true (which is the default). To delete a permission, this property must first be set to false. At that point, in a subsequent call, the permission may be removed.  | [optional] 
**type** | **String** | Specifies whether this scope permission can be consented to by an end user, or whether it is a tenant-wide permission that must be consented to by a Company Administrator. Possible values are \&quot;User\&quot; or \&quot;Admin\&quot;. | [optional] 
**userConsentDescription** | **String** | Permission help text that appears in the end user consent experience. | [optional] 
**userConsentDisplayName** | **String** | Display name for the permission that appears in the end user consent experience. | [optional] 
**value** | **String** | The value of the scope claim that the resource application should expect in the OAuth 2.0 access token. | [optional] 


