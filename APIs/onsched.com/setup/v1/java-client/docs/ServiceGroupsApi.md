# ServiceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1ServicegroupsGet**](ServiceGroupsApi.md#setupV1ServicegroupsGet) | **GET** /setup/v1/servicegroups | List Service Groups |
| [**setupV1ServicegroupsIdDelete**](ServiceGroupsApi.md#setupV1ServicegroupsIdDelete) | **DELETE** /setup/v1/servicegroups/{id} | Delete Service Group |
| [**setupV1ServicegroupsIdGet**](ServiceGroupsApi.md#setupV1ServicegroupsIdGet) | **GET** /setup/v1/servicegroups/{id} | Get Service Group |
| [**setupV1ServicegroupsIdPut**](ServiceGroupsApi.md#setupV1ServicegroupsIdPut) | **PUT** /setup/v1/servicegroups/{id} | Update Service Group |
| [**setupV1ServicegroupsIdRecoverPut**](ServiceGroupsApi.md#setupV1ServicegroupsIdRecoverPut) | **PUT** /setup/v1/servicegroups/{id}/recover | Recover Service Group |
| [**setupV1ServicegroupsPost**](ServiceGroupsApi.md#setupV1ServicegroupsPost) | **POST** /setup/v1/servicegroups | Create Service Group |


<a id="setupV1ServicegroupsGet"></a>
# **setupV1ServicegroupsGet**
> ServiceGroupListViewModel setupV1ServicegroupsGet(locationId, offset, limit)

List Service Groups

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If no business location is specified it will default to the Primary Business Location of the company. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;

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
      ServiceGroupListViewModel result = apiInstance.setupV1ServicegroupsGet(locationId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#setupV1ServicegroupsGet");
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

<a id="setupV1ServicegroupsIdDelete"></a>
# **setupV1ServicegroupsIdDelete**
> ServiceGroupViewModel setupV1ServicegroupsIdDelete(id)

Delete Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Service Group object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. The service group is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/servicegroups​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

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
    Integer id = 56; // Integer | id of serviceGroup object
    try {
      ServiceGroupViewModel result = apiInstance.setupV1ServicegroupsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#setupV1ServicegroupsIdDelete");
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
| **id** | **Integer**| id of serviceGroup object | |

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

<a id="setupV1ServicegroupsIdGet"></a>
# **setupV1ServicegroupsIdGet**
> ServiceGroupViewModel setupV1ServicegroupsIdGet(id)

Get Service Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find service group id&#39;s by using the &lt;i&gt;GET /setup/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

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
    Integer id = 56; // Integer | id of serviceGroup object
    try {
      ServiceGroupViewModel result = apiInstance.setupV1ServicegroupsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#setupV1ServicegroupsIdGet");
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
| **id** | **Integer**| id of serviceGroup object | |

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

<a id="setupV1ServicegroupsIdPut"></a>
# **setupV1ServicegroupsIdPut**
> ServiceGroupViewModel setupV1ServicegroupsIdPut(id, serviceGroupInputModel)

Update Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Service Group object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. &lt;/p&gt;

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
    Integer id = 56; // Integer | id of serviceGroup object
    ServiceGroupInputModel serviceGroupInputModel = new ServiceGroupInputModel(); // ServiceGroupInputModel | 
    try {
      ServiceGroupViewModel result = apiInstance.setupV1ServicegroupsIdPut(id, serviceGroupInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#setupV1ServicegroupsIdPut");
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
| **id** | **Integer**| id of serviceGroup object | |
| **serviceGroupInputModel** | [**ServiceGroupInputModel**](ServiceGroupInputModel.md)|  | [optional] |

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1ServicegroupsIdRecoverPut"></a>
# **setupV1ServicegroupsIdRecoverPut**
> ServiceGroupViewModel setupV1ServicegroupsIdRecoverPut(id)

Recover Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted Service Group. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. &lt;/p&gt;

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
    Integer id = 56; // Integer | id of serviceGroup object
    try {
      ServiceGroupViewModel result = apiInstance.setupV1ServicegroupsIdRecoverPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#setupV1ServicegroupsIdRecoverPut");
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
| **id** | **Integer**| id of serviceGroup object | |

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

<a id="setupV1ServicegroupsPost"></a>
# **setupV1ServicegroupsPost**
> ServiceGroupViewModel setupV1ServicegroupsPost(serviceGroupInputModel)

Create Service Group

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Service Group. If no locationId is specified in the body, the business location will default to the primary business location. Service groups are used to categorize services. Service groups are optional and only make sense if you have multiple services that will be easier read if categorized. Only the service group Type of 0 is supported by the API. It defaults to 0 if not supplied.&lt;/p&gt;

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
    ServiceGroupInputModel serviceGroupInputModel = new ServiceGroupInputModel(); // ServiceGroupInputModel | 
    try {
      ServiceGroupViewModel result = apiInstance.setupV1ServicegroupsPost(serviceGroupInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceGroupsApi#setupV1ServicegroupsPost");
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
| **serviceGroupInputModel** | [**ServiceGroupInputModel**](ServiceGroupInputModel.md)|  | [optional] |

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

