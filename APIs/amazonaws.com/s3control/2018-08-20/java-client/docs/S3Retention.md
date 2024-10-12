

# S3Retention

Contains the S3 Object Lock retention mode to be applied to all objects in the S3 Batch Operations job. If you don't provide <code>Mode</code> and <code>RetainUntilDate</code> data types in your operation, you will remove the retention from your objects. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html\">Using S3 Object Lock retention with S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retainUntilDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**mode** | [**S3ObjectLockRetentionMode**](S3ObjectLockRetentionMode.md) |  |  [optional] |



