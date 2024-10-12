# SecurityCenter.IoTSecurityAggregatedRecommendationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the incident and what it means | [optional] [readonly] 
**detectedBy** | **String** | Name of the vendor that discovered the issue | [optional] [readonly] 
**healthyDevices** | **Number** | the number of the healthy devices within the solution | [optional] [readonly] 
**logAnalyticsQuery** | **String** | query in log analytics to get the list of affected devices/alerts | [optional] [readonly] 
**recommendationDisplayName** | **String** | Display name of the recommendation type. | [optional] [readonly] 
**recommendationName** | **String** | Name of the recommendation | [optional] 
**recommendationTypeId** | **String** | The recommendation-type GUID. | [optional] [readonly] 
**remediationSteps** | **String** | Recommended steps for remediation | [optional] [readonly] 
**reportedSeverity** | **String** | Estimated severity of this recommendation | [optional] [readonly] 
**unhealthyDeviceCount** | **Number** | the number of the unhealthy devices within the solution | [optional] [readonly] 



## Enum: ReportedSeverityEnum


* `Informational` (value: `"Informational"`)

* `Low` (value: `"Low"`)

* `Medium` (value: `"Medium"`)

* `High` (value: `"High"`)




