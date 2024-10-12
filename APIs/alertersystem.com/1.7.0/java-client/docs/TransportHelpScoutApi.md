# TransportHelpScoutApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportHelpScoutGetCollection**](TransportHelpScoutApi.md#apiTransportHelpScoutGetCollection) | **GET** /api/transport-help-scout | Retrieves the collection of TransportHelpScout resources. |
| [**apiTransportHelpScoutIdDelete**](TransportHelpScoutApi.md#apiTransportHelpScoutIdDelete) | **DELETE** /api/transport-help-scout/{id} | Removes the TransportHelpScout resource. |
| [**apiTransportHelpScoutIdGet**](TransportHelpScoutApi.md#apiTransportHelpScoutIdGet) | **GET** /api/transport-help-scout/{id} | Retrieves a TransportHelpScout resource. |
| [**apiTransportHelpScoutIdPatch**](TransportHelpScoutApi.md#apiTransportHelpScoutIdPatch) | **PATCH** /api/transport-help-scout/{id} | Updates the TransportHelpScout resource. |
| [**apiTransportHelpScoutIdPut**](TransportHelpScoutApi.md#apiTransportHelpScoutIdPut) | **PUT** /api/transport-help-scout/{id} | Replaces the TransportHelpScout resource. |
| [**apiTransportHelpScoutPost**](TransportHelpScoutApi.md#apiTransportHelpScoutPost) | **POST** /api/transport-help-scout | Creates a TransportHelpScout resource. |


<a id="apiTransportHelpScoutGetCollection"></a>
# **apiTransportHelpScoutGetCollection**
> List&lt;TransportHelpScoutGet&gt; apiTransportHelpScoutGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportHelpScout resources.

Retrieves the collection of TransportHelpScout resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportHelpScoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportHelpScoutApi apiInstance = new TransportHelpScoutApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportHelpScoutGet> result = apiInstance.apiTransportHelpScoutGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportHelpScoutApi#apiTransportHelpScoutGetCollection");
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

[**List&lt;TransportHelpScoutGet&gt;**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportHelpScout collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportHelpScoutIdDelete"></a>
# **apiTransportHelpScoutIdDelete**
> apiTransportHelpScoutIdDelete(id)

Removes the TransportHelpScout resource.

Removes the TransportHelpScout resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportHelpScoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportHelpScoutApi apiInstance = new TransportHelpScoutApi(defaultClient);
    String id = "id_example"; // String | TransportHelpScout identifier
    try {
      apiInstance.apiTransportHelpScoutIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportHelpScoutApi#apiTransportHelpScoutIdDelete");
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
| **id** | **String**| TransportHelpScout identifier | |

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
| **204** | TransportHelpScout resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportHelpScoutIdGet"></a>
# **apiTransportHelpScoutIdGet**
> TransportHelpScoutGet apiTransportHelpScoutIdGet(id)

Retrieves a TransportHelpScout resource.

Retrieves a TransportHelpScout resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportHelpScoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportHelpScoutApi apiInstance = new TransportHelpScoutApi(defaultClient);
    String id = "id_example"; // String | TransportHelpScout identifier
    try {
      TransportHelpScoutGet result = apiInstance.apiTransportHelpScoutIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportHelpScoutApi#apiTransportHelpScoutIdGet");
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
| **id** | **String**| TransportHelpScout identifier | |

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportHelpScout resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportHelpScoutIdPatch"></a>
# **apiTransportHelpScoutIdPatch**
> TransportHelpScoutGet apiTransportHelpScoutIdPatch(id, transportHelpScoutPatch)

Updates the TransportHelpScout resource.

Updates the TransportHelpScout resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportHelpScoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportHelpScoutApi apiInstance = new TransportHelpScoutApi(defaultClient);
    String id = "id_example"; // String | TransportHelpScout identifier
    TransportHelpScoutPatch transportHelpScoutPatch = new TransportHelpScoutPatch(); // TransportHelpScoutPatch | The updated TransportHelpScout resource
    try {
      TransportHelpScoutGet result = apiInstance.apiTransportHelpScoutIdPatch(id, transportHelpScoutPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportHelpScoutApi#apiTransportHelpScoutIdPatch");
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
| **id** | **String**| TransportHelpScout identifier | |
| **transportHelpScoutPatch** | [**TransportHelpScoutPatch**](TransportHelpScoutPatch.md)| The updated TransportHelpScout resource | |

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportHelpScout resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportHelpScoutIdPut"></a>
# **apiTransportHelpScoutIdPut**
> TransportHelpScoutGet apiTransportHelpScoutIdPut(id, transportHelpScoutPut)

Replaces the TransportHelpScout resource.

Replaces the TransportHelpScout resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportHelpScoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportHelpScoutApi apiInstance = new TransportHelpScoutApi(defaultClient);
    String id = "id_example"; // String | TransportHelpScout identifier
    TransportHelpScoutPut transportHelpScoutPut = new TransportHelpScoutPut(); // TransportHelpScoutPut | The updated TransportHelpScout resource
    try {
      TransportHelpScoutGet result = apiInstance.apiTransportHelpScoutIdPut(id, transportHelpScoutPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportHelpScoutApi#apiTransportHelpScoutIdPut");
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
| **id** | **String**| TransportHelpScout identifier | |
| **transportHelpScoutPut** | [**TransportHelpScoutPut**](TransportHelpScoutPut.md)| The updated TransportHelpScout resource | |

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportHelpScout resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportHelpScoutPost"></a>
# **apiTransportHelpScoutPost**
> TransportHelpScoutGet apiTransportHelpScoutPost(transportHelpScoutPost)

Creates a TransportHelpScout resource.

Creates a TransportHelpScout resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportHelpScoutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportHelpScoutApi apiInstance = new TransportHelpScoutApi(defaultClient);
    TransportHelpScoutPost transportHelpScoutPost = new TransportHelpScoutPost(); // TransportHelpScoutPost | The new TransportHelpScout resource
    try {
      TransportHelpScoutGet result = apiInstance.apiTransportHelpScoutPost(transportHelpScoutPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportHelpScoutApi#apiTransportHelpScoutPost");
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
| **transportHelpScoutPost** | [**TransportHelpScoutPost**](TransportHelpScoutPost.md)| The new TransportHelpScout resource | |

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportHelpScout resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

