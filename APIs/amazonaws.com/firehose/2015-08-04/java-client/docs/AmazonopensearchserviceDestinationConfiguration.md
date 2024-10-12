

# AmazonopensearchserviceDestinationConfiguration

Describes the configuration of a destination in Amazon OpenSearch Service

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  |
|**domainARN** | [**String**](String.md) |  |  [optional] |
|**clusterEndpoint** | [**String**](String.md) |  |  [optional] |
|**indexName** | [**String**](String.md) |  |  |
|**typeName** | [**String**](String.md) |  |  [optional] |
|**indexRotationPeriod** | [**AmazonopensearchserviceIndexRotationPeriod**](AmazonopensearchserviceIndexRotationPeriod.md) |  |  [optional] |
|**bufferingHints** | [**AmazonopensearchserviceDestinationConfigurationBufferingHints**](AmazonopensearchserviceDestinationConfigurationBufferingHints.md) |  |  [optional] |
|**retryOptions** | [**AmazonopensearchserviceDestinationConfigurationRetryOptions**](AmazonopensearchserviceDestinationConfigurationRetryOptions.md) |  |  [optional] |
|**s3BackupMode** | [**AmazonopensearchserviceS3BackupMode**](AmazonopensearchserviceS3BackupMode.md) |  |  [optional] |
|**s3Configuration** | [**S3DestinationConfiguration**](S3DestinationConfiguration.md) |  |  |
|**processingConfiguration** | [**ProcessingConfiguration**](ProcessingConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**CloudWatchLoggingOptions**](CloudWatchLoggingOptions.md) |  |  [optional] |
|**vpcConfiguration** | [**VpcConfiguration**](VpcConfiguration.md) |  |  [optional] |



