# HdInsightManagementClient.ApplicationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationState** | **String** | The application state. | [optional] [readonly] 
**applicationType** | **String** | The application type. | [optional] 
**computeProfile** | [**ApplicationPropertiesComputeProfile**](ApplicationPropertiesComputeProfile.md) |  | [optional] 
**createdDate** | **String** | The application create date time. | [optional] [readonly] 
**errors** | [**[ApplicationPropertiesErrorsInner]**](ApplicationPropertiesErrorsInner.md) | The list of errors. | [optional] 
**httpsEndpoints** | [**[ApplicationGetHttpsEndpoint]**](ApplicationGetHttpsEndpoint.md) | The list of application HTTPS endpoints. | [optional] 
**installScriptActions** | [**[ApplicationPropertiesInstallScriptActionsInner]**](ApplicationPropertiesInstallScriptActionsInner.md) | The list of install script actions. | [optional] 
**marketplaceIdentifier** | **String** | The marketplace identifier. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the application. | [optional] [readonly] 
**sshEndpoints** | [**[ApplicationGetEndpoint]**](ApplicationGetEndpoint.md) | The list of application SSH endpoints. | [optional] 
**uninstallScriptActions** | [**[ApplicationPropertiesInstallScriptActionsInner]**](ApplicationPropertiesInstallScriptActionsInner.md) | The list of uninstall script actions. | [optional] 


