

# CreateTargetGroupInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  |  [optional] |
|**protocolVersion** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**vpcId** | [**String**](String.md) |  |  [optional] |
|**healthCheckProtocol** | [**ProtocolEnum**](ProtocolEnum.md) |  |  [optional] |
|**healthCheckPort** | [**String**](String.md) |  |  [optional] |
|**healthCheckEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**healthCheckPath** | [**String**](String.md) |  |  [optional] |
|**healthCheckIntervalSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**healthCheckTimeoutSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**healthyThresholdCount** | [**Integer**](Integer.md) |  |  [optional] |
|**unhealthyThresholdCount** | [**Integer**](Integer.md) |  |  [optional] |
|**matcher** | [**CreateTargetGroupInputMatcher**](CreateTargetGroupInputMatcher.md) |  |  [optional] |
|**targetType** | [**TargetTypeEnum**](TargetTypeEnum.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**ipAddressType** | [**TargetGroupIpAddressTypeEnum**](TargetGroupIpAddressTypeEnum.md) |  |  [optional] |



