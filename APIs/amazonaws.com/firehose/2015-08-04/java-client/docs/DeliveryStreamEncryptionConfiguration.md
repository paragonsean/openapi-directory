

# DeliveryStreamEncryptionConfiguration

Contains information about the server-side encryption (SSE) status for the delivery stream, the type customer master key (CMK) in use, if any, and the ARN of the CMK. You can get <code>DeliveryStreamEncryptionConfiguration</code> by invoking the <a>DescribeDeliveryStream</a> operation. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyARN** | [**String**](String.md) |  |  [optional] |
|**keyType** | [**KeyType**](KeyType.md) |  |  [optional] |
|**status** | [**DeliveryStreamEncryptionStatus**](DeliveryStreamEncryptionStatus.md) |  |  [optional] |
|**failureDescription** | [**DeliveryStreamEncryptionConfigurationFailureDescription**](DeliveryStreamEncryptionConfigurationFailureDescription.md) |  |  [optional] |



