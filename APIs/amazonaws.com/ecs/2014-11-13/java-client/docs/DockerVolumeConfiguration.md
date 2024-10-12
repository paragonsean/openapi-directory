

# DockerVolumeConfiguration

This parameter is specified when you're using Docker volumes. Docker volumes are only supported when you're using the EC2 launch type. Windows containers only support the use of the <code>local</code> driver. To use bind mounts, specify a <code>host</code> instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scope** | [**Scope**](Scope.md) |  |  [optional] |
|**autoprovision** | [**Boolean**](Boolean.md) |  |  [optional] |
|**driver** | [**String**](String.md) |  |  [optional] |
|**driverOpts** | [**Map**](Map.md) |  |  [optional] |
|**labels** | [**Map**](Map.md) |  |  [optional] |



