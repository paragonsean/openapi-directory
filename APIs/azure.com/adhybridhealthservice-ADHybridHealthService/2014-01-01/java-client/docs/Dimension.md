

# Dimension

The connector object error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeAlerts** | **Integer** | The count of alerts that are currently active for the service. |  [optional] |
|**additionalInformation** | **String** | The additional information related to the service. |  [optional] |
|**displayName** | **String** | The display name of the service. |  [optional] |
|**health** | [**HealthEnum**](#HealthEnum) | The health status for the domain controller. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The date or time , in UTC, when the service properties were last updated. |  [optional] |
|**resolvedAlerts** | **Integer** | The total count of alerts that has been resolved for the service. |  [optional] |
|**signature** | **String** | The signature of the service. |  [optional] |
|**simpleProperties** | **Object** | List of service specific configuration properties. |  [optional] |
|**type** | **String** | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |  [optional] |



## Enum: HealthEnum

| Name | Value |
|---- | -----|
| HEALTHY | &quot;Healthy&quot; |
| WARNING | &quot;Warning&quot; |
| ERROR | &quot;Error&quot; |
| NOT_MONITORED | &quot;NotMonitored&quot; |
| MISSING | &quot;Missing&quot; |



