

# TransformEncryption

<p>The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.</p> <p>Additionally, imported labels and trained transforms can now be encrypted using a customer provided KMS key.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mlUserDataEncryption** | [**TransformEncryptionMlUserDataEncryption**](TransformEncryptionMlUserDataEncryption.md) |  |  [optional] |
|**taskRunSecurityConfigurationName** | [**String**](String.md) |  |  [optional] |



