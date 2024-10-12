# FinanceReportsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**financeReportsGetCollection**](FinanceReportsApi.md#financeReportsGetCollection) | **GET** /v1/financeReports |  |


<a id="financeReportsGetCollection"></a>
# **financeReportsGetCollection**
> File financeReportsGetCollection(filterRegionCode, filterReportDate, filterReportType, filterVendorNumber)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinanceReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    FinanceReportsApi apiInstance = new FinanceReportsApi(defaultClient);
    List<String> filterRegionCode = Arrays.asList(); // List<String> | filter by attribute 'regionCode'
    List<String> filterReportDate = Arrays.asList(); // List<String> | filter by attribute 'reportDate'
    List<String> filterReportType = Arrays.asList(); // List<String> | filter by attribute 'reportType'
    List<String> filterVendorNumber = Arrays.asList(); // List<String> | filter by attribute 'vendorNumber'
    try {
      File result = apiInstance.financeReportsGetCollection(filterRegionCode, filterReportDate, filterReportType, filterVendorNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinanceReportsApi#financeReportsGetCollection");
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
| **filterRegionCode** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;regionCode&#39; | |
| **filterReportDate** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;reportDate&#39; | |
| **filterReportType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;reportType&#39; | [enum: FINANCIAL, FINANCE_DETAIL] |
| **filterVendorNumber** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;vendorNumber&#39; | |

### Return type

[**File**](File.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: gzip, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of FinanceReports |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

