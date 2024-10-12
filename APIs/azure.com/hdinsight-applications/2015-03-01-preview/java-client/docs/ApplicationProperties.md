

# ApplicationProperties

The HDInsight cluster application GET response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationState** | **String** | The application state. |  [optional] [readonly] |
|**applicationType** | **String** | The application type. |  [optional] |
|**computeProfile** | [**ApplicationPropertiesComputeProfile**](ApplicationPropertiesComputeProfile.md) |  |  [optional] |
|**createdDate** | **String** | The application create date time. |  [optional] [readonly] |
|**errors** | [**List&lt;ApplicationPropertiesErrorsInner&gt;**](ApplicationPropertiesErrorsInner.md) | The list of errors. |  [optional] |
|**httpsEndpoints** | [**List&lt;ApplicationGetHttpsEndpoint&gt;**](ApplicationGetHttpsEndpoint.md) | The list of application HTTPS endpoints. |  [optional] |
|**installScriptActions** | [**List&lt;ApplicationPropertiesInstallScriptActionsInner&gt;**](ApplicationPropertiesInstallScriptActionsInner.md) | The list of install script actions. |  [optional] |
|**marketplaceIdentifier** | **String** | The marketplace identifier. |  [optional] [readonly] |
|**provisioningState** | **String** | The provisioning state of the application. |  [optional] [readonly] |
|**sshEndpoints** | [**List&lt;ApplicationGetEndpoint&gt;**](ApplicationGetEndpoint.md) | The list of application SSH endpoints. |  [optional] |
|**uninstallScriptActions** | [**List&lt;ApplicationPropertiesInstallScriptActionsInner&gt;**](ApplicationPropertiesInstallScriptActionsInner.md) | The list of uninstall script actions. |  [optional] |



