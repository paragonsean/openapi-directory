

# AmazonopensearchserviceDestinationUpdate

Describes an update for a destination in Amazon OpenSearch Service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roleARN** | [**String**](String.md) |  |  [optional] |
|**domainARN** | [**String**](String.md) |  |  [optional] |
|**clusterEndpoint** | [**String**](String.md) |  |  [optional] |
|**indexName** | [**String**](String.md) |  |  [optional] |
|**typeName** | [**String**](String.md) |  |  [optional] |
|**indexRotationPeriod** | [**AmazonopensearchserviceIndexRotationPeriod**](AmazonopensearchserviceIndexRotationPeriod.md) |  |  [optional] |
|**bufferingHints** | [**AmazonopensearchserviceDestinationUpdateBufferingHints**](AmazonopensearchserviceDestinationUpdateBufferingHints.md) |  |  [optional] |
|**retryOptions** | [**AmazonopensearchserviceDestinationConfigurationRetryOptions**](AmazonopensearchserviceDestinationConfigurationRetryOptions.md) |  |  [optional] |
|**s3Update** | [**S3DestinationUpdate**](S3DestinationUpdate.md) |  |  [optional] |
|**processingConfiguration** | [**ProcessingConfiguration**](ProcessingConfiguration.md) |  |  [optional] |
|**cloudWatchLoggingOptions** | [**CloudWatchLoggingOptions**](CloudWatchLoggingOptions.md) |  |  [optional] |



