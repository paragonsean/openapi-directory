

# HistogramQueryResult

Histogram result that matches HistogramQuery specified in searches.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**histogram** | **Map&lt;String, String&gt;** | A map from the values of the facet associated with distinct values to the number of matching entries with corresponding value. The key format is: * (for string histogram) string values stored in the field. * (for named numeric bucket) name specified in &#x60;bucket()&#x60; function, like for &#x60;bucket(0, MAX, \&quot;non-negative\&quot;)&#x60;, the key will be &#x60;non-negative&#x60;. * (for anonymous numeric bucket) range formatted as &#x60;-&#x60;, for example, &#x60;0-1000&#x60;, &#x60;MIN-0&#x60;, and &#x60;0-MAX&#x60;. |  [optional] |
|**histogramQuery** | **String** | Requested histogram expression. |  [optional] |



