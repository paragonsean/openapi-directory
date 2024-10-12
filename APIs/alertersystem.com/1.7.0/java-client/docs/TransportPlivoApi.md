# TransportPlivoApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportPlivoGetCollection**](TransportPlivoApi.md#apiTransportPlivoGetCollection) | **GET** /api/transport-plivo | Retrieves the collection of TransportPlivo resources. |
| [**apiTransportPlivoIdDelete**](TransportPlivoApi.md#apiTransportPlivoIdDelete) | **DELETE** /api/transport-plivo/{id} | Removes the TransportPlivo resource. |
| [**apiTransportPlivoIdGet**](TransportPlivoApi.md#apiTransportPlivoIdGet) | **GET** /api/transport-plivo/{id} | Retrieves a TransportPlivo resource. |
| [**apiTransportPlivoIdPatch**](TransportPlivoApi.md#apiTransportPlivoIdPatch) | **PATCH** /api/transport-plivo/{id} | Updates the TransportPlivo resource. |
| [**apiTransportPlivoIdPut**](TransportPlivoApi.md#apiTransportPlivoIdPut) | **PUT** /api/transport-plivo/{id} | Replaces the TransportPlivo resource. |
| [**apiTransportPlivoPost**](TransportPlivoApi.md#apiTransportPlivoPost) | **POST** /api/transport-plivo | Creates a TransportPlivo resource. |


<a id="apiTransportPlivoGetCollection"></a>
# **apiTransportPlivoGetCollection**
> List&lt;TransportPlivoGet&gt; apiTransportPlivoGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportPlivo resources.

Retrieves the collection of TransportPlivo resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPlivoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPlivoApi apiInstance = new TransportPlivoApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportPlivoGet> result = apiInstance.apiTransportPlivoGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPlivoApi#apiTransportPlivoGetCollection");
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

[**List&lt;TransportPlivoGet&gt;**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPlivo collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPlivoIdDelete"></a>
# **apiTransportPlivoIdDelete**
> apiTransportPlivoIdDelete(id)

Removes the TransportPlivo resource.

Removes the TransportPlivo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPlivoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPlivoApi apiInstance = new TransportPlivoApi(defaultClient);
    String id = "id_example"; // String | TransportPlivo identifier
    try {
      apiInstance.apiTransportPlivoIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPlivoApi#apiTransportPlivoIdDelete");
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
| **id** | **String**| TransportPlivo identifier | |

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
| **204** | TransportPlivo resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPlivoIdGet"></a>
# **apiTransportPlivoIdGet**
> TransportPlivoGet apiTransportPlivoIdGet(id)

Retrieves a TransportPlivo resource.

Retrieves a TransportPlivo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPlivoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPlivoApi apiInstance = new TransportPlivoApi(defaultClient);
    String id = "id_example"; // String | TransportPlivo identifier
    try {
      TransportPlivoGet result = apiInstance.apiTransportPlivoIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPlivoApi#apiTransportPlivoIdGet");
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
| **id** | **String**| TransportPlivo identifier | |

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPlivo resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPlivoIdPatch"></a>
# **apiTransportPlivoIdPatch**
> TransportPlivoGet apiTransportPlivoIdPatch(id, transportPlivoPatch)

Updates the TransportPlivo resource.

Updates the TransportPlivo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPlivoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPlivoApi apiInstance = new TransportPlivoApi(defaultClient);
    String id = "id_example"; // String | TransportPlivo identifier
    TransportPlivoPatch transportPlivoPatch = new TransportPlivoPatch(); // TransportPlivoPatch | The updated TransportPlivo resource
    try {
      TransportPlivoGet result = apiInstance.apiTransportPlivoIdPatch(id, transportPlivoPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPlivoApi#apiTransportPlivoIdPatch");
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
| **id** | **String**| TransportPlivo identifier | |
| **transportPlivoPatch** | [**TransportPlivoPatch**](TransportPlivoPatch.md)| The updated TransportPlivo resource | |

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPlivo resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPlivoIdPut"></a>
# **apiTransportPlivoIdPut**
> TransportPlivoGet apiTransportPlivoIdPut(id, transportPlivoPut)

Replaces the TransportPlivo resource.

Replaces the TransportPlivo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPlivoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPlivoApi apiInstance = new TransportPlivoApi(defaultClient);
    String id = "id_example"; // String | TransportPlivo identifier
    TransportPlivoPut transportPlivoPut = new TransportPlivoPut(); // TransportPlivoPut | The updated TransportPlivo resource
    try {
      TransportPlivoGet result = apiInstance.apiTransportPlivoIdPut(id, transportPlivoPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPlivoApi#apiTransportPlivoIdPut");
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
| **id** | **String**| TransportPlivo identifier | |
| **transportPlivoPut** | [**TransportPlivoPut**](TransportPlivoPut.md)| The updated TransportPlivo resource | |

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPlivo resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPlivoPost"></a>
# **apiTransportPlivoPost**
> TransportPlivoGet apiTransportPlivoPost(transportPlivoPost)

Creates a TransportPlivo resource.

Creates a TransportPlivo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPlivoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPlivoApi apiInstance = new TransportPlivoApi(defaultClient);
    TransportPlivoPost transportPlivoPost = new TransportPlivoPost(); // TransportPlivoPost | The new TransportPlivo resource
    try {
      TransportPlivoGet result = apiInstance.apiTransportPlivoPost(transportPlivoPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPlivoApi#apiTransportPlivoPost");
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
| **transportPlivoPost** | [**TransportPlivoPost**](TransportPlivoPost.md)| The new TransportPlivo resource | |

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportPlivo resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

