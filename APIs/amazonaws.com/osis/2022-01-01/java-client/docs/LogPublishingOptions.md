

# LogPublishingOptions

Container for the values required to configure logging for the pipeline. If you don't specify these values, OpenSearch Ingestion will not publish logs from your application to CloudWatch Logs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isLoggingEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**cloudWatchLogDestination** | [**CreatePipelineRequestLogPublishingOptionsCloudWatchLogDestination**](CreatePipelineRequestLogPublishingOptionsCloudWatchLogDestination.md) |  |  [optional] |



