# TransportMessageMediaApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMessageMediaGetCollection**](TransportMessageMediaApi.md#apiTransportMessageMediaGetCollection) | **GET** /api/transport-message-media | Retrieves the collection of TransportMessageMedia resources. |
| [**apiTransportMessageMediaIdDelete**](TransportMessageMediaApi.md#apiTransportMessageMediaIdDelete) | **DELETE** /api/transport-message-media/{id} | Removes the TransportMessageMedia resource. |
| [**apiTransportMessageMediaIdGet**](TransportMessageMediaApi.md#apiTransportMessageMediaIdGet) | **GET** /api/transport-message-media/{id} | Retrieves a TransportMessageMedia resource. |
| [**apiTransportMessageMediaIdPatch**](TransportMessageMediaApi.md#apiTransportMessageMediaIdPatch) | **PATCH** /api/transport-message-media/{id} | Updates the TransportMessageMedia resource. |
| [**apiTransportMessageMediaIdPut**](TransportMessageMediaApi.md#apiTransportMessageMediaIdPut) | **PUT** /api/transport-message-media/{id} | Replaces the TransportMessageMedia resource. |
| [**apiTransportMessageMediaPost**](TransportMessageMediaApi.md#apiTransportMessageMediaPost) | **POST** /api/transport-message-media | Creates a TransportMessageMedia resource. |


<a id="apiTransportMessageMediaGetCollection"></a>
# **apiTransportMessageMediaGetCollection**
> List&lt;TransportMessageMediaGet&gt; apiTransportMessageMediaGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMessageMedia resources.

Retrieves the collection of TransportMessageMedia resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageMediaApi apiInstance = new TransportMessageMediaApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMessageMediaGet> result = apiInstance.apiTransportMessageMediaGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageMediaApi#apiTransportMessageMediaGetCollection");
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

[**List&lt;TransportMessageMediaGet&gt;**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageMedia collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageMediaIdDelete"></a>
# **apiTransportMessageMediaIdDelete**
> apiTransportMessageMediaIdDelete(id)

Removes the TransportMessageMedia resource.

Removes the TransportMessageMedia resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageMediaApi apiInstance = new TransportMessageMediaApi(defaultClient);
    String id = "id_example"; // String | TransportMessageMedia identifier
    try {
      apiInstance.apiTransportMessageMediaIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageMediaApi#apiTransportMessageMediaIdDelete");
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
| **id** | **String**| TransportMessageMedia identifier | |

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
| **204** | TransportMessageMedia resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageMediaIdGet"></a>
# **apiTransportMessageMediaIdGet**
> TransportMessageMediaGet apiTransportMessageMediaIdGet(id)

Retrieves a TransportMessageMedia resource.

Retrieves a TransportMessageMedia resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageMediaApi apiInstance = new TransportMessageMediaApi(defaultClient);
    String id = "id_example"; // String | TransportMessageMedia identifier
    try {
      TransportMessageMediaGet result = apiInstance.apiTransportMessageMediaIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageMediaApi#apiTransportMessageMediaIdGet");
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
| **id** | **String**| TransportMessageMedia identifier | |

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageMedia resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageMediaIdPatch"></a>
# **apiTransportMessageMediaIdPatch**
> TransportMessageMediaGet apiTransportMessageMediaIdPatch(id, transportMessageMediaPatch)

Updates the TransportMessageMedia resource.

Updates the TransportMessageMedia resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageMediaApi apiInstance = new TransportMessageMediaApi(defaultClient);
    String id = "id_example"; // String | TransportMessageMedia identifier
    TransportMessageMediaPatch transportMessageMediaPatch = new TransportMessageMediaPatch(); // TransportMessageMediaPatch | The updated TransportMessageMedia resource
    try {
      TransportMessageMediaGet result = apiInstance.apiTransportMessageMediaIdPatch(id, transportMessageMediaPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageMediaApi#apiTransportMessageMediaIdPatch");
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
| **id** | **String**| TransportMessageMedia identifier | |
| **transportMessageMediaPatch** | [**TransportMessageMediaPatch**](TransportMessageMediaPatch.md)| The updated TransportMessageMedia resource | |

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageMedia resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageMediaIdPut"></a>
# **apiTransportMessageMediaIdPut**
> TransportMessageMediaGet apiTransportMessageMediaIdPut(id, transportMessageMediaPut)

Replaces the TransportMessageMedia resource.

Replaces the TransportMessageMedia resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageMediaApi apiInstance = new TransportMessageMediaApi(defaultClient);
    String id = "id_example"; // String | TransportMessageMedia identifier
    TransportMessageMediaPut transportMessageMediaPut = new TransportMessageMediaPut(); // TransportMessageMediaPut | The updated TransportMessageMedia resource
    try {
      TransportMessageMediaGet result = apiInstance.apiTransportMessageMediaIdPut(id, transportMessageMediaPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageMediaApi#apiTransportMessageMediaIdPut");
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
| **id** | **String**| TransportMessageMedia identifier | |
| **transportMessageMediaPut** | [**TransportMessageMediaPut**](TransportMessageMediaPut.md)| The updated TransportMessageMedia resource | |

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMessageMedia resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMessageMediaPost"></a>
# **apiTransportMessageMediaPost**
> TransportMessageMediaGet apiTransportMessageMediaPost(transportMessageMediaPost)

Creates a TransportMessageMedia resource.

Creates a TransportMessageMedia resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMessageMediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMessageMediaApi apiInstance = new TransportMessageMediaApi(defaultClient);
    TransportMessageMediaPost transportMessageMediaPost = new TransportMessageMediaPost(); // TransportMessageMediaPost | The new TransportMessageMedia resource
    try {
      TransportMessageMediaGet result = apiInstance.apiTransportMessageMediaPost(transportMessageMediaPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMessageMediaApi#apiTransportMessageMediaPost");
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
| **transportMessageMediaPost** | [**TransportMessageMediaPost**](TransportMessageMediaPost.md)| The new TransportMessageMedia resource | |

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMessageMedia resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

