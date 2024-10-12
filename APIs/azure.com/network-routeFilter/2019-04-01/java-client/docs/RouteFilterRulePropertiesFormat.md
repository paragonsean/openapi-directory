

# RouteFilterRulePropertiesFormat

Route Filter Rule Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Access to be allowed or denied. |  |
|**communities** | **List&lt;String&gt;** | The collection for bgp community values to filter on. e.g. [&#39;12076:5010&#39;,&#39;12076:5020&#39;]. |  |
|**provisioningState** | **String** | The provisioning state of the resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, &#39;Succeeded&#39; and &#39;Failed&#39;. |  [optional] [readonly] |
|**routeFilterRuleType** | [**RouteFilterRuleTypeEnum**](#RouteFilterRuleTypeEnum) | The rule type of the rule. |  |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



## Enum: RouteFilterRuleTypeEnum

| Name | Value |
|---- | -----|
| COMMUNITY | &quot;Community&quot; |



