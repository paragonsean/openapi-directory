# GooglePlayAndroidDeveloperApi.UpgradeTargetingRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingPeriodDuration** | **String** | The specific billing period duration, specified in ISO 8601 format, that a user must be currently subscribed to to be eligible for this rule. If not specified, users subscribed to any billing period are matched. | [optional] 
**oncePerUser** | **Boolean** | Limit this offer to only once per user. If set to true, a user can never be eligible for this offer again if they ever subscribed to this offer. | [optional] 
**scope** | [**TargetingRuleScope**](TargetingRuleScope.md) |  | [optional] 


