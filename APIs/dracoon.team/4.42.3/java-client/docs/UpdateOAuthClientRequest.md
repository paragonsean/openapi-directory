

# UpdateOAuthClientRequest

Request model for updating an OAuth client

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTokenValidity** | **Integer** | Validity of the access token in seconds. |  [optional] |
|**approvalValidity** | **Integer** | &amp;#128640; Since v4.22.0  Validity of the approval interval in seconds. |  [optional] |
|**clientName** | **String** | Name, which is shown at the client configuration and authorization. |  [optional] |
|**clientSecret** | **String** | Secret, which client uses at authentication. |  [optional] |
|**clientType** | [**ClientTypeEnum**](#ClientTypeEnum) | Determines whether client is a confidential or public client. |  [optional] |
|**grantTypes** | [**GrantTypesEnum**](#GrantTypesEnum) | Authorized grant types  * &#x60;authorization_code&#x60;  * &#x60;implicit&#x60;  * &#x60;password&#x60;  * &#x60;client_credentials&#x60;  * &#x60;refresh_token&#x60;    cf. [RFC 6749](https://tools.ietf.org/html/rfc6749) |  |
|**isEnabled** | **Boolean** | Determines whether client is enabled. |  [optional] |
|**redirectUris** | **List&lt;String&gt;** | URIs, to which a user is redirected after authorization. |  [optional] |
|**refreshTokenValidity** | **Integer** | Validity of the refresh token in seconds. |  [optional] |



## Enum: ClientTypeEnum

| Name | Value |
|---- | -----|
| CONFIDENTIAL | &quot;confidential&quot; |
| PUBLIC | &quot;public&quot; |



## Enum: GrantTypesEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorization_code&quot; |
| CLIENT_CREDENTIALS | &quot;client_credentials&quot; |
| IMPLICIT | &quot;implicit&quot; |
| PASSWORD | &quot;password&quot; |
| REFRESH_TOKEN | &quot;refresh_token&quot; |



