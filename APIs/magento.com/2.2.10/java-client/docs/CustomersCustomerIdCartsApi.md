# CustomersCustomerIdCartsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CustomersCustomerIdCartsPost**](CustomersCustomerIdCartsApi.md#v1CustomersCustomerIdCartsPost) | **POST** /V1/customers/{customerId}/carts | customers/{customerId}/carts |


<a id="v1CustomersCustomerIdCartsPost"></a>
# **v1CustomersCustomerIdCartsPost**
> Integer v1CustomersCustomerIdCartsPost(customerId)

customers/{customerId}/carts

Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdCartsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdCartsApi apiInstance = new CustomersCustomerIdCartsApi(defaultClient);
    Integer customerId = 56; // Integer | The customer ID.
    try {
      Integer result = apiInstance.v1CustomersCustomerIdCartsPost(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdCartsApi#v1CustomersCustomerIdCartsPost");
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
| **customerId** | **Integer**| The customer ID. | |

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

