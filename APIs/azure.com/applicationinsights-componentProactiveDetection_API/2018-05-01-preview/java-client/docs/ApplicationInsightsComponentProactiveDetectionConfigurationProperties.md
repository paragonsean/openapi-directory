

# ApplicationInsightsComponentProactiveDetectionConfigurationProperties

Properties that define a ProactiveDetection configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customEmails** | **List&lt;String&gt;** | Custom email addresses for this rule notifications |  [optional] |
|**enabled** | **Boolean** | A flag that indicates whether this rule is enabled by the user |  [optional] |
|**lastUpdatedTime** | **String** | The last time this rule was updated |  [optional] [readonly] |
|**name** | **String** | The rule name |  [optional] [readonly] |
|**ruleDefinitions** | [**ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitions**](ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitions.md) |  |  [optional] |
|**sendEmailsToSubscriptionOwners** | **Boolean** | A flag that indicated whether notifications on this rule should be sent to subscription owners |  [optional] |



