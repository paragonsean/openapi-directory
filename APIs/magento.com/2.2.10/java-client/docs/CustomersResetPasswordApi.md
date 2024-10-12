# CustomersResetPasswordApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ResetPasswordPost**](CustomersResetPasswordApi.md#customerAccountManagementV1ResetPasswordPost) | **POST** /V1/customers/resetPassword | customers/resetPassword |


<a id="customerAccountManagementV1ResetPasswordPost"></a>
# **customerAccountManagementV1ResetPasswordPost**
> Boolean customerAccountManagementV1ResetPasswordPost(customerAccountManagementV1ResetPasswordPostRequest)

customers/resetPassword

Reset customer password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersResetPasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersResetPasswordApi apiInstance = new CustomersResetPasswordApi(defaultClient);
    CustomerAccountManagementV1ResetPasswordPostRequest customerAccountManagementV1ResetPasswordPostRequest = new CustomerAccountManagementV1ResetPasswordPostRequest(); // CustomerAccountManagementV1ResetPasswordPostRequest | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1ResetPasswordPost(customerAccountManagementV1ResetPasswordPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersResetPasswordApi#customerAccountManagementV1ResetPasswordPost");
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
| **customerAccountManagementV1ResetPasswordPostRequest** | [**CustomerAccountManagementV1ResetPasswordPostRequest**](CustomerAccountManagementV1ResetPasswordPostRequest.md)|  | [optional] |

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

