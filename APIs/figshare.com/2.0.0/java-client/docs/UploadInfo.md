

# UploadInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**md5** | **String** | md5 provided on upload initialization |  [optional] |
|**name** | **String** | name of file on upload server |  [optional] |
|**parts** | [**List&lt;UploadFilePart&gt;**](UploadFilePart.md) | Uploads parts |  [optional] |
|**size** | **Long** | size of file in bytes |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Upload status |  [optional] |
|**token** | **String** | token received after initializing a file upload |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| ABORTED | &quot;ABORTED&quot; |



