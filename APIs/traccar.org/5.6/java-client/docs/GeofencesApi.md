# GeofencesApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geofencesGet**](GeofencesApi.md#geofencesGet) | **GET** /geofences | Fetch a list of Geofences |
| [**geofencesIdDelete**](GeofencesApi.md#geofencesIdDelete) | **DELETE** /geofences/{id} | Delete a Geofence |
| [**geofencesIdPut**](GeofencesApi.md#geofencesIdPut) | **PUT** /geofences/{id} | Update a Geofence |
| [**geofencesPost**](GeofencesApi.md#geofencesPost) | **POST** /geofences | Create a Geofence |


<a id="geofencesGet"></a>
# **geofencesGet**
> List&lt;Geofence&gt; geofencesGet(all, userId, deviceId, groupId, refresh)

Fetch a list of Geofences

Without params, it returns a list of Geofences the user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeofencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GeofencesApi apiInstance = new GeofencesApi(defaultClient);
    Boolean all = true; // Boolean | Can only be used by admins or managers to fetch all entities
    Integer userId = 56; // Integer | Standard users can use this only with their own _userId_
    Integer deviceId = 56; // Integer | Standard users can use this only with _deviceId_s, they have access to
    Integer groupId = 56; // Integer | Standard users can use this only with _groupId_s, they have access to
    Boolean refresh = true; // Boolean | 
    try {
      List<Geofence> result = apiInstance.geofencesGet(all, userId, deviceId, groupId, refresh);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeofencesApi#geofencesGet");
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

[**List&lt;Geofence&gt;**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="geofencesIdDelete"></a>
# **geofencesIdDelete**
> geofencesIdDelete(id)

Delete a Geofence

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeofencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GeofencesApi apiInstance = new GeofencesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      apiInstance.geofencesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeofencesApi#geofencesIdDelete");
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

<a id="geofencesIdPut"></a>
# **geofencesIdPut**
> Geofence geofencesIdPut(id, body)

Update a Geofence

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeofencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GeofencesApi apiInstance = new GeofencesApi(defaultClient);
    Integer id = 56; // Integer | 
    Geofence body = new Geofence(); // Geofence | 
    try {
      Geofence result = apiInstance.geofencesIdPut(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeofencesApi#geofencesIdPut");
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
| **body** | [**Geofence**](Geofence.md)|  | |

### Return type

[**Geofence**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="geofencesPost"></a>
# **geofencesPost**
> Geofence geofencesPost(body)

Create a Geofence

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeofencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GeofencesApi apiInstance = new GeofencesApi(defaultClient);
    Geofence body = new Geofence(); // Geofence | 
    try {
      Geofence result = apiInstance.geofencesPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeofencesApi#geofencesPost");
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
| **body** | [**Geofence**](Geofence.md)|  | |

### Return type

[**Geofence**](Geofence.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

