# CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ValidateResetPasswordLinkTokenGet**](CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi.md#customerAccountManagementV1ValidateResetPasswordLinkTokenGet) | **GET** /V1/customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken} | customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken} |


<a id="customerAccountManagementV1ValidateResetPasswordLinkTokenGet"></a>
# **customerAccountManagementV1ValidateResetPasswordLinkTokenGet**
> Boolean customerAccountManagementV1ValidateResetPasswordLinkTokenGet(customerId, resetPasswordLinkToken)

customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}

Check if password reset token is valid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi apiInstance = new CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi(defaultClient);
    Integer customerId = 56; // Integer | If 0 is given then a customer will be matched by the RP token.
    String resetPasswordLinkToken = "resetPasswordLinkToken_example"; // String | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1ValidateResetPasswordLinkTokenGet(customerId, resetPasswordLinkToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkTokenApi#customerAccountManagementV1ValidateResetPasswordLinkTokenGet");
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
| **customerId** | **Integer**| If 0 is given then a customer will be matched by the RP token. | |
| **resetPasswordLinkToken** | **String**|  | |

### Return type

**Boolean**

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

