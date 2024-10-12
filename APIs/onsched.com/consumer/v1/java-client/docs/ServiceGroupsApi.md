# ServiceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1ServicegroupsGet**](ServiceGroupsApi.md#consumerV1ServicegroupsGet) | **GET** /consumer/v1/servicegroups | List Service Groups |
| [**consumerV1ServicegroupsIdGet**](ServiceGroupsApi.md#consumerV1ServicegroupsIdGet) | **GET** /consumer/v1/servicegroups/{id} | Get Service Group |


<a id="consumerV1ServicegroupsGet"></a>
# **consumerV1ServicegroupsGet**
> ServiceGroupListViewModel consumerV1ServicegroupsGet(locationId, offset, limit)

List Service Groups

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServiceGroupsApi apiInstance = new ServiceGroupsApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ServiceGroupListViewModel result = apiInstance.consumerV1ServicegroupsGet(locationId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#consumerV1ServicegroupsGet");
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
| **locationId** | **String**| id of business location, defaults to primary business location | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ServiceGroupListViewModel**](ServiceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1ServicegroupsIdGet"></a>
# **consumerV1ServicegroupsIdGet**
> ServiceGroupViewModel consumerV1ServicegroupsIdGet(id)

Get Service Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find serviceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServiceGroupsApi apiInstance = new ServiceGroupsApi(defaultClient);
    Integer id = 56; // Integer | id of the serviceGroup object
    try {
      ServiceGroupViewModel result = apiInstance.consumerV1ServicegroupsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#consumerV1ServicegroupsIdGet");
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
| **id** | **Integer**| id of the serviceGroup object | |

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

