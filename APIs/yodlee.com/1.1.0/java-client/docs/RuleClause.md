

# RuleClause


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) | Field for which the clause is created.&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid Values&lt;/b&gt;:amount,description&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; |  [optional] [readonly] |
|**fieldValue** | **String** | The value would be the amount value in case of amount based rule clause or the string value in case of description based rule clause.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; |  [optional] [readonly] |
|**operation** | [**OperationEnum**](#OperationEnum) | Operation for which the clause is created.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; |  [optional] [readonly] |
|**ruleClauseId** | **Long** | Unique identifier generated for the rule clause.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; |  [optional] [readonly] |
|**userDefinedRuleId** | **Long** | Unique identifier generated for every rule the user creates.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;:  creditCard, investment, insurance, loan&lt;br&gt; |  [optional] [readonly] |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| AMOUNT | &quot;amount&quot; |
| DESCRIPTION | &quot;description&quot; |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| NUMBER_EQUALS | &quot;numberEquals&quot; |
| NUMBER_LESS_THAN | &quot;numberLessThan&quot; |
| NUMBER_LESS_THAN_EQUALS | &quot;numberLessThanEquals&quot; |
| NUMBER_GREATER_THAN | &quot;numberGreaterThan&quot; |
| NUMBER_GREATER_THAN_EQUALS | &quot;numberGreaterThanEquals&quot; |
| STRING_EQUALS | &quot;stringEquals&quot; |
| STRING_CONTAINS | &quot;stringContains&quot; |



