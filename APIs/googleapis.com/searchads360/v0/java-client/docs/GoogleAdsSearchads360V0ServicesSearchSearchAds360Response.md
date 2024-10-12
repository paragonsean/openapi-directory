

# GoogleAdsSearchads360V0ServicesSearchSearchAds360Response

Response message for SearchAds360Service.Search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversionCustomDimensionHeaders** | [**List&lt;GoogleAdsSearchads360V0ServicesConversionCustomDimensionHeader&gt;**](GoogleAdsSearchads360V0ServicesConversionCustomDimensionHeader.md) | The headers of the conversion custom dimensions in the results. |  [optional] |
|**conversionCustomMetricHeaders** | [**List&lt;GoogleAdsSearchads360V0ServicesConversionCustomMetricHeader&gt;**](GoogleAdsSearchads360V0ServicesConversionCustomMetricHeader.md) | The headers of the conversion custom metrics in the results. |  [optional] |
|**customColumnHeaders** | [**List&lt;GoogleAdsSearchads360V0ServicesCustomColumnHeader&gt;**](GoogleAdsSearchads360V0ServicesCustomColumnHeader.md) | The headers of the custom columns in the results. |  [optional] |
|**fieldMask** | **String** | FieldMask that represents what fields were requested by the user. |  [optional] |
|**nextPageToken** | **String** | Pagination token used to retrieve the next page of results. Pass the content of this string as the &#x60;page_token&#x60; attribute of the next request. &#x60;next_page_token&#x60; is not returned for the last page. |  [optional] |
|**rawEventConversionDimensionHeaders** | [**List&lt;GoogleAdsSearchads360V0ServicesRawEventConversionDimensionHeader&gt;**](GoogleAdsSearchads360V0ServicesRawEventConversionDimensionHeader.md) | The headers of the raw event conversion dimensions in the results. |  [optional] |
|**rawEventConversionMetricHeaders** | [**List&lt;GoogleAdsSearchads360V0ServicesRawEventConversionMetricHeader&gt;**](GoogleAdsSearchads360V0ServicesRawEventConversionMetricHeader.md) | The headers of the raw event conversion metrics in the results. |  [optional] |
|**results** | [**List&lt;GoogleAdsSearchads360V0ServicesSearchAds360Row&gt;**](GoogleAdsSearchads360V0ServicesSearchAds360Row.md) | The list of rows that matched the query. |  [optional] |
|**summaryRow** | [**GoogleAdsSearchads360V0ServicesSearchAds360Row**](GoogleAdsSearchads360V0ServicesSearchAds360Row.md) |  |  [optional] |
|**totalResultsCount** | **String** | Total number of results that match the query ignoring the LIMIT clause. |  [optional] |



