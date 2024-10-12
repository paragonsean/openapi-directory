

# GoogleCloudContactcenterinsightsV1PhraseMatchRuleGroup

A message representing a rule in the phrase matcher.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phraseMatchRules** | [**List&lt;GoogleCloudContactcenterinsightsV1PhraseMatchRule&gt;**](GoogleCloudContactcenterinsightsV1PhraseMatchRule.md) | A list of phrase match rules that are included in this group. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of this phrase match rule group. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED | &quot;PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED&quot; |
| ALL_OF | &quot;ALL_OF&quot; |
| ANY_OF | &quot;ANY_OF&quot; |



