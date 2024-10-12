

# CacheBehavior

<p>A complex type that describes how CloudFront processes requests.</p> <p>You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.</p> <p>For the current limit on the number of cache behaviors that you can add to a distribution, see <a href=\"http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront\">Amazon CloudFront Limits</a> in the <i>AWS General Reference</i>.</p> <p>If you don't want to specify any cache behaviors, include only an empty <code>CacheBehaviors</code> element. Don't include an empty <code>CacheBehavior</code> element, or CloudFront returns a <code>MalformedXML</code> error.</p> <p>To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty <code>CacheBehaviors</code> element.</p> <p>To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.</p> <p>For more information about cache behaviors, see <a href=\"http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior\">Cache Behaviors</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pathPattern** | [**String**](String.md) |  |  |
|**targetOriginId** | [**String**](String.md) |  |  |
|**forwardedValues** | [**DefaultCacheBehaviorForwardedValues**](DefaultCacheBehaviorForwardedValues.md) |  |  |
|**trustedSigners** | [**DefaultCacheBehaviorTrustedSigners**](DefaultCacheBehaviorTrustedSigners.md) |  |  |
|**viewerProtocolPolicy** | [**ViewerProtocolPolicy**](ViewerProtocolPolicy.md) |  |  |
|**minTTL** | [**Integer**](Integer.md) |  |  |
|**allowedMethods** | [**AllowedMethods**](AllowedMethods.md) |  |  [optional] |
|**smoothStreaming** | [**Boolean**](Boolean.md) |  |  [optional] |
|**defaultTTL** | [**Integer**](Integer.md) |  |  [optional] |
|**maxTTL** | [**Integer**](Integer.md) |  |  [optional] |
|**compress** | [**Boolean**](Boolean.md) |  |  [optional] |
|**lambdaFunctionAssociations** | [**DefaultCacheBehaviorLambdaFunctionAssociations**](DefaultCacheBehaviorLambdaFunctionAssociations.md) |  |  [optional] |
|**fieldLevelEncryptionId** | [**String**](String.md) |  |  [optional] |



