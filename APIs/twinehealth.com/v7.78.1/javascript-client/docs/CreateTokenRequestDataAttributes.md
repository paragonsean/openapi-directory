# FitbitPlusApi.CreateTokenRequestDataAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Contact Fitbit Plus API Support to get a client id and secret. | 
**clientSecret** | **String** | Contact Fitbit Plus API Support to get a client id and secret. Secret is required if grant_type is \&quot;client_credentials\&quot; | [optional] 
**grantType** | **String** |  | 
**refreshToken** | **String** | Required if grant_type is \&quot;refresh_token\&quot; | [optional] 



## Enum: GrantTypeEnum


* `refresh_token` (value: `"refresh_token"`)

* `client_credentials` (value: `"client_credentials"`)




