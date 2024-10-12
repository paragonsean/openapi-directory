

# GetNamespaceRepositoryImagesTagsResponse

Paginated list of tags for this repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Total count of tags for this image. |  [optional] |
|**next** | **String** | Link to the next page if there are more tags. |  [optional] |
|**previous** | **String** | Link to the previous page if not on first page. |  [optional] |
|**results** | [**List&lt;GetNamespaceRepositoryImagesResponseResultsInnerTagsInner&gt;**](GetNamespaceRepositoryImagesResponseResultsInnerTagsInner.md) | The current and historical tags for this image. |  [optional] |



