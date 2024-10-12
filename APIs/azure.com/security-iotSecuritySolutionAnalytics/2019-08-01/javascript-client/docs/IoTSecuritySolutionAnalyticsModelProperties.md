# SecurityCenter.IoTSecuritySolutionAnalyticsModelProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devicesMetrics** | [**[IoTSecuritySolutionAnalyticsModelPropertiesDevicesMetricsInner]**](IoTSecuritySolutionAnalyticsModelPropertiesDevicesMetricsInner.md) | List of device metrics by the aggregation date. | [optional] [readonly] 
**metrics** | [**IoTSeverityMetrics**](IoTSeverityMetrics.md) |  | [optional] 
**mostPrevalentDeviceAlerts** | [**[IoTSecurityDeviceAlert]**](IoTSecurityDeviceAlert.md) | List of alerts with the count of raised alerts | [optional] 
**mostPrevalentDeviceRecommendations** | [**[IoTSecurityDeviceRecommendation]**](IoTSecurityDeviceRecommendation.md) | List of aggregated recommendation data, per recommendation type, per device. | [optional] 
**topAlertedDevices** | [**[IoTSecurityAlertedDevice]**](IoTSecurityAlertedDevice.md) | List of devices with open alerts including the count of alerts per device. | [optional] 
**unhealthyDeviceCount** | **Number** | Number of unhealthy devices within your IoT Security solution. | [optional] [readonly] 


