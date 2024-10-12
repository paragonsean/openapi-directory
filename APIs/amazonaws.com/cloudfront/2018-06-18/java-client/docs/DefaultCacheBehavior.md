

# DefaultCacheBehavior

A complex type that describes the default cache behavior if you don't specify a <code>CacheBehavior</code> element or if files don't match any of the values of <code>PathPattern</code> in <code>CacheBehavior</code> elements. You must create exactly one default cache behavior.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetOriginId** | [**String**](String.md) |  |  |
|**forwardedValues** | [**DefaultCacheBehaviorForwardedValues**](DefaultCacheBehaviorForwardedValues.md) |  |  |
|**trustedSigners** | [**DefaultCacheBehaviorTrustedSigners**](DefaultCacheBehaviorTrustedSigners.md) |  |  |
|**viewerProtocolPolicy** | [**ViewerProtocolPolicy**](ViewerProtocolPolicy.md) |  |  |
|**minTTL** | [**Integer**](Integer.md) |  |  |
|**allowedMethods** | [**AllowedMethods**](AllowedMethods.md) |  |  [optional] |
|**smoothStreaming** | [**Boolean**](Boolean.md) |  |  [optional] |
|**defaultTTL** | [**Integer**](Integer.md) |  |  [optional] |
|**maxTTL** | **Integer** |  |  [optional] |
|**compress** | [**Boolean**](Boolean.md) |  |  [optional] |
|**lambdaFunctionAssociations** | [**DefaultCacheBehaviorLambdaFunctionAssociations**](DefaultCacheBehaviorLambdaFunctionAssociations.md) |  |  [optional] |
|**fieldLevelEncryptionId** | [**String**](String.md) |  |  [optional] |



