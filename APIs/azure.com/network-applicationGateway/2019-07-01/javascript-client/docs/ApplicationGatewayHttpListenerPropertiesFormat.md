# NetworkManagementClient.ApplicationGatewayHttpListenerPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customErrorConfigurations** | [**[ApplicationGatewayCustomError]**](ApplicationGatewayCustomError.md) | Custom error configurations of the HTTP listener. | [optional] 
**frontendIPConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**frontendPort** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**hostName** | **String** | Host name of HTTP listener. | [optional] 
**protocol** | [**ApplicationGatewayProtocol**](ApplicationGatewayProtocol.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. | [optional] 
**sslCertificate** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




