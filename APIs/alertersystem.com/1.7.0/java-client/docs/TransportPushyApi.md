# TransportPushyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportPushyGetCollection**](TransportPushyApi.md#apiTransportPushyGetCollection) | **GET** /api/transport-pushy | Retrieves the collection of TransportPushy resources. |
| [**apiTransportPushyIdDelete**](TransportPushyApi.md#apiTransportPushyIdDelete) | **DELETE** /api/transport-pushy/{id} | Removes the TransportPushy resource. |
| [**apiTransportPushyIdGet**](TransportPushyApi.md#apiTransportPushyIdGet) | **GET** /api/transport-pushy/{id} | Retrieves a TransportPushy resource. |
| [**apiTransportPushyIdPatch**](TransportPushyApi.md#apiTransportPushyIdPatch) | **PATCH** /api/transport-pushy/{id} | Updates the TransportPushy resource. |
| [**apiTransportPushyIdPut**](TransportPushyApi.md#apiTransportPushyIdPut) | **PUT** /api/transport-pushy/{id} | Replaces the TransportPushy resource. |
| [**apiTransportPushyPost**](TransportPushyApi.md#apiTransportPushyPost) | **POST** /api/transport-pushy | Creates a TransportPushy resource. |


<a id="apiTransportPushyGetCollection"></a>
# **apiTransportPushyGetCollection**
> List&lt;TransportPushyGet&gt; apiTransportPushyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportPushy resources.

Retrieves the collection of TransportPushy resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushyApi apiInstance = new TransportPushyApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportPushyGet> result = apiInstance.apiTransportPushyGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushyApi#apiTransportPushyGetCollection");
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

[**List&lt;TransportPushyGet&gt;**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushy collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushyIdDelete"></a>
# **apiTransportPushyIdDelete**
> apiTransportPushyIdDelete(id)

Removes the TransportPushy resource.

Removes the TransportPushy resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushyApi apiInstance = new TransportPushyApi(defaultClient);
    String id = "id_example"; // String | TransportPushy identifier
    try {
      apiInstance.apiTransportPushyIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushyApi#apiTransportPushyIdDelete");
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
| **id** | **String**| TransportPushy identifier | |

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
| **204** | TransportPushy resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushyIdGet"></a>
# **apiTransportPushyIdGet**
> TransportPushyGet apiTransportPushyIdGet(id)

Retrieves a TransportPushy resource.

Retrieves a TransportPushy resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushyApi apiInstance = new TransportPushyApi(defaultClient);
    String id = "id_example"; // String | TransportPushy identifier
    try {
      TransportPushyGet result = apiInstance.apiTransportPushyIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushyApi#apiTransportPushyIdGet");
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
| **id** | **String**| TransportPushy identifier | |

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushy resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushyIdPatch"></a>
# **apiTransportPushyIdPatch**
> TransportPushyGet apiTransportPushyIdPatch(id, transportPushyPatch)

Updates the TransportPushy resource.

Updates the TransportPushy resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushyApi apiInstance = new TransportPushyApi(defaultClient);
    String id = "id_example"; // String | TransportPushy identifier
    TransportPushyPatch transportPushyPatch = new TransportPushyPatch(); // TransportPushyPatch | The updated TransportPushy resource
    try {
      TransportPushyGet result = apiInstance.apiTransportPushyIdPatch(id, transportPushyPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushyApi#apiTransportPushyIdPatch");
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
| **id** | **String**| TransportPushy identifier | |
| **transportPushyPatch** | [**TransportPushyPatch**](TransportPushyPatch.md)| The updated TransportPushy resource | |

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushy resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushyIdPut"></a>
# **apiTransportPushyIdPut**
> TransportPushyGet apiTransportPushyIdPut(id, transportPushyPut)

Replaces the TransportPushy resource.

Replaces the TransportPushy resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushyApi apiInstance = new TransportPushyApi(defaultClient);
    String id = "id_example"; // String | TransportPushy identifier
    TransportPushyPut transportPushyPut = new TransportPushyPut(); // TransportPushyPut | The updated TransportPushy resource
    try {
      TransportPushyGet result = apiInstance.apiTransportPushyIdPut(id, transportPushyPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushyApi#apiTransportPushyIdPut");
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
| **id** | **String**| TransportPushy identifier | |
| **transportPushyPut** | [**TransportPushyPut**](TransportPushyPut.md)| The updated TransportPushy resource | |

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushy resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushyPost"></a>
# **apiTransportPushyPost**
> TransportPushyGet apiTransportPushyPost(transportPushyPost)

Creates a TransportPushy resource.

Creates a TransportPushy resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushyApi apiInstance = new TransportPushyApi(defaultClient);
    TransportPushyPost transportPushyPost = new TransportPushyPost(); // TransportPushyPost | The new TransportPushy resource
    try {
      TransportPushyGet result = apiInstance.apiTransportPushyPost(transportPushyPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushyApi#apiTransportPushyPost");
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
| **transportPushyPost** | [**TransportPushyPost**](TransportPushyPost.md)| The new TransportPushy resource | |

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportPushy resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

