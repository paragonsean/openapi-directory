# ServicesApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1ServicesAllocationsIdGet**](ServicesApi.md#consumerV1ServicesAllocationsIdGet) | **GET** /consumer/v1/services/allocations/{id} | Get Service Allocation |
| [**consumerV1ServicesGet**](ServicesApi.md#consumerV1ServicesGet) | **GET** /consumer/v1/services | List Services |
| [**consumerV1ServicesIdAllocationsGet**](ServicesApi.md#consumerV1ServicesIdAllocationsGet) | **GET** /consumer/v1/services/{id}/allocations | List Service Allocations |
| [**consumerV1ServicesIdGet**](ServicesApi.md#consumerV1ServicesIdGet) | **GET** /consumer/v1/services/{id} | Get Service |
| [**consumerV1ServicesIdResourcesGet**](ServicesApi.md#consumerV1ServicesIdResourcesGet) | **GET** /consumer/v1/services/{id}/resources | List Resources for Service |


<a id="consumerV1ServicesAllocationsIdGet"></a>
# **consumerV1ServicesAllocationsIdGet**
> ServiceAllocationViewModel consumerV1ServicesAllocationsIdGet(id)

Get Service Allocation

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Allocation&lt;/b&gt; object. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required. Find service allocation id&#39;s by using the &lt;i&gt;GET/consumer​/v1​/services​/{id}​/allocations&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String id = "id_example"; // String | id of serviceAllocation object
    try {
      ServiceAllocationViewModel result = apiInstance.consumerV1ServicesAllocationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#consumerV1ServicesAllocationsIdGet");
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
| **id** | **String**| id of serviceAllocation object | |

### Return type

[**ServiceAllocationViewModel**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1ServicesGet"></a>
# **consumerV1ServicesGet**
> ServiceListViewModel consumerV1ServicesGet(locationId, serviceGroupId, defaultService, allLocations, scope, name, serviceId, offset, limit, sortOrder, sortDescending)

List Services

&lt;p&gt;Use this endpoint to &lt;b&gt;List Services&lt;/b&gt; available at your business location and/or company. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Integer serviceGroupId = 56; // Integer | Filter by groupId
    Boolean defaultService = true; // Boolean | Filter by default service, default is false
    Boolean allLocations = true; // Boolean | Search All Locations, default is false
    ServicesScope scope = ServicesScope.fromValue("company"); // ServicesScope | Filter by scope, Company, Location or All, default is All
    String name = "name_example"; // String | Filter by Name, supports Partial name search
    String serviceId = "serviceId_example"; // String | Filter by ServiceId, using this parameter would ignore all other parameters
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    ServiceSortOrder sortOrder = ServiceSortOrder.fromValue("natural"); // ServiceSortOrder | Sort results using Natural Sort or Sorted alphabetically by Service Names, default is natural
    Boolean sortDescending = true; // Boolean | Sort results in Descending Order, default true
    try {
      ServiceListViewModel result = apiInstance.consumerV1ServicesGet(locationId, serviceGroupId, defaultService, allLocations, scope, name, serviceId, offset, limit, sortOrder, sortDescending);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#consumerV1ServicesGet");
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
| **serviceGroupId** | **Integer**| Filter by groupId | [optional] |
| **defaultService** | **Boolean**| Filter by default service, default is false | [optional] |
| **allLocations** | **Boolean**| Search All Locations, default is false | [optional] |
| **scope** | [**ServicesScope**](.md)| Filter by scope, Company, Location or All, default is All | [optional] [enum: company, location, all] |
| **name** | **String**| Filter by Name, supports Partial name search | [optional] |
| **serviceId** | **String**| Filter by ServiceId, using this parameter would ignore all other parameters | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |
| **sortOrder** | [**ServiceSortOrder**](.md)| Sort results using Natural Sort or Sorted alphabetically by Service Names, default is natural | [optional] [enum: natural, name] |
| **sortDescending** | **Boolean**| Sort results in Descending Order, default true | [optional] |

### Return type

[**ServiceListViewModel**](ServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1ServicesIdAllocationsGet"></a>
# **consumerV1ServicesIdAllocationsGet**
> ServiceAllocationListViewModel consumerV1ServicesIdAllocationsGet(id, locationId, resourceId, startDate, endDate, offset, limit)

List Service Allocations

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service Allocations&lt;/b&gt; associated with the requested service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Allocations are used for Event type services/bookings. Retrieve all allocations for a location by passing in zero as the service id. Otherwise, to get allocations for a specific service supply the service id. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: &lt;a href&#x3D;\&quot;https://docs.onsched.com/reference/post_setup-v1-services-id-allocations\&quot;&gt;Create Service Allocations&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String id = "id_example"; // String | id of service to list allocations for, 0 for all
    String locationId = "locationId_example"; // String | id of the location, defaults to the primary location
    String resourceId = "resourceId_example"; // String | id of the resource to filter on
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: Filter allocations on/after startDate
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD. Filter allocations on/before endDate
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ServiceAllocationListViewModel result = apiInstance.consumerV1ServicesIdAllocationsGet(id, locationId, resourceId, startDate, endDate, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#consumerV1ServicesIdAllocationsGet");
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
| **id** | **String**| id of service to list allocations for, 0 for all | |
| **locationId** | **String**| id of the location, defaults to the primary location | [optional] |
| **resourceId** | **String**| id of the resource to filter on | [optional] |
| **startDate** | **OffsetDateTime**| Format YYYY-MM-DD: Filter allocations on/after startDate | [optional] |
| **endDate** | **OffsetDateTime**| Format YYYY-MM-DD. Filter allocations on/before endDate | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**ServiceAllocationListViewModel**](ServiceAllocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | service alloaction object |  -  |
| **400** | Missing or invalid values in the request |  -  |
| **401** | Authorization error. |  -  |
| **404** | Service was not found |  -  |

<a id="consumerV1ServicesIdGet"></a>
# **consumerV1ServicesIdGet**
> ServiceViewModel consumerV1ServicesIdGet(id)

Get Service

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service&lt;/b&gt; object. A valid &lt;b&gt;service id&lt;/b&gt; is required. Find service id&#39;s by using the &lt;i&gt;GET /consumer/v1/services&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    Integer id = 56; // Integer | id of service object
    try {
      ServiceViewModel result = apiInstance.consumerV1ServicesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#consumerV1ServicesIdGet");
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
| **id** | **Integer**| id of service object | |

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1ServicesIdResourcesGet"></a>
# **consumerV1ServicesIdResourcesGet**
> ResourceListViewModel consumerV1ServicesIdResourcesGet(id, locationId, offset, limit)

List Resources for Service

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resources that provide the Service requested&lt;/b&gt;. A valid &lt;b&gt;service id&lt;/b&gt; is required. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String id = "id_example"; // String | id of service object
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      ResourceListViewModel result = apiInstance.consumerV1ServicesIdResourcesGet(id, locationId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#consumerV1ServicesIdResourcesGet");
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
| **id** | **String**| id of service object | |
| **locationId** | **String**| id of business location, defaults to primary business location | [optional] |
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
| **200** | Success |  -  |

