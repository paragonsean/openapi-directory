# AzureAlertsManagementServiceResourceProvider.Essentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertRule** | **String** | Rule(monitor) which fired alert instance. Depending on the monitor service,  this would be ARM id or name of the rule. | [optional] [readonly] 
**alertState** | **String** | Alert object state, which can be modified by the user. | [optional] [readonly] 
**lastModifiedDateTime** | **Date** | Last modification time(ISO-8601 format) of alert instance. | [optional] [readonly] 
**lastModifiedUserName** | **String** | User who last modified the alert, in case of monitor service updates user would be &#39;system&#39;, otherwise name of the user. | [optional] [readonly] 
**monitorCondition** | **String** | Condition of the rule at the monitor service. It represents whether the underlying conditions have crossed the defined alert rule thresholds. | [optional] [readonly] 
**monitorConditionResolvedDateTime** | **Date** | Resolved time(ISO-8601 format) of alert instance. This will be updated when monitor service resolves the alert instance because the rule condition is no longer met. | [optional] [readonly] 
**monitorService** | **String** | Monitor service on which the rule(monitor) is set. | [optional] [readonly] 
**severity** | **String** | Severity of alert Sev0 being highest and Sev4 being lowest. | [optional] [readonly] 
**signalType** | **String** | The type of signal the alert is based on, which could be metrics, logs or activity logs. | [optional] [readonly] 
**smartGroupId** | **String** | Unique Id of the smart group | [optional] [readonly] 
**smartGroupingReason** | **String** | Verbose reason describing the reason why this alert instance is added to a smart group | [optional] [readonly] 
**sourceCreatedId** | **String** | Unique Id created by monitor service for each alert instance. This could be used to track the issue at the monitor service, in case of Nagios, Zabbix, SCOM etc. | [optional] [readonly] 
**startDateTime** | **Date** | Creation time(ISO-8601 format) of alert instance. | [optional] [readonly] 
**targetResource** | **String** | Target ARM resource, on which alert got created. | [optional] 
**targetResourceGroup** | **String** | Resource group of target ARM resource, on which alert got created. | [optional] 
**targetResourceName** | **String** | Name of the target ARM resource name, on which alert got created. | [optional] 
**targetResourceType** | **String** | Resource type of target ARM resource, on which alert got created. | [optional] 



## Enum: AlertStateEnum


* `New` (value: `"New"`)

* `Acknowledged` (value: `"Acknowledged"`)

* `Closed` (value: `"Closed"`)





## Enum: MonitorConditionEnum


* `Fired` (value: `"Fired"`)

* `Resolved` (value: `"Resolved"`)





## Enum: MonitorServiceEnum


* `Application Insights` (value: `"Application Insights"`)

* `ActivityLog Administrative` (value: `"ActivityLog Administrative"`)

* `ActivityLog Security` (value: `"ActivityLog Security"`)

* `ActivityLog Recommendation` (value: `"ActivityLog Recommendation"`)

* `ActivityLog Policy` (value: `"ActivityLog Policy"`)

* `ActivityLog Autoscale` (value: `"ActivityLog Autoscale"`)

* `Log Analytics` (value: `"Log Analytics"`)

* `Nagios` (value: `"Nagios"`)

* `Platform` (value: `"Platform"`)

* `SCOM` (value: `"SCOM"`)

* `ServiceHealth` (value: `"ServiceHealth"`)

* `SmartDetector` (value: `"SmartDetector"`)

* `VM Insights` (value: `"VM Insights"`)

* `Zabbix` (value: `"Zabbix"`)





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




