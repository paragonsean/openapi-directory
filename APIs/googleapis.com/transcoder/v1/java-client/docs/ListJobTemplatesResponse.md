

# ListJobTemplatesResponse

Response message for `TranscoderService.ListJobTemplates`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobTemplates** | [**List&lt;JobTemplate&gt;**](JobTemplate.md) | List of job templates in the specified region. |  [optional] |
|**nextPageToken** | **String** | The pagination token. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | List of regions that could not be reached. |  [optional] |



