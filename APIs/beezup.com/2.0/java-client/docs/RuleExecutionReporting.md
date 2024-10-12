

# RuleExecutionReporting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeAffectedProductCount** | **Integer** | The count of affected active products |  [optional] |
|**affectedChannelCount** | **Integer** | The count of affected Channels across all products |  [optional] |
|**affectedProductCount** | **Integer** | The count of affected products, active or not |  [optional] |
|**completedUtcDate** | **OffsetDateTime** | The completed utc date of the execution of the rule |  [optional] |
|**errorType** | **RuleExecutionReportingErrorType** |  |  [optional] |
|**executionSource** | **RuleExecutionReportingExecutionSource** |  |  |
|**links** | [**RuleExecutionReportingLinks**](RuleExecutionReportingLinks.md) |  |  [optional] |
|**optimisationActionName** | **OptimisationActionName** |  |  [optional] |
|**reportUrl** | **String** | The url for the excel report for this execution |  [optional] |
|**ruleId** | **String** | The rule identifier |  |
|**ruleName** | **String** | The name of the rule |  |
|**startedUtcDate** | **OffsetDateTime** | The start utc date of the execution of the rule |  [optional] |
|**status** | **RuleExecutionReportingStatus** |  |  |
|**userId** | **String** | The userId that executed the rule if any |  [optional] |



