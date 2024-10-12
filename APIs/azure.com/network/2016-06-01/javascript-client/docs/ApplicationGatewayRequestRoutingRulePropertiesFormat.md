# NetworkManagementClient.ApplicationGatewayRequestRoutingRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendAddressPool** | [**SubResource**](SubResource.md) |  | [optional] 
**backendHttpSettings** | [**SubResource**](SubResource.md) |  | [optional] 
**httpListener** | [**SubResource**](SubResource.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the request routing rule resource Updating/Deleting/Failed | [optional] 
**ruleType** | **String** | Rule type | [optional] 
**urlPathMap** | [**SubResource**](SubResource.md) |  | [optional] 



## Enum: RuleTypeEnum


* `Basic` (value: `"Basic"`)

* `PathBasedRouting` (value: `"PathBasedRouting"`)




