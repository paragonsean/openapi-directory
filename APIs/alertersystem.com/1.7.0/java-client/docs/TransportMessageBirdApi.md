# TransportMessageBirdApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMessageBirdGetCollection**](TransportMessageBirdApi.md#apiTransportMessageBirdGetCollection) | **GET** /api/transport-message-bird | Retrieves the collection of TransportMessageBird resources. |
| [**apiTransportMessageBirdIdDelete**](TransportMessageBirdApi.md#apiTransportMessageBirdIdDelete) | **DELETE** /api/transport-message-bird/{id} | Removes the TransportMessageBird resource. |
| [**apiTransportMessageBirdIdGet**](TransportMessageBirdApi.md#apiTransportMessageBirdIdGet) | **GET** /api/transport-message-bird/{id} | Retrieves a TransportMessageBird resource. |
| [**apiTransportMessageBirdIdPatch**](TransportMessageBirdApi.md#apiTransportMessageBirdIdPatch) | **PATCH** /api/transport-message-bird/{id} | Updates the TransportMessageBird resource. |
| [**apiTransportMessageBirdIdPut**](TransportMessageBirdApi.md#apiTransportMessageBirdIdPut) | **PUT** /api/transport-message-bird/{id} | Replaces the TransportMessageBird resource. |
| [**apiTransportMessageBirdPost**](TransportMessageBirdApi.md#apiTransportMessageBirdPost) | **POST** /api/transport-message-bird | Creates a TransportMessageBird resource. |


<a id="apiTransportMessageBirdGetCollection"></a>
# **apiTransportMessageBirdGetCollection**
> List&lt;TransportMessageBirdGet&gt; apiTransportMessageBirdGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMessageBird resources.

Retrieves the collection of TransportMessageBird resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageBirdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageBirdApi apiInstance = new TransportMessageBirdApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMessageBirdGet> result = apiInstance.apiTransportMessageBirdGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageBirdApi#apiTransportMessageBirdGetCollection");
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

[**List&lt;TransportMessageBirdGet&gt;**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageBird collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageBirdIdDelete"></a>
# **apiTransportMessageBirdIdDelete**
> apiTransportMessageBirdIdDelete(id)

Removes the TransportMessageBird resource.

Removes the TransportMessageBird resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageBirdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageBirdApi apiInstance = new TransportMessageBirdApi(defaultClient);
    String id = "id_example"; // String | TransportMessageBird identifier
    try {
      apiInstance.apiTransportMessageBirdIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageBirdApi#apiTransportMessageBirdIdDelete");
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
| **id** | **String**| TransportMessageBird identifier | |

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
| **204** | TransportMessageBird resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageBirdIdGet"></a>
# **apiTransportMessageBirdIdGet**
> TransportMessageBirdGet apiTransportMessageBirdIdGet(id)

Retrieves a TransportMessageBird resource.

Retrieves a TransportMessageBird resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageBirdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageBirdApi apiInstance = new TransportMessageBirdApi(defaultClient);
    String id = "id_example"; // String | TransportMessageBird identifier
    try {
      TransportMessageBirdGet result = apiInstance.apiTransportMessageBirdIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageBirdApi#apiTransportMessageBirdIdGet");
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
| **id** | **String**| TransportMessageBird identifier | |

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageBird resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageBirdIdPatch"></a>
# **apiTransportMessageBirdIdPatch**
> TransportMessageBirdGet apiTransportMessageBirdIdPatch(id, transportMessageBirdPatch)

Updates the TransportMessageBird resource.

Updates the TransportMessageBird resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageBirdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageBirdApi apiInstance = new TransportMessageBirdApi(defaultClient);
    String id = "id_example"; // String | TransportMessageBird identifier
    TransportMessageBirdPatch transportMessageBirdPatch = new TransportMessageBirdPatch(); // TransportMessageBirdPatch | The updated TransportMessageBird resource
    try {
      TransportMessageBirdGet result = apiInstance.apiTransportMessageBirdIdPatch(id, transportMessageBirdPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageBirdApi#apiTransportMessageBirdIdPatch");
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
| **id** | **String**| TransportMessageBird identifier | |
| **transportMessageBirdPatch** | [**TransportMessageBirdPatch**](TransportMessageBirdPatch.md)| The updated TransportMessageBird resource | |

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageBird resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageBirdIdPut"></a>
# **apiTransportMessageBirdIdPut**
> TransportMessageBirdGet apiTransportMessageBirdIdPut(id, transportMessageBirdPut)

Replaces the TransportMessageBird resource.

Replaces the TransportMessageBird resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageBirdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageBirdApi apiInstance = new TransportMessageBirdApi(defaultClient);
    String id = "id_example"; // String | TransportMessageBird identifier
    TransportMessageBirdPut transportMessageBirdPut = new TransportMessageBirdPut(); // TransportMessageBirdPut | The updated TransportMessageBird resource
    try {
      TransportMessageBirdGet result = apiInstance.apiTransportMessageBirdIdPut(id, transportMessageBirdPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageBirdApi#apiTransportMessageBirdIdPut");
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
| **id** | **String**| TransportMessageBird identifier | |
| **transportMessageBirdPut** | [**TransportMessageBirdPut**](TransportMessageBirdPut.md)| The updated TransportMessageBird resource | |

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageBird resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageBirdPost"></a>
# **apiTransportMessageBirdPost**
> TransportMessageBirdGet apiTransportMessageBirdPost(transportMessageBirdPost)

Creates a TransportMessageBird resource.

Creates a TransportMessageBird resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageBirdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageBirdApi apiInstance = new TransportMessageBirdApi(defaultClient);
    TransportMessageBirdPost transportMessageBirdPost = new TransportMessageBirdPost(); // TransportMessageBirdPost | The new TransportMessageBird resource
    try {
      TransportMessageBirdGet result = apiInstance.apiTransportMessageBirdPost(transportMessageBirdPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageBirdApi#apiTransportMessageBirdPost");
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
| **transportMessageBirdPost** | [**TransportMessageBirdPost**](TransportMessageBirdPost.md)| The new TransportMessageBird resource | |

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMessageBird resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

