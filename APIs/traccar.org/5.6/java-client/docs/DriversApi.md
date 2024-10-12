# DriversApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**driversGet**](DriversApi.md#driversGet) | **GET** /drivers | Fetch a list of Drivers |
| [**driversIdDelete**](DriversApi.md#driversIdDelete) | **DELETE** /drivers/{id} | Delete a Driver |
| [**driversIdPut**](DriversApi.md#driversIdPut) | **PUT** /drivers/{id} | Update a Driver |
| [**driversPost**](DriversApi.md#driversPost) | **POST** /drivers | Create a Driver |


<a id="driversGet"></a>
# **driversGet**
> List&lt;Driver&gt; driversGet(all, userId, deviceId, groupId, refresh)

Fetch a list of Drivers

Without params, it returns a list of Drivers the user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DriversApi apiInstance = new DriversApi(defaultClient);
    Boolean all = true; // Boolean | Can only be used by admins or managers to fetch all entities
    Integer userId = 56; // Integer | Standard users can use this only with their own _userId_
    Integer deviceId = 56; // Integer | Standard users can use this only with _deviceId_s, they have access to
    Integer groupId = 56; // Integer | Standard users can use this only with _groupId_s, they have access to
    Boolean refresh = true; // Boolean | 
    try {
      List<Driver> result = apiInstance.driversGet(all, userId, deviceId, groupId, refresh);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#driversGet");
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
| **all** | **Boolean**| Can only be used by admins or managers to fetch all entities | [optional] |
| **userId** | **Integer**| Standard users can use this only with their own _userId_ | [optional] |
| **deviceId** | **Integer**| Standard users can use this only with _deviceId_s, they have access to | [optional] |
| **groupId** | **Integer**| Standard users can use this only with _groupId_s, they have access to | [optional] |
| **refresh** | **Boolean**|  | [optional] |

### Return type

[**List&lt;Driver&gt;**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="driversIdDelete"></a>
# **driversIdDelete**
> driversIdDelete(id)

Delete a Driver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DriversApi apiInstance = new DriversApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      apiInstance.driversIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#driversIdDelete");
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

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="driversIdPut"></a>
# **driversIdPut**
> Driver driversIdPut(id, body)

Update a Driver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DriversApi apiInstance = new DriversApi(defaultClient);
    Integer id = 56; // Integer | 
    Driver body = new Driver(); // Driver | 
    try {
      Driver result = apiInstance.driversIdPut(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#driversIdPut");
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
| **body** | [**Driver**](Driver.md)|  | |

### Return type

[**Driver**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="driversPost"></a>
# **driversPost**
> Driver driversPost(body)

Create a Driver

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DriversApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DriversApi apiInstance = new DriversApi(defaultClient);
    Driver body = new Driver(); // Driver | 
    try {
      Driver result = apiInstance.driversPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DriversApi#driversPost");
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
| **body** | [**Driver**](Driver.md)|  | |

### Return type

[**Driver**](Driver.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

