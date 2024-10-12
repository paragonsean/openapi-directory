

# PublicAccessBlockConfiguration

<p>The <code>PublicAccessBlock</code> configuration that you want to apply to this Amazon S3 account. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status\">The Meaning of \"Public\"</a> in the <i>Amazon S3 User Guide</i>.</p> <p>This data type is not supported for Amazon S3 on Outposts.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockPublicAcls** | [**Boolean**](Boolean.md) |  |  [optional] |
|**ignorePublicAcls** | [**Boolean**](Boolean.md) |  |  [optional] |
|**blockPublicPolicy** | [**Boolean**](Boolean.md) |  |  [optional] |
|**restrictPublicBuckets** | [**Boolean**](Boolean.md) |  |  [optional] |



