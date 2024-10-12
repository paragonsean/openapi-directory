# CustomerGroupsDefaultIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerCustomerGroupConfigV1SetDefaultCustomerGroupPut**](CustomerGroupsDefaultIdApi.md#customerCustomerGroupConfigV1SetDefaultCustomerGroupPut) | **PUT** /V1/customerGroups/default/{id} | customerGroups/default/{id} |


<a id="customerCustomerGroupConfigV1SetDefaultCustomerGroupPut"></a>
# **customerCustomerGroupConfigV1SetDefaultCustomerGroupPut**
> Integer customerCustomerGroupConfigV1SetDefaultCustomerGroupPut(id)

customerGroups/default/{id}

Set system default customer group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsDefaultIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsDefaultIdApi apiInstance = new CustomerGroupsDefaultIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Integer result = apiInstance.customerCustomerGroupConfigV1SetDefaultCustomerGroupPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsDefaultIdApi#customerCustomerGroupConfigV1SetDefaultCustomerGroupPut");
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
| **id** | **Integer**|  | |

### Return type

**Integer**

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

