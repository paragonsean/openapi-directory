# MonitorManagementClient.MetricAlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[MetricAlertAction]**](MetricAlertAction.md) | the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved. | [optional] 
**autoMitigate** | **Boolean** | the flag that indicates whether the alert should be auto resolved or not. | [optional] 
**criteria** | [**MetricAlertCriteria**](MetricAlertCriteria.md) |  | 
**description** | **String** | the description of the metric alert that will be included in the alert email. | 
**enabled** | **Boolean** | the flag that indicates whether the metric alert is enabled. | 
**evaluationFrequency** | **String** | how often the metric alert is evaluated represented in ISO 8601 duration format. | 
**lastUpdatedTime** | **Date** | Last time the rule was updated in ISO8601 format. | [optional] [readonly] 
**scopes** | **[String]** | the list of resource id&#39;s that this metric alert is scoped to. | [optional] 
**severity** | **Number** | Alert severity {0, 1, 2, 3, 4} | 
**targetResourceRegion** | **String** | the region of the target resource(s) on which the alert is created/updated. Mandatory for MultipleResourceMultipleMetricCriteria. | [optional] 
**targetResourceType** | **String** | the resource type of the target resource(s) on which the alert is created/updated. Mandatory for MultipleResourceMultipleMetricCriteria. | [optional] 
**windowSize** | **String** | the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. | 


