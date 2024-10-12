# AdHybridHealthService.ServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeAlerts** | **Number** | The count of alerts that are currently active for the service. | [optional] 
**additionalInformation** | **String** | The additional information related to the service. | [optional] 
**createdDate** | **Date** | The date and time, in UTC, when the service was onboarded to Azure Active Directory Connect Health. | [optional] 
**customNotificationEmails** | **[String]** | The list of additional emails that are configured to receive notifications about the service. | [optional] 
**disabled** | **Boolean** | Indicates if the service is disabled or not. | [optional] 
**displayName** | **String** | The display name of the service. | [optional] 
**health** | **String** | The health of the service. | [optional] 
**id** | **String** | The id of the service. | [optional] 
**lastDisabled** | **Date** | The date and time, in UTC, when the service was last disabled. | [optional] 
**lastUpdated** | **Date** | The date or time , in UTC, when the service properties were last updated. | [optional] 
**monitoringConfigurationsComputed** | **Object** | The monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. | [optional] 
**monitoringConfigurationsCustomized** | **Object** | The customized monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. | [optional] 
**notificationEmailEnabled** | **Boolean** | Indicates if email notification is enabled or not. | [optional] 
**notificationEmailEnabledForGlobalAdmins** | **Boolean** | Indicates if email notification is enabled for global administrators of the tenant. | [optional] 
**notificationEmails** | **[String]** | The list of emails to whom service notifications will be sent. | [optional] 
**notificationEmailsEnabledForGlobalAdmins** | **Boolean** | Indicates if email notification is enabled for global administrators of the tenant. | [optional] 
**originalDisabledState** | **Boolean** | Gets the original disable state. | [optional] 
**resolvedAlerts** | **Number** | The total count of alerts that has been resolved for the service. | [optional] 
**serviceId** | **String** | The id of the service. | [optional] 
**serviceName** | **String** | The name of the service. | [optional] 
**signature** | **String** | The signature of the service. | [optional] 
**simpleProperties** | **Object** | List of service specific configuration properties. | [optional] 
**tenantId** | **String** | The id of the tenant to which the service is registered to. | [optional] 
**type** | **String** | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] 


