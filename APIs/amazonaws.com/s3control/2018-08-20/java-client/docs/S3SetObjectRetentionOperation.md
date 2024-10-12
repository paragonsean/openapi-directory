

# S3SetObjectRetentionOperation

Contains the configuration parameters for the Object Lock retention action for an S3 Batch Operations job. Batch Operations passes every object to the underlying <code>PutObjectRetention</code> API operation. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html\">Using S3 Object Lock retention with S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bypassGovernanceRetention** | [**Boolean**](Boolean.md) |  |  [optional] |
|**retention** | [**S3SetObjectRetentionOperationRetention**](S3SetObjectRetentionOperationRetention.md) |  |  |



