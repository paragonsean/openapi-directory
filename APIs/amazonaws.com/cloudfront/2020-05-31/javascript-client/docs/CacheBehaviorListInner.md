# AmazonCloudFront.CacheBehaviorListInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pathPattern** | **String** |  | 
**targetOriginId** | **String** |  | 
**trustedSigners** | [**CacheBehaviorTrustedSigners**](CacheBehaviorTrustedSigners.md) |  | [optional] 
**trustedKeyGroups** | [**DefaultCacheBehaviorTrustedKeyGroups**](DefaultCacheBehaviorTrustedKeyGroups.md) |  | [optional] 
**viewerProtocolPolicy** | [**ViewerProtocolPolicy**](ViewerProtocolPolicy.md) |  | 
**allowedMethods** | [**AllowedMethods**](AllowedMethods.md) |  | [optional] 
**smoothStreaming** | **Boolean** |  | [optional] 
**compress** | **Boolean** |  | [optional] 
**lambdaFunctionAssociations** | [**DefaultCacheBehaviorLambdaFunctionAssociations**](DefaultCacheBehaviorLambdaFunctionAssociations.md) |  | [optional] 
**functionAssociations** | [**DefaultCacheBehaviorFunctionAssociations**](DefaultCacheBehaviorFunctionAssociations.md) |  | [optional] 
**fieldLevelEncryptionId** | **String** |  | [optional] 
**realtimeLogConfigArn** | **String** |  | [optional] 
**cachePolicyId** | **String** |  | [optional] 
**originRequestPolicyId** | **String** |  | [optional] 
**responseHeadersPolicyId** | **String** |  | [optional] 
**forwardedValues** | [**CacheBehaviorForwardedValues**](CacheBehaviorForwardedValues.md) |  | [optional] 
**minTTL** | **Number** |  | [optional] 
**defaultTTL** | **Number** |  | [optional] 
**maxTTL** | **Number** |  | [optional] 


