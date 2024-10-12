# AttributesApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attributesComputedGet**](AttributesApi.md#attributesComputedGet) | **GET** /attributes/computed | Fetch a list of Attributes |
| [**attributesComputedIdDelete**](AttributesApi.md#attributesComputedIdDelete) | **DELETE** /attributes/computed/{id} | Delete an Attribute |
| [**attributesComputedIdPut**](AttributesApi.md#attributesComputedIdPut) | **PUT** /attributes/computed/{id} | Update an Attribute |
| [**attributesComputedPost**](AttributesApi.md#attributesComputedPost) | **POST** /attributes/computed | Create an Attribute |


<a id="attributesComputedGet"></a>
# **attributesComputedGet**
> List&lt;Attribute&gt; attributesComputedGet(all, userId, deviceId, groupId, refresh)

Fetch a list of Attributes

Without params, it returns a list of Attributes the user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AttributesApi apiInstance = new AttributesApi(defaultClient);
    Boolean all = true; // Boolean | Can only be used by admins or managers to fetch all entities
    Integer userId = 56; // Integer | Standard users can use this only with their own _userId_
    Integer deviceId = 56; // Integer | Standard users can use this only with _deviceId_s, they have access to
    Integer groupId = 56; // Integer | Standard users can use this only with _groupId_s, they have access to
    Boolean refresh = true; // Boolean | 
    try {
      List<Attribute> result = apiInstance.attributesComputedGet(all, userId, deviceId, groupId, refresh);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributesApi#attributesComputedGet");
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

[**List&lt;Attribute&gt;**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="attributesComputedIdDelete"></a>
# **attributesComputedIdDelete**
> attributesComputedIdDelete(id)

Delete an Attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AttributesApi apiInstance = new AttributesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      apiInstance.attributesComputedIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributesApi#attributesComputedIdDelete");
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

<a id="attributesComputedIdPut"></a>
# **attributesComputedIdPut**
> Attribute attributesComputedIdPut(id, body)

Update an Attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AttributesApi apiInstance = new AttributesApi(defaultClient);
    Integer id = 56; // Integer | 
    Attribute body = new Attribute(); // Attribute | 
    try {
      Attribute result = apiInstance.attributesComputedIdPut(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributesApi#attributesComputedIdPut");
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
| **body** | [**Attribute**](Attribute.md)|  | |

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="attributesComputedPost"></a>
# **attributesComputedPost**
> Attribute attributesComputedPost(body)

Create an Attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AttributesApi apiInstance = new AttributesApi(defaultClient);
    Attribute body = new Attribute(); // Attribute | 
    try {
      Attribute result = apiInstance.attributesComputedPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributesApi#attributesComputedPost");
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
| **body** | [**Attribute**](Attribute.md)|  | |

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

