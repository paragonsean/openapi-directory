# SecurityCenter.IoTSecurityAggregatedAlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionTaken** | **String** | IoT Security solution alert response. | [optional] [readonly] 
**aggregatedDateUtc** | **Date** | Date of detection. | [optional] [readonly] 
**alertDisplayName** | **String** | Display name of the alert type. | [optional] [readonly] 
**alertType** | **String** | Name of the alert type. | [optional] [readonly] 
**count** | **Number** | Number of alerts occurrences within the aggregated time window. | [optional] [readonly] 
**description** | **String** | Description of the suspected vulnerability and meaning. | [optional] [readonly] 
**effectedResourceType** | **String** | Azure resource ID of the resource that received the alerts. | [optional] [readonly] 
**logAnalyticsQuery** | **String** | Log analytics query for getting the list of affected devices/alerts. | [optional] [readonly] 
**remediationSteps** | **String** | Recommended steps for remediation. | [optional] [readonly] 
**reportedSeverity** | **String** | Assessed alert severity. | [optional] [readonly] 
**systemSource** | **String** | The type of the alerted resource (Azure, Non-Azure). | [optional] [readonly] 
**topDevicesList** | [**[IoTSecurityAggregatedAlertPropertiesTopDevicesListInner]**](IoTSecurityAggregatedAlertPropertiesTopDevicesListInner.md) | 10 devices with the highest number of occurrences of this alert type, on this day. | [optional] [readonly] 
**vendorName** | **String** | Name of the organization that raised the alert. | [optional] [readonly] 



## Enum: ReportedSeverityEnum


* `Informational` (value: `"Informational"`)

* `Low` (value: `"Low"`)

* `Medium` (value: `"Medium"`)

* `High` (value: `"High"`)




