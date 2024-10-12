# CartsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartManagementV1CreateEmptyCartPost**](CartsApi.md#quoteCartManagementV1CreateEmptyCartPost) | **POST** /V1/carts/ | carts/ |


<a id="quoteCartManagementV1CreateEmptyCartPost"></a>
# **quoteCartManagementV1CreateEmptyCartPost**
> Integer quoteCartManagementV1CreateEmptyCartPost()

carts/

Creates an empty cart and quote for a guest.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsApi apiInstance = new CartsApi(defaultClient);
    try {
      Integer result = apiInstance.quoteCartManagementV1CreateEmptyCartPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsApi#quoteCartManagementV1CreateEmptyCartPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

