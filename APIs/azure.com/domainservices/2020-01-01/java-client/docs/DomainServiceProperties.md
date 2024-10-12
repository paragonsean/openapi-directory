

# DomainServiceProperties

Properties of the Domain Service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentId** | **String** | Deployment Id |  [optional] [readonly] |
|**domainName** | **String** | The name of the Azure domain that the user would like to deploy Domain Services to. |  [optional] |
|**domainSecuritySettings** | [**DomainSecuritySettings**](DomainSecuritySettings.md) |  |  [optional] |
|**filteredSync** | [**FilteredSyncEnum**](#FilteredSyncEnum) | Enabled or Disabled flag to turn on Group-based filtered sync |  [optional] |
|**ldapsSettings** | [**LdapsSettings**](LdapsSettings.md) |  |  [optional] |
|**notificationSettings** | [**NotificationSettings**](NotificationSettings.md) |  |  [optional] |
|**provisioningState** | **String** | the current deployment or provisioning state, which only appears in the response. |  [optional] [readonly] |
|**replicaSets** | [**List&lt;ReplicaSet&gt;**](ReplicaSet.md) | List of ReplicaSets |  [optional] |
|**syncOwner** | **String** | SyncOwner ReplicaSet Id |  [optional] [readonly] |
|**tenantId** | **String** | Azure Active Directory Tenant Id |  [optional] [readonly] |
|**version** | **Integer** | Data Model Version |  [optional] [readonly] |



## Enum: FilteredSyncEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



