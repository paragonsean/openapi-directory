

# DestinationConfiguration

A complex type that describes a location where chat logs will be stored. Each member represents the configuration of one log destination. For logging, you define only one type of destination (for CloudWatch Logs, Kinesis Firehose, or S3).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudWatchLogs** | [**CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs**](CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs.md) |  |  [optional] |
|**firehose** | [**CreateLoggingConfigurationRequestDestinationConfigurationFirehose**](CreateLoggingConfigurationRequestDestinationConfigurationFirehose.md) |  |  [optional] |
|**s3** | [**CreateLoggingConfigurationRequestDestinationConfigurationS3**](CreateLoggingConfigurationRequestDestinationConfigurationS3.md) |  |  [optional] |



