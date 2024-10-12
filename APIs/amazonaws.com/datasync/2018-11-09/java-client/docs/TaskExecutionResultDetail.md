

# TaskExecutionResultDetail

Describes the detailed result of a <code>TaskExecution</code> operation. This result includes the time in milliseconds spent in each phase, the status of the task execution, and the errors encountered.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**prepareDuration** | [**Integer**](Integer.md) |  |  [optional] |
|**prepareStatus** | [**PhaseStatus**](PhaseStatus.md) |  |  [optional] |
|**totalDuration** | [**Integer**](Integer.md) |  |  [optional] |
|**transferDuration** | [**Integer**](Integer.md) |  |  [optional] |
|**transferStatus** | [**PhaseStatus**](PhaseStatus.md) |  |  [optional] |
|**verifyDuration** | [**Integer**](Integer.md) |  |  [optional] |
|**verifyStatus** | [**PhaseStatus**](PhaseStatus.md) |  |  [optional] |
|**errorCode** | [**String**](String.md) |  |  [optional] |
|**errorDetail** | [**String**](String.md) |  |  [optional] |



