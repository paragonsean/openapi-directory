# GameServicesApi.Rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Required | [optional] 
**conditions** | [**[Condition]**](Condition.md) | Additional restrictions that must be met. All conditions must pass for the rule to match. | [optional] 
**description** | **String** | Human-readable description of the rule. | [optional] 
**_in** | **[String]** | If one or more &#39;in&#39; clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in at least one of these entries. | [optional] 
**logConfig** | [**[LogConfig]**](LogConfig.md) | The config returned to callers of CheckPolicy for any entries that match the LOG action. | [optional] 
**notIn** | **[String]** | If one or more &#39;not_in&#39; clauses are specified, the rule matches if the PRINCIPAL/AUTHORITY_SELECTOR is in none of the entries. The format for in and not_in entries can be found at in the Local IAM documentation (see go/local-iam#features). | [optional] 
**permissions** | **[String]** | A permission is a string of form &#39;..&#39; (e.g., &#39;storage.buckets.list&#39;). A value of &#39;*&#39; matches all permissions, and a verb part of &#39;*&#39; (e.g., &#39;storage.buckets.*&#39;) matches all verbs. | [optional] 



## Enum: ActionEnum


* `NO_ACTION` (value: `"NO_ACTION"`)

* `ALLOW` (value: `"ALLOW"`)

* `ALLOW_WITH_LOG` (value: `"ALLOW_WITH_LOG"`)

* `DENY` (value: `"DENY"`)

* `DENY_WITH_LOG` (value: `"DENY_WITH_LOG"`)

* `LOG` (value: `"LOG"`)




