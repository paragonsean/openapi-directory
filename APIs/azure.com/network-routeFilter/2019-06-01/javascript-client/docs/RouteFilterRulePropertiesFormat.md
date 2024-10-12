# NetworkManagementClient.RouteFilterRulePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | Access to be allowed or denied. | 
**communities** | **[String]** | The collection for bgp community values to filter on. e.g. [&#39;12076:5010&#39;,&#39;12076:5020&#39;]. | 
**provisioningState** | **String** | The provisioning state of the resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, &#39;Succeeded&#39; and &#39;Failed&#39;. | [optional] [readonly] 
**routeFilterRuleType** | **String** | The rule type of the rule. | 



## Enum: AccessEnum


* `Allow` (value: `"Allow"`)

* `Deny` (value: `"Deny"`)





## Enum: RouteFilterRuleTypeEnum


* `Community` (value: `"Community"`)




