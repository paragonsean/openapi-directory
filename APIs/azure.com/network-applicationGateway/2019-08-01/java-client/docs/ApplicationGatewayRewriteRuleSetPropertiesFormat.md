

# ApplicationGatewayRewriteRuleSetPropertiesFormat

Properties of rewrite rule set of the application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**rewriteRules** | [**List&lt;ApplicationGatewayRewriteRule&gt;**](ApplicationGatewayRewriteRule.md) | Rewrite rules in the rewrite rule set. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



