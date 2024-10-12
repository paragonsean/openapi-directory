

# ListUptimeCheckConfigsResponse

The protocol for the ListUptimeCheckConfigs response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the next_page_token is passed to the subsequent List method call (in the request message&#39;s page_token field). |  [optional] |
|**totalSize** | **Integer** | The total number of Uptime check configurations for the project, irrespective of any pagination. |  [optional] |
|**uptimeCheckConfigs** | [**List&lt;UptimeCheckConfig&gt;**](UptimeCheckConfig.md) | The returned Uptime check configurations. |  [optional] |



