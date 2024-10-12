# RubrikRestApi.VerificationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The end time of the request. | [optional] 
**error** | [**RequestErrorInfo**](RequestErrorInfo.md) |  | [optional] 
**id** | **String** | The ID of the request object used to poll the status. | 
**links** | [**[Link]**](Link.md) | References to any related objects. | 
**nodeId** | **String** | The ID of the node where the job ran. | [optional] 
**progress** | **Number** | The current percentage progress of the asynchronous request. | [optional] 
**startTime** | **Date** | The start time of the request. | [optional] 
**status** | **String** | Status of the ID. | 
**snapshotVerificationInfo** | [**[SnapshotEventSeries]**](SnapshotEventSeries.md) | List of IDs of the snapshots requested for verification and their corresponding event series IDs.  | 


