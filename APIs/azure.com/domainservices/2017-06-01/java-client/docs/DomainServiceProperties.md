

# DomainServiceProperties

Properties of the Domain Service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainControllerIpAddress** | **List&lt;String&gt;** | List of Domain Controller IP Address |  [optional] [readonly] |
|**domainName** | **String** | The name of the Azure domain that the user would like to deploy Domain Services to. |  [optional] |
|**domainSecuritySettings** | [**DomainSecuritySettings**](DomainSecuritySettings.md) |  |  [optional] |
|**filteredSync** | [**FilteredSyncEnum**](#FilteredSyncEnum) | Enabled or Disabled flag to turn on Group-based filtered sync |  [optional] |
|**healthAlerts** | [**List&lt;HealthAlert&gt;**](HealthAlert.md) | List of Domain Health Alerts |  [optional] [readonly] |
|**healthLastEvaluated** | **OffsetDateTime** | Last domain evaluation run DateTime |  [optional] [readonly] |
|**healthMonitors** | [**List&lt;HealthMonitor&gt;**](HealthMonitor.md) | List of Domain Health Monitors |  [optional] [readonly] |
|**ldapsSettings** | [**LdapsSettings**](LdapsSettings.md) |  |  [optional] |
|**notificationSettings** | [**NotificationSettings**](NotificationSettings.md) |  |  [optional] |
|**provisioningState** | **String** | the current deployment or provisioning state, which only appears in the response. |  [optional] [readonly] |
|**serviceStatus** | **String** | Status of Domain Service instance |  [optional] [readonly] |
|**subnetId** | **String** | The name of the virtual network that Domain Services will be deployed on. The id of the subnet that Domain Services will be deployed on. /virtualNetwork/vnetName/subnets/subnetName. |  [optional] |
|**tenantId** | **String** | Azure Active Directory tenant id |  [optional] [readonly] |
|**vnetSiteId** | **String** | Virtual network site id |  [optional] [readonly] |



## Enum: FilteredSyncEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



