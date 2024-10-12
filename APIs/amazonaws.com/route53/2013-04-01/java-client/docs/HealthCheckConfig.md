

# HealthCheckConfig

A complex type that contains information about the health check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**type** | [**HealthCheckType**](HealthCheckType.md) |  |  |
|**resourcePath** | [**String**](String.md) |  |  [optional] |
|**fullyQualifiedDomainName** | [**String**](String.md) |  |  [optional] |
|**searchString** | [**String**](String.md) |  |  [optional] |
|**requestInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**failureThreshold** | [**Integer**](Integer.md) |  |  [optional] |
|**measureLatency** | [**Boolean**](Boolean.md) |  |  [optional] |
|**inverted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**disabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**healthThreshold** | [**Integer**](Integer.md) |  |  [optional] |
|**childHealthChecks** | [**List**](List.md) |  |  [optional] |
|**enableSNI** | [**Boolean**](Boolean.md) |  |  [optional] |
|**regions** | [**List**](List.md) |  |  [optional] |
|**alarmIdentifier** | [**CreateHealthCheckRequestHealthCheckConfigAlarmIdentifier**](CreateHealthCheckRequestHealthCheckConfigAlarmIdentifier.md) |  |  [optional] |
|**insufficientDataHealthStatus** | [**InsufficientDataHealthStatus**](InsufficientDataHealthStatus.md) |  |  [optional] |
|**routingControlArn** | [**String**](String.md) |  |  [optional] |



