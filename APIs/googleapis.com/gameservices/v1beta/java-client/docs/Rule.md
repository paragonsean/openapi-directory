

# Rule

A rule to be applied in a Policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Required |  [optional] |
|**conditions** | [**List&lt;Condition&gt;**](Condition.md) | Additional restrictions that must be met. All conditions must pass for the rule to match. |  [optional] |
|**description** | **String** | Human-readable description of the rule. |  [optional] |
|**in** | **List&lt;String&gt;** | If one or more &#39;in&#39; clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in at least one of these entries. |  [optional] |
|**logConfig** | [**List&lt;LogConfig&gt;**](LogConfig.md) | The config returned to callers of CheckPolicy for any entries that match the LOG action. |  [optional] |
|**notIn** | **List&lt;String&gt;** | If one or more &#39;not_in&#39; clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in none of the entries. The format for in and not_in entries can be found at in the Local IAM documentation (see go/local-iam#features). |  [optional] |
|**permissions** | **List&lt;String&gt;** | A permission is a string of form &#39;..&#39; (e.g., &#39;storage.buckets.list&#39;). A value of &#39;*&#39; matches all permissions, and a verb part of &#39;*&#39; (e.g., &#39;storage.buckets.*&#39;) matches all verbs. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;NO_ACTION&quot; |
| ALLOW | &quot;ALLOW&quot; |
| ALLOW_WITH_LOG | &quot;ALLOW_WITH_LOG&quot; |
| DENY | &quot;DENY&quot; |
| DENY_WITH_LOG | &quot;DENY_WITH_LOG&quot; |
| LOG | &quot;LOG&quot; |



