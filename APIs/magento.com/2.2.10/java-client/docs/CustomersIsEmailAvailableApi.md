# CustomersIsEmailAvailableApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1IsEmailAvailablePost**](CustomersIsEmailAvailableApi.md#customerAccountManagementV1IsEmailAvailablePost) | **POST** /V1/customers/isEmailAvailable | customers/isEmailAvailable |


<a id="customerAccountManagementV1IsEmailAvailablePost"></a>
# **customerAccountManagementV1IsEmailAvailablePost**
> Boolean customerAccountManagementV1IsEmailAvailablePost(customerAccountManagementV1IsEmailAvailablePostRequest)

customers/isEmailAvailable

Check if given email is associated with a customer account in given website.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersIsEmailAvailableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersIsEmailAvailableApi apiInstance = new CustomersIsEmailAvailableApi(defaultClient);
    CustomerAccountManagementV1IsEmailAvailablePostRequest customerAccountManagementV1IsEmailAvailablePostRequest = new CustomerAccountManagementV1IsEmailAvailablePostRequest(); // CustomerAccountManagementV1IsEmailAvailablePostRequest | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1IsEmailAvailablePost(customerAccountManagementV1IsEmailAvailablePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersIsEmailAvailableApi#customerAccountManagementV1IsEmailAvailablePost");
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
| **customerAccountManagementV1IsEmailAvailablePostRequest** | [**CustomerAccountManagementV1IsEmailAvailablePostRequest**](CustomerAccountManagementV1IsEmailAvailablePostRequest.md)|  | [optional] |

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

