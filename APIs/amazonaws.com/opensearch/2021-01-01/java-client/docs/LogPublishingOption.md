

# LogPublishingOption

<p>Specifies whether the Amazon OpenSearch Service domain publishes the OpenSearch application and slow logs to Amazon CloudWatch. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createdomain-configure-slow-logs.html\">Monitoring OpenSearch logs with Amazon CloudWatch Logs</a>.</p> <note> <p>After you enable log publishing, you still have to enable the collection of slow logs using the OpenSearch REST API.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudWatchLogsLogGroupArn** | [**String**](String.md) |  |  [optional] |
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |



