# ResourcesApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1ResourcesGet**](ResourcesApi.md#consumerV1ResourcesGet) | **GET** /consumer/v1/resources | List Resources |
| [**consumerV1ResourcesIdGet**](ResourcesApi.md#consumerV1ResourcesIdGet) | **GET** /consumer/v1/resources/{id} | Get Resource |
| [**consumerV1ResourcesIdServicesGet**](ResourcesApi.md#consumerV1ResourcesIdServicesGet) | **GET** /consumer/v1/resources/{id}/services | Get Resource Linked Services |


<a id="consumerV1ResourcesGet"></a>
# **consumerV1ResourcesGet**
> ResourceListViewModel consumerV1ResourcesGet(locationId, resourceGroupId, email, name, sortOrder, offset, limit)

List Resources

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Resources&lt;/b&gt; associated with a business location. If not specified, the business location defaults to the primary business location. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Integer resourceGroupId = 56; // Integer | Filter by groupId
    String email = "email_example"; // String | Filter by email address
    String name = "name_example"; // String | Search by name, supports Partial name search
    String sortOrder = "sortOrder_example"; // String | Specify sort order of response
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceListViewModel result = apiInstance.consumerV1ResourcesGet(locationId, resourceGroupId, email, name, sortOrder, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#consumerV1ResourcesGet");
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
| **resourceGroupId** | **Integer**| Filter by groupId | [optional] |
| **email** | **String**| Filter by email address | [optional] |
| **name** | **String**| Search by name, supports Partial name search | [optional] |
| **sortOrder** | **String**| Specify sort order of response | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ResourceListViewModel**](ResourceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | resource object |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **404** | Resource was not found |  -  |

<a id="consumerV1ResourcesIdGet"></a>
# **consumerV1ResourcesIdGet**
> ResourceViewModel consumerV1ResourcesIdGet(id)

Get Resource

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource&lt;/b&gt; object. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Find resource id&#39;s by using the &lt;i&gt;GET consumer/v1/resources&lt;/i&gt; endpoint. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    Integer id = 56; // Integer | id of resource object
    try {
      ResourceViewModel result = apiInstance.consumerV1ResourcesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#consumerV1ResourcesIdGet");
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
| **id** | **Integer**| id of resource object | |

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1ResourcesIdServicesGet"></a>
# **consumerV1ResourcesIdServicesGet**
> ResourceServiceListViewModel consumerV1ResourcesIdServicesGet(id, offset, limit)

Get Resource Linked Services

&lt;p&gt;Use this endpoint to get a &lt;b&gt;List of Linked Services&lt;/b&gt; associated with the resource requested. The results are returned in pages. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, the maximum limit is 100. Use the other query parameters to filter the results further.&lt;/p&gt;  &lt;p&gt;Resource linked services are used to explicitly define the services that can be booked for a specified resource. By default, all services are bookable for any resource. For more information: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/linked-services\&quot;&gt;Linked Services Overview&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    Integer id = 56; // Integer | id of resource object
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceServiceListViewModel result = apiInstance.consumerV1ResourcesIdServicesGet(id, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#consumerV1ResourcesIdServicesGet");
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
| **id** | **Integer**| id of resource object | |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ResourceServiceListViewModel**](ResourceServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of resource services |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Unauthorized request |  -  |
| **404** | Resource was not found |  -  |

