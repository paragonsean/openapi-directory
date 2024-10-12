# BeezUpMerchantApi.RuleExecutionReporting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeAffectedProductCount** | **Number** | The count of affected active products | [optional] 
**affectedChannelCount** | **Number** | The count of affected Channels across all products | [optional] 
**affectedProductCount** | **Number** | The count of affected products, active or not | [optional] 
**completedUtcDate** | **Date** | The completed utc date of the execution of the rule | [optional] 
**errorType** | [**RuleExecutionReportingErrorType**](RuleExecutionReportingErrorType.md) |  | [optional] 
**executionSource** | [**RuleExecutionReportingExecutionSource**](RuleExecutionReportingExecutionSource.md) |  | 
**links** | [**RuleExecutionReportingLinks**](RuleExecutionReportingLinks.md) |  | [optional] 
**optimisationActionName** | [**OptimisationActionName**](OptimisationActionName.md) |  | [optional] 
**reportUrl** | **String** | The url for the excel report for this execution | [optional] 
**ruleId** | **String** | The rule identifier | 
**ruleName** | **String** | The name of the rule | 
**startedUtcDate** | **Date** | The start utc date of the execution of the rule | [optional] 
**status** | [**RuleExecutionReportingStatus**](RuleExecutionReportingStatus.md) |  | 
**userId** | **String** | The userId that executed the rule if any | [optional] 


