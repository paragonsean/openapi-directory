

# GoogleCloudDialogflowCxV3beta1ContinuousTestResult

Represents a result from running a test case in an agent environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The resource name for the continuous test result. Format: &#x60;projects//locations//agents//environments//continuousTestResults/&#x60;. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | The result of this continuous test run, i.e. whether all the tests in this continuous test run pass or not. |  [optional] |
|**runTime** | **String** | Time when the continuous testing run starts. |  [optional] |
|**testCaseResults** | **List&lt;String&gt;** | A list of individual test case results names in this continuous test run. |  [optional] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| AGGREGATED_TEST_RESULT_UNSPECIFIED | &quot;AGGREGATED_TEST_RESULT_UNSPECIFIED&quot; |
| PASSED | &quot;PASSED&quot; |
| FAILED | &quot;FAILED&quot; |



