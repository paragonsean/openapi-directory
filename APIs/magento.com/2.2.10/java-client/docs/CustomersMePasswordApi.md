# CustomersMePasswordApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ChangePasswordByIdPut**](CustomersMePasswordApi.md#customerAccountManagementV1ChangePasswordByIdPut) | **PUT** /V1/customers/me/password | customers/me/password |


<a id="customerAccountManagementV1ChangePasswordByIdPut"></a>
# **customerAccountManagementV1ChangePasswordByIdPut**
> Boolean customerAccountManagementV1ChangePasswordByIdPut(customerAccountManagementV1ChangePasswordByIdPutRequest)

customers/me/password

Change customer password.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersMePasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersMePasswordApi apiInstance = new CustomersMePasswordApi(defaultClient);
    CustomerAccountManagementV1ChangePasswordByIdPutRequest customerAccountManagementV1ChangePasswordByIdPutRequest = new CustomerAccountManagementV1ChangePasswordByIdPutRequest(); // CustomerAccountManagementV1ChangePasswordByIdPutRequest | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1ChangePasswordByIdPut(customerAccountManagementV1ChangePasswordByIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersMePasswordApi#customerAccountManagementV1ChangePasswordByIdPut");
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
| **customerAccountManagementV1ChangePasswordByIdPutRequest** | [**CustomerAccountManagementV1ChangePasswordByIdPutRequest**](CustomerAccountManagementV1ChangePasswordByIdPutRequest.md)|  | [optional] |

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

