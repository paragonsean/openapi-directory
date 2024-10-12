

# ApplicationGatewayHttpListenerPropertiesFormat

Properties of HTTP listener of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customErrorConfigurations** | [**List&lt;ApplicationGatewayCustomError&gt;**](ApplicationGatewayCustomError.md) | Custom error configurations of the HTTP listener. |  [optional] |
|**frontendIPConfiguration** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**frontendPort** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**hostName** | **String** | Host name of HTTP listener. |  [optional] |
|**protocol** | **ApplicationGatewayProtocol** |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**requireServerNameIndication** | **Boolean** | Applicable only if protocol is https. Enables SNI for multi-hosting. |  [optional] |
|**sslCertificate** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



