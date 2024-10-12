# DracoonApi.CreateOAuthClientRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokenValidity** | **Number** | Validity of the access token in seconds. | [optional] 
**approvalValidity** | **Number** | &amp;#128640; Since v4.22.0  Validity of the approval interval in seconds. | [optional] 
**clientId** | **String** | ID of the OAuth client | [optional] 
**clientName** | **String** | Name, which is shown at the client configuration and authorization. | 
**clientSecret** | **String** | Secret, which client uses at authentication. | [optional] 
**clientType** | **String** | Determines whether client is a confidential or public client. | [optional] 
**grantTypes** | **[String]** | Authorized grant types  * &#x60;authorization_code&#x60;  * &#x60;implicit&#x60;  * &#x60;password&#x60;  * &#x60;client_credentials&#x60;  * &#x60;refresh_token&#x60;    cf. [RFC 6749](https://tools.ietf.org/html/rfc6749) | 
**redirectUris** | **[String]** | URIs, to which a user is redirected after authorization. | 
**refreshTokenValidity** | **Number** | Validity of the refresh token in seconds. | [optional] 



## Enum: ClientTypeEnum


* `confidential` (value: `"confidential"`)

* `public` (value: `"public"`)





## Enum: GrantTypesEnum


* `authorization_code` (value: `"authorization_code"`)

* `client_credentials` (value: `"client_credentials"`)

* `implicit` (value: `"implicit"`)

* `password` (value: `"password"`)

* `refresh_token` (value: `"refresh_token"`)




