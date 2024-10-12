# DracoonApi.UpdateOpenIdIdpConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationEndPointUrl** | **String** | URL of the authorization endpoint | [optional] 
**clientId** | **String** | ID of the OpenID client | [optional] 
**clientSecret** | **String** | Secret, which client uses at authentication. | [optional] 
**fallbackMappingClaim** | **String** | Name of the claim which is used for the user mapping fallback. | [optional] 
**flow** | **String** | &amp;#128640; Since v4.11.0  Flow, which is used at authentication | [optional] 
**issuer** | **String** | Issuer identifier of the IDP  The value is a case sensitive URL. | [optional] 
**jwksEndPointUrl** | **String** | URL of the JWKS endpoint | [optional] 
**mappingClaim** | **String** | Name of the claim which is used for the user mapping. | [optional] 
**name** | **String** | Name of the IDP | [optional] 
**pkceChallengeMethod** | **String** | PKCE code challenge method.  cf. [RFC 7636](https://tools.ietf.org/html/rfc7636) | [optional] 
**pkceEnabled** | **Boolean** | Determines whether PKCE is enabled.  cf. [RFC 7636](https://tools.ietf.org/html/rfc7636) | [optional] [default to false]
**redirectUris** | **[String]** | URIs, to which a user is redirected after authorization. | [optional] 
**resetFallbackMappingClaim** | **Boolean** | Set &#x60;true&#x60; to reset &#x60;fallbackMappingClaim&#x60;. | [optional] 
**scopes** | **[String]** | List of requested scopes  Usually &#x60;openid&#x60; and the names of the requested claims. | [optional] 
**tokenEndPointUrl** | **String** | URL of the token endpoint | [optional] 
**userImportEnabled** | **Boolean** | Determines if a DRACOON account is automatically created for a new user  who successfully logs on with his / her AD / IDP account. | [optional] [default to false]
**userImportGroup** | **Number** | User group that is assigned to users who are created by automatic import.  Reset with &#x60;0&#x60; | [optional] 
**userInfoEndPointUrl** | **String** | URL of the user info endpoint | [optional] 
**userInfoSource** | **String** | &amp;#128640; Since v4.23.0  Source, which is used to get user information at the import or update of a user. | [optional] 
**userManagementUrl** | **String** | URL of the user management UI.  Use empty string to remove. | [optional] 
**userUpdateEnabled** | **Boolean** | Determines if the DRACOON account is updated with data from AD / IDP.  For OpenID Connect, the scopes &#x60;email&#x60; and &#x60;profile&#x60; are needed. | [optional] [default to false]



## Enum: FlowEnum


* `authorization_code` (value: `"authorization_code"`)

* `hybrid` (value: `"hybrid"`)





## Enum: UserInfoSourceEnum


* `user_info_endpoint` (value: `"user_info_endpoint"`)

* `id_token` (value: `"id_token"`)




