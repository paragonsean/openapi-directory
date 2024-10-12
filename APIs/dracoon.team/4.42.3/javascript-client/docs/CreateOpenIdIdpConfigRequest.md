# DracoonApi.CreateOpenIdIdpConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationEndPointUrl** | **String** | URL of the authorization endpoint | 
**clientId** | **String** | ID of the OpenID client | 
**clientSecret** | **String** | Secret, which client uses at authentication. | 
**fallbackMappingClaim** | **String** | Name of the claim which is used for the user mapping fallback. | [optional] 
**flow** | **String** | &amp;#128640; Since v4.11.0  Flow, which is used at authentication | [optional] 
**issuer** | **String** | Issuer identifier of the IDP  The value is a case sensitive URL. | 
**jwksEndPointUrl** | **String** | URL of the JWKS endpoint | 
**mappingClaim** | **String** | Name of the claim which is used for the user mapping. | 
**name** | **String** | Name of the IDP | 
**pkceChallengeMethod** | **String** | PKCE code challenge method.  cf. [RFC 7636](https://tools.ietf.org/html/rfc7636) | [optional] [default to &#39;plain&#39;]
**pkceEnabled** | **Boolean** | Determines whether PKCE is enabled.  cf. [RFC 7636](https://tools.ietf.org/html/rfc7636) | [optional] [default to false]
**redirectUris** | **[String]** | URIs, to which a user is redirected after authorization. | 
**scopes** | **[String]** | List of requested scopes | 
**tokenEndPointUrl** | **String** | URL of the token endpoint | 
**userImportEnabled** | **Boolean** | Determines if a DRACOON account is automatically created for a new user  who successfully logs on with his / her AD / IDP account. | [optional] [default to false]
**userImportGroup** | **Number** | User group that is assigned to users who are created by automatic import.  Reset with &#x60;0&#x60; | [optional] 
**userInfoEndPointUrl** | **String** | URL of the user info endpoint | 
**userInfoSource** | **String** | &amp;#128640; Since v4.23.0  Source, which is used to get user information at the import or update of a user. | [optional] 
**userManagementUrl** | **String** | URL of the user management UI.  Use empty string to remove. | [optional] 
**userUpdateEnabled** | **Boolean** | Determines if the DRACOON account is updated with data from AD / IDP.  For OpenID Connect, the scopes &#x60;email&#x60; and &#x60;profile&#x60; are needed. | [optional] [default to false]



## Enum: FlowEnum


* `authorization_code` (value: `"authorization_code"`)

* `hybrid` (value: `"hybrid"`)





## Enum: UserInfoSourceEnum


* `user_info_endpoint` (value: `"user_info_endpoint"`)

* `id_token` (value: `"id_token"`)




