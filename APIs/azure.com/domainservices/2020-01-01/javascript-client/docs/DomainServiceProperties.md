# DomainServicesResourceProvider.DomainServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentId** | **String** | Deployment Id | [optional] [readonly] 
**domainName** | **String** | The name of the Azure domain that the user would like to deploy Domain Services to. | [optional] 
**domainSecuritySettings** | [**DomainSecuritySettings**](DomainSecuritySettings.md) |  | [optional] 
**filteredSync** | **String** | Enabled or Disabled flag to turn on Group-based filtered sync | [optional] 
**ldapsSettings** | [**LdapsSettings**](LdapsSettings.md) |  | [optional] 
**notificationSettings** | [**NotificationSettings**](NotificationSettings.md) |  | [optional] 
**provisioningState** | **String** | the current deployment or provisioning state, which only appears in the response. | [optional] [readonly] 
**replicaSets** | [**[ReplicaSet]**](ReplicaSet.md) | List of ReplicaSets | [optional] 
**syncOwner** | **String** | SyncOwner ReplicaSet Id | [optional] [readonly] 
**tenantId** | **String** | Azure Active Directory Tenant Id | [optional] [readonly] 
**version** | **Number** | Data Model Version | [optional] [readonly] 



## Enum: FilteredSyncEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




