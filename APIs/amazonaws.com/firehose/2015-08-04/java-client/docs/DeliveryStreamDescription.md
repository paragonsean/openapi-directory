

# DeliveryStreamDescription

Contains information about a delivery stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryStreamName** | [**String**](String.md) |  |  |
|**deliveryStreamARN** | [**String**](String.md) |  |  |
|**deliveryStreamStatus** | [**DeliveryStreamStatus**](DeliveryStreamStatus.md) |  |  |
|**failureDescription** | [**DeliveryStreamEncryptionConfigurationFailureDescription**](DeliveryStreamEncryptionConfigurationFailureDescription.md) |  |  [optional] |
|**deliveryStreamEncryptionConfiguration** | [**DeliveryStreamDescriptionDeliveryStreamEncryptionConfiguration**](DeliveryStreamDescriptionDeliveryStreamEncryptionConfiguration.md) |  |  [optional] |
|**deliveryStreamType** | [**DeliveryStreamType**](DeliveryStreamType.md) |  |  |
|**versionId** | [**String**](String.md) |  |  |
|**createTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdateTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**source** | [**DeliveryStreamDescriptionSource**](DeliveryStreamDescriptionSource.md) |  |  [optional] |
|**destinations** | [**List**](List.md) |  |  |
|**hasMoreDestinations** | [**Boolean**](Boolean.md) |  |  |



