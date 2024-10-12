

# AzureManagedOverrideRuleGroup

Defines contents of a web application rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Type of Actions |  |
|**ruleGroupOverride** | [**RuleGroupOverrideEnum**](#RuleGroupOverrideEnum) | Describes override rule group |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| BLOCK | &quot;Block&quot; |
| LOG | &quot;Log&quot; |



## Enum: RuleGroupOverrideEnum

| Name | Value |
|---- | -----|
| SQL_INJECTION | &quot;SqlInjection&quot; |
| XSS | &quot;XSS&quot; |



