

# Origin

<p>A complex type that describes the Amazon S3 bucket, HTTP server (for example, a web server), Amazon MediaStore, or other server from which CloudFront gets your files. This can also be an origin group, if you've created an origin group. You must specify at least one origin or origin group.</p> <p>For the current limit on the number of origins or origin groups that you can specify for a distribution, see <a href=\"http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront\">Amazon CloudFront Limits</a> in the <i>AWS General Reference</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**domainName** | [**String**](String.md) |  |  |
|**originPath** | [**String**](String.md) |  |  [optional] |
|**customHeaders** | [**OriginCustomHeaders**](OriginCustomHeaders.md) |  |  [optional] |
|**s3OriginConfig** | [**OriginS3OriginConfig**](OriginS3OriginConfig.md) |  |  [optional] |
|**customOriginConfig** | [**OriginCustomOriginConfig**](OriginCustomOriginConfig.md) |  |  [optional] |



