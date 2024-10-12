# TransportSinchApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSinchGetCollection**](TransportSinchApi.md#apiTransportSinchGetCollection) | **GET** /api/transport-sinch | Retrieves the collection of TransportSinch resources. |
| [**apiTransportSinchIdDelete**](TransportSinchApi.md#apiTransportSinchIdDelete) | **DELETE** /api/transport-sinch/{id} | Removes the TransportSinch resource. |
| [**apiTransportSinchIdGet**](TransportSinchApi.md#apiTransportSinchIdGet) | **GET** /api/transport-sinch/{id} | Retrieves a TransportSinch resource. |
| [**apiTransportSinchIdPatch**](TransportSinchApi.md#apiTransportSinchIdPatch) | **PATCH** /api/transport-sinch/{id} | Updates the TransportSinch resource. |
| [**apiTransportSinchIdPut**](TransportSinchApi.md#apiTransportSinchIdPut) | **PUT** /api/transport-sinch/{id} | Replaces the TransportSinch resource. |
| [**apiTransportSinchPost**](TransportSinchApi.md#apiTransportSinchPost) | **POST** /api/transport-sinch | Creates a TransportSinch resource. |


<a id="apiTransportSinchGetCollection"></a>
# **apiTransportSinchGetCollection**
> List&lt;TransportSinchGet&gt; apiTransportSinchGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSinch resources.

Retrieves the collection of TransportSinch resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSinchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSinchApi apiInstance = new TransportSinchApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSinchGet> result = apiInstance.apiTransportSinchGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSinchApi#apiTransportSinchGetCollection");
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

[**List&lt;TransportSinchGet&gt;**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSinch collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSinchIdDelete"></a>
# **apiTransportSinchIdDelete**
> apiTransportSinchIdDelete(id)

Removes the TransportSinch resource.

Removes the TransportSinch resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSinchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSinchApi apiInstance = new TransportSinchApi(defaultClient);
    String id = "id_example"; // String | TransportSinch identifier
    try {
      apiInstance.apiTransportSinchIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSinchApi#apiTransportSinchIdDelete");
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
| **id** | **String**| TransportSinch identifier | |

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
| **204** | TransportSinch resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSinchIdGet"></a>
# **apiTransportSinchIdGet**
> TransportSinchGet apiTransportSinchIdGet(id)

Retrieves a TransportSinch resource.

Retrieves a TransportSinch resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSinchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSinchApi apiInstance = new TransportSinchApi(defaultClient);
    String id = "id_example"; // String | TransportSinch identifier
    try {
      TransportSinchGet result = apiInstance.apiTransportSinchIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSinchApi#apiTransportSinchIdGet");
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
| **id** | **String**| TransportSinch identifier | |

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSinch resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSinchIdPatch"></a>
# **apiTransportSinchIdPatch**
> TransportSinchGet apiTransportSinchIdPatch(id, transportSinchPatch)

Updates the TransportSinch resource.

Updates the TransportSinch resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSinchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSinchApi apiInstance = new TransportSinchApi(defaultClient);
    String id = "id_example"; // String | TransportSinch identifier
    TransportSinchPatch transportSinchPatch = new TransportSinchPatch(); // TransportSinchPatch | The updated TransportSinch resource
    try {
      TransportSinchGet result = apiInstance.apiTransportSinchIdPatch(id, transportSinchPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSinchApi#apiTransportSinchIdPatch");
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
| **id** | **String**| TransportSinch identifier | |
| **transportSinchPatch** | [**TransportSinchPatch**](TransportSinchPatch.md)| The updated TransportSinch resource | |

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSinch resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSinchIdPut"></a>
# **apiTransportSinchIdPut**
> TransportSinchGet apiTransportSinchIdPut(id, transportSinchPut)

Replaces the TransportSinch resource.

Replaces the TransportSinch resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSinchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSinchApi apiInstance = new TransportSinchApi(defaultClient);
    String id = "id_example"; // String | TransportSinch identifier
    TransportSinchPut transportSinchPut = new TransportSinchPut(); // TransportSinchPut | The updated TransportSinch resource
    try {
      TransportSinchGet result = apiInstance.apiTransportSinchIdPut(id, transportSinchPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSinchApi#apiTransportSinchIdPut");
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
| **id** | **String**| TransportSinch identifier | |
| **transportSinchPut** | [**TransportSinchPut**](TransportSinchPut.md)| The updated TransportSinch resource | |

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSinch resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSinchPost"></a>
# **apiTransportSinchPost**
> TransportSinchGet apiTransportSinchPost(transportSinchPost)

Creates a TransportSinch resource.

Creates a TransportSinch resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSinchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSinchApi apiInstance = new TransportSinchApi(defaultClient);
    TransportSinchPost transportSinchPost = new TransportSinchPost(); // TransportSinchPost | The new TransportSinch resource
    try {
      TransportSinchGet result = apiInstance.apiTransportSinchPost(transportSinchPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSinchApi#apiTransportSinchPost");
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
| **transportSinchPost** | [**TransportSinchPost**](TransportSinchPost.md)| The new TransportSinch resource | |

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSinch resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

