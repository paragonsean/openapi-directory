# Taxamo.ReportingApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDomesticSummaryReport**](ReportingApi.md#getDomesticSummaryReport) | **GET** /api/v1/reports/domestic/summary | Calculate domestic summary
[**getEuViesReport**](ReportingApi.md#getEuViesReport) | **GET** /api/v1/reports/eu/vies | Calculate EU VIES report



## getDomesticSummaryReport

> GetDomesticSummaryReportOut getDomesticSummaryReport(countryCode, startMonth, endMonth, opts)

Calculate domestic summary

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.ReportingApi();
let countryCode = "countryCode_example"; // String | ISO 2-letter country code which will be used for determining which country is domestic.
let startMonth = "startMonth_example"; // String | Period start month in yyyy-MM format.
let endMonth = "endMonth_example"; // String | Period end month in yyyy-MM format.
let opts = {
  'format': "format_example", // String | Output format. 'xml' and 'csv' values are accepted. Default format - json
  'currencyCode': "currencyCode_example", // String | ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
  'fxDateType': "fxDateType_example" // String | Which date should be used for FX.
};
apiInstance.getDomesticSummaryReport(countryCode, startMonth, endMonth, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryCode** | **String**| ISO 2-letter country code which will be used for determining which country is domestic. | 
 **startMonth** | **String**| Period start month in yyyy-MM format. | 
 **endMonth** | **String**| Period end month in yyyy-MM format. | 
 **format** | **String**| Output format. &#39;xml&#39; and &#39;csv&#39; values are accepted. Default format - json | [optional] 
 **currencyCode** | **String**| ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code. | [optional] 
 **fxDateType** | **String**| Which date should be used for FX. | [optional] 

### Return type

[**GetDomesticSummaryReportOut**](GetDomesticSummaryReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEuViesReport

> GetEuViesReportOut getEuViesReport(endMonth, startMonth, euCountryCode, opts)

Calculate EU VIES report

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.ReportingApi();
let endMonth = "endMonth_example"; // String | Period end month in yyyy-MM format.
let startMonth = "startMonth_example"; // String | Period start month in yyyy-MM format.
let euCountryCode = "euCountryCode_example"; // String | ISO 2-letter country code which will be used for determining which country is domestic.
let opts = {
  'periodLength': "periodLength_example", // String | Length of report period. 'month', 'quarter' and 'year' values are accepted. Required only if Large Filer Format is requested.
  'lffSequenceNumber': "lffSequenceNumber_example", // String | Sequence number used to generate report in Large Filer Format. If not specified then '0000000001' will be used.
  'transformation': "transformation_example", // String | Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats.
  'currencyCode': "currencyCode_example", // String | ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
  'taxId': "taxId_example", // String | MOSS-assigned tax ID - if not provided, merchant's national tax number will be used.
  'fxDateType': "fxDateType_example", // String | Which date should be used for FX.
  'format': "format_example" // String | Output format. 'xml', 'csv' and 'lff' (only for Ireland) values are accepted as well
};
apiInstance.getEuViesReport(endMonth, startMonth, euCountryCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endMonth** | **String**| Period end month in yyyy-MM format. | 
 **startMonth** | **String**| Period start month in yyyy-MM format. | 
 **euCountryCode** | **String**| ISO 2-letter country code which will be used for determining which country is domestic. | 
 **periodLength** | **String**| Length of report period. &#39;month&#39;, &#39;quarter&#39; and &#39;year&#39; values are accepted. Required only if Large Filer Format is requested. | [optional] 
 **lffSequenceNumber** | **String**| Sequence number used to generate report in Large Filer Format. If not specified then &#39;0000000001&#39; will be used. | [optional] 
 **transformation** | **String**| Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats. | [optional] 
 **currencyCode** | **String**| ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code. | [optional] 
 **taxId** | **String**| MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. | [optional] 
 **fxDateType** | **String**| Which date should be used for FX. | [optional] 
 **format** | **String**| Output format. &#39;xml&#39;, &#39;csv&#39; and &#39;lff&#39; (only for Ireland) values are accepted as well | [optional] 

### Return type

[**GetEuViesReportOut**](GetEuViesReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

