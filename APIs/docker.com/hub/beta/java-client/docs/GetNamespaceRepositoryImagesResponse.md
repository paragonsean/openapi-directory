

# GetNamespaceRepositoryImagesResponse

Paginated list of images in a repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Total count of images in the repository. |  [optional] |
|**next** | **String** | Link to the next page with the same query parameters if there are more images. |  [optional] |
|**previous** | **String** | Link to the previous page with the same query parameters if not on first page. |  [optional] |
|**results** | [**List&lt;GetNamespaceRepositoryImagesResponseResultsInner&gt;**](GetNamespaceRepositoryImagesResponseResultsInner.md) | Image details. |  [optional] |



