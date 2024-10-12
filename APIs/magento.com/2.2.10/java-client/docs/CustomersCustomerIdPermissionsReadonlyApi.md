# CustomersCustomerIdPermissionsReadonlyApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1IsReadonlyGet**](CustomersCustomerIdPermissionsReadonlyApi.md#customerAccountManagementV1IsReadonlyGet) | **GET** /V1/customers/{customerId}/permissions/readonly | customers/{customerId}/permissions/readonly |


<a id="customerAccountManagementV1IsReadonlyGet"></a>
# **customerAccountManagementV1IsReadonlyGet**
> Boolean customerAccountManagementV1IsReadonlyGet(customerId)

customers/{customerId}/permissions/readonly

Check if customer can be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersCustomerIdPermissionsReadonlyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersCustomerIdPermissionsReadonlyApi apiInstance = new CustomersCustomerIdPermissionsReadonlyApi(defaultClient);
    Integer customerId = 56; // Integer | 
    try {
      Boolean result = apiInstance.customerAccountManagementV1IsReadonlyGet(customerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersCustomerIdPermissionsReadonlyApi#customerAccountManagementV1IsReadonlyGet");
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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

