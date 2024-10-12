# TransportGitterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportGitterGetCollection**](TransportGitterApi.md#apiTransportGitterGetCollection) | **GET** /api/transport-gitter | Retrieves the collection of TransportGitter resources. |
| [**apiTransportGitterIdDelete**](TransportGitterApi.md#apiTransportGitterIdDelete) | **DELETE** /api/transport-gitter/{id} | Removes the TransportGitter resource. |
| [**apiTransportGitterIdGet**](TransportGitterApi.md#apiTransportGitterIdGet) | **GET** /api/transport-gitter/{id} | Retrieves a TransportGitter resource. |
| [**apiTransportGitterIdPatch**](TransportGitterApi.md#apiTransportGitterIdPatch) | **PATCH** /api/transport-gitter/{id} | Updates the TransportGitter resource. |
| [**apiTransportGitterIdPut**](TransportGitterApi.md#apiTransportGitterIdPut) | **PUT** /api/transport-gitter/{id} | Replaces the TransportGitter resource. |
| [**apiTransportGitterPost**](TransportGitterApi.md#apiTransportGitterPost) | **POST** /api/transport-gitter | Creates a TransportGitter resource. |


<a id="apiTransportGitterGetCollection"></a>
# **apiTransportGitterGetCollection**
> List&lt;TransportGitterGet&gt; apiTransportGitterGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportGitter resources.

Retrieves the collection of TransportGitter resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGitterApi apiInstance = new TransportGitterApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportGitterGet> result = apiInstance.apiTransportGitterGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGitterApi#apiTransportGitterGetCollection");
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

[**List&lt;TransportGitterGet&gt;**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGitter collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGitterIdDelete"></a>
# **apiTransportGitterIdDelete**
> apiTransportGitterIdDelete(id)

Removes the TransportGitter resource.

Removes the TransportGitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGitterApi apiInstance = new TransportGitterApi(defaultClient);
    String id = "id_example"; // String | TransportGitter identifier
    try {
      apiInstance.apiTransportGitterIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGitterApi#apiTransportGitterIdDelete");
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
| **id** | **String**| TransportGitter identifier | |

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
| **204** | TransportGitter resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGitterIdGet"></a>
# **apiTransportGitterIdGet**
> TransportGitterGet apiTransportGitterIdGet(id)

Retrieves a TransportGitter resource.

Retrieves a TransportGitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGitterApi apiInstance = new TransportGitterApi(defaultClient);
    String id = "id_example"; // String | TransportGitter identifier
    try {
      TransportGitterGet result = apiInstance.apiTransportGitterIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGitterApi#apiTransportGitterIdGet");
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
| **id** | **String**| TransportGitter identifier | |

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGitter resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGitterIdPatch"></a>
# **apiTransportGitterIdPatch**
> TransportGitterGet apiTransportGitterIdPatch(id, transportGitterPatch)

Updates the TransportGitter resource.

Updates the TransportGitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGitterApi apiInstance = new TransportGitterApi(defaultClient);
    String id = "id_example"; // String | TransportGitter identifier
    TransportGitterPatch transportGitterPatch = new TransportGitterPatch(); // TransportGitterPatch | The updated TransportGitter resource
    try {
      TransportGitterGet result = apiInstance.apiTransportGitterIdPatch(id, transportGitterPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGitterApi#apiTransportGitterIdPatch");
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
| **id** | **String**| TransportGitter identifier | |
| **transportGitterPatch** | [**TransportGitterPatch**](TransportGitterPatch.md)| The updated TransportGitter resource | |

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGitter resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGitterIdPut"></a>
# **apiTransportGitterIdPut**
> TransportGitterGet apiTransportGitterIdPut(id, transportGitterPut)

Replaces the TransportGitter resource.

Replaces the TransportGitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGitterApi apiInstance = new TransportGitterApi(defaultClient);
    String id = "id_example"; // String | TransportGitter identifier
    TransportGitterPut transportGitterPut = new TransportGitterPut(); // TransportGitterPut | The updated TransportGitter resource
    try {
      TransportGitterGet result = apiInstance.apiTransportGitterIdPut(id, transportGitterPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGitterApi#apiTransportGitterIdPut");
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
| **id** | **String**| TransportGitter identifier | |
| **transportGitterPut** | [**TransportGitterPut**](TransportGitterPut.md)| The updated TransportGitter resource | |

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGitter resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGitterPost"></a>
# **apiTransportGitterPost**
> TransportGitterGet apiTransportGitterPost(transportGitterPost)

Creates a TransportGitter resource.

Creates a TransportGitter resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGitterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGitterApi apiInstance = new TransportGitterApi(defaultClient);
    TransportGitterPost transportGitterPost = new TransportGitterPost(); // TransportGitterPost | The new TransportGitter resource
    try {
      TransportGitterGet result = apiInstance.apiTransportGitterPost(transportGitterPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGitterApi#apiTransportGitterPost");
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
| **transportGitterPost** | [**TransportGitterPost**](TransportGitterPost.md)| The new TransportGitter resource | |

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportGitter resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

