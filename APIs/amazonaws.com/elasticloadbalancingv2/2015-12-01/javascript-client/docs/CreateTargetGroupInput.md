# ElasticLoadBalancing.CreateTargetGroupInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 
**protocolVersion** | **String** |  | [optional] 
**port** | **Number** |  | [optional] 
**vpcId** | **String** |  | [optional] 
**healthCheckProtocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 
**healthCheckPort** | **String** |  | [optional] 
**healthCheckEnabled** | **Boolean** |  | [optional] 
**healthCheckPath** | **String** |  | [optional] 
**healthCheckIntervalSeconds** | **Number** |  | [optional] 
**healthCheckTimeoutSeconds** | **Number** |  | [optional] 
**healthyThresholdCount** | **Number** |  | [optional] 
**unhealthyThresholdCount** | **Number** |  | [optional] 
**matcher** | [**CreateTargetGroupInputMatcher**](CreateTargetGroupInputMatcher.md) |  | [optional] 
**targetType** | [**TargetTypeEnum**](TargetTypeEnum.md) |  | [optional] 
**tags** | **Array** |  | [optional] 
**ipAddressType** | [**TargetGroupIpAddressTypeEnum**](TargetGroupIpAddressTypeEnum.md) |  | [optional] 


