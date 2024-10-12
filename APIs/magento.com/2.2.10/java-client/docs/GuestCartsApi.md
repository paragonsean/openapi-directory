# GuestCartsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartManagementV1CreateEmptyCartPost**](GuestCartsApi.md#quoteGuestCartManagementV1CreateEmptyCartPost) | **POST** /V1/guest-carts | guest-carts |


<a id="quoteGuestCartManagementV1CreateEmptyCartPost"></a>
# **quoteGuestCartManagementV1CreateEmptyCartPost**
> String quoteGuestCartManagementV1CreateEmptyCartPost()

guest-carts

Enable an customer or guest user to create an empty cart and quote for an anonymous customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsApi apiInstance = new GuestCartsApi(defaultClient);
    try {
      String result = apiInstance.quoteGuestCartManagementV1CreateEmptyCartPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsApi#quoteGuestCartManagementV1CreateEmptyCartPost");
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

**String**

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
| **0** | Unexpected error |  -  |

