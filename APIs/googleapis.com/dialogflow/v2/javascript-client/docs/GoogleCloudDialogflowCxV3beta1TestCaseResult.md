# DialogflowApi.GoogleCloudDialogflowCxV3beta1TestCaseResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversationTurns** | [**[GoogleCloudDialogflowCxV3beta1ConversationTurn]**](GoogleCloudDialogflowCxV3beta1ConversationTurn.md) | The conversation turns uttered during the test case replay in chronological order. | [optional] 
**environment** | **String** | Environment where the test was run. If not set, it indicates the draft environment. | [optional] 
**name** | **String** | The resource name for the test case result. Format: &#x60;projects//locations//agents//testCases/ /results/&#x60;. | [optional] 
**testResult** | **String** | Whether the test case passed in the agent environment. | [optional] 
**testTime** | **String** | The time that the test was run. | [optional] 



## Enum: TestResultEnum


* `TEST_RESULT_UNSPECIFIED` (value: `"TEST_RESULT_UNSPECIFIED"`)

* `PASSED` (value: `"PASSED"`)

* `FAILED` (value: `"FAILED"`)




