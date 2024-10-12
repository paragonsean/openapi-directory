# CustomersEmailActivateApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ActivatePut**](CustomersEmailActivateApi.md#customerAccountManagementV1ActivatePut) | **PUT** /V1/customers/{email}/activate | customers/{email}/activate |


<a id="customerAccountManagementV1ActivatePut"></a>
# **customerAccountManagementV1ActivatePut**
> CustomerDataCustomerInterface customerAccountManagementV1ActivatePut(email, customerAccountManagementV1ActivateByIdPutRequest)

customers/{email}/activate

Activate a customer account using a key that was sent in a confirmation email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersEmailActivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersEmailActivateApi apiInstance = new CustomersEmailActivateApi(defaultClient);
    String email = "email_example"; // String | 
    CustomerAccountManagementV1ActivateByIdPutRequest customerAccountManagementV1ActivateByIdPutRequest = new CustomerAccountManagementV1ActivateByIdPutRequest(); // CustomerAccountManagementV1ActivateByIdPutRequest | 
    try {
      CustomerDataCustomerInterface result = apiInstance.customerAccountManagementV1ActivatePut(email, customerAccountManagementV1ActivateByIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersEmailActivateApi#customerAccountManagementV1ActivatePut");
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
| **email** | **String**|  | |
| **customerAccountManagementV1ActivateByIdPutRequest** | [**CustomerAccountManagementV1ActivateByIdPutRequest**](CustomerAccountManagementV1ActivateByIdPutRequest.md)|  | [optional] |

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

