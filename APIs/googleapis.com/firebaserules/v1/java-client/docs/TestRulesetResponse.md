

# TestRulesetResponse

The response for FirebaseRulesService.TestRuleset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issues** | [**List&lt;Issue&gt;**](Issue.md) | Syntactic and semantic &#x60;Source&#x60; issues of varying severity. Issues of &#x60;ERROR&#x60; severity will prevent tests from executing. |  [optional] |
|**testResults** | [**List&lt;TestResult&gt;**](TestResult.md) | The set of test results given the test cases in the &#x60;TestSuite&#x60;. The results will appear in the same order as the test cases appear in the &#x60;TestSuite&#x60;. |  [optional] |



