# TransportGotifyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportGotifyGetCollection**](TransportGotifyApi.md#apiTransportGotifyGetCollection) | **GET** /api/transport-gotify | Retrieves the collection of TransportGotify resources. |
| [**apiTransportGotifyIdDelete**](TransportGotifyApi.md#apiTransportGotifyIdDelete) | **DELETE** /api/transport-gotify/{id} | Removes the TransportGotify resource. |
| [**apiTransportGotifyIdGet**](TransportGotifyApi.md#apiTransportGotifyIdGet) | **GET** /api/transport-gotify/{id} | Retrieves a TransportGotify resource. |
| [**apiTransportGotifyIdPatch**](TransportGotifyApi.md#apiTransportGotifyIdPatch) | **PATCH** /api/transport-gotify/{id} | Updates the TransportGotify resource. |
| [**apiTransportGotifyIdPut**](TransportGotifyApi.md#apiTransportGotifyIdPut) | **PUT** /api/transport-gotify/{id} | Replaces the TransportGotify resource. |
| [**apiTransportGotifyPost**](TransportGotifyApi.md#apiTransportGotifyPost) | **POST** /api/transport-gotify | Creates a TransportGotify resource. |


<a id="apiTransportGotifyGetCollection"></a>
# **apiTransportGotifyGetCollection**
> List&lt;TransportGotifyGet&gt; apiTransportGotifyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportGotify resources.

Retrieves the collection of TransportGotify resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGotifyApi apiInstance = new TransportGotifyApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportGotifyGet> result = apiInstance.apiTransportGotifyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGotifyApi#apiTransportGotifyGetCollection");
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

[**List&lt;TransportGotifyGet&gt;**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGotify collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGotifyIdDelete"></a>
# **apiTransportGotifyIdDelete**
> apiTransportGotifyIdDelete(id)

Removes the TransportGotify resource.

Removes the TransportGotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGotifyApi apiInstance = new TransportGotifyApi(defaultClient);
    String id = "id_example"; // String | TransportGotify identifier
    try {
      apiInstance.apiTransportGotifyIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGotifyApi#apiTransportGotifyIdDelete");
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
| **id** | **String**| TransportGotify identifier | |

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
| **204** | TransportGotify resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGotifyIdGet"></a>
# **apiTransportGotifyIdGet**
> TransportGotifyGet apiTransportGotifyIdGet(id)

Retrieves a TransportGotify resource.

Retrieves a TransportGotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGotifyApi apiInstance = new TransportGotifyApi(defaultClient);
    String id = "id_example"; // String | TransportGotify identifier
    try {
      TransportGotifyGet result = apiInstance.apiTransportGotifyIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGotifyApi#apiTransportGotifyIdGet");
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
| **id** | **String**| TransportGotify identifier | |

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGotify resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGotifyIdPatch"></a>
# **apiTransportGotifyIdPatch**
> TransportGotifyGet apiTransportGotifyIdPatch(id, transportGotifyPatch)

Updates the TransportGotify resource.

Updates the TransportGotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGotifyApi apiInstance = new TransportGotifyApi(defaultClient);
    String id = "id_example"; // String | TransportGotify identifier
    TransportGotifyPatch transportGotifyPatch = new TransportGotifyPatch(); // TransportGotifyPatch | The updated TransportGotify resource
    try {
      TransportGotifyGet result = apiInstance.apiTransportGotifyIdPatch(id, transportGotifyPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGotifyApi#apiTransportGotifyIdPatch");
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
| **id** | **String**| TransportGotify identifier | |
| **transportGotifyPatch** | [**TransportGotifyPatch**](TransportGotifyPatch.md)| The updated TransportGotify resource | |

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGotify resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGotifyIdPut"></a>
# **apiTransportGotifyIdPut**
> TransportGotifyGet apiTransportGotifyIdPut(id, transportGotifyPut)

Replaces the TransportGotify resource.

Replaces the TransportGotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGotifyApi apiInstance = new TransportGotifyApi(defaultClient);
    String id = "id_example"; // String | TransportGotify identifier
    TransportGotifyPut transportGotifyPut = new TransportGotifyPut(); // TransportGotifyPut | The updated TransportGotify resource
    try {
      TransportGotifyGet result = apiInstance.apiTransportGotifyIdPut(id, transportGotifyPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGotifyApi#apiTransportGotifyIdPut");
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
| **id** | **String**| TransportGotify identifier | |
| **transportGotifyPut** | [**TransportGotifyPut**](TransportGotifyPut.md)| The updated TransportGotify resource | |

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGotify resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGotifyPost"></a>
# **apiTransportGotifyPost**
> TransportGotifyGet apiTransportGotifyPost(transportGotifyPost)

Creates a TransportGotify resource.

Creates a TransportGotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGotifyApi apiInstance = new TransportGotifyApi(defaultClient);
    TransportGotifyPost transportGotifyPost = new TransportGotifyPost(); // TransportGotifyPost | The new TransportGotify resource
    try {
      TransportGotifyGet result = apiInstance.apiTransportGotifyPost(transportGotifyPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGotifyApi#apiTransportGotifyPost");
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
| **transportGotifyPost** | [**TransportGotifyPost**](TransportGotifyPost.md)| The new TransportGotify resource | |

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportGotify resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

