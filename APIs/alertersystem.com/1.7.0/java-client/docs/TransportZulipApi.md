# TransportZulipApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportZulipGetCollection**](TransportZulipApi.md#apiTransportZulipGetCollection) | **GET** /api/transport-zulip | Retrieves the collection of TransportZulip resources. |
| [**apiTransportZulipIdDelete**](TransportZulipApi.md#apiTransportZulipIdDelete) | **DELETE** /api/transport-zulip/{id} | Removes the TransportZulip resource. |
| [**apiTransportZulipIdGet**](TransportZulipApi.md#apiTransportZulipIdGet) | **GET** /api/transport-zulip/{id} | Retrieves a TransportZulip resource. |
| [**apiTransportZulipIdPatch**](TransportZulipApi.md#apiTransportZulipIdPatch) | **PATCH** /api/transport-zulip/{id} | Updates the TransportZulip resource. |
| [**apiTransportZulipIdPut**](TransportZulipApi.md#apiTransportZulipIdPut) | **PUT** /api/transport-zulip/{id} | Replaces the TransportZulip resource. |
| [**apiTransportZulipPost**](TransportZulipApi.md#apiTransportZulipPost) | **POST** /api/transport-zulip | Creates a TransportZulip resource. |


<a id="apiTransportZulipGetCollection"></a>
# **apiTransportZulipGetCollection**
> List&lt;TransportZulipGet&gt; apiTransportZulipGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportZulip resources.

Retrieves the collection of TransportZulip resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZulipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZulipApi apiInstance = new TransportZulipApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportZulipGet> result = apiInstance.apiTransportZulipGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZulipApi#apiTransportZulipGetCollection");
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

[**List&lt;TransportZulipGet&gt;**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZulip collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZulipIdDelete"></a>
# **apiTransportZulipIdDelete**
> apiTransportZulipIdDelete(id)

Removes the TransportZulip resource.

Removes the TransportZulip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZulipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZulipApi apiInstance = new TransportZulipApi(defaultClient);
    String id = "id_example"; // String | TransportZulip identifier
    try {
      apiInstance.apiTransportZulipIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZulipApi#apiTransportZulipIdDelete");
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
| **id** | **String**| TransportZulip identifier | |

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
| **204** | TransportZulip resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZulipIdGet"></a>
# **apiTransportZulipIdGet**
> TransportZulipGet apiTransportZulipIdGet(id)

Retrieves a TransportZulip resource.

Retrieves a TransportZulip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZulipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZulipApi apiInstance = new TransportZulipApi(defaultClient);
    String id = "id_example"; // String | TransportZulip identifier
    try {
      TransportZulipGet result = apiInstance.apiTransportZulipIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZulipApi#apiTransportZulipIdGet");
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
| **id** | **String**| TransportZulip identifier | |

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZulip resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZulipIdPatch"></a>
# **apiTransportZulipIdPatch**
> TransportZulipGet apiTransportZulipIdPatch(id, transportZulipPatch)

Updates the TransportZulip resource.

Updates the TransportZulip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZulipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZulipApi apiInstance = new TransportZulipApi(defaultClient);
    String id = "id_example"; // String | TransportZulip identifier
    TransportZulipPatch transportZulipPatch = new TransportZulipPatch(); // TransportZulipPatch | The updated TransportZulip resource
    try {
      TransportZulipGet result = apiInstance.apiTransportZulipIdPatch(id, transportZulipPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZulipApi#apiTransportZulipIdPatch");
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
| **id** | **String**| TransportZulip identifier | |
| **transportZulipPatch** | [**TransportZulipPatch**](TransportZulipPatch.md)| The updated TransportZulip resource | |

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZulip resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZulipIdPut"></a>
# **apiTransportZulipIdPut**
> TransportZulipGet apiTransportZulipIdPut(id, transportZulipPut)

Replaces the TransportZulip resource.

Replaces the TransportZulip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZulipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZulipApi apiInstance = new TransportZulipApi(defaultClient);
    String id = "id_example"; // String | TransportZulip identifier
    TransportZulipPut transportZulipPut = new TransportZulipPut(); // TransportZulipPut | The updated TransportZulip resource
    try {
      TransportZulipGet result = apiInstance.apiTransportZulipIdPut(id, transportZulipPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZulipApi#apiTransportZulipIdPut");
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
| **id** | **String**| TransportZulip identifier | |
| **transportZulipPut** | [**TransportZulipPut**](TransportZulipPut.md)| The updated TransportZulip resource | |

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportZulip resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportZulipPost"></a>
# **apiTransportZulipPost**
> TransportZulipGet apiTransportZulipPost(transportZulipPost)

Creates a TransportZulip resource.

Creates a TransportZulip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportZulipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportZulipApi apiInstance = new TransportZulipApi(defaultClient);
    TransportZulipPost transportZulipPost = new TransportZulipPost(); // TransportZulipPost | The new TransportZulip resource
    try {
      TransportZulipGet result = apiInstance.apiTransportZulipPost(transportZulipPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportZulipApi#apiTransportZulipPost");
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
| **transportZulipPost** | [**TransportZulipPost**](TransportZulipPost.md)| The new TransportZulip resource | |

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportZulip resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

