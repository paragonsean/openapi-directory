

# AddsServiceMember

The server details for ADDS service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeAlerts** | **Integer** | The total number of alerts that are currently active for the server. |  [optional] |
|**additionalInformation** | **String** | The additional information, if any, for the server. |  [optional] |
|**addsRoles** | **List&lt;String&gt;** | The list of ADDS roles. |  [optional] |
|**createdDate** | **OffsetDateTime** | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |  [optional] |
|**dcTypes** | **List&lt;String&gt;** | The list of domain controller types. |  [optional] |
|**dimensions** | [**List&lt;Item&gt;**](Item.md) | The server specific configuration related dimensions. |  [optional] |
|**disabled** | **Boolean** | Indicates if the server is disabled or not.  |  [optional] |
|**disabledReason** | **Integer** | The reason for disabling the server. |  [optional] |
|**domainName** | **String** | The domain name. |  [optional] |
|**gcReachable** | **Boolean** | Indicates if the global catalog for this domain is reachable or not. |  [optional] |
|**installedQfes** | [**List&lt;Hotfix&gt;**](Hotfix.md) | The list of installed QFEs for the server. |  [optional] |
|**isAdvertising** | **Boolean** | Indicates if the Dc is advertising or not. |  [optional] |
|**lastDisabled** | **OffsetDateTime** | The date and time , in UTC, when the server was last disabled. |  [optional] |
|**lastReboot** | **OffsetDateTime** | The date and time, in UTC, when the server was last rebooted. |  [optional] |
|**lastServerReportedMonitoringLevelChange** | **OffsetDateTime** | The date and time, in UTC, when the server&#39;s data monitoring configuration was last changed. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The date and time, in UTC, when the server properties were last updated. |  [optional] |
|**machineId** | **String** | The id of the machine. |  [optional] |
|**machineName** | **String** | The name of the server. |  [optional] |
|**monitoringConfigurationsComputed** | [**List&lt;Item&gt;**](Item.md) | The monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |  [optional] |
|**monitoringConfigurationsCustomized** | [**List&lt;Item&gt;**](Item.md) | The customized monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |  [optional] |
|**osName** | **String** | The name of the operating system installed in the machine. |  [optional] |
|**osVersion** | **String** | The version of the operating system installed in the machine. |  [optional] |
|**pdcReachable** | **Boolean** | Indicates if the primary domain controller is reachable or not. |  [optional] |
|**properties** | [**List&lt;Item&gt;**](Item.md) | Server specific properties. |  [optional] |
|**recommendedQfes** | [**List&lt;Hotfix&gt;**](Hotfix.md) | The list of recommended hotfixes for the server. |  [optional] |
|**resolvedAlerts** | **Integer** | The total count of alerts that are resolved for this server. |  [optional] |
|**role** | **String** | The service role that is being monitored in the server. |  [optional] |
|**serverReportedMonitoringLevel** | [**ServerReportedMonitoringLevelEnum**](#ServerReportedMonitoringLevelEnum) | The monitoring level reported by the server. |  [optional] |
|**serviceId** | **String** | The service id to whom this server belongs. |  [optional] |
|**serviceMemberId** | **String** | The id of the server. |  [optional] |
|**siteName** | **String** | The site name. |  [optional] |
|**status** | **String** | The health status of the server. |  [optional] |
|**sysvolState** | **Boolean** | Indicates if the SYSVOL state is healthy or not. |  [optional] |
|**tenantId** | **String** | The tenant id to whom this server belongs. |  [optional] |



## Enum: ServerReportedMonitoringLevelEnum

| Name | Value |
|---- | -----|
| PARTIAL | &quot;Partial&quot; |
| FULL | &quot;Full&quot; |
| OFF | &quot;Off&quot; |



