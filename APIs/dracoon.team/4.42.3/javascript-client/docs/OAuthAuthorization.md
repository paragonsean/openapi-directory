# DracoonApi.OAuthAuthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | ID of the OAuth client | 
**clientName** | **String** | Name, which is shown at the client configuration and authorization. | 
**createdAt** | **Date** | &amp;#128640; Since v4.13.0  Creation date of the authorization | [optional] 
**expiresAt** | **Date** | Expiration date of the authorization | [optional] 
**id** | **Number** | &amp;#128640; Since v4.12.0  ID of the OAuth authorization | [optional] 
**isCurrentAuthorization** | **Boolean** | &amp;#128640; Since v4.25.0  Determines whether authorization matches the one from Authorization Header | [optional] 
**isStandard** | **Boolean** | &amp;#128640; Since v4.12.0  Determines whether client is a standard client. | [optional] 
**usedAt** | **Date** | &amp;#128640; Since v4.13.0  Usage date of the authorization  (Time of last usage.) | [optional] 
**userAgentCategory** | **String** | &amp;#128640; Since v4.12.0  User agent category. | 
**userAgentInfo** | **String** | &amp;#128640; Since v4.12.0  User agent info. | [optional] 
**userAgentOs** | **String** | &amp;#128640; Since v4.12.0  User agent OS. | [optional] 
**userAgentType** | **String** | &amp;#128640; Since v4.12.0  User agent type. | [optional] 



## Enum: UserAgentCategoryEnum


* `browser` (value: `"browser"`)

* `native` (value: `"native"`)

* `unknown` (value: `"unknown"`)




