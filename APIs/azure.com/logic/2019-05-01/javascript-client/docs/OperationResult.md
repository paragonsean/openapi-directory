# LogicManagementClient.OperationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Object** |  | [optional] 
**inputsLink** | [**ContentLink**](ContentLink.md) |  | [optional] 
**iterationCount** | **Number** |  | [optional] 
**outputs** | **Object** |  | [optional] 
**outputsLink** | [**ContentLink**](ContentLink.md) |  | [optional] 
**retryHistory** | [**[RetryHistory]**](RetryHistory.md) | Gets the retry histories. | [optional] 
**trackedProperties** | **Object** |  | [optional] 
**trackingId** | **String** | Gets the tracking id. | [optional] [readonly] 
**code** | **String** | The workflow scope repetition code. | [optional] 
**correlation** | [**RunActionCorrelation**](RunActionCorrelation.md) |  | [optional] 
**endTime** | **Date** | The end time of the workflow scope repetition. | [optional] 
**error** | **Object** |  | [optional] 
**startTime** | **Date** | The start time of the workflow scope repetition. | [optional] 
**status** | [**WorkflowStatus**](WorkflowStatus.md) |  | [optional] 


