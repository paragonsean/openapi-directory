# DialogflowApi.GoogleCloudDialogflowCxV3EnvironmentTestCasesConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableContinuousRun** | **Boolean** | Whether to run test cases in TestCasesConfig.test_cases periodically. Default false. If set to true, run once a day. | [optional] 
**enablePredeploymentRun** | **Boolean** | Whether to run test cases in TestCasesConfig.test_cases before deploying a flow version to the environment. Default false. | [optional] 
**testCases** | **[String]** | A list of test case names to run. They should be under the same agent. Format of each test case name: &#x60;projects//locations/ /agents//testCases/&#x60; | [optional] 


