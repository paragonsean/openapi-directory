# CustomerGroupsIdPermissionsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerGroupManagementV1IsReadonlyGet**](CustomerGroupsIdPermissionsApi.md#customerGroupManagementV1IsReadonlyGet) | **GET** /V1/customerGroups/{id}/permissions | customerGroups/{id}/permissions |


<a id="customerGroupManagementV1IsReadonlyGet"></a>
# **customerGroupManagementV1IsReadonlyGet**
> Boolean customerGroupManagementV1IsReadonlyGet(id)

customerGroups/{id}/permissions

Check if customer group can be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsIdPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsIdPermissionsApi apiInstance = new CustomerGroupsIdPermissionsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Boolean result = apiInstance.customerGroupManagementV1IsReadonlyGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsIdPermissionsApi#customerGroupManagementV1IsReadonlyGet");
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

