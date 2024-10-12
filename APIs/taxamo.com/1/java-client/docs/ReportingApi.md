# ReportingApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDomesticSummaryReport**](ReportingApi.md#getDomesticSummaryReport) | **GET** /api/v1/reports/domestic/summary | Calculate domestic summary |
| [**getEuViesReport**](ReportingApi.md#getEuViesReport) | **GET** /api/v1/reports/eu/vies | Calculate EU VIES report |


<a id="getDomesticSummaryReport"></a>
# **getDomesticSummaryReport**
> GetDomesticSummaryReportOut getDomesticSummaryReport(countryCode, startMonth, endMonth, format, currencyCode, fxDateType)

Calculate domestic summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String countryCode = "countryCode_example"; // String | ISO 2-letter country code which will be used for determining which country is domestic.
    String startMonth = "startMonth_example"; // String | Period start month in yyyy-MM format.
    String endMonth = "endMonth_example"; // String | Period end month in yyyy-MM format.
    String format = "format_example"; // String | Output format. 'xml' and 'csv' values are accepted. Default format - json
    String currencyCode = "currencyCode_example"; // String | ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
    String fxDateType = "fxDateType_example"; // String | Which date should be used for FX.
    try {
      GetDomesticSummaryReportOut result = apiInstance.getDomesticSummaryReport(countryCode, startMonth, endMonth, format, currencyCode, fxDateType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#getDomesticSummaryReport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **countryCode** | **String**| ISO 2-letter country code which will be used for determining which country is domestic. | |
| **startMonth** | **String**| Period start month in yyyy-MM format. | |
| **endMonth** | **String**| Period end month in yyyy-MM format. | |
| **format** | **String**| Output format. &#39;xml&#39; and &#39;csv&#39; values are accepted. Default format - json | [optional] |
| **currencyCode** | **String**| ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code. | [optional] |
| **fxDateType** | **String**| Which date should be used for FX. | [optional] |

### Return type

[**GetDomesticSummaryReportOut**](GetDomesticSummaryReportOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getEuViesReport"></a>
# **getEuViesReport**
> GetEuViesReportOut getEuViesReport(endMonth, startMonth, euCountryCode, periodLength, lffSequenceNumber, transformation, currencyCode, taxId, fxDateType, format)

Calculate EU VIES report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String endMonth = "endMonth_example"; // String | Period end month in yyyy-MM format.
    String startMonth = "startMonth_example"; // String | Period start month in yyyy-MM format.
    String euCountryCode = "euCountryCode_example"; // String | ISO 2-letter country code which will be used for determining which country is domestic.
    String periodLength = "periodLength_example"; // String | Length of report period. 'month', 'quarter' and 'year' values are accepted. Required only if Large Filer Format is requested.
    String lffSequenceNumber = "lffSequenceNumber_example"; // String | Sequence number used to generate report in Large Filer Format. If not specified then '0000000001' will be used.
    String transformation = "transformation_example"; // String | Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats.
    String currencyCode = "currencyCode_example"; // String | ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code.
    String taxId = "taxId_example"; // String | MOSS-assigned tax ID - if not provided, merchant's national tax number will be used.
    String fxDateType = "fxDateType_example"; // String | Which date should be used for FX.
    String format = "format_example"; // String | Output format. 'xml', 'csv' and 'lff' (only for Ireland) values are accepted as well
    try {
      GetEuViesReportOut result = apiInstance.getEuViesReport(endMonth, startMonth, euCountryCode, periodLength, lffSequenceNumber, transformation, currencyCode, taxId, fxDateType, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#getEuViesReport");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **endMonth** | **String**| Period end month in yyyy-MM format. | |
| **startMonth** | **String**| Period start month in yyyy-MM format. | |
| **euCountryCode** | **String**| ISO 2-letter country code which will be used for determining which country is domestic. | |
| **periodLength** | **String**| Length of report period. &#39;month&#39;, &#39;quarter&#39; and &#39;year&#39; values are accepted. Required only if Large Filer Format is requested. | [optional] |
| **lffSequenceNumber** | **String**| Sequence number used to generate report in Large Filer Format. If not specified then &#39;0000000001&#39; will be used. | [optional] |
| **transformation** | **String**| Which transformation should be applied. Please note that transformation will be applied only for xml and csv formats. | [optional] |
| **currencyCode** | **String**| ISO 3-letter currency code, e.g. EUR or USD. Defaults to the one assigned to MOSS calculations for a given country code. | [optional] |
| **taxId** | **String**| MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. | [optional] |
| **fxDateType** | **String**| Which date should be used for FX. | [optional] |
| **format** | **String**| Output format. &#39;xml&#39;, &#39;csv&#39; and &#39;lff&#39; (only for Ireland) values are accepted as well | [optional] |

### Return type

[**GetEuViesReportOut**](GetEuViesReportOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

