

# CustomOriginConfig

A custom origin. A custom origin is any origin that is <i>not</i> an Amazon S3 bucket, with one exception. An Amazon S3 bucket that is <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html\">configured with static website hosting</a> <i>is</i> a custom origin.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**htTPPort** | [**Integer**](Integer.md) |  |  |
|**htTPSPort** | [**Integer**](Integer.md) |  |  |
|**originProtocolPolicy** | [**OriginProtocolPolicy**](OriginProtocolPolicy.md) |  |  |
|**originSslProtocols** | [**CustomOriginConfigOriginSslProtocols**](CustomOriginConfigOriginSslProtocols.md) |  |  [optional] |
|**originReadTimeout** | [**Integer**](Integer.md) |  |  [optional] |
|**originKeepaliveTimeout** | [**Integer**](Integer.md) |  |  [optional] |



