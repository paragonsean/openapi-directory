

# HealthCheckConfig

The health check configuration of a target group. Health check configurations aren't used for <code>LAMBDA</code> and <code>ALB</code> target groups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**healthCheckIntervalSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**healthCheckTimeoutSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**healthyThresholdCount** | [**Integer**](Integer.md) |  |  [optional] |
|**matcher** | [**UpdateTargetGroupRequestHealthCheckMatcher**](UpdateTargetGroupRequestHealthCheckMatcher.md) |  |  [optional] |
|**path** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**protocol** | [**TargetGroupProtocol**](TargetGroupProtocol.md) |  |  [optional] |
|**protocolVersion** | [**HealthCheckProtocolVersion**](HealthCheckProtocolVersion.md) |  |  [optional] |
|**unhealthyThresholdCount** | [**Integer**](Integer.md) |  |  [optional] |



