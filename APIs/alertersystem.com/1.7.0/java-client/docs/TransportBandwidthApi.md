# TransportBandwidthApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportBandwidthGetCollection**](TransportBandwidthApi.md#apiTransportBandwidthGetCollection) | **GET** /api/transport-bandwidth | Retrieves the collection of TransportBandwidth resources. |
| [**apiTransportBandwidthIdDelete**](TransportBandwidthApi.md#apiTransportBandwidthIdDelete) | **DELETE** /api/transport-bandwidth/{id} | Removes the TransportBandwidth resource. |
| [**apiTransportBandwidthIdGet**](TransportBandwidthApi.md#apiTransportBandwidthIdGet) | **GET** /api/transport-bandwidth/{id} | Retrieves a TransportBandwidth resource. |
| [**apiTransportBandwidthIdPatch**](TransportBandwidthApi.md#apiTransportBandwidthIdPatch) | **PATCH** /api/transport-bandwidth/{id} | Updates the TransportBandwidth resource. |
| [**apiTransportBandwidthIdPut**](TransportBandwidthApi.md#apiTransportBandwidthIdPut) | **PUT** /api/transport-bandwidth/{id} | Replaces the TransportBandwidth resource. |
| [**apiTransportBandwidthPost**](TransportBandwidthApi.md#apiTransportBandwidthPost) | **POST** /api/transport-bandwidth | Creates a TransportBandwidth resource. |


<a id="apiTransportBandwidthGetCollection"></a>
# **apiTransportBandwidthGetCollection**
> List&lt;TransportBandwidthGet&gt; apiTransportBandwidthGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportBandwidth resources.

Retrieves the collection of TransportBandwidth resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportBandwidthApi apiInstance = new TransportBandwidthApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportBandwidthGet> result = apiInstance.apiTransportBandwidthGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportBandwidthApi#apiTransportBandwidthGetCollection");
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

[**List&lt;TransportBandwidthGet&gt;**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportBandwidth collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportBandwidthIdDelete"></a>
# **apiTransportBandwidthIdDelete**
> apiTransportBandwidthIdDelete(id)

Removes the TransportBandwidth resource.

Removes the TransportBandwidth resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportBandwidthApi apiInstance = new TransportBandwidthApi(defaultClient);
    String id = "id_example"; // String | TransportBandwidth identifier
    try {
      apiInstance.apiTransportBandwidthIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportBandwidthApi#apiTransportBandwidthIdDelete");
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
| **id** | **String**| TransportBandwidth identifier | |

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
| **204** | TransportBandwidth resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportBandwidthIdGet"></a>
# **apiTransportBandwidthIdGet**
> TransportBandwidthGet apiTransportBandwidthIdGet(id)

Retrieves a TransportBandwidth resource.

Retrieves a TransportBandwidth resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportBandwidthApi apiInstance = new TransportBandwidthApi(defaultClient);
    String id = "id_example"; // String | TransportBandwidth identifier
    try {
      TransportBandwidthGet result = apiInstance.apiTransportBandwidthIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportBandwidthApi#apiTransportBandwidthIdGet");
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
| **id** | **String**| TransportBandwidth identifier | |

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportBandwidth resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportBandwidthIdPatch"></a>
# **apiTransportBandwidthIdPatch**
> TransportBandwidthGet apiTransportBandwidthIdPatch(id, transportBandwidthPatch)

Updates the TransportBandwidth resource.

Updates the TransportBandwidth resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportBandwidthApi apiInstance = new TransportBandwidthApi(defaultClient);
    String id = "id_example"; // String | TransportBandwidth identifier
    TransportBandwidthPatch transportBandwidthPatch = new TransportBandwidthPatch(); // TransportBandwidthPatch | The updated TransportBandwidth resource
    try {
      TransportBandwidthGet result = apiInstance.apiTransportBandwidthIdPatch(id, transportBandwidthPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportBandwidthApi#apiTransportBandwidthIdPatch");
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
| **id** | **String**| TransportBandwidth identifier | |
| **transportBandwidthPatch** | [**TransportBandwidthPatch**](TransportBandwidthPatch.md)| The updated TransportBandwidth resource | |

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportBandwidth resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportBandwidthIdPut"></a>
# **apiTransportBandwidthIdPut**
> TransportBandwidthGet apiTransportBandwidthIdPut(id, transportBandwidthPut)

Replaces the TransportBandwidth resource.

Replaces the TransportBandwidth resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportBandwidthApi apiInstance = new TransportBandwidthApi(defaultClient);
    String id = "id_example"; // String | TransportBandwidth identifier
    TransportBandwidthPut transportBandwidthPut = new TransportBandwidthPut(); // TransportBandwidthPut | The updated TransportBandwidth resource
    try {
      TransportBandwidthGet result = apiInstance.apiTransportBandwidthIdPut(id, transportBandwidthPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportBandwidthApi#apiTransportBandwidthIdPut");
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
| **id** | **String**| TransportBandwidth identifier | |
| **transportBandwidthPut** | [**TransportBandwidthPut**](TransportBandwidthPut.md)| The updated TransportBandwidth resource | |

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportBandwidth resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportBandwidthPost"></a>
# **apiTransportBandwidthPost**
> TransportBandwidthGet apiTransportBandwidthPost(transportBandwidthPost)

Creates a TransportBandwidth resource.

Creates a TransportBandwidth resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportBandwidthApi apiInstance = new TransportBandwidthApi(defaultClient);
    TransportBandwidthPost transportBandwidthPost = new TransportBandwidthPost(); // TransportBandwidthPost | The new TransportBandwidth resource
    try {
      TransportBandwidthGet result = apiInstance.apiTransportBandwidthPost(transportBandwidthPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportBandwidthApi#apiTransportBandwidthPost");
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
| **transportBandwidthPost** | [**TransportBandwidthPost**](TransportBandwidthPost.md)| The new TransportBandwidth resource | |

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportBandwidth resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

