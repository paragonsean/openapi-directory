# ExportApi

All URIs are relative to *https://api.slideroom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportGetV2**](ExportApi.md#exportGetV2) | **GET** /api/v2/export/{token} | Gets the status/result of a requested export. |


<a id="exportGetV2"></a>
# **exportGetV2**
> ExportResultV2 exportGetV2(token)

Gets the status/result of a requested export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ExportApi apiInstance = new ExportApi(defaultClient);
    Integer token = 56; // Integer | 
    try {
      ExportResultV2 result = apiInstance.exportGetV2(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportApi#exportGetV2");
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
| **token** | **Integer**|  | |

### Return type

[**ExportResultV2**](ExportResultV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

