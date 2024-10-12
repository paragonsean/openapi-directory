

# GoogleCloudDialogflowCxV3beta1TestCase

Represents a test case.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | Output only. When the test was created. |  [optional] [readonly] |
|**displayName** | **String** | Required. The human-readable name of the test case, unique within the agent. Limit of 200 characters. |  [optional] |
|**lastTestResult** | [**GoogleCloudDialogflowCxV3beta1TestCaseResult**](GoogleCloudDialogflowCxV3beta1TestCaseResult.md) |  |  [optional] |
|**name** | **String** | The unique identifier of the test case. TestCases.CreateTestCase will populate the name automatically. Otherwise use format: &#x60;projects//locations//agents/ /testCases/&#x60;. |  [optional] |
|**notes** | **String** | Additional freeform notes about the test case. Limit of 400 characters. |  [optional] |
|**tags** | **List&lt;String&gt;** | Tags are short descriptions that users may apply to test cases for organizational and filtering purposes. Each tag should start with \&quot;#\&quot; and has a limit of 30 characters. |  [optional] |
|**testCaseConversationTurns** | [**List&lt;GoogleCloudDialogflowCxV3beta1ConversationTurn&gt;**](GoogleCloudDialogflowCxV3beta1ConversationTurn.md) | The conversation turns uttered when the test case was created, in chronological order. These include the canonical set of agent utterances that should occur when the agent is working properly. |  [optional] |
|**testConfig** | [**GoogleCloudDialogflowCxV3beta1TestConfig**](GoogleCloudDialogflowCxV3beta1TestConfig.md) |  |  [optional] |



