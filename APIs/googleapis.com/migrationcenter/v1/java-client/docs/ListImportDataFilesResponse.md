

# ListImportDataFilesResponse

Response for listing payload files of an import job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**importDataFiles** | [**List&lt;ImportDataFile&gt;**](ImportDataFile.md) | The list of import data files. |  [optional] |
|**nextPageToken** | **String** | A token that can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



