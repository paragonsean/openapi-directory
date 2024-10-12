# CustomersConfirmApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ResendConfirmationPost**](CustomersConfirmApi.md#customerAccountManagementV1ResendConfirmationPost) | **POST** /V1/customers/confirm | customers/confirm |


<a id="customerAccountManagementV1ResendConfirmationPost"></a>
# **customerAccountManagementV1ResendConfirmationPost**
> Boolean customerAccountManagementV1ResendConfirmationPost(customerAccountManagementV1ResendConfirmationPostRequest)

customers/confirm

Resend confirmation email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersConfirmApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersConfirmApi apiInstance = new CustomersConfirmApi(defaultClient);
    CustomerAccountManagementV1ResendConfirmationPostRequest customerAccountManagementV1ResendConfirmationPostRequest = new CustomerAccountManagementV1ResendConfirmationPostRequest(); // CustomerAccountManagementV1ResendConfirmationPostRequest | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1ResendConfirmationPost(customerAccountManagementV1ResendConfirmationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersConfirmApi#customerAccountManagementV1ResendConfirmationPost");
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
| **customerAccountManagementV1ResendConfirmationPostRequest** | [**CustomerAccountManagementV1ResendConfirmationPostRequest**](CustomerAccountManagementV1ResendConfirmationPostRequest.md)|  | [optional] |

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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

