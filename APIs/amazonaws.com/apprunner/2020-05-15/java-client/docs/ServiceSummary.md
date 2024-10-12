

# ServiceSummary

<p>Provides summary information for an App Runner service.</p> <p>This type contains limited information about a service. It doesn't include configuration details. It's returned by the <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_ListServices.html\">ListServices</a> action. Complete service information is returned by the <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_CreateService.html\">CreateService</a>, <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_DescribeService.html\">DescribeService</a>, and <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_DeleteService.html\">DeleteService</a> actions using the <a href=\"https://docs.aws.amazon.com/apprunner/latest/api/API_Service.html\">Service</a> type.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceName** | [**String**](String.md) |  |  [optional] |
|**serviceId** | [**String**](String.md) |  |  [optional] |
|**serviceArn** | [**String**](String.md) |  |  [optional] |
|**serviceUrl** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**ServiceStatus**](ServiceStatus.md) |  |  [optional] |



