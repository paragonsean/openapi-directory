

# ListConfigsResponse

`ListConfigs()` returns the following response. The order of returned objects is arbitrary; that is, it is not ordered in any particular way.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configs** | [**List&lt;RuntimeConfig&gt;**](RuntimeConfig.md) | A list of the configurations in the project. The order of returned objects is arbitrary; that is, it is not ordered in any particular way. |  [optional] |
|**nextPageToken** | **String** | This token allows you to get the next page of results for list requests. If the number of results is larger than &#x60;pageSize&#x60;, use the &#x60;nextPageToken&#x60; as a value for the query parameter &#x60;pageToken&#x60; in the next list request. Subsequent list requests will have their own &#x60;nextPageToken&#x60; to continue paging through the results |  [optional] |



