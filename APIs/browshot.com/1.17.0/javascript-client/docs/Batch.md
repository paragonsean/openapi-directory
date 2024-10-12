# BrowshotApi.Batch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | number of unique URLs in the batch | [optional] 
**failed** | **Number** | number of screenshots failed | [optional] 
**finished** | **Number** | time of batch completed (UNIX timestamp) | [optional] 
**id** | **Number** | batch ID | [optional] 
**processed** | **Number** | number of screenshots finishe | [optional] 
**started** | **Number** | time of processing (UNIX timestamp) | [optional] 
**status** | **String** | status of the request - \&quot;in_queue\&quot;, \&quot;processing\&quot;, \&quot;finished\&quot;, \&quot;error\&quot; | [optional] 
**urls** | **[String]** | URLs to download the batch | [optional] 



## Enum: StatusEnum


* `in_queue` (value: `"in_queue"`)

* `processing` (value: `"processing"`)

* `finished` (value: `"finished"`)

* `error` (value: `"error"`)




