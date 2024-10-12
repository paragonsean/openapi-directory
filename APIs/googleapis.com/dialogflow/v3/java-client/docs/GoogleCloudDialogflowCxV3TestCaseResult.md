

# GoogleCloudDialogflowCxV3TestCaseResult

Represents a result from running a test case in an agent environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationTurns** | [**List&lt;GoogleCloudDialogflowCxV3ConversationTurn&gt;**](GoogleCloudDialogflowCxV3ConversationTurn.md) | The conversation turns uttered during the test case replay in chronological order. |  [optional] |
|**environment** | **String** | Environment where the test was run. If not set, it indicates the draft environment. |  [optional] |
|**name** | **String** | The resource name for the test case result. Format: &#x60;projects//locations//agents//testCases/ /results/&#x60;. |  [optional] |
|**testResult** | [**TestResultEnum**](#TestResultEnum) | Whether the test case passed in the agent environment. |  [optional] |
|**testTime** | **String** | The time that the test was run. |  [optional] |



## Enum: TestResultEnum

| Name | Value |
|---- | -----|
| TEST_RESULT_UNSPECIFIED | &quot;TEST_RESULT_UNSPECIFIED&quot; |
| PASSED | &quot;PASSED&quot; |
| FAILED | &quot;FAILED&quot; |



