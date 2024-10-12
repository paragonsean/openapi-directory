# TransportPagerTreeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportPagerTreeGetCollection**](TransportPagerTreeApi.md#apiTransportPagerTreeGetCollection) | **GET** /api/transport-pager-tree | Retrieves the collection of TransportPagerTree resources. |
| [**apiTransportPagerTreeIdDelete**](TransportPagerTreeApi.md#apiTransportPagerTreeIdDelete) | **DELETE** /api/transport-pager-tree/{id} | Removes the TransportPagerTree resource. |
| [**apiTransportPagerTreeIdGet**](TransportPagerTreeApi.md#apiTransportPagerTreeIdGet) | **GET** /api/transport-pager-tree/{id} | Retrieves a TransportPagerTree resource. |
| [**apiTransportPagerTreeIdPatch**](TransportPagerTreeApi.md#apiTransportPagerTreeIdPatch) | **PATCH** /api/transport-pager-tree/{id} | Updates the TransportPagerTree resource. |
| [**apiTransportPagerTreeIdPut**](TransportPagerTreeApi.md#apiTransportPagerTreeIdPut) | **PUT** /api/transport-pager-tree/{id} | Replaces the TransportPagerTree resource. |
| [**apiTransportPagerTreePost**](TransportPagerTreeApi.md#apiTransportPagerTreePost) | **POST** /api/transport-pager-tree | Creates a TransportPagerTree resource. |


<a id="apiTransportPagerTreeGetCollection"></a>
# **apiTransportPagerTreeGetCollection**
> List&lt;TransportPagerTreeGet&gt; apiTransportPagerTreeGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportPagerTree resources.

Retrieves the collection of TransportPagerTree resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerTreeApi apiInstance = new TransportPagerTreeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportPagerTreeGet> result = apiInstance.apiTransportPagerTreeGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerTreeApi#apiTransportPagerTreeGetCollection");
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

[**List&lt;TransportPagerTreeGet&gt;**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerTree collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerTreeIdDelete"></a>
# **apiTransportPagerTreeIdDelete**
> apiTransportPagerTreeIdDelete(id)

Removes the TransportPagerTree resource.

Removes the TransportPagerTree resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerTreeApi apiInstance = new TransportPagerTreeApi(defaultClient);
    String id = "id_example"; // String | TransportPagerTree identifier
    try {
      apiInstance.apiTransportPagerTreeIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerTreeApi#apiTransportPagerTreeIdDelete");
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
| **id** | **String**| TransportPagerTree identifier | |

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
| **204** | TransportPagerTree resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerTreeIdGet"></a>
# **apiTransportPagerTreeIdGet**
> TransportPagerTreeGet apiTransportPagerTreeIdGet(id)

Retrieves a TransportPagerTree resource.

Retrieves a TransportPagerTree resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerTreeApi apiInstance = new TransportPagerTreeApi(defaultClient);
    String id = "id_example"; // String | TransportPagerTree identifier
    try {
      TransportPagerTreeGet result = apiInstance.apiTransportPagerTreeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerTreeApi#apiTransportPagerTreeIdGet");
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
| **id** | **String**| TransportPagerTree identifier | |

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerTree resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerTreeIdPatch"></a>
# **apiTransportPagerTreeIdPatch**
> TransportPagerTreeGet apiTransportPagerTreeIdPatch(id, transportPagerTreePatch)

Updates the TransportPagerTree resource.

Updates the TransportPagerTree resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerTreeApi apiInstance = new TransportPagerTreeApi(defaultClient);
    String id = "id_example"; // String | TransportPagerTree identifier
    TransportPagerTreePatch transportPagerTreePatch = new TransportPagerTreePatch(); // TransportPagerTreePatch | The updated TransportPagerTree resource
    try {
      TransportPagerTreeGet result = apiInstance.apiTransportPagerTreeIdPatch(id, transportPagerTreePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerTreeApi#apiTransportPagerTreeIdPatch");
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
| **id** | **String**| TransportPagerTree identifier | |
| **transportPagerTreePatch** | [**TransportPagerTreePatch**](TransportPagerTreePatch.md)| The updated TransportPagerTree resource | |

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerTree resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerTreeIdPut"></a>
# **apiTransportPagerTreeIdPut**
> TransportPagerTreeGet apiTransportPagerTreeIdPut(id, transportPagerTreePut)

Replaces the TransportPagerTree resource.

Replaces the TransportPagerTree resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerTreeApi apiInstance = new TransportPagerTreeApi(defaultClient);
    String id = "id_example"; // String | TransportPagerTree identifier
    TransportPagerTreePut transportPagerTreePut = new TransportPagerTreePut(); // TransportPagerTreePut | The updated TransportPagerTree resource
    try {
      TransportPagerTreeGet result = apiInstance.apiTransportPagerTreeIdPut(id, transportPagerTreePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerTreeApi#apiTransportPagerTreeIdPut");
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
| **id** | **String**| TransportPagerTree identifier | |
| **transportPagerTreePut** | [**TransportPagerTreePut**](TransportPagerTreePut.md)| The updated TransportPagerTree resource | |

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPagerTree resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPagerTreePost"></a>
# **apiTransportPagerTreePost**
> TransportPagerTreeGet apiTransportPagerTreePost(transportPagerTreePost)

Creates a TransportPagerTree resource.

Creates a TransportPagerTree resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPagerTreeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPagerTreeApi apiInstance = new TransportPagerTreeApi(defaultClient);
    TransportPagerTreePost transportPagerTreePost = new TransportPagerTreePost(); // TransportPagerTreePost | The new TransportPagerTree resource
    try {
      TransportPagerTreeGet result = apiInstance.apiTransportPagerTreePost(transportPagerTreePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPagerTreeApi#apiTransportPagerTreePost");
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
| **transportPagerTreePost** | [**TransportPagerTreePost**](TransportPagerTreePost.md)| The new TransportPagerTree resource | |

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportPagerTree resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

