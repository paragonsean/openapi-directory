# CustomerGroupsDefaultStoreIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CustomerGroupsDefaultStoreIdGet**](CustomerGroupsDefaultStoreIdApi.md#v1CustomerGroupsDefaultStoreIdGet) | **GET** /V1/customerGroups/default/{storeId} | customerGroups/default/{storeId} |


<a id="v1CustomerGroupsDefaultStoreIdGet"></a>
# **v1CustomerGroupsDefaultStoreIdGet**
> CustomerDataGroupInterface v1CustomerGroupsDefaultStoreIdGet(storeId)

customerGroups/default/{storeId}

Get default customer group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsDefaultStoreIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomerGroupsDefaultStoreIdApi apiInstance = new CustomerGroupsDefaultStoreIdApi(defaultClient);
    Integer storeId = 56; // Integer | 
    try {
      CustomerDataGroupInterface result = apiInstance.v1CustomerGroupsDefaultStoreIdGet(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsDefaultStoreIdApi#v1CustomerGroupsDefaultStoreIdGet");
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
| **storeId** | **Integer**|  | |

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

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

