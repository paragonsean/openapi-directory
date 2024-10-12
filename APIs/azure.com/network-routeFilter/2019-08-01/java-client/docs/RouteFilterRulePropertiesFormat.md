

# RouteFilterRulePropertiesFormat

Route Filter Rule Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Access to be allowed or denied. |  |
|**communities** | **List&lt;String&gt;** | The collection for bgp community values to filter on. e.g. [&#39;12076:5010&#39;,&#39;12076:5020&#39;]. |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**routeFilterRuleType** | [**RouteFilterRuleTypeEnum**](#RouteFilterRuleTypeEnum) | The rule type of the rule. |  |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: RouteFilterRuleTypeEnum

| Name | Value |
|---- | -----|
| COMMUNITY | &quot;Community&quot; |



