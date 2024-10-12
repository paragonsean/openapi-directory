

# SecretProperties

Properties of the secret

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**SecretAttributes**](SecretAttributes.md) |  |  [optional] |
|**contentType** | **String** | The content type of the secret. |  [optional] |
|**secretUri** | **String** | The URI to retrieve the current version of the secret. |  [optional] [readonly] |
|**secretUriWithVersion** | **String** | The URI to retrieve the specific version of the secret. |  [optional] [readonly] |
|**value** | **String** | The value of the secret. NOTE: &#39;value&#39; will never be returned from the service, as APIs using this model are is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |  [optional] |



