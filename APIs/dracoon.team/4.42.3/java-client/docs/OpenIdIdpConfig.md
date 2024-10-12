

# OpenIdIdpConfig

OpenID Connect IDP configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationEndPointUrl** | **String** | URL of the authorization endpoint |  [optional] |
|**clientId** | **String** | ID of the OpenID client |  [optional] |
|**clientSecret** | **String** | Secret, which client uses at authentication. |  [optional] |
|**fallbackMappingClaim** | **String** | Name of the claim which is used for the user mapping fallback. |  [optional] |
|**flow** | [**FlowEnum**](#FlowEnum) | &amp;#128640; Since v4.11.0  Flow, which is used at authentication |  [optional] |
|**id** | **Integer** | ID |  |
|**issuer** | **String** | Issuer identifier of the IDP  The value is a case sensitive URL. |  [optional] |
|**jwksEndPointUrl** | **String** | URL of the JWKS endpoint |  [optional] |
|**mappingClaim** | **String** | Name of the claim which is used for the user mapping. |  [optional] |
|**name** | **String** | Name of the IDP |  [optional] |
|**pkceChallengeMethod** | **String** | PKCE code challenge method.  cf. [RFC 7636](https://tools.ietf.org/html/rfc7636) |  [optional] |
|**pkceEnabled** | **Boolean** | Determines whether PKCE is enabled.  cf. [RFC 7636](https://tools.ietf.org/html/rfc7636) |  [optional] |
|**redirectUris** | **List&lt;String&gt;** | URIs, to which a user is redirected after authorization. |  [optional] |
|**scopes** | **List&lt;String&gt;** | List of requested scopes  Usually &#x60;openid&#x60; and the names of the requested claims. |  [optional] |
|**tokenEndPointUrl** | **String** | URL of the token endpoint |  [optional] |
|**userImportEnabled** | **Boolean** | Determines if a DRACOON account is automatically created for a new user  who successfully logs on with his / her AD / IDP account. |  [optional] |
|**userImportGroup** | **Long** | User group that is assigned to users who are created by automatic import.  Reset with &#x60;0&#x60; |  [optional] |
|**userInfoEndPointUrl** | **String** | URL of the user info endpoint |  [optional] |
|**userInfoSource** | [**UserInfoSourceEnum**](#UserInfoSourceEnum) | &amp;#128640; Since v4.23.0  Source, which is used to get user information at the import or update of a user. |  [optional] |
|**userManagementUrl** | **String** | URL of the user management UI.  Use empty string to remove. |  [optional] |
|**userUpdateEnabled** | **Boolean** | Determines if the DRACOON account is updated with data from AD / IDP.  For OpenID Connect, the scopes &#x60;email&#x60; and &#x60;profile&#x60; are needed. |  [optional] |



## Enum: FlowEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorization_code&quot; |
| HYBRID | &quot;hybrid&quot; |



## Enum: UserInfoSourceEnum

| Name | Value |
|---- | -----|
| USER_INFO_ENDPOINT | &quot;user_info_endpoint&quot; |
| ID_TOKEN | &quot;id_token&quot; |



