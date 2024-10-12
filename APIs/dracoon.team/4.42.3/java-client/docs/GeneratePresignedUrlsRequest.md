

# GeneratePresignedUrlsRequest

Request model for generating presigned URLs

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstPartNumber** | **Integer** | First part number of a range of requested presigned URLs (for S3 it is: &#x60;1&#x60;) |  |
|**lastPartNumber** | **Integer** | Last part number of a range of requested presigned URLs |  |
|**size** | **Long** | &#x60;Content-Length&#x60; header size for each presigned URL (in bytes)  *MUST* be &gt;&#x3D; 5 MB except the last part. |  |



