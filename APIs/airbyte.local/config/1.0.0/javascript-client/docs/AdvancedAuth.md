# AirbyteConfigurationApi.AdvancedAuth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authFlowType** | **String** |  | [optional] 
**oauthConfigSpecification** | [**OAuthConfigSpecification**](OAuthConfigSpecification.md) |  | [optional] 
**predicateKey** | **[String]** | Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable. | [optional] 
**predicateValue** | **String** | Value of the predicate_key fields for the advanced auth to be applicable. | [optional] 



## Enum: AuthFlowTypeEnum


* `oauth2.0` (value: `"oauth2.0"`)

* `oauth1.0` (value: `"oauth1.0"`)




