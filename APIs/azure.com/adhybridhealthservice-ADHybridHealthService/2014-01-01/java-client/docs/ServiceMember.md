

# ServiceMember

The server properties for a given service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeAlerts** | **Integer** | The total number of alerts that are currently active for the server. |  [optional] |
|**additionalInformation** | **String** | The additional information, if any, for the server. |  [optional] |
|**createdDate** | **OffsetDateTime** | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |  [optional] |
|**dimensions** | **Object** | The server specific configuration related dimensions. |  [optional] |
|**disabled** | **Boolean** | Indicates if the server is disabled or not.  |  [optional] |
|**disabledReason** | **Integer** | The reason for disabling the server. |  [optional] |
|**installedQfes** | **Object** | The list of installed QFEs for the server. |  [optional] |
|**lastDisabled** | **OffsetDateTime** | The date and time , in UTC, when the server was last disabled. |  [optional] |
|**lastReboot** | **OffsetDateTime** | The date and time, in UTC, when the server was last rebooted. |  [optional] |
|**lastServerReportedMonitoringLevelChange** | **OffsetDateTime** | The date and time, in UTC, when the server&#39;s data monitoring configuration was last changed. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The date and time, in UTC, when the server properties were last updated. |  [optional] |
|**machineId** | **String** | The id of the machine. |  [optional] |
|**machineName** | **String** | The name of the server. |  [optional] |
|**monitoringConfigurationsComputed** | **Object** | The monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |  [optional] |
|**monitoringConfigurationsCustomized** | **Object** | The customized monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |  [optional] |
|**osName** | **String** | The name of the operating system installed in the machine. |  [optional] |
|**osVersion** | **String** | The version of the operating system installed in the machine. |  [optional] |
|**properties** | **Object** | Server specific properties. |  [optional] |
|**recommendedQfes** | **Object** | The list of recommended hotfixes for the server. |  [optional] |
|**resolvedAlerts** | **Integer** | The total count of alerts that are resolved for this server. |  [optional] |
|**role** | **String** | The service role that is being monitored in the server. |  [optional] |
|**serverReportedMonitoringLevel** | [**ServerReportedMonitoringLevelEnum**](#ServerReportedMonitoringLevelEnum) | The monitoring level reported by the server. |  [optional] |
|**serviceId** | **String** | The service id to whom this server belongs. |  [optional] |
|**serviceMemberId** | **String** | The id of the server. |  [optional] |
|**status** | **String** | The health status of the server. |  [optional] |
|**tenantId** | **String** | The tenant id to whom this server belongs. |  [optional] |



## Enum: ServerReportedMonitoringLevelEnum

| Name | Value |
|---- | -----|
| PARTIAL | &quot;Partial&quot; |
| FULL | &quot;Full&quot; |
| OFF | &quot;Off&quot; |



