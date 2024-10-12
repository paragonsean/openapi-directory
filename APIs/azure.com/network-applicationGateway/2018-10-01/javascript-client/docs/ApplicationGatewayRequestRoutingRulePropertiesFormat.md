# NetworkManagementClient.ApplicationGatewayRequestRoutingRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPool** | [**Model0**](Model0.md) |  | [optional] 
**backendHttpSettings** | [**Model0**](Model0.md) |  | [optional] 
**httpListener** | [**Model0**](Model0.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the request routing rule resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**redirectConfiguration** | [**Model0**](Model0.md) |  | [optional] 
**rewriteRuleSet** | [**Model0**](Model0.md) |  | [optional] 
**ruleType** | **String** | Rule type. | [optional] 
**urlPathMap** | [**Model0**](Model0.md) |  | [optional] 



## Enum: RuleTypeEnum


* `Basic` (value: `"Basic"`)

* `PathBasedRouting` (value: `"PathBasedRouting"`)




