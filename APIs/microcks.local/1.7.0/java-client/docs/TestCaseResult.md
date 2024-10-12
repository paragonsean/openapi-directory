

# TestCaseResult

Companion objects for TestResult. Each TestCaseResult correspond to a particuliar service operation / action reference by the operationName field. TestCaseResults owns a collection of TestStepResults (one for every request associated to service operation / action).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elapsedTime** | **BigDecimal** | Elapsed time in milliseconds since the test case beginning |  |
|**operationName** | **String** | Name of operation this test case is bound to |  |
|**success** | **Boolean** | Flag telling if test case is a success |  |
|**testStepResults** | [**List&lt;TestStepResult&gt;**](TestStepResult.md) | Test steps associated to this test case |  [optional] |



