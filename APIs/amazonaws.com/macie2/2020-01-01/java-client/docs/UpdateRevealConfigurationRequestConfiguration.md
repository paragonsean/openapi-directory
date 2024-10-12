

# UpdateRevealConfigurationRequestConfiguration

Specifies the configuration settings for retrieving occurrences of sensitive data reported by findings, and the status of the configuration for an Amazon Macie account. When you enable the configuration for the first time, your request must specify an Key Management Service (KMS) key. Otherwise, an error occurs. Macie uses the specified key to encrypt the sensitive data that you retrieve.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**status** | [**RevealStatus**](RevealStatus.md) |  |  [optional] |



