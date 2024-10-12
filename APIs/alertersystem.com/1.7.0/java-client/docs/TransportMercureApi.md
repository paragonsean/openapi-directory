# TransportMercureApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMercureGetCollection**](TransportMercureApi.md#apiTransportMercureGetCollection) | **GET** /api/transport-mercure | Retrieves the collection of TransportMercure resources. |
| [**apiTransportMercureIdDelete**](TransportMercureApi.md#apiTransportMercureIdDelete) | **DELETE** /api/transport-mercure/{id} | Removes the TransportMercure resource. |
| [**apiTransportMercureIdGet**](TransportMercureApi.md#apiTransportMercureIdGet) | **GET** /api/transport-mercure/{id} | Retrieves a TransportMercure resource. |
| [**apiTransportMercureIdPatch**](TransportMercureApi.md#apiTransportMercureIdPatch) | **PATCH** /api/transport-mercure/{id} | Updates the TransportMercure resource. |
| [**apiTransportMercureIdPut**](TransportMercureApi.md#apiTransportMercureIdPut) | **PUT** /api/transport-mercure/{id} | Replaces the TransportMercure resource. |
| [**apiTransportMercurePost**](TransportMercureApi.md#apiTransportMercurePost) | **POST** /api/transport-mercure | Creates a TransportMercure resource. |


<a id="apiTransportMercureGetCollection"></a>
# **apiTransportMercureGetCollection**
> List&lt;TransportMercureGet&gt; apiTransportMercureGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMercure resources.

Retrieves the collection of TransportMercure resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMercureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMercureApi apiInstance = new TransportMercureApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMercureGet> result = apiInstance.apiTransportMercureGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMercureApi#apiTransportMercureGetCollection");
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

[**List&lt;TransportMercureGet&gt;**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMercure collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMercureIdDelete"></a>
# **apiTransportMercureIdDelete**
> apiTransportMercureIdDelete(id)

Removes the TransportMercure resource.

Removes the TransportMercure resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMercureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMercureApi apiInstance = new TransportMercureApi(defaultClient);
    String id = "id_example"; // String | TransportMercure identifier
    try {
      apiInstance.apiTransportMercureIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMercureApi#apiTransportMercureIdDelete");
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
| **id** | **String**| TransportMercure identifier | |

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
| **204** | TransportMercure resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMercureIdGet"></a>
# **apiTransportMercureIdGet**
> TransportMercureGet apiTransportMercureIdGet(id)

Retrieves a TransportMercure resource.

Retrieves a TransportMercure resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMercureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMercureApi apiInstance = new TransportMercureApi(defaultClient);
    String id = "id_example"; // String | TransportMercure identifier
    try {
      TransportMercureGet result = apiInstance.apiTransportMercureIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMercureApi#apiTransportMercureIdGet");
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
| **id** | **String**| TransportMercure identifier | |

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMercure resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMercureIdPatch"></a>
# **apiTransportMercureIdPatch**
> TransportMercureGet apiTransportMercureIdPatch(id, transportMercurePatch)

Updates the TransportMercure resource.

Updates the TransportMercure resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMercureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMercureApi apiInstance = new TransportMercureApi(defaultClient);
    String id = "id_example"; // String | TransportMercure identifier
    TransportMercurePatch transportMercurePatch = new TransportMercurePatch(); // TransportMercurePatch | The updated TransportMercure resource
    try {
      TransportMercureGet result = apiInstance.apiTransportMercureIdPatch(id, transportMercurePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMercureApi#apiTransportMercureIdPatch");
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
| **id** | **String**| TransportMercure identifier | |
| **transportMercurePatch** | [**TransportMercurePatch**](TransportMercurePatch.md)| The updated TransportMercure resource | |

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMercure resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMercureIdPut"></a>
# **apiTransportMercureIdPut**
> TransportMercureGet apiTransportMercureIdPut(id, transportMercurePut)

Replaces the TransportMercure resource.

Replaces the TransportMercure resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMercureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMercureApi apiInstance = new TransportMercureApi(defaultClient);
    String id = "id_example"; // String | TransportMercure identifier
    TransportMercurePut transportMercurePut = new TransportMercurePut(); // TransportMercurePut | The updated TransportMercure resource
    try {
      TransportMercureGet result = apiInstance.apiTransportMercureIdPut(id, transportMercurePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMercureApi#apiTransportMercureIdPut");
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
| **id** | **String**| TransportMercure identifier | |
| **transportMercurePut** | [**TransportMercurePut**](TransportMercurePut.md)| The updated TransportMercure resource | |

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMercure resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMercurePost"></a>
# **apiTransportMercurePost**
> TransportMercureGet apiTransportMercurePost(transportMercurePost)

Creates a TransportMercure resource.

Creates a TransportMercure resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMercureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMercureApi apiInstance = new TransportMercureApi(defaultClient);
    TransportMercurePost transportMercurePost = new TransportMercurePost(); // TransportMercurePost | The new TransportMercure resource
    try {
      TransportMercureGet result = apiInstance.apiTransportMercurePost(transportMercurePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMercureApi#apiTransportMercurePost");
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
| **transportMercurePost** | [**TransportMercurePost**](TransportMercurePost.md)| The new TransportMercure resource | |

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMercure resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

