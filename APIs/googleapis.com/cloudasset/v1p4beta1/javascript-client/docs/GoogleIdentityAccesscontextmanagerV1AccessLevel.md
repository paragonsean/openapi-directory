# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1AccessLevel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**GoogleIdentityAccesscontextmanagerV1BasicLevel**](GoogleIdentityAccesscontextmanagerV1BasicLevel.md) |  | [optional] 
**custom** | [**GoogleIdentityAccesscontextmanagerV1CustomLevel**](GoogleIdentityAccesscontextmanagerV1CustomLevel.md) |  | [optional] 
**description** | **String** | Description of the &#x60;AccessLevel&#x60; and its use. Does not affect behavior. | [optional] 
**name** | **String** | Required. Resource name for the Access Level. The &#x60;short_name&#x60; component must begin with a letter and only include alphanumeric and &#39;_&#39;. Format: &#x60;accessPolicies/{access_policy}/accessLevels/{access_level}&#x60;. The maximum length of the &#x60;access_level&#x60; component is 50 characters. | [optional] 
**title** | **String** | Human readable title. Must be unique within the Policy. | [optional] 


