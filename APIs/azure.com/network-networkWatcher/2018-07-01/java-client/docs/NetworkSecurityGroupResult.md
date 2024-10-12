

# NetworkSecurityGroupResult

Network configuration diagnostic result corresponded provided traffic query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluatedNetworkSecurityGroups** | [**List&lt;EvaluatedNetworkSecurityGroup&gt;**](EvaluatedNetworkSecurityGroup.md) | List of results network security groups diagnostic. |  [optional] [readonly] |
|**securityRuleAccessResult** | [**SecurityRuleAccessResultEnum**](#SecurityRuleAccessResultEnum) | The network traffic is allowed or denied. Possible values are &#39;Allow&#39; and &#39;Deny&#39;. |  [optional] |



## Enum: SecurityRuleAccessResultEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



