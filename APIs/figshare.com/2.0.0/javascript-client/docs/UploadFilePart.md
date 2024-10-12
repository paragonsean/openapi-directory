# FigshareApi.UploadFilePart

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endOffset** | **Number** | Indexes on byte range. zero-based and inclusive | [optional] 
**locked** | **Boolean** | When a part is being uploaded it is being locked, by setting the locked flag to true. No changes/uploads can happen on this part from other requests. | [optional] 
**partNo** | **Number** | File part id | [optional] 
**startOffset** | **Number** | Indexes on byte range. zero-based and inclusive | [optional] 
**status** | **String** | part status | [optional] 



## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `COMPLETE` (value: `"COMPLETE"`)




