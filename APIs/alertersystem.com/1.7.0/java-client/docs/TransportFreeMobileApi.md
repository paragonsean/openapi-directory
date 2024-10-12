# TransportFreeMobileApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportFreeMobileGetCollection**](TransportFreeMobileApi.md#apiTransportFreeMobileGetCollection) | **GET** /api/transport-free-mobile | Retrieves the collection of TransportFreeMobile resources. |
| [**apiTransportFreeMobileIdDelete**](TransportFreeMobileApi.md#apiTransportFreeMobileIdDelete) | **DELETE** /api/transport-free-mobile/{id} | Removes the TransportFreeMobile resource. |
| [**apiTransportFreeMobileIdGet**](TransportFreeMobileApi.md#apiTransportFreeMobileIdGet) | **GET** /api/transport-free-mobile/{id} | Retrieves a TransportFreeMobile resource. |
| [**apiTransportFreeMobileIdPatch**](TransportFreeMobileApi.md#apiTransportFreeMobileIdPatch) | **PATCH** /api/transport-free-mobile/{id} | Updates the TransportFreeMobile resource. |
| [**apiTransportFreeMobileIdPut**](TransportFreeMobileApi.md#apiTransportFreeMobileIdPut) | **PUT** /api/transport-free-mobile/{id} | Replaces the TransportFreeMobile resource. |
| [**apiTransportFreeMobilePost**](TransportFreeMobileApi.md#apiTransportFreeMobilePost) | **POST** /api/transport-free-mobile | Creates a TransportFreeMobile resource. |


<a id="apiTransportFreeMobileGetCollection"></a>
# **apiTransportFreeMobileGetCollection**
> List&lt;TransportFreeMobileGet&gt; apiTransportFreeMobileGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportFreeMobile resources.

Retrieves the collection of TransportFreeMobile resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreeMobileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreeMobileApi apiInstance = new TransportFreeMobileApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportFreeMobileGet> result = apiInstance.apiTransportFreeMobileGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreeMobileApi#apiTransportFreeMobileGetCollection");
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

[**List&lt;TransportFreeMobileGet&gt;**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreeMobile collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreeMobileIdDelete"></a>
# **apiTransportFreeMobileIdDelete**
> apiTransportFreeMobileIdDelete(id)

Removes the TransportFreeMobile resource.

Removes the TransportFreeMobile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreeMobileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreeMobileApi apiInstance = new TransportFreeMobileApi(defaultClient);
    String id = "id_example"; // String | TransportFreeMobile identifier
    try {
      apiInstance.apiTransportFreeMobileIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreeMobileApi#apiTransportFreeMobileIdDelete");
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
| **id** | **String**| TransportFreeMobile identifier | |

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
| **204** | TransportFreeMobile resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreeMobileIdGet"></a>
# **apiTransportFreeMobileIdGet**
> TransportFreeMobileGet apiTransportFreeMobileIdGet(id)

Retrieves a TransportFreeMobile resource.

Retrieves a TransportFreeMobile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreeMobileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreeMobileApi apiInstance = new TransportFreeMobileApi(defaultClient);
    String id = "id_example"; // String | TransportFreeMobile identifier
    try {
      TransportFreeMobileGet result = apiInstance.apiTransportFreeMobileIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreeMobileApi#apiTransportFreeMobileIdGet");
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
| **id** | **String**| TransportFreeMobile identifier | |

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreeMobile resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreeMobileIdPatch"></a>
# **apiTransportFreeMobileIdPatch**
> TransportFreeMobileGet apiTransportFreeMobileIdPatch(id, transportFreeMobilePatch)

Updates the TransportFreeMobile resource.

Updates the TransportFreeMobile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreeMobileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreeMobileApi apiInstance = new TransportFreeMobileApi(defaultClient);
    String id = "id_example"; // String | TransportFreeMobile identifier
    TransportFreeMobilePatch transportFreeMobilePatch = new TransportFreeMobilePatch(); // TransportFreeMobilePatch | The updated TransportFreeMobile resource
    try {
      TransportFreeMobileGet result = apiInstance.apiTransportFreeMobileIdPatch(id, transportFreeMobilePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreeMobileApi#apiTransportFreeMobileIdPatch");
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
| **id** | **String**| TransportFreeMobile identifier | |
| **transportFreeMobilePatch** | [**TransportFreeMobilePatch**](TransportFreeMobilePatch.md)| The updated TransportFreeMobile resource | |

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreeMobile resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreeMobileIdPut"></a>
# **apiTransportFreeMobileIdPut**
> TransportFreeMobileGet apiTransportFreeMobileIdPut(id, transportFreeMobilePut)

Replaces the TransportFreeMobile resource.

Replaces the TransportFreeMobile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreeMobileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreeMobileApi apiInstance = new TransportFreeMobileApi(defaultClient);
    String id = "id_example"; // String | TransportFreeMobile identifier
    TransportFreeMobilePut transportFreeMobilePut = new TransportFreeMobilePut(); // TransportFreeMobilePut | The updated TransportFreeMobile resource
    try {
      TransportFreeMobileGet result = apiInstance.apiTransportFreeMobileIdPut(id, transportFreeMobilePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreeMobileApi#apiTransportFreeMobileIdPut");
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
| **id** | **String**| TransportFreeMobile identifier | |
| **transportFreeMobilePut** | [**TransportFreeMobilePut**](TransportFreeMobilePut.md)| The updated TransportFreeMobile resource | |

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFreeMobile resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFreeMobilePost"></a>
# **apiTransportFreeMobilePost**
> TransportFreeMobileGet apiTransportFreeMobilePost(transportFreeMobilePost)

Creates a TransportFreeMobile resource.

Creates a TransportFreeMobile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFreeMobileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFreeMobileApi apiInstance = new TransportFreeMobileApi(defaultClient);
    TransportFreeMobilePost transportFreeMobilePost = new TransportFreeMobilePost(); // TransportFreeMobilePost | The new TransportFreeMobile resource
    try {
      TransportFreeMobileGet result = apiInstance.apiTransportFreeMobilePost(transportFreeMobilePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFreeMobileApi#apiTransportFreeMobilePost");
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
| **transportFreeMobilePost** | [**TransportFreeMobilePost**](TransportFreeMobilePost.md)| The new TransportFreeMobile resource | |

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportFreeMobile resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

