

# ConnectorConfigurationSecret

Secret value parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**plaintext** | **String** | Input only. Secret as plaintext. |  [optional] |
|**secretType** | [**SecretTypeEnum**](#SecretTypeEnum) | Output only. Indicates type of secret. Can be used to check type of stored secret value even if it&#39;s &#x60;INPUT_ONLY&#x60;. |  [optional] [readonly] |



## Enum: SecretTypeEnum

| Name | Value |
|---- | -----|
| SECRET_TYPE_UNSPECIFIED | &quot;SECRET_TYPE_UNSPECIFIED&quot; |
| PLAINTEXT | &quot;PLAINTEXT&quot; |



