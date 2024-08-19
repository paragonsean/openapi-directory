# ElasticLoadBalancing.ModifyTargetGroupInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targetGroupArn** | **String** |  | 
**healthCheckProtocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 
**healthCheckPort** | **String** |  | [optional] 
**healthCheckPath** | **String** |  | [optional] 
**healthCheckEnabled** | **Boolean** |  | [optional] 
**healthCheckIntervalSeconds** | **Number** |  | [optional] 
**healthCheckTimeoutSeconds** | **Number** |  | [optional] 
**healthyThresholdCount** | **Number** |  | [optional] 
**unhealthyThresholdCount** | **Number** |  | [optional] 
**matcher** | [**CreateTargetGroupInputMatcher**](CreateTargetGroupInputMatcher.md) |  | [optional] 


