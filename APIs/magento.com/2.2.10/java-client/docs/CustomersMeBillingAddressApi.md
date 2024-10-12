# CustomersMeBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1GetDefaultBillingAddressGet**](CustomersMeBillingAddressApi.md#customerAccountManagementV1GetDefaultBillingAddressGet) | **GET** /V1/customers/me/billingAddress | customers/me/billingAddress |


<a id="customerAccountManagementV1GetDefaultBillingAddressGet"></a>
# **customerAccountManagementV1GetDefaultBillingAddressGet**
> CustomerDataAddressInterface customerAccountManagementV1GetDefaultBillingAddressGet()

customers/me/billingAddress

Retrieve default billing address for the given customerId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersMeBillingAddressApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersMeBillingAddressApi apiInstance = new CustomersMeBillingAddressApi(defaultClient);
    try {
      CustomerDataAddressInterface result = apiInstance.customerAccountManagementV1GetDefaultBillingAddressGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersMeBillingAddressApi#customerAccountManagementV1GetDefaultBillingAddressGet");
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

