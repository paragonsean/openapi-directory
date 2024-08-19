# CloudTestingApi.CancelTestMatrixResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**testState** | **String** | The current rolled-up state of the test matrix. If this state is already final, then the cancelation request will have no effect. | [optional] 



## Enum: TestStateEnum


* `TEST_STATE_UNSPECIFIED` (value: `"TEST_STATE_UNSPECIFIED"`)

* `VALIDATING` (value: `"VALIDATING"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `FINISHED` (value: `"FINISHED"`)

* `ERROR` (value: `"ERROR"`)

* `UNSUPPORTED_ENVIRONMENT` (value: `"UNSUPPORTED_ENVIRONMENT"`)

* `INCOMPATIBLE_ENVIRONMENT` (value: `"INCOMPATIBLE_ENVIRONMENT"`)

* `INCOMPATIBLE_ARCHITECTURE` (value: `"INCOMPATIBLE_ARCHITECTURE"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `INVALID` (value: `"INVALID"`)




