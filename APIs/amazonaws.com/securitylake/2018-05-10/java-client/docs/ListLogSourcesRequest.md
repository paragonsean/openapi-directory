

# ListLogSourcesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accounts** | **List&lt;String&gt;** | The list of Amazon Web Services accounts for which log sources are displayed. |  [optional] |
|**maxResults** | **Integer** | The maximum number of accounts for which the log sources are displayed. |  [optional] |
|**nextToken** | **String** | If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page. |  [optional] |
|**regions** | **List&lt;String&gt;** | The list of regions for which log sources are displayed. |  [optional] |
|**sources** | [**List&lt;LogSourceResource&gt;**](LogSourceResource.md) | The list of sources for which log sources are displayed. |  [optional] |



