# CustomersApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1CreateAccountPost**](CustomersApi.md#customerAccountManagementV1CreateAccountPost) | **POST** /V1/customers | customers |


<a id="customerAccountManagementV1CreateAccountPost"></a>
# **customerAccountManagementV1CreateAccountPost**
> CustomerDataCustomerInterface customerAccountManagementV1CreateAccountPost(customerAccountManagementV1CreateAccountPostRequest)

customers

Create customer account. Perform necessary business operations like sending email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersApi apiInstance = new CustomersApi(defaultClient);
    CustomerAccountManagementV1CreateAccountPostRequest customerAccountManagementV1CreateAccountPostRequest = new CustomerAccountManagementV1CreateAccountPostRequest(); // CustomerAccountManagementV1CreateAccountPostRequest | 
    try {
      CustomerDataCustomerInterface result = apiInstance.customerAccountManagementV1CreateAccountPost(customerAccountManagementV1CreateAccountPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersApi#customerAccountManagementV1CreateAccountPost");
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
| **customerAccountManagementV1CreateAccountPostRequest** | [**CustomerAccountManagementV1CreateAccountPostRequest**](CustomerAccountManagementV1CreateAccountPostRequest.md)|  | [optional] |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

