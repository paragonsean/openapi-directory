# CustomersCustomerIdConfirmApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1GetConfirmationStatusGet**](CustomersCustomerIdConfirmApi.md#customerAccountManagementV1GetConfirmationStatusGet) | **GET** /V1/customers/{customerId}/confirm | customers/{customerId}/confirm |


<a id="customerAccountManagementV1GetConfirmationStatusGet"></a>
# **customerAccountManagementV1GetConfirmationStatusGet**
> String customerAccountManagementV1GetConfirmationStatusGet(customerId)

customers/{customerId}/confirm

Gets the account confirmation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdConfirmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdConfirmApi apiInstance = new CustomersCustomerIdConfirmApi(defaultClient);
    Integer customerId = 56; // Integer | 
    try {
      String result = apiInstance.customerAccountManagementV1GetConfirmationStatusGet(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdConfirmApi#customerAccountManagementV1GetConfirmationStatusGet");
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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

