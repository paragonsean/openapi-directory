# SecurityCenter.IoTSecurityAggregatedRecommendationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the suspected vulnerability and meaning. | [optional] [readonly] 
**detectedBy** | **String** | Name of the organization that made the recommendation. | [optional] [readonly] 
**healthyDevices** | **Number** | Number of healthy devices within the IoT Security solution. | [optional] [readonly] 
**logAnalyticsQuery** | **String** | Log analytics query for getting the list of affected devices/alerts. | [optional] [readonly] 
**recommendationDisplayName** | **String** | Display name of the recommendation type. | [optional] [readonly] 
**recommendationName** | **String** | Name of the recommendation. | [optional] 
**recommendationTypeId** | **String** | Recommendation-type GUID. | [optional] [readonly] 
**remediationSteps** | **String** | Recommended steps for remediation | [optional] [readonly] 
**reportedSeverity** | **String** | Assessed recommendation severity. | [optional] [readonly] 
**unhealthyDeviceCount** | **Number** | Number of unhealthy devices within the IoT Security solution. | [optional] [readonly] 



## Enum: ReportedSeverityEnum


* `Informational` (value: `"Informational"`)

* `Low` (value: `"Low"`)

* `Medium` (value: `"Medium"`)

* `High` (value: `"High"`)




