

# DataMaskingRuleProperties

The properties of a database data masking rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aliasName** | **String** | The alias name. This is a legacy parameter and is no longer used. |  [optional] |
|**columnName** | **String** | The column name on which the data masking rule is applied. |  |
|**id** | **String** | The rule Id. |  [optional] [readonly] |
|**maskingFunction** | [**MaskingFunctionEnum**](#MaskingFunctionEnum) | The masking function that is used for the data masking rule. |  |
|**numberFrom** | **String** | The numberFrom property of the masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored. |  [optional] |
|**numberTo** | **String** | The numberTo property of the data masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored. |  [optional] |
|**prefixSize** | **String** | If maskingFunction is set to Text, the number of characters to show unmasked in the beginning of the string. Otherwise, this parameter will be ignored. |  [optional] |
|**replacementString** | **String** | If maskingFunction is set to Text, the character to use for masking the unexposed part of the string. Otherwise, this parameter will be ignored. |  [optional] |
|**ruleState** | [**RuleStateEnum**](#RuleStateEnum) | The rule state. Used to delete a rule. To delete an existing rule, specify the schemaName, tableName, columnName, maskingFunction, and specify ruleState as disabled. However, if the rule doesn&#39;t already exist, the rule will be created with ruleState set to enabled, regardless of the provided value of ruleState. |  [optional] |
|**schemaName** | **String** | The schema name on which the data masking rule is applied. |  |
|**suffixSize** | **String** | If maskingFunction is set to Text, the number of characters to show unmasked at the end of the string. Otherwise, this parameter will be ignored. |  [optional] |
|**tableName** | **String** | The table name on which the data masking rule is applied. |  |



## Enum: MaskingFunctionEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| CCN | &quot;CCN&quot; |
| EMAIL | &quot;Email&quot; |
| NUMBER | &quot;Number&quot; |
| SSN | &quot;SSN&quot; |
| TEXT | &quot;Text&quot; |



## Enum: RuleStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



