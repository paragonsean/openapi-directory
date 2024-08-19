

# TargetGroup

Information about a target group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetGroupArn** | [**String**](String.md) |  |  [optional] |
|**targetGroupName** | [**String**](String.md) |  |  [optional] |
|**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**vpcId** | [**String**](String.md) |  |  [optional] |
|**healthCheckProtocol** | [**ProtocolEnum**](ProtocolEnum.md) |  |  [optional] |
|**healthCheckPort** | [**String**](String.md) |  |  [optional] |
|**healthCheckEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**healthCheckIntervalSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**healthCheckTimeoutSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**healthyThresholdCount** | [**Integer**](Integer.md) |  |  [optional] |
|**unhealthyThresholdCount** | [**Integer**](Integer.md) |  |  [optional] |
|**healthCheckPath** | [**String**](String.md) |  |  [optional] |
|**matcher** | [**TargetGroupMatcher**](TargetGroupMatcher.md) |  |  [optional] |
|**loadBalancerArns** | [**List**](List.md) |  |  [optional] |
|**targetType** | [**TargetTypeEnum**](TargetTypeEnum.md) |  |  [optional] |
|**protocolVersion** | [**String**](String.md) |  |  [optional] |
|**ipAddressType** | [**TargetGroupIpAddressTypeEnum**](TargetGroupIpAddressTypeEnum.md) |  |  [optional] |



