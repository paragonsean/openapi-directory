

# CreateTrailRequest

Specifies the settings for each trail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**s3BucketName** | [**String**](String.md) |  |  |
|**s3KeyPrefix** | [**String**](String.md) |  |  [optional] |
|**snsTopicName** | [**String**](String.md) |  |  [optional] |
|**includeGlobalServiceEvents** | [**Boolean**](Boolean.md) |  |  [optional] |
|**isMultiRegionTrail** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableLogFileValidation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**cloudWatchLogsLogGroupArn** | [**String**](String.md) |  |  [optional] |
|**cloudWatchLogsRoleArn** | [**String**](String.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**isOrganizationTrail** | [**Boolean**](Boolean.md) |  |  [optional] |
|**tagsList** | [**List&lt;Tag&gt;**](Tag.md) | A list of tags. |  [optional] |



