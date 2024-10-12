# ElasticLoadBalancing.TargetGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targetGroupArn** | **String** |  | [optional] 
**targetGroupName** | **String** |  | [optional] 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 
**port** | **Number** |  | [optional] 
**vpcId** | **String** |  | [optional] 
**healthCheckProtocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 
**healthCheckPort** | **String** |  | [optional] 
**healthCheckEnabled** | **Boolean** |  | [optional] 
**healthCheckIntervalSeconds** | **Number** |  | [optional] 
**healthCheckTimeoutSeconds** | **Number** |  | [optional] 
**healthyThresholdCount** | **Number** |  | [optional] 
**unhealthyThresholdCount** | **Number** |  | [optional] 
**healthCheckPath** | **String** |  | [optional] 
**matcher** | [**TargetGroupMatcher**](TargetGroupMatcher.md) |  | [optional] 
**loadBalancerArns** | **Array** |  | [optional] 
**targetType** | [**TargetTypeEnum**](TargetTypeEnum.md) |  | [optional] 
**protocolVersion** | **String** |  | [optional] 
**ipAddressType** | [**TargetGroupIpAddressTypeEnum**](TargetGroupIpAddressTypeEnum.md) |  | [optional] 


