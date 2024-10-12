# DracoonApi.GeneratePresignedUrlsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstPartNumber** | **Number** | First part number of a range of requested presigned URLs (for S3 it is: &#x60;1&#x60;) | 
**lastPartNumber** | **Number** | Last part number of a range of requested presigned URLs | 
**size** | **Number** | &#x60;Content-Length&#x60; header size for each presigned URL (in bytes)  *MUST* be &gt;&#x3D; 5 MB except the last part. | 


