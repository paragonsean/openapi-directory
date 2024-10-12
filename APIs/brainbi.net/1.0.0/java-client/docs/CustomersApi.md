# CustomersApi

All URIs are relative to *http://,*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customers**](CustomersApi.md#customers) | **GET** /api/customers | Customers |


<a id="customers"></a>
# **customers**
> customers()

Customers

This resource lists all cusomters that are currently saved in your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.customers();
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customers");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

