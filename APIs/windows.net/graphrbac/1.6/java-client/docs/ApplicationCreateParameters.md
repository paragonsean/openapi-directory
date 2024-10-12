

# ApplicationCreateParameters

Request parameters for creating a new application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The display name of the application. |  |
|**identifierUris** | **List&lt;String&gt;** | A collection of URIs for the application. |  [optional] |
|**allowGuestsSignIn** | **Boolean** | A property on the application to indicate if the application accepts other IDPs or not or partially accepts. |  [optional] |
|**allowPassthroughUsers** | **Boolean** | Indicates that the application supports pass through users who have no presence in the resource tenant. |  [optional] |
|**appLogoUrl** | **String** | The url for the application logo image stored in a CDN. |  [optional] |
|**appPermissions** | **List&lt;String&gt;** | The application permissions. |  [optional] |
|**appRoles** | [**List&lt;AppRole&gt;**](AppRole.md) | The collection of application roles that an application may declare. These roles can be assigned to users, groups or service principals. |  [optional] |
|**availableToOtherTenants** | **Boolean** | Whether the application is available to other tenants. |  [optional] |
|**errorUrl** | **String** | A URL provided by the author of the application to report errors when using the application. |  [optional] |
|**groupMembershipClaims** | **GroupMembershipClaims** |  |  [optional] |
|**homepage** | **String** | The home page of the application. |  [optional] |
|**informationalUrls** | [**InformationalUrl**](InformationalUrl.md) |  |  [optional] |
|**isDeviceOnlyAuthSupported** | **Boolean** | Specifies whether this application supports device authentication without a user. The default is false. |  [optional] |
|**keyCredentials** | **List&lt;KeyCredential&gt;** | A collection of KeyCredential objects. |  [optional] |
|**knownClientApplications** | **List&lt;String&gt;** | Client applications that are tied to this resource application. Consent to any of the known client applications will result in implicit consent to the resource application through a combined consent dialog (showing the OAuth permission scopes required by the client and the resource). |  [optional] |
|**logoutUrl** | **String** | the url of the logout page |  [optional] |
|**oauth2AllowImplicitFlow** | **Boolean** | Whether to allow implicit grant flow for OAuth2 |  [optional] |
|**oauth2AllowUrlPathMatching** | **Boolean** | Specifies whether during a token Request Azure AD will allow path matching of the redirect URI against the applications collection of replyURLs. The default is false. |  [optional] |
|**oauth2Permissions** | [**List&lt;OAuth2Permission&gt;**](OAuth2Permission.md) | The collection of OAuth 2.0 permission scopes that the web API (resource) application exposes to client applications. These permission scopes may be granted to client applications during consent. |  [optional] |
|**oauth2RequirePostResponse** | **Boolean** | Specifies whether, as part of OAuth 2.0 token requests, Azure AD will allow POST requests, as opposed to GET requests. The default is false, which specifies that only GET requests will be allowed. |  [optional] |
|**optionalClaims** | [**OptionalClaims**](OptionalClaims.md) |  |  [optional] |
|**orgRestrictions** | **List&lt;String&gt;** | A list of tenants allowed to access application. |  [optional] |
|**passwordCredentials** | **List&lt;PasswordCredential&gt;** | A collection of PasswordCredential objects |  [optional] |
|**preAuthorizedApplications** | [**List&lt;PreAuthorizedApplication&gt;**](PreAuthorizedApplication.md) | list of pre-authorized applications. |  [optional] |
|**publicClient** | **Boolean** | Specifies whether this application is a public client (such as an installed application running on a mobile device). Default is false. |  [optional] |
|**publisherDomain** | **String** | Reliable domain which can be used to identify an application. |  [optional] |
|**replyUrls** | **List&lt;String&gt;** | A collection of reply URLs for the application. |  [optional] |
|**requiredResourceAccess** | **List&lt;RequiredResourceAccess&gt;** | Specifies resources that this application requires access to and the set of OAuth permission scopes and application roles that it needs under each of those resources. This pre-configuration of required resource access drives the consent experience. |  [optional] |
|**samlMetadataUrl** | **String** | The URL to the SAML metadata for the application. |  [optional] |
|**signInAudience** | **String** | Audience for signing in to the application (AzureADMyOrganization, AzureADAllOrganizations, AzureADAndMicrosoftAccounts). |  [optional] |
|**wwwHomepage** | **String** | The primary Web page. |  [optional] |



