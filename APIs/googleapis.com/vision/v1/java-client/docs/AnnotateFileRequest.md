

# AnnotateFileRequest

A request to annotate one single file, e.g. a PDF, TIFF or GIF file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**features** | [**List&lt;Feature&gt;**](Feature.md) | Required. Requested features. |  [optional] |
|**imageContext** | [**ImageContext**](ImageContext.md) |  |  [optional] |
|**inputConfig** | [**InputConfig**](InputConfig.md) |  |  [optional] |
|**pages** | **List&lt;Integer&gt;** | Pages of the file to perform image annotation. Pages starts from 1, we assume the first page of the file is page 1. At most 5 pages are supported per request. Pages can be negative. Page 1 means the first page. Page 2 means the second page. Page -1 means the last page. Page -2 means the second to the last page. If the file is GIF instead of PDF or TIFF, page refers to GIF frames. If this field is empty, by default the service performs image annotation for the first 5 pages of the file. |  [optional] |



