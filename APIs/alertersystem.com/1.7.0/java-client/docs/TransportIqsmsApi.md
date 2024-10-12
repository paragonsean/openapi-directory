# TransportIqsmsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportIqsmsGetCollection**](TransportIqsmsApi.md#apiTransportIqsmsGetCollection) | **GET** /api/transport-iqsms | Retrieves the collection of TransportIqsms resources. |
| [**apiTransportIqsmsIdDelete**](TransportIqsmsApi.md#apiTransportIqsmsIdDelete) | **DELETE** /api/transport-iqsms/{id} | Removes the TransportIqsms resource. |
| [**apiTransportIqsmsIdGet**](TransportIqsmsApi.md#apiTransportIqsmsIdGet) | **GET** /api/transport-iqsms/{id} | Retrieves a TransportIqsms resource. |
| [**apiTransportIqsmsIdPatch**](TransportIqsmsApi.md#apiTransportIqsmsIdPatch) | **PATCH** /api/transport-iqsms/{id} | Updates the TransportIqsms resource. |
| [**apiTransportIqsmsIdPut**](TransportIqsmsApi.md#apiTransportIqsmsIdPut) | **PUT** /api/transport-iqsms/{id} | Replaces the TransportIqsms resource. |
| [**apiTransportIqsmsPost**](TransportIqsmsApi.md#apiTransportIqsmsPost) | **POST** /api/transport-iqsms | Creates a TransportIqsms resource. |


<a id="apiTransportIqsmsGetCollection"></a>
# **apiTransportIqsmsGetCollection**
> List&lt;TransportIqsmsGet&gt; apiTransportIqsmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportIqsms resources.

Retrieves the collection of TransportIqsms resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportIqsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportIqsmsApi apiInstance = new TransportIqsmsApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportIqsmsGet> result = apiInstance.apiTransportIqsmsGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportIqsmsApi#apiTransportIqsmsGetCollection");
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

[**List&lt;TransportIqsmsGet&gt;**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportIqsms collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportIqsmsIdDelete"></a>
# **apiTransportIqsmsIdDelete**
> apiTransportIqsmsIdDelete(id)

Removes the TransportIqsms resource.

Removes the TransportIqsms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportIqsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportIqsmsApi apiInstance = new TransportIqsmsApi(defaultClient);
    String id = "id_example"; // String | TransportIqsms identifier
    try {
      apiInstance.apiTransportIqsmsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportIqsmsApi#apiTransportIqsmsIdDelete");
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
| **id** | **String**| TransportIqsms identifier | |

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
| **204** | TransportIqsms resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportIqsmsIdGet"></a>
# **apiTransportIqsmsIdGet**
> TransportIqsmsGet apiTransportIqsmsIdGet(id)

Retrieves a TransportIqsms resource.

Retrieves a TransportIqsms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportIqsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportIqsmsApi apiInstance = new TransportIqsmsApi(defaultClient);
    String id = "id_example"; // String | TransportIqsms identifier
    try {
      TransportIqsmsGet result = apiInstance.apiTransportIqsmsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportIqsmsApi#apiTransportIqsmsIdGet");
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
| **id** | **String**| TransportIqsms identifier | |

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportIqsms resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportIqsmsIdPatch"></a>
# **apiTransportIqsmsIdPatch**
> TransportIqsmsGet apiTransportIqsmsIdPatch(id, transportIqsmsPatch)

Updates the TransportIqsms resource.

Updates the TransportIqsms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportIqsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportIqsmsApi apiInstance = new TransportIqsmsApi(defaultClient);
    String id = "id_example"; // String | TransportIqsms identifier
    TransportIqsmsPatch transportIqsmsPatch = new TransportIqsmsPatch(); // TransportIqsmsPatch | The updated TransportIqsms resource
    try {
      TransportIqsmsGet result = apiInstance.apiTransportIqsmsIdPatch(id, transportIqsmsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportIqsmsApi#apiTransportIqsmsIdPatch");
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
| **id** | **String**| TransportIqsms identifier | |
| **transportIqsmsPatch** | [**TransportIqsmsPatch**](TransportIqsmsPatch.md)| The updated TransportIqsms resource | |

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportIqsms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportIqsmsIdPut"></a>
# **apiTransportIqsmsIdPut**
> TransportIqsmsGet apiTransportIqsmsIdPut(id, transportIqsmsPut)

Replaces the TransportIqsms resource.

Replaces the TransportIqsms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportIqsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportIqsmsApi apiInstance = new TransportIqsmsApi(defaultClient);
    String id = "id_example"; // String | TransportIqsms identifier
    TransportIqsmsPut transportIqsmsPut = new TransportIqsmsPut(); // TransportIqsmsPut | The updated TransportIqsms resource
    try {
      TransportIqsmsGet result = apiInstance.apiTransportIqsmsIdPut(id, transportIqsmsPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportIqsmsApi#apiTransportIqsmsIdPut");
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
| **id** | **String**| TransportIqsms identifier | |
| **transportIqsmsPut** | [**TransportIqsmsPut**](TransportIqsmsPut.md)| The updated TransportIqsms resource | |

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportIqsms resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportIqsmsPost"></a>
# **apiTransportIqsmsPost**
> TransportIqsmsGet apiTransportIqsmsPost(transportIqsmsPost)

Creates a TransportIqsms resource.

Creates a TransportIqsms resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportIqsmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportIqsmsApi apiInstance = new TransportIqsmsApi(defaultClient);
    TransportIqsmsPost transportIqsmsPost = new TransportIqsmsPost(); // TransportIqsmsPost | The new TransportIqsms resource
    try {
      TransportIqsmsGet result = apiInstance.apiTransportIqsmsPost(transportIqsmsPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportIqsmsApi#apiTransportIqsmsPost");
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
| **transportIqsmsPost** | [**TransportIqsmsPost**](TransportIqsmsPost.md)| The new TransportIqsms resource | |

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportIqsms resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

