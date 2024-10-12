

# DatafeedstatusesCustomBatchRequestEntry

A batch entry encoding a single non-batch datafeedstatuses request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**country** | **String** | Deprecated. Use &#x60;feedLabel&#x60; instead. The country to get the datafeed status for. If this parameter is provided, then &#x60;language&#x60; must also be provided. Note that for multi-target datafeeds this parameter is required. |  [optional] |
|**datafeedId** | **String** | The ID of the data feed to get. |  [optional] |
|**feedLabel** | **String** | The feed label to get the datafeed status for. If this parameter is provided, then &#x60;language&#x60; must also be provided. Note that for multi-target datafeeds this parameter is required. |  [optional] |
|**language** | **String** | The language to get the datafeed status for. If this parameter is provided then &#x60;country&#x60; must also be provided. Note that for multi-target datafeeds this parameter is required. |  [optional] |
|**merchantId** | **String** | The ID of the managing account. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;get&#x60;\&quot;  |  [optional] |



