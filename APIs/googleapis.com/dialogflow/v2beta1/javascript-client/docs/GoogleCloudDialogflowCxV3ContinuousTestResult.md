# DialogflowApi.GoogleCloudDialogflowCxV3ContinuousTestResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The resource name for the continuous test result. Format: &#x60;projects//locations//agents//environments//continuousTestResults/&#x60;. | [optional] 
**result** | **String** | The result of this continuous test run, i.e. whether all the tests in this continuous test run pass or not. | [optional] 
**runTime** | **String** | Time when the continuous testing run starts. | [optional] 
**testCaseResults** | **[String]** | A list of individual test case results names in this continuous test run. | [optional] 



## Enum: ResultEnum


* `AGGREGATED_TEST_RESULT_UNSPECIFIED` (value: `"AGGREGATED_TEST_RESULT_UNSPECIFIED"`)

* `PASSED` (value: `"PASSED"`)

* `FAILED` (value: `"FAILED"`)




