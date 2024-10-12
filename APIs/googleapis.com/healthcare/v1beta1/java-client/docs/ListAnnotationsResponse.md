

# ListAnnotationsResponse

Lists the Annotations in the specified Annotation store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | [**List&lt;Annotation&gt;**](Annotation.md) | The returned Annotations. Won&#39;t be more values than the value of page_size in the request. See &#x60;AnnotationView&#x60; in the request for populated fields. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results or empty if there are no more results in the list. |  [optional] |



