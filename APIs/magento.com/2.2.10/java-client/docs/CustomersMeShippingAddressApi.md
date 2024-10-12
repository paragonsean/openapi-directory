# CustomersMeShippingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1GetDefaultShippingAddressGet**](CustomersMeShippingAddressApi.md#customerAccountManagementV1GetDefaultShippingAddressGet) | **GET** /V1/customers/me/shippingAddress | customers/me/shippingAddress |


<a id="customerAccountManagementV1GetDefaultShippingAddressGet"></a>
# **customerAccountManagementV1GetDefaultShippingAddressGet**
> CustomerDataAddressInterface customerAccountManagementV1GetDefaultShippingAddressGet()

customers/me/shippingAddress

Retrieve default shipping address for the given customerId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersMeShippingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersMeShippingAddressApi apiInstance = new CustomersMeShippingAddressApi(defaultClient);
    try {
      CustomerDataAddressInterface result = apiInstance.customerAccountManagementV1GetDefaultShippingAddressGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersMeShippingAddressApi#customerAccountManagementV1GetDefaultShippingAddressGet");
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

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

