# ProductDetailsApi

All URIs are relative to *http://dropx.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsGet**](ProductDetailsApi.md#productsGet) | **GET** /products/ | Get product details by providing the product IDs |


<a id="productsGet"></a>
# **productsGet**
> productsGet(pids)

Get product details by providing the product IDs

Returns product details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ProductDetailsApi apiInstance = new ProductDetailsApi(defaultClient);
    String pids = "pids_example"; // String | search array of ids
    try {
      apiInstance.productsGet(pids);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDetailsApi#productsGet");
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
| **pids** | **String**| search array of ids | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of search details |  -  |
| **401** | Invalid authentication |  -  |
| **456** | We are sorry, You have reached your limit |  -  |
| **458** | Oops...! we don\\&#39;t have enough data to serve your request |  -  |
| **459** | Oops...! Missing reqired \&quot;pids\&quot; parameter to serve your request |  -  |
| **464** | Error in finding default plan |  -  |
| **490** | Unexpected error occurred while processing your request |  -  |
| **500** | internal server error |  -  |

