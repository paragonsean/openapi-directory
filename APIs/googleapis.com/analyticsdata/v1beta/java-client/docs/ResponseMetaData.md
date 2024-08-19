

# ResponseMetaData

Response's metadata carrying additional information about the report content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | The currency code used in this report. Intended to be used in formatting currency metrics like &#x60;purchaseRevenue&#x60; for visualization. If currency_code was specified in the request, this response parameter will echo the request parameter; otherwise, this response parameter is the property&#39;s current currency_code. Currency codes are string encodings of currency types from the ISO 4217 standard (https://en.wikipedia.org/wiki/ISO_4217); for example \&quot;USD\&quot;, \&quot;EUR\&quot;, \&quot;JPY\&quot;. To learn more, see https://support.google.com/analytics/answer/9796179. |  [optional] |
|**dataLossFromOtherRow** | **Boolean** | If true, indicates some buckets of dimension combinations are rolled into \&quot;(other)\&quot; row. This can happen for high cardinality reports. The metadata parameter dataLossFromOtherRow is populated based on the aggregated data table used in the report. The parameter will be accurately populated regardless of the filters and limits in the report. For example, the (other) row could be dropped from the report because the request contains a filter on sessionSource &#x3D; google. This parameter will still be populated if data loss from other row was present in the input aggregate data used to generate this report. To learn more, see [About the (other) row and data sampling](https://support.google.com/analytics/answer/13208658#reports). |  [optional] |
|**emptyReason** | **String** | If empty reason is specified, the report is empty for this reason. |  [optional] |
|**samplingMetadatas** | [**List&lt;SamplingMetadata&gt;**](SamplingMetadata.md) | If this report results is [sampled](https://support.google.com/analytics/answer/13331292), this describes the percentage of events used in this report. One &#x60;samplingMetadatas&#x60; is populated for each date range. Each &#x60;samplingMetadatas&#x60; corresponds to a date range in order that date ranges were specified in the request. However if the results are not sampled, this field will not be defined. |  [optional] |
|**schemaRestrictionResponse** | [**SchemaRestrictionResponse**](SchemaRestrictionResponse.md) |  |  [optional] |
|**subjectToThresholding** | **Boolean** | If &#x60;subjectToThresholding&#x60; is true, this report is subject to thresholding and only returns data that meets the minimum aggregation thresholds. It is possible for a request to be subject to thresholding thresholding and no data is absent from the report, and this happens when all data is above the thresholds. To learn more, see [Data thresholds](https://support.google.com/analytics/answer/9383630). |  [optional] |
|**timeZone** | **String** | The property&#39;s current timezone. Intended to be used to interpret time-based dimensions like &#x60;hour&#x60; and &#x60;minute&#x60;. Formatted as strings from the IANA Time Zone database (https://www.iana.org/time-zones); for example \&quot;America/New_York\&quot; or \&quot;Asia/Tokyo\&quot;. |  [optional] |



