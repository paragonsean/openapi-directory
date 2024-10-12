

# VerificationIPFlowResult

Results of IP flow verification on the target resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccessEnum**](#AccessEnum) | Access to be allowed or denied. |  [optional] |
|**ruleName** | **String** | Name of the rule. If input is not matched against any security rule, it is not displayed. |  [optional] |



## Enum: AccessEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



