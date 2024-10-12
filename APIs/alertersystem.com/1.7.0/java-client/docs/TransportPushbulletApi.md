# TransportPushbulletApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportPushbulletGetCollection**](TransportPushbulletApi.md#apiTransportPushbulletGetCollection) | **GET** /api/transport-pushbullet | Retrieves the collection of TransportPushbullet resources. |
| [**apiTransportPushbulletIdDelete**](TransportPushbulletApi.md#apiTransportPushbulletIdDelete) | **DELETE** /api/transport-pushbullet/{id} | Removes the TransportPushbullet resource. |
| [**apiTransportPushbulletIdGet**](TransportPushbulletApi.md#apiTransportPushbulletIdGet) | **GET** /api/transport-pushbullet/{id} | Retrieves a TransportPushbullet resource. |
| [**apiTransportPushbulletIdPatch**](TransportPushbulletApi.md#apiTransportPushbulletIdPatch) | **PATCH** /api/transport-pushbullet/{id} | Updates the TransportPushbullet resource. |
| [**apiTransportPushbulletIdPut**](TransportPushbulletApi.md#apiTransportPushbulletIdPut) | **PUT** /api/transport-pushbullet/{id} | Replaces the TransportPushbullet resource. |
| [**apiTransportPushbulletPost**](TransportPushbulletApi.md#apiTransportPushbulletPost) | **POST** /api/transport-pushbullet | Creates a TransportPushbullet resource. |


<a id="apiTransportPushbulletGetCollection"></a>
# **apiTransportPushbulletGetCollection**
> List&lt;TransportPushbulletGet&gt; apiTransportPushbulletGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportPushbullet resources.

Retrieves the collection of TransportPushbullet resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushbulletApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushbulletApi apiInstance = new TransportPushbulletApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportPushbulletGet> result = apiInstance.apiTransportPushbulletGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushbulletApi#apiTransportPushbulletGetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **dataSegmentCode** | **String**|  | [optional] |
| **dataSegmentCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **partition** | **String**|  | [optional] |
| **partition2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TransportPushbulletGet&gt;**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushbullet collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushbulletIdDelete"></a>
# **apiTransportPushbulletIdDelete**
> apiTransportPushbulletIdDelete(id)

Removes the TransportPushbullet resource.

Removes the TransportPushbullet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushbulletApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushbulletApi apiInstance = new TransportPushbulletApi(defaultClient);
    String id = "id_example"; // String | TransportPushbullet identifier
    try {
      apiInstance.apiTransportPushbulletIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushbulletApi#apiTransportPushbulletIdDelete");
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
| **id** | **String**| TransportPushbullet identifier | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | TransportPushbullet resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushbulletIdGet"></a>
# **apiTransportPushbulletIdGet**
> TransportPushbulletGet apiTransportPushbulletIdGet(id)

Retrieves a TransportPushbullet resource.

Retrieves a TransportPushbullet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushbulletApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushbulletApi apiInstance = new TransportPushbulletApi(defaultClient);
    String id = "id_example"; // String | TransportPushbullet identifier
    try {
      TransportPushbulletGet result = apiInstance.apiTransportPushbulletIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushbulletApi#apiTransportPushbulletIdGet");
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
| **id** | **String**| TransportPushbullet identifier | |

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushbullet resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushbulletIdPatch"></a>
# **apiTransportPushbulletIdPatch**
> TransportPushbulletGet apiTransportPushbulletIdPatch(id, transportPushbulletPatch)

Updates the TransportPushbullet resource.

Updates the TransportPushbullet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushbulletApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushbulletApi apiInstance = new TransportPushbulletApi(defaultClient);
    String id = "id_example"; // String | TransportPushbullet identifier
    TransportPushbulletPatch transportPushbulletPatch = new TransportPushbulletPatch(); // TransportPushbulletPatch | The updated TransportPushbullet resource
    try {
      TransportPushbulletGet result = apiInstance.apiTransportPushbulletIdPatch(id, transportPushbulletPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushbulletApi#apiTransportPushbulletIdPatch");
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
| **id** | **String**| TransportPushbullet identifier | |
| **transportPushbulletPatch** | [**TransportPushbulletPatch**](TransportPushbulletPatch.md)| The updated TransportPushbullet resource | |

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushbullet resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushbulletIdPut"></a>
# **apiTransportPushbulletIdPut**
> TransportPushbulletGet apiTransportPushbulletIdPut(id, transportPushbulletPut)

Replaces the TransportPushbullet resource.

Replaces the TransportPushbullet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushbulletApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushbulletApi apiInstance = new TransportPushbulletApi(defaultClient);
    String id = "id_example"; // String | TransportPushbullet identifier
    TransportPushbulletPut transportPushbulletPut = new TransportPushbulletPut(); // TransportPushbulletPut | The updated TransportPushbullet resource
    try {
      TransportPushbulletGet result = apiInstance.apiTransportPushbulletIdPut(id, transportPushbulletPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushbulletApi#apiTransportPushbulletIdPut");
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
| **id** | **String**| TransportPushbullet identifier | |
| **transportPushbulletPut** | [**TransportPushbulletPut**](TransportPushbulletPut.md)| The updated TransportPushbullet resource | |

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushbullet resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushbulletPost"></a>
# **apiTransportPushbulletPost**
> TransportPushbulletGet apiTransportPushbulletPost(transportPushbulletPost)

Creates a TransportPushbullet resource.

Creates a TransportPushbullet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushbulletApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushbulletApi apiInstance = new TransportPushbulletApi(defaultClient);
    TransportPushbulletPost transportPushbulletPost = new TransportPushbulletPost(); // TransportPushbulletPost | The new TransportPushbullet resource
    try {
      TransportPushbulletGet result = apiInstance.apiTransportPushbulletPost(transportPushbulletPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushbulletApi#apiTransportPushbulletPost");
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
| **transportPushbulletPost** | [**TransportPushbulletPost**](TransportPushbulletPost.md)| The new TransportPushbullet resource | |

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportPushbullet resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

