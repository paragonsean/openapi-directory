# TransportRocketChatApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportRocketChatGetCollection**](TransportRocketChatApi.md#apiTransportRocketChatGetCollection) | **GET** /api/transport-rocket-chat | Retrieves the collection of TransportRocketChat resources. |
| [**apiTransportRocketChatIdDelete**](TransportRocketChatApi.md#apiTransportRocketChatIdDelete) | **DELETE** /api/transport-rocket-chat/{id} | Removes the TransportRocketChat resource. |
| [**apiTransportRocketChatIdGet**](TransportRocketChatApi.md#apiTransportRocketChatIdGet) | **GET** /api/transport-rocket-chat/{id} | Retrieves a TransportRocketChat resource. |
| [**apiTransportRocketChatIdPatch**](TransportRocketChatApi.md#apiTransportRocketChatIdPatch) | **PATCH** /api/transport-rocket-chat/{id} | Updates the TransportRocketChat resource. |
| [**apiTransportRocketChatIdPut**](TransportRocketChatApi.md#apiTransportRocketChatIdPut) | **PUT** /api/transport-rocket-chat/{id} | Replaces the TransportRocketChat resource. |
| [**apiTransportRocketChatPost**](TransportRocketChatApi.md#apiTransportRocketChatPost) | **POST** /api/transport-rocket-chat | Creates a TransportRocketChat resource. |


<a id="apiTransportRocketChatGetCollection"></a>
# **apiTransportRocketChatGetCollection**
> List&lt;TransportRocketChatGet&gt; apiTransportRocketChatGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportRocketChat resources.

Retrieves the collection of TransportRocketChat resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRocketChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRocketChatApi apiInstance = new TransportRocketChatApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportRocketChatGet> result = apiInstance.apiTransportRocketChatGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRocketChatApi#apiTransportRocketChatGetCollection");
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

[**List&lt;TransportRocketChatGet&gt;**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRocketChat collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRocketChatIdDelete"></a>
# **apiTransportRocketChatIdDelete**
> apiTransportRocketChatIdDelete(id)

Removes the TransportRocketChat resource.

Removes the TransportRocketChat resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRocketChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRocketChatApi apiInstance = new TransportRocketChatApi(defaultClient);
    String id = "id_example"; // String | TransportRocketChat identifier
    try {
      apiInstance.apiTransportRocketChatIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRocketChatApi#apiTransportRocketChatIdDelete");
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
| **id** | **String**| TransportRocketChat identifier | |

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
| **204** | TransportRocketChat resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRocketChatIdGet"></a>
# **apiTransportRocketChatIdGet**
> TransportRocketChatGet apiTransportRocketChatIdGet(id)

Retrieves a TransportRocketChat resource.

Retrieves a TransportRocketChat resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRocketChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRocketChatApi apiInstance = new TransportRocketChatApi(defaultClient);
    String id = "id_example"; // String | TransportRocketChat identifier
    try {
      TransportRocketChatGet result = apiInstance.apiTransportRocketChatIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRocketChatApi#apiTransportRocketChatIdGet");
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
| **id** | **String**| TransportRocketChat identifier | |

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRocketChat resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRocketChatIdPatch"></a>
# **apiTransportRocketChatIdPatch**
> TransportRocketChatGet apiTransportRocketChatIdPatch(id, transportRocketChatPatch)

Updates the TransportRocketChat resource.

Updates the TransportRocketChat resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRocketChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRocketChatApi apiInstance = new TransportRocketChatApi(defaultClient);
    String id = "id_example"; // String | TransportRocketChat identifier
    TransportRocketChatPatch transportRocketChatPatch = new TransportRocketChatPatch(); // TransportRocketChatPatch | The updated TransportRocketChat resource
    try {
      TransportRocketChatGet result = apiInstance.apiTransportRocketChatIdPatch(id, transportRocketChatPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRocketChatApi#apiTransportRocketChatIdPatch");
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
| **id** | **String**| TransportRocketChat identifier | |
| **transportRocketChatPatch** | [**TransportRocketChatPatch**](TransportRocketChatPatch.md)| The updated TransportRocketChat resource | |

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRocketChat resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRocketChatIdPut"></a>
# **apiTransportRocketChatIdPut**
> TransportRocketChatGet apiTransportRocketChatIdPut(id, transportRocketChatPut)

Replaces the TransportRocketChat resource.

Replaces the TransportRocketChat resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRocketChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRocketChatApi apiInstance = new TransportRocketChatApi(defaultClient);
    String id = "id_example"; // String | TransportRocketChat identifier
    TransportRocketChatPut transportRocketChatPut = new TransportRocketChatPut(); // TransportRocketChatPut | The updated TransportRocketChat resource
    try {
      TransportRocketChatGet result = apiInstance.apiTransportRocketChatIdPut(id, transportRocketChatPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRocketChatApi#apiTransportRocketChatIdPut");
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
| **id** | **String**| TransportRocketChat identifier | |
| **transportRocketChatPut** | [**TransportRocketChatPut**](TransportRocketChatPut.md)| The updated TransportRocketChat resource | |

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRocketChat resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRocketChatPost"></a>
# **apiTransportRocketChatPost**
> TransportRocketChatGet apiTransportRocketChatPost(transportRocketChatPost)

Creates a TransportRocketChat resource.

Creates a TransportRocketChat resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRocketChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRocketChatApi apiInstance = new TransportRocketChatApi(defaultClient);
    TransportRocketChatPost transportRocketChatPost = new TransportRocketChatPost(); // TransportRocketChatPost | The new TransportRocketChat resource
    try {
      TransportRocketChatGet result = apiInstance.apiTransportRocketChatPost(transportRocketChatPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRocketChatApi#apiTransportRocketChatPost");
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
| **transportRocketChatPost** | [**TransportRocketChatPost**](TransportRocketChatPost.md)| The new TransportRocketChat resource | |

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportRocketChat resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

