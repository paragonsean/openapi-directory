# CustomersPasswordApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1InitiatePasswordResetPut**](CustomersPasswordApi.md#customerAccountManagementV1InitiatePasswordResetPut) | **PUT** /V1/customers/password | customers/password |


<a id="customerAccountManagementV1InitiatePasswordResetPut"></a>
# **customerAccountManagementV1InitiatePasswordResetPut**
> Boolean customerAccountManagementV1InitiatePasswordResetPut(customerAccountManagementV1InitiatePasswordResetPutRequest)

customers/password

Send an email to the customer with a password reset link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersPasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersPasswordApi apiInstance = new CustomersPasswordApi(defaultClient);
    CustomerAccountManagementV1InitiatePasswordResetPutRequest customerAccountManagementV1InitiatePasswordResetPutRequest = new CustomerAccountManagementV1InitiatePasswordResetPutRequest(); // CustomerAccountManagementV1InitiatePasswordResetPutRequest | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1InitiatePasswordResetPut(customerAccountManagementV1InitiatePasswordResetPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersPasswordApi#customerAccountManagementV1InitiatePasswordResetPut");
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
| **customerAccountManagementV1InitiatePasswordResetPutRequest** | [**CustomerAccountManagementV1InitiatePasswordResetPutRequest**](CustomerAccountManagementV1InitiatePasswordResetPutRequest.md)|  | [optional] |

### Return type

**Boolean**

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

