# TransportTelnyxApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTelnyxGetCollection**](TransportTelnyxApi.md#apiTransportTelnyxGetCollection) | **GET** /api/transport-telnyx | Retrieves the collection of TransportTelnyx resources. |
| [**apiTransportTelnyxIdDelete**](TransportTelnyxApi.md#apiTransportTelnyxIdDelete) | **DELETE** /api/transport-telnyx/{id} | Removes the TransportTelnyx resource. |
| [**apiTransportTelnyxIdGet**](TransportTelnyxApi.md#apiTransportTelnyxIdGet) | **GET** /api/transport-telnyx/{id} | Retrieves a TransportTelnyx resource. |
| [**apiTransportTelnyxIdPatch**](TransportTelnyxApi.md#apiTransportTelnyxIdPatch) | **PATCH** /api/transport-telnyx/{id} | Updates the TransportTelnyx resource. |
| [**apiTransportTelnyxIdPut**](TransportTelnyxApi.md#apiTransportTelnyxIdPut) | **PUT** /api/transport-telnyx/{id} | Replaces the TransportTelnyx resource. |
| [**apiTransportTelnyxPost**](TransportTelnyxApi.md#apiTransportTelnyxPost) | **POST** /api/transport-telnyx | Creates a TransportTelnyx resource. |


<a id="apiTransportTelnyxGetCollection"></a>
# **apiTransportTelnyxGetCollection**
> List&lt;TransportTelnyxGet&gt; apiTransportTelnyxGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTelnyx resources.

Retrieves the collection of TransportTelnyx resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelnyxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelnyxApi apiInstance = new TransportTelnyxApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTelnyxGet> result = apiInstance.apiTransportTelnyxGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelnyxApi#apiTransportTelnyxGetCollection");
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

[**List&lt;TransportTelnyxGet&gt;**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelnyx collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelnyxIdDelete"></a>
# **apiTransportTelnyxIdDelete**
> apiTransportTelnyxIdDelete(id)

Removes the TransportTelnyx resource.

Removes the TransportTelnyx resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelnyxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelnyxApi apiInstance = new TransportTelnyxApi(defaultClient);
    String id = "id_example"; // String | TransportTelnyx identifier
    try {
      apiInstance.apiTransportTelnyxIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelnyxApi#apiTransportTelnyxIdDelete");
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
| **id** | **String**| TransportTelnyx identifier | |

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
| **204** | TransportTelnyx resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelnyxIdGet"></a>
# **apiTransportTelnyxIdGet**
> TransportTelnyxGet apiTransportTelnyxIdGet(id)

Retrieves a TransportTelnyx resource.

Retrieves a TransportTelnyx resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelnyxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelnyxApi apiInstance = new TransportTelnyxApi(defaultClient);
    String id = "id_example"; // String | TransportTelnyx identifier
    try {
      TransportTelnyxGet result = apiInstance.apiTransportTelnyxIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelnyxApi#apiTransportTelnyxIdGet");
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
| **id** | **String**| TransportTelnyx identifier | |

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelnyx resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelnyxIdPatch"></a>
# **apiTransportTelnyxIdPatch**
> TransportTelnyxGet apiTransportTelnyxIdPatch(id, transportTelnyxPatch)

Updates the TransportTelnyx resource.

Updates the TransportTelnyx resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelnyxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelnyxApi apiInstance = new TransportTelnyxApi(defaultClient);
    String id = "id_example"; // String | TransportTelnyx identifier
    TransportTelnyxPatch transportTelnyxPatch = new TransportTelnyxPatch(); // TransportTelnyxPatch | The updated TransportTelnyx resource
    try {
      TransportTelnyxGet result = apiInstance.apiTransportTelnyxIdPatch(id, transportTelnyxPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelnyxApi#apiTransportTelnyxIdPatch");
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
| **id** | **String**| TransportTelnyx identifier | |
| **transportTelnyxPatch** | [**TransportTelnyxPatch**](TransportTelnyxPatch.md)| The updated TransportTelnyx resource | |

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelnyx resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelnyxIdPut"></a>
# **apiTransportTelnyxIdPut**
> TransportTelnyxGet apiTransportTelnyxIdPut(id, transportTelnyxPut)

Replaces the TransportTelnyx resource.

Replaces the TransportTelnyx resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelnyxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelnyxApi apiInstance = new TransportTelnyxApi(defaultClient);
    String id = "id_example"; // String | TransportTelnyx identifier
    TransportTelnyxPut transportTelnyxPut = new TransportTelnyxPut(); // TransportTelnyxPut | The updated TransportTelnyx resource
    try {
      TransportTelnyxGet result = apiInstance.apiTransportTelnyxIdPut(id, transportTelnyxPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelnyxApi#apiTransportTelnyxIdPut");
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
| **id** | **String**| TransportTelnyx identifier | |
| **transportTelnyxPut** | [**TransportTelnyxPut**](TransportTelnyxPut.md)| The updated TransportTelnyx resource | |

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTelnyx resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTelnyxPost"></a>
# **apiTransportTelnyxPost**
> TransportTelnyxGet apiTransportTelnyxPost(transportTelnyxPost)

Creates a TransportTelnyx resource.

Creates a TransportTelnyx resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTelnyxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTelnyxApi apiInstance = new TransportTelnyxApi(defaultClient);
    TransportTelnyxPost transportTelnyxPost = new TransportTelnyxPost(); // TransportTelnyxPost | The new TransportTelnyx resource
    try {
      TransportTelnyxGet result = apiInstance.apiTransportTelnyxPost(transportTelnyxPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTelnyxApi#apiTransportTelnyxPost");
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
| **transportTelnyxPost** | [**TransportTelnyxPost**](TransportTelnyxPost.md)| The new TransportTelnyx resource | |

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTelnyx resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

