

# IoTSecuritySolutionAnalyticsModelProperties

Security analytics properties of your IoT Security solution

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devicesMetrics** | [**List&lt;IoTSecuritySolutionAnalyticsModelPropertiesDevicesMetricsInner&gt;**](IoTSecuritySolutionAnalyticsModelPropertiesDevicesMetricsInner.md) | List of device metrics by the aggregation date. |  [optional] [readonly] |
|**metrics** | [**IoTSeverityMetrics**](IoTSeverityMetrics.md) |  |  [optional] |
|**mostPrevalentDeviceAlerts** | [**List&lt;IoTSecurityDeviceAlert&gt;**](IoTSecurityDeviceAlert.md) | List of alerts with the count of raised alerts |  [optional] |
|**mostPrevalentDeviceRecommendations** | [**List&lt;IoTSecurityDeviceRecommendation&gt;**](IoTSecurityDeviceRecommendation.md) | List of aggregated recommendation data, per recommendation type, per device. |  [optional] |
|**topAlertedDevices** | [**List&lt;IoTSecurityAlertedDevice&gt;**](IoTSecurityAlertedDevice.md) | List of devices with open alerts including the count of alerts per device. |  [optional] |
|**unhealthyDeviceCount** | **Integer** | Number of unhealthy devices within your IoT Security solution. |  [optional] [readonly] |



