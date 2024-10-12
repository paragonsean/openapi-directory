# FulfillmentComApiv2.AccessTokenRequestV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **String** |  | 
**username** | **String** |  | 
**clientId** | **String** | Id and secret provided by FDC | 
**clientSecret** | **String** |  | 
**grantType** | **String** | Indicates how you&#39;re authenticating your request | 
**scope** | **String** | Currently limited to Order Management System | [default to &#39;oms&#39;]
**refreshToken** | **String** | You may request future tokens with the &#x60;refresh_token&#x60; from your previous &#x60;/oauth/access_token&#x60; request | 



## Enum: GrantTypeEnum


* `password` (value: `"password"`)

* `refresh_token` (value: `"refresh_token"`)





## Enum: ScopeEnum


* `oms` (value: `"oms"`)




