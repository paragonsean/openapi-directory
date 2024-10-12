

# Essentials

This object contains consistent fields across different monitor services.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertRule** | **String** | Rule(monitor) which fired alert instance. Depending on the monitor service,  this would be ARM id or name of the rule. |  [optional] [readonly] |
|**alertState** | [**AlertStateEnum**](#AlertStateEnum) | Alert object state, which can be modified by the user. |  [optional] [readonly] |
|**lastModifiedDateTime** | **OffsetDateTime** | Last modification time(ISO-8601 format) of alert instance. |  [optional] [readonly] |
|**lastModifiedUserName** | **String** | User who last modified the alert, in case of monitor service updates user would be &#39;system&#39;, otherwise name of the user. |  [optional] [readonly] |
|**monitorCondition** | [**MonitorConditionEnum**](#MonitorConditionEnum) | Can be &#39;Fired&#39; or &#39;Resolved&#39;, which represents whether the underlying conditions have crossed the defined alert rule thresholds. |  [optional] [readonly] |
|**monitorConditionResolvedDateTime** | **OffsetDateTime** | Resolved time(ISO-8601 format) of alert instance. This will be updated when monitor service resolves the alert instance because the rule condition is no longer met. |  [optional] [readonly] |
|**monitorService** | [**MonitorServiceEnum**](#MonitorServiceEnum) | Monitor service on which the rule(monitor) is set. |  [optional] [readonly] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of alert Sev0 being highest and Sev4 being lowest. |  [optional] [readonly] |
|**signalType** | [**SignalTypeEnum**](#SignalTypeEnum) | The type of signal the alert is based on, which could be metrics, logs or activity logs. |  [optional] [readonly] |
|**smartGroupId** | **String** | Unique Id of the smart group |  [optional] [readonly] |
|**smartGroupingReason** | **String** | Verbose reason describing the reason why this alert instance is added to a smart group |  [optional] [readonly] |
|**sourceCreatedId** | **String** | Unique Id created by monitor service for each alert instance. This could be used to track the issue at the monitor service, in case of Nagios, Zabbix, SCOM etc. |  [optional] [readonly] |
|**startDateTime** | **OffsetDateTime** | Creation time(ISO-8601 format) of alert instance. |  [optional] [readonly] |
|**targetResource** | **String** | Target ARM resource, on which alert got created. |  [optional] |
|**targetResourceGroup** | **String** | Resource group of target ARM resource, on which alert got created. |  [optional] |
|**targetResourceName** | **String** | Name of the target ARM resource name, on which alert got created. |  [optional] |
|**targetResourceType** | **String** | Resource type of target ARM resource, on which alert got created. |  [optional] |



## Enum: AlertStateEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| ACKNOWLEDGED | &quot;Acknowledged&quot; |
| CLOSED | &quot;Closed&quot; |



## Enum: MonitorConditionEnum

| Name | Value |
|---- | -----|
| FIRED | &quot;Fired&quot; |
| RESOLVED | &quot;Resolved&quot; |



## Enum: MonitorServiceEnum

| Name | Value |
|---- | -----|
| APPLICATION_INSIGHTS | &quot;Application Insights&quot; |
| ACTIVITY_LOG_ADMINISTRATIVE | &quot;ActivityLog Administrative&quot; |
| ACTIVITY_LOG_SECURITY | &quot;ActivityLog Security&quot; |
| ACTIVITY_LOG_RECOMMENDATION | &quot;ActivityLog Recommendation&quot; |
| ACTIVITY_LOG_POLICY | &quot;ActivityLog Policy&quot; |
| ACTIVITY_LOG_AUTOSCALE | &quot;ActivityLog Autoscale&quot; |
| LOG_ANALYTICS | &quot;Log Analytics&quot; |
| NAGIOS | &quot;Nagios&quot; |
| PLATFORM | &quot;Platform&quot; |
| SCOM | &quot;SCOM&quot; |
| SERVICE_HEALTH | &quot;ServiceHealth&quot; |
| SMART_DETECTOR | &quot;SmartDetector&quot; |
| VM_INSIGHTS | &quot;VM Insights&quot; |
| ZABBIX | &quot;Zabbix&quot; |
| RESOURCE_HEALTH | &quot;Resource Health&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEV0 | &quot;Sev0&quot; |
| SEV1 | &quot;Sev1&quot; |
| SEV2 | &quot;Sev2&quot; |
| SEV3 | &quot;Sev3&quot; |
| SEV4 | &quot;Sev4&quot; |



## Enum: SignalTypeEnum

| Name | Value |
|---- | -----|
| METRIC | &quot;Metric&quot; |
| LOG | &quot;Log&quot; |
| UNKNOWN | &quot;Unknown&quot; |



