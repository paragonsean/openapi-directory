

# RecipientInfo

<p>Contains information about the party that receives the response from the API operation.</p> <p>This data type is designed to support Amazon Web Services Nitro Enclaves, which lets you create an isolated compute environment in Amazon EC2. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html\">How Amazon Web Services Nitro Enclaves uses KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyEncryptionAlgorithm** | [**KeyEncryptionMechanism**](KeyEncryptionMechanism.md) |  |  [optional] |
|**attestationDocument** | [**String**](String.md) |  |  [optional] |



