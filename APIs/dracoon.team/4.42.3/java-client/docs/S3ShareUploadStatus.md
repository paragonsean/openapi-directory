

# S3ShareUploadStatus

S3 file upload status information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorDetails** | [**ErrorResponse**](ErrorResponse.md) |  |  [optional] |
|**fileName** | **String** | File name |  |
|**size** | **Long** | File size in byte |  [optional] |
|**status** | **String** | S3 file upload status:  * &#x60;transfer&#x60; - upload in progress  * &#x60;finishing&#x60; - completing file upload  * &#x60;done&#x60; - file upload successully done  * &#x60;error&#x60; - an error occurred while file upload |  |



