

# Service

<p>Describes an App Runner service. It can describe a service in any state, including deleted services.</p> <p>This type contains the full information about a service, including configuration details. It's returned by the <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html\">CreateService</a>, <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeService.html\">DescribeService</a>, and <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteService.html\">DeleteService</a> actions. A subset of this information is returned by the <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_ListServices.html\">ListServices</a> action using the <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_ServiceSummary.html\">ServiceSummary</a> type.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceName** | [**String**](String.md) |  |  |
|**serviceId** | [**String**](String.md) |  |  |
|**serviceArn** | [**String**](String.md) |  |  |
|**serviceUrl** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**deletedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**ServiceStatus**](ServiceStatus.md) |  |  |
|**sourceConfiguration** | [**ServiceSourceConfiguration**](ServiceSourceConfiguration.md) |  |  |
|**instanceConfiguration** | [**ServiceInstanceConfiguration**](ServiceInstanceConfiguration.md) |  |  |
|**encryptionConfiguration** | [**ServiceEncryptionConfiguration**](ServiceEncryptionConfiguration.md) |  |  [optional] |
|**healthCheckConfiguration** | [**ServiceHealthCheckConfiguration**](ServiceHealthCheckConfiguration.md) |  |  [optional] |
|**autoScalingConfigurationSummary** | [**ServiceAutoScalingConfigurationSummary**](ServiceAutoScalingConfigurationSummary.md) |  |  |
|**networkConfiguration** | [**ServiceNetworkConfiguration**](ServiceNetworkConfiguration.md) |  |  |
|**observabilityConfiguration** | [**ServiceObservabilityConfiguration**](ServiceObservabilityConfiguration.md) |  |  [optional] |



