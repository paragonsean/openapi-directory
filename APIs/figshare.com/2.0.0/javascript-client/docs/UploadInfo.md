# FigshareApi.UploadInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md5** | **String** | md5 provided on upload initialization | [optional] 
**name** | **String** | name of file on upload server | [optional] 
**parts** | [**[UploadFilePart]**](UploadFilePart.md) | Uploads parts | [optional] 
**size** | **Number** | size of file in bytes | [optional] 
**status** | **String** | Upload status | [optional] 
**token** | **String** | token received after initializing a file upload | [optional] 



## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `ABORTED` (value: `"ABORTED"`)




