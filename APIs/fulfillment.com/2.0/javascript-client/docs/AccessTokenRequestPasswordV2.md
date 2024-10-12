# FulfillmentComApiv2.AccessTokenRequestPasswordV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **String** |  | 
**username** | **String** |  | 
**clientId** | **String** | Id and secret provided by FDC | 
**clientSecret** | **String** |  | 
**grantType** | **String** | Indicates how you&#39;re authenticating your request | 
**scope** | **String** | Currently limited to Order Management System | [default to &#39;oms&#39;]



## Enum: GrantTypeEnum


* `password` (value: `"password"`)

* `refresh_token` (value: `"refresh_token"`)





## Enum: ScopeEnum


* `oms` (value: `"oms"`)




