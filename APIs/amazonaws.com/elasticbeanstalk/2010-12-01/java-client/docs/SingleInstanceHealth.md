

# SingleInstanceHealth

Detailed health information about an Amazon EC2 instance in your Elastic Beanstalk environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | [**String**](String.md) |  |  [optional] |
|**healthStatus** | [**String**](String.md) |  |  [optional] |
|**color** | [**String**](String.md) |  |  [optional] |
|**causes** | [**List**](List.md) |  |  [optional] |
|**launchedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**applicationMetrics** | [**SingleInstanceHealthApplicationMetrics**](SingleInstanceHealthApplicationMetrics.md) |  |  [optional] |
|**system** | [**SingleInstanceHealthSystem**](SingleInstanceHealthSystem.md) |  |  [optional] |
|**deployment** | [**SingleInstanceHealthDeployment**](SingleInstanceHealthDeployment.md) |  |  [optional] |
|**availabilityZone** | [**String**](String.md) |  |  [optional] |
|**instanceType** | [**String**](String.md) |  |  [optional] |



