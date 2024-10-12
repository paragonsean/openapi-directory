# NetworkManagementClient.ApplicationGatewayRequestRoutingRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPool** | [**SubResource**](SubResource.md) |  | [optional] 
**backendHttpSettings** | [**SubResource**](SubResource.md) |  | [optional] 
**httpListener** | [**SubResource**](SubResource.md) |  | [optional] 
**provisioningState** | **String** | Gets or sets Provisioning state of the request routing rule resource Updating/Deleting/Failed | [optional] 
**ruleType** | **String** | Gets or sets the rule type | [optional] 
**urlPathMap** | [**SubResource**](SubResource.md) |  | [optional] 



## Enum: RuleTypeEnum


* `Basic` (value: `"Basic"`)

* `PathBasedRouting` (value: `"PathBasedRouting"`)




