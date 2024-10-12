# DomainServicesResourceProvider.DomainServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainControllerIpAddress** | **[String]** | List of Domain Controller IP Address | [optional] [readonly] 
**domainName** | **String** | The name of the Azure domain that the user would like to deploy Domain Services to. | [optional] 
**domainSecuritySettings** | [**DomainSecuritySettings**](DomainSecuritySettings.md) |  | [optional] 
**filteredSync** | **String** | Enabled or Disabled flag to turn on Group-based filtered sync | [optional] 
**healthAlerts** | [**[HealthAlert]**](HealthAlert.md) | List of Domain Health Alerts | [optional] [readonly] 
**healthLastEvaluated** | **Date** | Last domain evaluation run DateTime | [optional] [readonly] 
**healthMonitors** | [**[HealthMonitor]**](HealthMonitor.md) | List of Domain Health Monitors | [optional] [readonly] 
**ldapsSettings** | [**LdapsSettings**](LdapsSettings.md) |  | [optional] 
**notificationSettings** | [**NotificationSettings**](NotificationSettings.md) |  | [optional] 
**provisioningState** | **String** | the current deployment or provisioning state, which only appears in the response. | [optional] [readonly] 
**serviceStatus** | **String** | Status of Domain Service instance | [optional] [readonly] 
**subnetId** | **String** | The name of the virtual network that Domain Services will be deployed on. The id of the subnet that Domain Services will be deployed on. /virtualNetwork/vnetName/subnets/subnetName. | [optional] 
**tenantId** | **String** | Azure Active Directory tenant id | [optional] [readonly] 
**vnetSiteId** | **String** | Virtual network site id | [optional] [readonly] 



## Enum: FilteredSyncEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




