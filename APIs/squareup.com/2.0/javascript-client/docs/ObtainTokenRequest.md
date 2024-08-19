# SquareConnectApi.ObtainTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | The Square-issued ID of your application, available from the [developer dashboard](https://developer.squareup.com/apps). | 
**clientSecret** | **String** | The Square-issued application secret for your application, available from the [developer dashboard](https://developer.squareup.com/apps). | 
**code** | **String** | The authorization code to exchange. This is required if &#x60;grant_type&#x60; is set to &#x60;authorization_code&#x60;, to indicate that the application wants to exchange an authorization code for an OAuth access token. | [optional] 
**grantType** | **String** | Specifies the method to request an OAuth access token. Valid values are: &#x60;authorization_code&#x60;, &#x60;refresh_token&#x60;, and &#x60;migration_token&#x60; | 
**migrationToken** | **String** | Legacy OAuth access token obtained using a Connect API version prior to 2019-03-13. This parameter is required if &#x60;grant_type&#x60; is set to &#x60;migration_token&#x60; to indicate that the application wants to get a replacement OAuth access token. The response also returns a refresh token. For more information, see [Migrate to Using Refresh Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens). | [optional] 
**redirectUri** | **String** | The redirect URL assigned in the [developer dashboard](https://developer.squareup.com/apps). | [optional] 
**refreshToken** | **String** | A valid refresh token for generating a new OAuth access token. A valid refresh token is required if &#x60;grant_type&#x60; is set to &#x60;refresh_token&#x60; , to indicate the application wants a replacement for an expired OAuth access token. | [optional] 
**scopes** | **[String]** | A JSON list of strings representing the permissions the application is requesting. For example: \&quot;&#x60;[\&quot;MERCHANT_PROFILE_READ\&quot;,\&quot;PAYMENTS_READ\&quot;,\&quot;BANK_ACCOUNTS_READ\&quot;]&#x60;\&quot; The access token returned in the response is granted the permissions that comprise the intersection between the requested list of permissions, and those that belong to the provided refresh token. | [optional] 
**shortLived** | **Boolean** | A boolean indicating a request for a short-lived access token. The short-lived access token returned in the response will expire in 24 hours. | [optional] 


