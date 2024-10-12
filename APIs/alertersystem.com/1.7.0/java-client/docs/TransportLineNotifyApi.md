# TransportLineNotifyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportLineNotifyGetCollection**](TransportLineNotifyApi.md#apiTransportLineNotifyGetCollection) | **GET** /api/transport-line-notify | Retrieves the collection of TransportLineNotify resources. |
| [**apiTransportLineNotifyIdDelete**](TransportLineNotifyApi.md#apiTransportLineNotifyIdDelete) | **DELETE** /api/transport-line-notify/{id} | Removes the TransportLineNotify resource. |
| [**apiTransportLineNotifyIdGet**](TransportLineNotifyApi.md#apiTransportLineNotifyIdGet) | **GET** /api/transport-line-notify/{id} | Retrieves a TransportLineNotify resource. |
| [**apiTransportLineNotifyIdPatch**](TransportLineNotifyApi.md#apiTransportLineNotifyIdPatch) | **PATCH** /api/transport-line-notify/{id} | Updates the TransportLineNotify resource. |
| [**apiTransportLineNotifyIdPut**](TransportLineNotifyApi.md#apiTransportLineNotifyIdPut) | **PUT** /api/transport-line-notify/{id} | Replaces the TransportLineNotify resource. |
| [**apiTransportLineNotifyPost**](TransportLineNotifyApi.md#apiTransportLineNotifyPost) | **POST** /api/transport-line-notify | Creates a TransportLineNotify resource. |


<a id="apiTransportLineNotifyGetCollection"></a>
# **apiTransportLineNotifyGetCollection**
> List&lt;TransportLineNotifyGet&gt; apiTransportLineNotifyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportLineNotify resources.

Retrieves the collection of TransportLineNotify resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLineNotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLineNotifyApi apiInstance = new TransportLineNotifyApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportLineNotifyGet> result = apiInstance.apiTransportLineNotifyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLineNotifyApi#apiTransportLineNotifyGetCollection");
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

[**List&lt;TransportLineNotifyGet&gt;**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLineNotify collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLineNotifyIdDelete"></a>
# **apiTransportLineNotifyIdDelete**
> apiTransportLineNotifyIdDelete(id)

Removes the TransportLineNotify resource.

Removes the TransportLineNotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLineNotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLineNotifyApi apiInstance = new TransportLineNotifyApi(defaultClient);
    String id = "id_example"; // String | TransportLineNotify identifier
    try {
      apiInstance.apiTransportLineNotifyIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLineNotifyApi#apiTransportLineNotifyIdDelete");
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
| **id** | **String**| TransportLineNotify identifier | |

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
| **204** | TransportLineNotify resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLineNotifyIdGet"></a>
# **apiTransportLineNotifyIdGet**
> TransportLineNotifyGet apiTransportLineNotifyIdGet(id)

Retrieves a TransportLineNotify resource.

Retrieves a TransportLineNotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLineNotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLineNotifyApi apiInstance = new TransportLineNotifyApi(defaultClient);
    String id = "id_example"; // String | TransportLineNotify identifier
    try {
      TransportLineNotifyGet result = apiInstance.apiTransportLineNotifyIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLineNotifyApi#apiTransportLineNotifyIdGet");
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
| **id** | **String**| TransportLineNotify identifier | |

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLineNotify resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLineNotifyIdPatch"></a>
# **apiTransportLineNotifyIdPatch**
> TransportLineNotifyGet apiTransportLineNotifyIdPatch(id, transportLineNotifyPatch)

Updates the TransportLineNotify resource.

Updates the TransportLineNotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLineNotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLineNotifyApi apiInstance = new TransportLineNotifyApi(defaultClient);
    String id = "id_example"; // String | TransportLineNotify identifier
    TransportLineNotifyPatch transportLineNotifyPatch = new TransportLineNotifyPatch(); // TransportLineNotifyPatch | The updated TransportLineNotify resource
    try {
      TransportLineNotifyGet result = apiInstance.apiTransportLineNotifyIdPatch(id, transportLineNotifyPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLineNotifyApi#apiTransportLineNotifyIdPatch");
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
| **id** | **String**| TransportLineNotify identifier | |
| **transportLineNotifyPatch** | [**TransportLineNotifyPatch**](TransportLineNotifyPatch.md)| The updated TransportLineNotify resource | |

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLineNotify resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLineNotifyIdPut"></a>
# **apiTransportLineNotifyIdPut**
> TransportLineNotifyGet apiTransportLineNotifyIdPut(id, transportLineNotifyPut)

Replaces the TransportLineNotify resource.

Replaces the TransportLineNotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLineNotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLineNotifyApi apiInstance = new TransportLineNotifyApi(defaultClient);
    String id = "id_example"; // String | TransportLineNotify identifier
    TransportLineNotifyPut transportLineNotifyPut = new TransportLineNotifyPut(); // TransportLineNotifyPut | The updated TransportLineNotify resource
    try {
      TransportLineNotifyGet result = apiInstance.apiTransportLineNotifyIdPut(id, transportLineNotifyPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLineNotifyApi#apiTransportLineNotifyIdPut");
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
| **id** | **String**| TransportLineNotify identifier | |
| **transportLineNotifyPut** | [**TransportLineNotifyPut**](TransportLineNotifyPut.md)| The updated TransportLineNotify resource | |

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLineNotify resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLineNotifyPost"></a>
# **apiTransportLineNotifyPost**
> TransportLineNotifyGet apiTransportLineNotifyPost(transportLineNotifyPost)

Creates a TransportLineNotify resource.

Creates a TransportLineNotify resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLineNotifyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLineNotifyApi apiInstance = new TransportLineNotifyApi(defaultClient);
    TransportLineNotifyPost transportLineNotifyPost = new TransportLineNotifyPost(); // TransportLineNotifyPost | The new TransportLineNotify resource
    try {
      TransportLineNotifyGet result = apiInstance.apiTransportLineNotifyPost(transportLineNotifyPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLineNotifyApi#apiTransportLineNotifyPost");
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
| **transportLineNotifyPost** | [**TransportLineNotifyPost**](TransportLineNotifyPost.md)| The new TransportLineNotify resource | |

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportLineNotify resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

