

# TestStepResult

TestStepResult is an entity embedded within TestCaseResult. They are created for each request associated with an operation / action of a microservice.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elapsedTime** | **BigDecimal** | Elapsed time in milliseconds since the test step beginning |  [optional] |
|**eventMessageName** | **String** | Name of event this test step is bound to |  [optional] |
|**message** | **String** | Error message that may be associated to this test step |  [optional] |
|**requestName** | **String** | Name of request this test step is bound to |  [optional] |
|**success** | **Boolean** | Flag telling if test case is a success |  |



