

# ListReleasesResponse

The response object from `ListReleases`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**releases** | [**List&lt;Release&gt;**](Release.md) | The &#x60;Release&#x60; objects. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



