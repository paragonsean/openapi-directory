# TransportTelegramApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTelegramGetCollection**](TransportTelegramApi.md#apiTransportTelegramGetCollection) | **GET** /api/transport-telegram | Retrieves the collection of TransportTelegram resources. |
| [**apiTransportTelegramIdDelete**](TransportTelegramApi.md#apiTransportTelegramIdDelete) | **DELETE** /api/transport-telegram/{id} | Removes the TransportTelegram resource. |
| [**apiTransportTelegramIdGet**](TransportTelegramApi.md#apiTransportTelegramIdGet) | **GET** /api/transport-telegram/{id} | Retrieves a TransportTelegram resource. |
| [**apiTransportTelegramIdPatch**](TransportTelegramApi.md#apiTransportTelegramIdPatch) | **PATCH** /api/transport-telegram/{id} | Updates the TransportTelegram resource. |
| [**apiTransportTelegramIdPut**](TransportTelegramApi.md#apiTransportTelegramIdPut) | **PUT** /api/transport-telegram/{id} | Replaces the TransportTelegram resource. |
| [**apiTransportTelegramPost**](TransportTelegramApi.md#apiTransportTelegramPost) | **POST** /api/transport-telegram | Creates a TransportTelegram resource. |


<a id="apiTransportTelegramGetCollection"></a>
# **apiTransportTelegramGetCollection**
> List&lt;TransportTelegramGet&gt; apiTransportTelegramGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTelegram resources.

Retrieves the collection of TransportTelegram resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelegramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelegramApi apiInstance = new TransportTelegramApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTelegramGet> result = apiInstance.apiTransportTelegramGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelegramApi#apiTransportTelegramGetCollection");
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

[**List&lt;TransportTelegramGet&gt;**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelegram collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelegramIdDelete"></a>
# **apiTransportTelegramIdDelete**
> apiTransportTelegramIdDelete(id)

Removes the TransportTelegram resource.

Removes the TransportTelegram resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelegramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelegramApi apiInstance = new TransportTelegramApi(defaultClient);
    String id = "id_example"; // String | TransportTelegram identifier
    try {
      apiInstance.apiTransportTelegramIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelegramApi#apiTransportTelegramIdDelete");
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
| **id** | **String**| TransportTelegram identifier | |

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
| **204** | TransportTelegram resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelegramIdGet"></a>
# **apiTransportTelegramIdGet**
> TransportTelegramGet apiTransportTelegramIdGet(id)

Retrieves a TransportTelegram resource.

Retrieves a TransportTelegram resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelegramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelegramApi apiInstance = new TransportTelegramApi(defaultClient);
    String id = "id_example"; // String | TransportTelegram identifier
    try {
      TransportTelegramGet result = apiInstance.apiTransportTelegramIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelegramApi#apiTransportTelegramIdGet");
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
| **id** | **String**| TransportTelegram identifier | |

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelegram resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelegramIdPatch"></a>
# **apiTransportTelegramIdPatch**
> TransportTelegramGet apiTransportTelegramIdPatch(id, transportTelegramPatch)

Updates the TransportTelegram resource.

Updates the TransportTelegram resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelegramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelegramApi apiInstance = new TransportTelegramApi(defaultClient);
    String id = "id_example"; // String | TransportTelegram identifier
    TransportTelegramPatch transportTelegramPatch = new TransportTelegramPatch(); // TransportTelegramPatch | The updated TransportTelegram resource
    try {
      TransportTelegramGet result = apiInstance.apiTransportTelegramIdPatch(id, transportTelegramPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelegramApi#apiTransportTelegramIdPatch");
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
| **id** | **String**| TransportTelegram identifier | |
| **transportTelegramPatch** | [**TransportTelegramPatch**](TransportTelegramPatch.md)| The updated TransportTelegram resource | |

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelegram resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelegramIdPut"></a>
# **apiTransportTelegramIdPut**
> TransportTelegramGet apiTransportTelegramIdPut(id, transportTelegramPut)

Replaces the TransportTelegram resource.

Replaces the TransportTelegram resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelegramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelegramApi apiInstance = new TransportTelegramApi(defaultClient);
    String id = "id_example"; // String | TransportTelegram identifier
    TransportTelegramPut transportTelegramPut = new TransportTelegramPut(); // TransportTelegramPut | The updated TransportTelegram resource
    try {
      TransportTelegramGet result = apiInstance.apiTransportTelegramIdPut(id, transportTelegramPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelegramApi#apiTransportTelegramIdPut");
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
| **id** | **String**| TransportTelegram identifier | |
| **transportTelegramPut** | [**TransportTelegramPut**](TransportTelegramPut.md)| The updated TransportTelegram resource | |

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelegram resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelegramPost"></a>
# **apiTransportTelegramPost**
> TransportTelegramGet apiTransportTelegramPost(transportTelegramPost)

Creates a TransportTelegram resource.

Creates a TransportTelegram resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelegramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelegramApi apiInstance = new TransportTelegramApi(defaultClient);
    TransportTelegramPost transportTelegramPost = new TransportTelegramPost(); // TransportTelegramPost | The new TransportTelegram resource
    try {
      TransportTelegramGet result = apiInstance.apiTransportTelegramPost(transportTelegramPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelegramApi#apiTransportTelegramPost");
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
| **transportTelegramPost** | [**TransportTelegramPost**](TransportTelegramPost.md)| The new TransportTelegram resource | |

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTelegram resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

