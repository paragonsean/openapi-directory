

# CancelTestMatrixResponse

Response containing the current state of the specified test matrix.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**testState** | [**TestStateEnum**](#TestStateEnum) | The current rolled-up state of the test matrix. If this state is already final, then the cancelation request will have no effect. |  [optional] |



## Enum: TestStateEnum

| Name | Value |
|---- | -----|
| TEST_STATE_UNSPECIFIED | &quot;TEST_STATE_UNSPECIFIED&quot; |
| VALIDATING | &quot;VALIDATING&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FINISHED | &quot;FINISHED&quot; |
| ERROR | &quot;ERROR&quot; |
| UNSUPPORTED_ENVIRONMENT | &quot;UNSUPPORTED_ENVIRONMENT&quot; |
| INCOMPATIBLE_ENVIRONMENT | &quot;INCOMPATIBLE_ENVIRONMENT&quot; |
| INCOMPATIBLE_ARCHITECTURE | &quot;INCOMPATIBLE_ARCHITECTURE&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| INVALID | &quot;INVALID&quot; |



