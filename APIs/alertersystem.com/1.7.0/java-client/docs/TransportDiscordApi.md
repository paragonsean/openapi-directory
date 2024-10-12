# TransportDiscordApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportDiscordGetCollection**](TransportDiscordApi.md#apiTransportDiscordGetCollection) | **GET** /api/transport-discord | Retrieves the collection of TransportDiscord resources. |
| [**apiTransportDiscordIdDelete**](TransportDiscordApi.md#apiTransportDiscordIdDelete) | **DELETE** /api/transport-discord/{id} | Removes the TransportDiscord resource. |
| [**apiTransportDiscordIdGet**](TransportDiscordApi.md#apiTransportDiscordIdGet) | **GET** /api/transport-discord/{id} | Retrieves a TransportDiscord resource. |
| [**apiTransportDiscordIdPatch**](TransportDiscordApi.md#apiTransportDiscordIdPatch) | **PATCH** /api/transport-discord/{id} | Updates the TransportDiscord resource. |
| [**apiTransportDiscordIdPut**](TransportDiscordApi.md#apiTransportDiscordIdPut) | **PUT** /api/transport-discord/{id} | Replaces the TransportDiscord resource. |
| [**apiTransportDiscordPost**](TransportDiscordApi.md#apiTransportDiscordPost) | **POST** /api/transport-discord | Creates a TransportDiscord resource. |


<a id="apiTransportDiscordGetCollection"></a>
# **apiTransportDiscordGetCollection**
> List&lt;TransportDiscordGet&gt; apiTransportDiscordGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportDiscord resources.

Retrieves the collection of TransportDiscord resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportDiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportDiscordApi apiInstance = new TransportDiscordApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportDiscordGet> result = apiInstance.apiTransportDiscordGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportDiscordApi#apiTransportDiscordGetCollection");
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

[**List&lt;TransportDiscordGet&gt;**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportDiscord collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportDiscordIdDelete"></a>
# **apiTransportDiscordIdDelete**
> apiTransportDiscordIdDelete(id)

Removes the TransportDiscord resource.

Removes the TransportDiscord resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportDiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportDiscordApi apiInstance = new TransportDiscordApi(defaultClient);
    String id = "id_example"; // String | TransportDiscord identifier
    try {
      apiInstance.apiTransportDiscordIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportDiscordApi#apiTransportDiscordIdDelete");
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
| **id** | **String**| TransportDiscord identifier | |

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
| **204** | TransportDiscord resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportDiscordIdGet"></a>
# **apiTransportDiscordIdGet**
> TransportDiscordGet apiTransportDiscordIdGet(id)

Retrieves a TransportDiscord resource.

Retrieves a TransportDiscord resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportDiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportDiscordApi apiInstance = new TransportDiscordApi(defaultClient);
    String id = "id_example"; // String | TransportDiscord identifier
    try {
      TransportDiscordGet result = apiInstance.apiTransportDiscordIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportDiscordApi#apiTransportDiscordIdGet");
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
| **id** | **String**| TransportDiscord identifier | |

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportDiscord resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportDiscordIdPatch"></a>
# **apiTransportDiscordIdPatch**
> TransportDiscordGet apiTransportDiscordIdPatch(id, transportDiscordPatch)

Updates the TransportDiscord resource.

Updates the TransportDiscord resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportDiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportDiscordApi apiInstance = new TransportDiscordApi(defaultClient);
    String id = "id_example"; // String | TransportDiscord identifier
    TransportDiscordPatch transportDiscordPatch = new TransportDiscordPatch(); // TransportDiscordPatch | The updated TransportDiscord resource
    try {
      TransportDiscordGet result = apiInstance.apiTransportDiscordIdPatch(id, transportDiscordPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportDiscordApi#apiTransportDiscordIdPatch");
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
| **id** | **String**| TransportDiscord identifier | |
| **transportDiscordPatch** | [**TransportDiscordPatch**](TransportDiscordPatch.md)| The updated TransportDiscord resource | |

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportDiscord resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportDiscordIdPut"></a>
# **apiTransportDiscordIdPut**
> TransportDiscordGet apiTransportDiscordIdPut(id, transportDiscordPut)

Replaces the TransportDiscord resource.

Replaces the TransportDiscord resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportDiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportDiscordApi apiInstance = new TransportDiscordApi(defaultClient);
    String id = "id_example"; // String | TransportDiscord identifier
    TransportDiscordPut transportDiscordPut = new TransportDiscordPut(); // TransportDiscordPut | The updated TransportDiscord resource
    try {
      TransportDiscordGet result = apiInstance.apiTransportDiscordIdPut(id, transportDiscordPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportDiscordApi#apiTransportDiscordIdPut");
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
| **id** | **String**| TransportDiscord identifier | |
| **transportDiscordPut** | [**TransportDiscordPut**](TransportDiscordPut.md)| The updated TransportDiscord resource | |

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportDiscord resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportDiscordPost"></a>
# **apiTransportDiscordPost**
> TransportDiscordGet apiTransportDiscordPost(transportDiscordPost)

Creates a TransportDiscord resource.

Creates a TransportDiscord resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportDiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportDiscordApi apiInstance = new TransportDiscordApi(defaultClient);
    TransportDiscordPost transportDiscordPost = new TransportDiscordPost(); // TransportDiscordPost | The new TransportDiscord resource
    try {
      TransportDiscordGet result = apiInstance.apiTransportDiscordPost(transportDiscordPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportDiscordApi#apiTransportDiscordPost");
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
| **transportDiscordPost** | [**TransportDiscordPost**](TransportDiscordPost.md)| The new TransportDiscord resource | |

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportDiscord resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

