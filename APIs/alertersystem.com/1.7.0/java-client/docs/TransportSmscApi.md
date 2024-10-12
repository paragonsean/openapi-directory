# TransportSmscApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSmscGetCollection**](TransportSmscApi.md#apiTransportSmscGetCollection) | **GET** /api/transport-smsc | Retrieves the collection of TransportSmsc resources. |
| [**apiTransportSmscIdDelete**](TransportSmscApi.md#apiTransportSmscIdDelete) | **DELETE** /api/transport-smsc/{id} | Removes the TransportSmsc resource. |
| [**apiTransportSmscIdGet**](TransportSmscApi.md#apiTransportSmscIdGet) | **GET** /api/transport-smsc/{id} | Retrieves a TransportSmsc resource. |
| [**apiTransportSmscIdPatch**](TransportSmscApi.md#apiTransportSmscIdPatch) | **PATCH** /api/transport-smsc/{id} | Updates the TransportSmsc resource. |
| [**apiTransportSmscIdPut**](TransportSmscApi.md#apiTransportSmscIdPut) | **PUT** /api/transport-smsc/{id} | Replaces the TransportSmsc resource. |
| [**apiTransportSmscPost**](TransportSmscApi.md#apiTransportSmscPost) | **POST** /api/transport-smsc | Creates a TransportSmsc resource. |


<a id="apiTransportSmscGetCollection"></a>
# **apiTransportSmscGetCollection**
> List&lt;TransportSmscGet&gt; apiTransportSmscGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSmsc resources.

Retrieves the collection of TransportSmsc resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmscApi apiInstance = new TransportSmscApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSmscGet> result = apiInstance.apiTransportSmscGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmscApi#apiTransportSmscGetCollection");
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

[**List&lt;TransportSmscGet&gt;**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsc collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmscIdDelete"></a>
# **apiTransportSmscIdDelete**
> apiTransportSmscIdDelete(id)

Removes the TransportSmsc resource.

Removes the TransportSmsc resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmscApi apiInstance = new TransportSmscApi(defaultClient);
    String id = "id_example"; // String | TransportSmsc identifier
    try {
      apiInstance.apiTransportSmscIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmscApi#apiTransportSmscIdDelete");
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
| **id** | **String**| TransportSmsc identifier | |

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
| **204** | TransportSmsc resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmscIdGet"></a>
# **apiTransportSmscIdGet**
> TransportSmscGet apiTransportSmscIdGet(id)

Retrieves a TransportSmsc resource.

Retrieves a TransportSmsc resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmscApi apiInstance = new TransportSmscApi(defaultClient);
    String id = "id_example"; // String | TransportSmsc identifier
    try {
      TransportSmscGet result = apiInstance.apiTransportSmscIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmscApi#apiTransportSmscIdGet");
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
| **id** | **String**| TransportSmsc identifier | |

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsc resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmscIdPatch"></a>
# **apiTransportSmscIdPatch**
> TransportSmscGet apiTransportSmscIdPatch(id, transportSmscPatch)

Updates the TransportSmsc resource.

Updates the TransportSmsc resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmscApi apiInstance = new TransportSmscApi(defaultClient);
    String id = "id_example"; // String | TransportSmsc identifier
    TransportSmscPatch transportSmscPatch = new TransportSmscPatch(); // TransportSmscPatch | The updated TransportSmsc resource
    try {
      TransportSmscGet result = apiInstance.apiTransportSmscIdPatch(id, transportSmscPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmscApi#apiTransportSmscIdPatch");
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
| **id** | **String**| TransportSmsc identifier | |
| **transportSmscPatch** | [**TransportSmscPatch**](TransportSmscPatch.md)| The updated TransportSmsc resource | |

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsc resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmscIdPut"></a>
# **apiTransportSmscIdPut**
> TransportSmscGet apiTransportSmscIdPut(id, transportSmscPut)

Replaces the TransportSmsc resource.

Replaces the TransportSmsc resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmscApi apiInstance = new TransportSmscApi(defaultClient);
    String id = "id_example"; // String | TransportSmsc identifier
    TransportSmscPut transportSmscPut = new TransportSmscPut(); // TransportSmscPut | The updated TransportSmsc resource
    try {
      TransportSmscGet result = apiInstance.apiTransportSmscIdPut(id, transportSmscPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmscApi#apiTransportSmscIdPut");
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
| **id** | **String**| TransportSmsc identifier | |
| **transportSmscPut** | [**TransportSmscPut**](TransportSmscPut.md)| The updated TransportSmsc resource | |

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSmsc resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSmscPost"></a>
# **apiTransportSmscPost**
> TransportSmscGet apiTransportSmscPost(transportSmscPost)

Creates a TransportSmsc resource.

Creates a TransportSmsc resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSmscApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSmscApi apiInstance = new TransportSmscApi(defaultClient);
    TransportSmscPost transportSmscPost = new TransportSmscPost(); // TransportSmscPost | The new TransportSmsc resource
    try {
      TransportSmscGet result = apiInstance.apiTransportSmscPost(transportSmscPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSmscApi#apiTransportSmscPost");
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
| **transportSmscPost** | [**TransportSmscPost**](TransportSmscPost.md)| The new TransportSmsc resource | |

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSmsc resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

