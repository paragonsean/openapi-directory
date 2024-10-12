# SearchAds360ReportingApi.GoogleAdsSearchads360V0ServicesSearchSearchAds360Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversionCustomDimensionHeaders** | [**[GoogleAdsSearchads360V0ServicesConversionCustomDimensionHeader]**](GoogleAdsSearchads360V0ServicesConversionCustomDimensionHeader.md) | The headers of the conversion custom dimensions in the results. | [optional] 
**conversionCustomMetricHeaders** | [**[GoogleAdsSearchads360V0ServicesConversionCustomMetricHeader]**](GoogleAdsSearchads360V0ServicesConversionCustomMetricHeader.md) | The headers of the conversion custom metrics in the results. | [optional] 
**customColumnHeaders** | [**[GoogleAdsSearchads360V0ServicesCustomColumnHeader]**](GoogleAdsSearchads360V0ServicesCustomColumnHeader.md) | The headers of the custom columns in the results. | [optional] 
**fieldMask** | **String** | FieldMask that represents what fields were requested by the user. | [optional] 
**nextPageToken** | **String** | Pagination token used to retrieve the next page of results. Pass the content of this string as the &#x60;page_token&#x60; attribute of the next request. &#x60;next_page_token&#x60; is not returned for the last page. | [optional] 
**rawEventConversionDimensionHeaders** | [**[GoogleAdsSearchads360V0ServicesRawEventConversionDimensionHeader]**](GoogleAdsSearchads360V0ServicesRawEventConversionDimensionHeader.md) | The headers of the raw event conversion dimensions in the results. | [optional] 
**rawEventConversionMetricHeaders** | [**[GoogleAdsSearchads360V0ServicesRawEventConversionMetricHeader]**](GoogleAdsSearchads360V0ServicesRawEventConversionMetricHeader.md) | The headers of the raw event conversion metrics in the results. | [optional] 
**results** | [**[GoogleAdsSearchads360V0ServicesSearchAds360Row]**](GoogleAdsSearchads360V0ServicesSearchAds360Row.md) | The list of rows that matched the query. | [optional] 
**summaryRow** | [**GoogleAdsSearchads360V0ServicesSearchAds360Row**](GoogleAdsSearchads360V0ServicesSearchAds360Row.md) |  | [optional] 
**totalResultsCount** | **String** | Total number of results that match the query ignoring the LIMIT clause. | [optional] 


