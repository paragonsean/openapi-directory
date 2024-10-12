# AzureAlertsManagementServiceResourceProvider.AlertProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertState** | **String** | Alert object state | [optional] [readonly] 
**lastModifiedDateTime** | **Date** | Last modification time(ISO-8601 format). | [optional] [readonly] 
**lastModifiedUserName** | **String** | User who last modified the alert. | [optional] [readonly] 
**monitorCondition** | **String** | Condition of the rule at the monitor service | [optional] [readonly] 
**monitorService** | **String** | Monitor service which is the source of the alert object. | [optional] [readonly] 
**payload** | **Object** | More details which are contextual to the monitor service. | [optional] [readonly] 
**severity** | **String** | Severity of alert Sev1 being highest and Sev3 being lowest. | [optional] [readonly] 
**signalType** | **String** | Log based alert or metric based alert | [optional] [readonly] 
**smartGroupId** | **String** | Unique Id of the smart group | [optional] [readonly] 
**smartGroupingReason** | **String** | Reason for addition to a smart group | [optional] [readonly] 
**sourceCreatedId** | **String** | Unique Id created by monitor service | [optional] [readonly] 
**startDateTime** | **Date** | Creation time(ISO-8601 format). | [optional] [readonly] 
**targetResource** | **String** | Target ARM resource, on which alert got created. | [optional] 
**targetResourceGroup** | **String** | Resource group of target ARM resource. | [optional] 
**targetResourceName** | **String** | Target ARM resource name, on which alert got created. | [optional] 
**targetResourceType** | **String** | Resource type of target ARM resource | [optional] 



## Enum: AlertStateEnum


* `New` (value: `"New"`)

* `Acknowledged` (value: `"Acknowledged"`)

* `Closed` (value: `"Closed"`)





## Enum: MonitorConditionEnum


* `Fired` (value: `"Fired"`)

* `Resolved` (value: `"Resolved"`)





## Enum: MonitorServiceEnum


* `Platform` (value: `"Platform"`)

* `Application Insights` (value: `"Application Insights"`)

* `Log Analytics` (value: `"Log Analytics"`)

* `Infrastructure Insights` (value: `"Infrastructure Insights"`)

* `ActivityLog Administrative` (value: `"ActivityLog Administrative"`)

* `ActivityLog Security` (value: `"ActivityLog Security"`)

* `ActivityLog Recommendation` (value: `"ActivityLog Recommendation"`)

* `ActivityLog Policy` (value: `"ActivityLog Policy"`)

* `ActivityLog Autoscale` (value: `"ActivityLog Autoscale"`)

* `ServiceHealth` (value: `"ServiceHealth"`)

* `SmartDetector` (value: `"SmartDetector"`)

* `Zabbix` (value: `"Zabbix"`)

* `SCOM` (value: `"SCOM"`)

* `Nagios` (value: `"Nagios"`)





## Enum: SeverityEnum


* `Sev0` (value: `"Sev0"`)

* `Sev1` (value: `"Sev1"`)

* `Sev2` (value: `"Sev2"`)

* `Sev3` (value: `"Sev3"`)

* `Sev4` (value: `"Sev4"`)





## Enum: SignalTypeEnum


* `Metric` (value: `"Metric"`)

* `Log` (value: `"Log"`)

* `Unknown` (value: `"Unknown"`)




