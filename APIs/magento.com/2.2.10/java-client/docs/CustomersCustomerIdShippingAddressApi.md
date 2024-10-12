# CustomersCustomerIdShippingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CustomersCustomerIdShippingAddressGet**](CustomersCustomerIdShippingAddressApi.md#v1CustomersCustomerIdShippingAddressGet) | **GET** /V1/customers/{customerId}/shippingAddress | customers/{customerId}/shippingAddress |


<a id="v1CustomersCustomerIdShippingAddressGet"></a>
# **v1CustomersCustomerIdShippingAddressGet**
> CustomerDataAddressInterface v1CustomersCustomerIdShippingAddressGet(customerId)

customers/{customerId}/shippingAddress

Retrieve default shipping address for the given customerId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdShippingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdShippingAddressApi apiInstance = new CustomersCustomerIdShippingAddressApi(defaultClient);
    Integer customerId = 56; // Integer | 
    try {
      CustomerDataAddressInterface result = apiInstance.v1CustomersCustomerIdShippingAddressGet(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdShippingAddressApi#v1CustomersCustomerIdShippingAddressGet");
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
| **customerId** | **Integer**|  | |

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

