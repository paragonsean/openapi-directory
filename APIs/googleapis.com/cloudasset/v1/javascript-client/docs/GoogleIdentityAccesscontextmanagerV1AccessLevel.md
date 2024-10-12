# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1AccessLevel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**GoogleIdentityAccesscontextmanagerV1BasicLevel**](GoogleIdentityAccesscontextmanagerV1BasicLevel.md) |  | [optional] 
**custom** | [**GoogleIdentityAccesscontextmanagerV1CustomLevel**](GoogleIdentityAccesscontextmanagerV1CustomLevel.md) |  | [optional] 
**description** | **String** | Description of the &#x60;AccessLevel&#x60; and its use. Does not affect behavior. | [optional] 
**name** | **String** | Resource name for the &#x60;AccessLevel&#x60;. Format: &#x60;accessPolicies/{access_policy}/accessLevels/{access_level}&#x60;. The &#x60;access_level&#x60; component must begin with a letter, followed by alphanumeric characters or &#x60;_&#x60;. Its maximum length is 50 characters. After you create an &#x60;AccessLevel&#x60;, you cannot change its &#x60;name&#x60;. | [optional] 
**title** | **String** | Human readable title. Must be unique within the Policy. | [optional] 


