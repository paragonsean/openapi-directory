# AdHybridHealthService.Tenant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadLicense** | **String** | The Azure Active Directory license of the tenant. | [optional] 
**aadPremium** | **Boolean** | Indicate if the tenant has Azure Active Directory Premium license or not. | [optional] 
**agentAutoUpdate** | **Boolean** | Indicates if the tenant is configured to automatically receive updates for Azure Active Directory Connect Health client side features. | [optional] 
**alertSuppressionTimeInMins** | **Number** | The time in minutes after which an alert will be auto-suppressed. | [optional] 
**consentedToMicrosoftDevOps** | **Boolean** | Indicates if the tenant data can be seen by Microsoft through Azure portal. | [optional] 
**countryLetterCode** | **String** | The country letter code of the tenant. | [optional] 
**createdDate** | **Date** | The date, in UTC, when the tenant was onboarded to Azure Active Directory Connect Health. | [optional] 
**devOpsTtl** | **Date** | The date and time, in UTC, till when the tenant data can be seen by Microsoft through Azure portal. | [optional] 
**disabled** | **Boolean** | Indicates if the tenant is disabled in Azure Active Directory Connect Health. | [optional] 
**disabledReason** | **Number** | The reason due to which the tenant was disabled in Azure Active Directory Connect Health. | [optional] 
**globalAdminsEmail** | **[String]** | The list of global administrators for the tenant. | [optional] 
**initialDomain** | **String** | The initial domain of the tenant. | [optional] 
**lastDisabled** | **Date** | The date and time, in UTC, when the tenant was last disabled in Azure Active Directory Connect Health. | [optional] 
**lastVerified** | **Date** | The date and time, in UTC, when the tenant onboarding status in Azure Active Directory Connect Health was last verified. | [optional] 
**onboarded** | **Boolean** | Indicates if the tenant is already onboarded to Azure Active Directory Connect Health. | [optional] 
**onboardingAllowed** | **Boolean** | Indicates if the tenant is allowed to  onboard to Azure Active Directory Connect Health. | [optional] 
**pksCertificate** | **Object** | The certificate associated with the tenant to onboard data to Azure Active Directory Connect Health. | [optional] 
**privatePreviewTenant** | **Boolean** | Indicates if the tenant has signed up for private preview of Azure Active Directory Connect Health features. | [optional] 
**tenantId** | **String** | The Id of the tenant. | [optional] 
**tenantInQuarantine** | **Boolean** | Indicates if data collection for this tenant is disabled or not. | [optional] 
**tenantName** | **String** | The name of the tenant. | [optional] 


