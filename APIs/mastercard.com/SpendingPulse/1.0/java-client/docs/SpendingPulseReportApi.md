# SpendingPulseReportApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**spendingpulseGet**](SpendingPulseReportApi.md#spendingpulseGet) | **GET** /spendingpulse | Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to. |


<a id="spendingpulseGet"></a>
# **spendingpulseGet**
> SpendingPulseListResponse spendingpulseGet(currentRow, offset, productLine, publicationCoveragePeriod, country, reportType, period, sector, ecomm)

Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to.

Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpendingPulseReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/spendingpulse/v1/spulse.svc");

    SpendingPulseReportApi apiInstance = new SpendingPulseReportApi(defaultClient);
    String currentRow = "1"; // String | Starting record number to return.
    String offset = "25"; // String | Used to restrict the number of records returned if needed to be less than max.
    String productLine = "Weekly Sales"; // String | Product Line.  Either ?US Executive Report? or ?Weekly Sales?
    String publicationCoveragePeriod = "March 2015"; // String | Publication Coverage Period indicates what period is to be covered, often the current report will include the month prior.
    String country = "US"; // String | Country code.
    String reportType = "reportA"; // String | Report type name, today the only report supported is \"monitor\".
    String period = "Weekly"; // String | Indicates the period covered by the data with possible values of - day, week, month, quarter, annual
    String sector = "sectorA"; // String | Sector name.
    String ecomm = "Y"; // String | Ecommerce indicator.
    try {
      SpendingPulseListResponse result = apiInstance.spendingpulseGet(currentRow, offset, productLine, publicationCoveragePeriod, country, reportType, period, sector, ecomm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpendingPulseReportApi#spendingpulseGet");
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
| **currentRow** | **String**| Starting record number to return. | [optional] |
| **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] |
| **productLine** | **String**| Product Line.  Either ?US Executive Report? or ?Weekly Sales? | [optional] |
| **publicationCoveragePeriod** | **String**| Publication Coverage Period indicates what period is to be covered, often the current report will include the month prior. | [optional] |
| **country** | **String**| Country code. | [optional] |
| **reportType** | **String**| Report type name, today the only report supported is \&quot;monitor\&quot;. | [optional] |
| **period** | **String**| Indicates the period covered by the data with possible values of - day, week, month, quarter, annual | [optional] |
| **sector** | **String**| Sector name. | [optional] |
| **ecomm** | **String**| Ecommerce indicator. | [optional] |

### Return type

[**SpendingPulseListResponse**](SpendingPulseListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of Spending Pulse Reports. |  -  |
| **0** | Unexpected errors |  -  |

