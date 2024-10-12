# GraphHopperDirectionsApi.Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyrights** | **[String]** |  | [optional] 
**processingTime** | **Number** | Processing time in ms. If job is still waiting in queue, processing_time is 0 | [optional] 
**solution** | [**Solution**](Solution.md) |  | [optional] 
**status** | **String** | Indicates the current status of the job | [optional] 
**waitingTimeInQueue** | **Number** | Waiting time in ms | [optional] 



## Enum: StatusEnum


* `waiting_in_queue` (value: `"waiting_in_queue"`)

* `processing` (value: `"processing"`)

* `finished` (value: `"finished"`)




