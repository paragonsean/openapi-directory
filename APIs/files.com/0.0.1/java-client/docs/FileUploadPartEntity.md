

# FileUploadPartEntity

Begin file upload

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Type of upload |  [optional] |
|**askAboutOverwrites** | **Boolean** | If &#x60;true&#x60;, this file exists and you may wish to ask the user for overwrite confirmation |  [optional] |
|**availableParts** | **Integer** | Number of parts in the upload |  [optional] |
|**expires** | **String** | Date/time of when this Upload part expires and the URL cannot be used any more |  [optional] |
|**headers** | **Object** | Additional upload headers to provide as part of the upload |  [optional] |
|**httpMethod** | **String** | HTTP Method to use for uploading the part, usually &#x60;PUT&#x60; |  [optional] |
|**nextPartsize** | **Integer** | Size in bytes for this part |  [optional] |
|**parallelParts** | **Boolean** | If &#x60;true&#x60;, multiple parts may be uploaded in parallel.  If &#x60;false&#x60;, be sure to only upload one part at a time, in order. |  [optional] |
|**parameters** | **Object** | Additional HTTP parameters to send with the upload |  [optional] |
|**partNumber** | **Integer** | Number of this upload part |  [optional] |
|**partsize** | **Integer** | Size in bytes for the next upload part |  [optional] |
|**path** | **String** | New file path |  [optional] |
|**ref** | **String** | Reference name for this upload part |  [optional] |
|**retryParts** | **Boolean** | If &#x60;true&#x60;, parts may be retried. If &#x60;false&#x60;, a part cannot be retried and the upload should be restarted. |  [optional] |
|**send** | **Object** | Content-Type and File to send |  [optional] |
|**uploadUri** | **String** | URI to upload this part to |  [optional] |



