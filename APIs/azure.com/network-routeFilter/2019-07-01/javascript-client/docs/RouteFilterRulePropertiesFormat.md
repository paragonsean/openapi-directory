# NetworkManagementClient.RouteFilterRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Access to be allowed or denied. | 
**communities** | **[String]** | The collection for bgp community values to filter on. e.g. [&#39;12076:5010&#39;,&#39;12076:5020&#39;]. | 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**routeFilterRuleType** | **String** | The rule type of the rule. | 



## Enum: AccessEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: RouteFilterRuleTypeEnum


* `Community` (value: `"Community"`)




