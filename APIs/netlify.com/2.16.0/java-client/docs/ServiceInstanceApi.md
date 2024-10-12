# ServiceInstanceApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createServiceInstance**](ServiceInstanceApi.md#createServiceInstance) | **POST** /sites/{site_id}/services/{addon}/instances |  |
| [**deleteServiceInstance**](ServiceInstanceApi.md#deleteServiceInstance) | **DELETE** /sites/{site_id}/services/{addon}/instances/{instance_id} |  |
| [**listServiceInstancesForSite**](ServiceInstanceApi.md#listServiceInstancesForSite) | **GET** /sites/{site_id}/service-instances |  |
| [**showServiceInstance**](ServiceInstanceApi.md#showServiceInstance) | **GET** /sites/{site_id}/services/{addon}/instances/{instance_id} |  |
| [**updateServiceInstance**](ServiceInstanceApi.md#updateServiceInstance) | **PUT** /sites/{site_id}/services/{addon}/instances/{instance_id} |  |


<a id="createServiceInstance"></a>
# **createServiceInstance**
> ServiceInstance createServiceInstance(siteId, addon, config)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceInstanceApi apiInstance = new ServiceInstanceApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String addon = "addon_example"; // String | 
    Object config = null; // Object | 
    try {
      ServiceInstance result = apiInstance.createServiceInstance(siteId, addon, config);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInstanceApi#createServiceInstance");
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
| **siteId** | **String**|  | |
| **addon** | **String**|  | |
| **config** | **Object**|  | |

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="deleteServiceInstance"></a>
# **deleteServiceInstance**
> deleteServiceInstance(siteId, addon, instanceId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceInstanceApi apiInstance = new ServiceInstanceApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String addon = "addon_example"; // String | 
    String instanceId = "instanceId_example"; // String | 
    try {
      apiInstance.deleteServiceInstance(siteId, addon, instanceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInstanceApi#deleteServiceInstance");
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
| **siteId** | **String**|  | |
| **addon** | **String**|  | |
| **instanceId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **0** | error |  -  |

<a id="listServiceInstancesForSite"></a>
# **listServiceInstancesForSite**
> List&lt;ServiceInstance&gt; listServiceInstancesForSite(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceInstanceApi apiInstance = new ServiceInstanceApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<ServiceInstance> result = apiInstance.listServiceInstancesForSite(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInstanceApi#listServiceInstancesForSite");
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
| **siteId** | **String**|  | |

### Return type

[**List&lt;ServiceInstance&gt;**](ServiceInstance.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="showServiceInstance"></a>
# **showServiceInstance**
> ServiceInstance showServiceInstance(siteId, addon, instanceId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceInstanceApi apiInstance = new ServiceInstanceApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String addon = "addon_example"; // String | 
    String instanceId = "instanceId_example"; // String | 
    try {
      ServiceInstance result = apiInstance.showServiceInstance(siteId, addon, instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInstanceApi#showServiceInstance");
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
| **siteId** | **String**|  | |
| **addon** | **String**|  | |
| **instanceId** | **String**|  | |

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="updateServiceInstance"></a>
# **updateServiceInstance**
> updateServiceInstance(siteId, addon, instanceId, config)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceInstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceInstanceApi apiInstance = new ServiceInstanceApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String addon = "addon_example"; // String | 
    String instanceId = "instanceId_example"; // String | 
    Object config = null; // Object | 
    try {
      apiInstance.updateServiceInstance(siteId, addon, instanceId, config);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceInstanceApi#updateServiceInstance");
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
| **siteId** | **String**|  | |
| **addon** | **String**|  | |
| **instanceId** | **String**|  | |
| **config** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | error |  -  |

