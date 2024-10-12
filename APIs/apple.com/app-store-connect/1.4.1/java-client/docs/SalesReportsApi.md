# SalesReportsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesReportsGetCollection**](SalesReportsApi.md#salesReportsGetCollection) | **GET** /v1/salesReports |  |


<a id="salesReportsGetCollection"></a>
# **salesReportsGetCollection**
> File salesReportsGetCollection(filterFrequency, filterReportSubType, filterReportType, filterVendorNumber, filterReportDate, filterVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    SalesReportsApi apiInstance = new SalesReportsApi(defaultClient);
    List<String> filterFrequency = Arrays.asList(); // List<String> | filter by attribute 'frequency'
    List<String> filterReportSubType = Arrays.asList(); // List<String> | filter by attribute 'reportSubType'
    List<String> filterReportType = Arrays.asList(); // List<String> | filter by attribute 'reportType'
    List<String> filterVendorNumber = Arrays.asList(); // List<String> | filter by attribute 'vendorNumber'
    List<String> filterReportDate = Arrays.asList(); // List<String> | filter by attribute 'reportDate'
    List<String> filterVersion = Arrays.asList(); // List<String> | filter by attribute 'version'
    try {
      File result = apiInstance.salesReportsGetCollection(filterFrequency, filterReportSubType, filterReportType, filterVendorNumber, filterReportDate, filterVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesReportsApi#salesReportsGetCollection");
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
| **filterFrequency** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;frequency&#39; | [enum: DAILY, WEEKLY, MONTHLY, YEARLY] |
| **filterReportSubType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;reportSubType&#39; | [enum: SUMMARY, DETAILED, OPT_IN] |
| **filterReportType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;reportType&#39; | [enum: SALES, PRE_ORDER, NEWSSTAND, SUBSCRIPTION, SUBSCRIPTION_EVENT, SUBSCRIBER] |
| **filterVendorNumber** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;vendorNumber&#39; | |
| **filterReportDate** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;reportDate&#39; | [optional] |
| **filterVersion** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;version&#39; | [optional] |

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
| **200** | List of SalesReports |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

