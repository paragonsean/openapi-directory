# SecurityCenter.IoTSecurityAggregatedAlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionTaken** | **String** | The action that was taken as a response to the alert (Active, Blocked etc.) | [optional] [readonly] 
**aggregatedDateUtc** | **Date** | The date the incidents were detected by the vendor | [optional] [readonly] 
**alertDisplayName** | **String** | Display name of the alert type | [optional] [readonly] 
**alertType** | **String** | Name of the alert type | [optional] [readonly] 
**count** | **Number** | Occurrence number of the alert within the aggregated date | [optional] [readonly] 
**description** | **String** | Description of the incident and what it means | [optional] [readonly] 
**effectedResourceType** | **String** | Azure resource ID of the resource that got the alerts | [optional] [readonly] 
**logAnalyticsQuery** | **String** | query in log analytics to get the list of affected devices/alerts | [optional] [readonly] 
**remediationSteps** | **String** | Recommended steps for remediation | [optional] [readonly] 
**reportedSeverity** | **String** | Estimated severity of this alert | [optional] [readonly] 
**systemSource** | **String** | The type of the alerted resource (Azure, Non-Azure) | [optional] [readonly] 
**vendorName** | **String** | Name of the vendor that discovered the incident | [optional] [readonly] 



## Enum: ReportedSeverityEnum


* `Informational` (value: `"Informational"`)

* `Low` (value: `"Low"`)

* `Medium` (value: `"Medium"`)

* `High` (value: `"High"`)




