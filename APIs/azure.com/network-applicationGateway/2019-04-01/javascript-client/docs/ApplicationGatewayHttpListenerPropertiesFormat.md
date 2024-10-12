# NetworkManagementClient.ApplicationGatewayHttpListenerPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customErrorConfigurations** | [**[ApplicationGatewayCustomError]**](ApplicationGatewayCustomError.md) | Custom error configurations of the HTTP listener. | [optional] 
**frontendIPConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**frontendPort** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 
**hostName** | **String** | Host name of HTTP listener. | [optional] 
**protocol** | [**ApplicationGatewayProtocol**](ApplicationGatewayProtocol.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the HTTP listener resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. | [optional] 
**sslCertificate** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  | [optional] 


