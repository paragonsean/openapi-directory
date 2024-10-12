

# WorkflowRunActionRepetitionProperties

The workflow run action repetition properties definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**repetitionIndexes** | [**List&lt;RepetitionIndex&gt;**](RepetitionIndex.md) | The repetition indexes. |  [optional] |
|**inputs** | **Object** |  |  [optional] |
|**inputsLink** | [**ContentLink**](ContentLink.md) |  |  [optional] |
|**iterationCount** | **Integer** |  |  [optional] |
|**outputs** | **Object** |  |  [optional] |
|**outputsLink** | [**ContentLink**](ContentLink.md) |  |  [optional] |
|**retryHistory** | [**List&lt;RetryHistory&gt;**](RetryHistory.md) | Gets the retry histories. |  [optional] |
|**trackedProperties** | **Object** |  |  [optional] |
|**trackingId** | **String** | Gets the tracking id. |  [optional] [readonly] |
|**code** | **String** | The workflow scope repetition code. |  [optional] |
|**correlation** | [**RunActionCorrelation**](RunActionCorrelation.md) |  |  [optional] |
|**endTime** | **OffsetDateTime** | The end time of the workflow scope repetition. |  [optional] |
|**error** | **Object** |  |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the workflow scope repetition. |  [optional] |
|**status** | **WorkflowStatus** |  |  [optional] |



