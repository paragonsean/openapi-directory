# CustomersMeActivateApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ActivateByIdPut**](CustomersMeActivateApi.md#customerAccountManagementV1ActivateByIdPut) | **PUT** /V1/customers/me/activate | customers/me/activate |


<a id="customerAccountManagementV1ActivateByIdPut"></a>
# **customerAccountManagementV1ActivateByIdPut**
> CustomerDataCustomerInterface customerAccountManagementV1ActivateByIdPut(customerAccountManagementV1ActivateByIdPutRequest)

customers/me/activate

Activate a customer account using a key that was sent in a confirmation email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersMeActivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersMeActivateApi apiInstance = new CustomersMeActivateApi(defaultClient);
    CustomerAccountManagementV1ActivateByIdPutRequest customerAccountManagementV1ActivateByIdPutRequest = new CustomerAccountManagementV1ActivateByIdPutRequest(); // CustomerAccountManagementV1ActivateByIdPutRequest | 
    try {
      CustomerDataCustomerInterface result = apiInstance.customerAccountManagementV1ActivateByIdPut(customerAccountManagementV1ActivateByIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersMeActivateApi#customerAccountManagementV1ActivateByIdPut");
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

