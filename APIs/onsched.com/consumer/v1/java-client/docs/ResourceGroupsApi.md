# ResourceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1ResourcegroupsGet**](ResourceGroupsApi.md#consumerV1ResourcegroupsGet) | **GET** /consumer/v1/resourcegroups | List Resource Groups |
| [**consumerV1ResourcegroupsIdGet**](ResourceGroupsApi.md#consumerV1ResourcegroupsIdGet) | **GET** /consumer/v1/resourcegroups/{id} | Get Resource Group |


<a id="consumerV1ResourcegroupsGet"></a>
# **consumerV1ResourcegroupsGet**
> ResourceGroupListViewModel consumerV1ResourcegroupsGet(locationId, deleted, offset, limit)

List Resource Groups

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Boolean deleted = true; // Boolean | Filter results by deleted status
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceGroupListViewModel result = apiInstance.consumerV1ResourcegroupsGet(locationId, deleted, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#consumerV1ResourcegroupsGet");
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
| **deleted** | **Boolean**| Filter results by deleted status | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ResourceGroupListViewModel**](ResourceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1ResourcegroupsIdGet"></a>
# **consumerV1ResourcegroupsIdGet**
> ResourceGroupViewModel consumerV1ResourcegroupsIdGet(id)

Get Resource Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Group&lt;/b&gt; object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. Find resourceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/resourceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourceGroupsApi apiInstance = new ResourceGroupsApi(defaultClient);
    String id = "id_example"; // String | id of the resourceGroup object
    try {
      ResourceGroupViewModel result = apiInstance.consumerV1ResourcegroupsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceGroupsApi#consumerV1ResourcegroupsIdGet");
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
| **id** | **String**| id of the resourceGroup object | |

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

