

# AlertProperties

An alert created in alert management service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertState** | [**AlertStateEnum**](#AlertStateEnum) | Alert object state |  [optional] [readonly] |
|**lastModifiedDateTime** | **OffsetDateTime** | Last modification time(ISO-8601 format). |  [optional] [readonly] |
|**lastModifiedUserName** | **String** | User who last modified the alert. |  [optional] [readonly] |
|**monitorCondition** | [**MonitorConditionEnum**](#MonitorConditionEnum) | Condition of the rule at the monitor service |  [optional] [readonly] |
|**monitorService** | [**MonitorServiceEnum**](#MonitorServiceEnum) | Monitor service which is the source of the alert object. |  [optional] [readonly] |
|**payload** | **Object** | More details which are contextual to the monitor service. |  [optional] [readonly] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Severity of alert Sev1 being highest and Sev3 being lowest. |  [optional] [readonly] |
|**signalType** | [**SignalTypeEnum**](#SignalTypeEnum) | Log based alert or metric based alert |  [optional] [readonly] |
|**smartGroupId** | **String** | Unique Id of the smart group |  [optional] [readonly] |
|**smartGroupingReason** | **String** | Reason for addition to a smart group |  [optional] [readonly] |
|**sourceCreatedId** | **String** | Unique Id created by monitor service |  [optional] [readonly] |
|**startDateTime** | **OffsetDateTime** | Creation time(ISO-8601 format). |  [optional] [readonly] |
|**targetResource** | **String** | Target ARM resource, on which alert got created. |  [optional] |
|**targetResourceGroup** | **String** | Resource group of target ARM resource. |  [optional] |
|**targetResourceName** | **String** | Target ARM resource name, on which alert got created. |  [optional] |
|**targetResourceType** | **String** | Resource type of target ARM resource |  [optional] |



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
| PLATFORM | &quot;Platform&quot; |
| APPLICATION_INSIGHTS | &quot;Application Insights&quot; |
| LOG_ANALYTICS | &quot;Log Analytics&quot; |
| INFRASTRUCTURE_INSIGHTS | &quot;Infrastructure Insights&quot; |
| ACTIVITY_LOG_ADMINISTRATIVE | &quot;ActivityLog Administrative&quot; |
| ACTIVITY_LOG_SECURITY | &quot;ActivityLog Security&quot; |
| ACTIVITY_LOG_RECOMMENDATION | &quot;ActivityLog Recommendation&quot; |
| ACTIVITY_LOG_POLICY | &quot;ActivityLog Policy&quot; |
| ACTIVITY_LOG_AUTOSCALE | &quot;ActivityLog Autoscale&quot; |
| SERVICE_HEALTH | &quot;ServiceHealth&quot; |
| SMART_DETECTOR | &quot;SmartDetector&quot; |
| ZABBIX | &quot;Zabbix&quot; |
| SCOM | &quot;SCOM&quot; |
| NAGIOS | &quot;Nagios&quot; |



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



