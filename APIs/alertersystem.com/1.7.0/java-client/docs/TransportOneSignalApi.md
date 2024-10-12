# TransportOneSignalApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportOneSignalGetCollection**](TransportOneSignalApi.md#apiTransportOneSignalGetCollection) | **GET** /api/transport-one-signal | Retrieves the collection of TransportOneSignal resources. |
| [**apiTransportOneSignalIdDelete**](TransportOneSignalApi.md#apiTransportOneSignalIdDelete) | **DELETE** /api/transport-one-signal/{id} | Removes the TransportOneSignal resource. |
| [**apiTransportOneSignalIdGet**](TransportOneSignalApi.md#apiTransportOneSignalIdGet) | **GET** /api/transport-one-signal/{id} | Retrieves a TransportOneSignal resource. |
| [**apiTransportOneSignalIdPatch**](TransportOneSignalApi.md#apiTransportOneSignalIdPatch) | **PATCH** /api/transport-one-signal/{id} | Updates the TransportOneSignal resource. |
| [**apiTransportOneSignalIdPut**](TransportOneSignalApi.md#apiTransportOneSignalIdPut) | **PUT** /api/transport-one-signal/{id} | Replaces the TransportOneSignal resource. |
| [**apiTransportOneSignalPost**](TransportOneSignalApi.md#apiTransportOneSignalPost) | **POST** /api/transport-one-signal | Creates a TransportOneSignal resource. |


<a id="apiTransportOneSignalGetCollection"></a>
# **apiTransportOneSignalGetCollection**
> List&lt;TransportOneSignalGet&gt; apiTransportOneSignalGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportOneSignal resources.

Retrieves the collection of TransportOneSignal resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOneSignalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOneSignalApi apiInstance = new TransportOneSignalApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportOneSignalGet> result = apiInstance.apiTransportOneSignalGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOneSignalApi#apiTransportOneSignalGetCollection");
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

[**List&lt;TransportOneSignalGet&gt;**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOneSignal collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOneSignalIdDelete"></a>
# **apiTransportOneSignalIdDelete**
> apiTransportOneSignalIdDelete(id)

Removes the TransportOneSignal resource.

Removes the TransportOneSignal resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOneSignalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOneSignalApi apiInstance = new TransportOneSignalApi(defaultClient);
    String id = "id_example"; // String | TransportOneSignal identifier
    try {
      apiInstance.apiTransportOneSignalIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOneSignalApi#apiTransportOneSignalIdDelete");
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
| **id** | **String**| TransportOneSignal identifier | |

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
| **204** | TransportOneSignal resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOneSignalIdGet"></a>
# **apiTransportOneSignalIdGet**
> TransportOneSignalGet apiTransportOneSignalIdGet(id)

Retrieves a TransportOneSignal resource.

Retrieves a TransportOneSignal resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOneSignalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOneSignalApi apiInstance = new TransportOneSignalApi(defaultClient);
    String id = "id_example"; // String | TransportOneSignal identifier
    try {
      TransportOneSignalGet result = apiInstance.apiTransportOneSignalIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOneSignalApi#apiTransportOneSignalIdGet");
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
| **id** | **String**| TransportOneSignal identifier | |

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOneSignal resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOneSignalIdPatch"></a>
# **apiTransportOneSignalIdPatch**
> TransportOneSignalGet apiTransportOneSignalIdPatch(id, transportOneSignalPatch)

Updates the TransportOneSignal resource.

Updates the TransportOneSignal resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOneSignalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOneSignalApi apiInstance = new TransportOneSignalApi(defaultClient);
    String id = "id_example"; // String | TransportOneSignal identifier
    TransportOneSignalPatch transportOneSignalPatch = new TransportOneSignalPatch(); // TransportOneSignalPatch | The updated TransportOneSignal resource
    try {
      TransportOneSignalGet result = apiInstance.apiTransportOneSignalIdPatch(id, transportOneSignalPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOneSignalApi#apiTransportOneSignalIdPatch");
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
| **id** | **String**| TransportOneSignal identifier | |
| **transportOneSignalPatch** | [**TransportOneSignalPatch**](TransportOneSignalPatch.md)| The updated TransportOneSignal resource | |

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOneSignal resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOneSignalIdPut"></a>
# **apiTransportOneSignalIdPut**
> TransportOneSignalGet apiTransportOneSignalIdPut(id, transportOneSignalPut)

Replaces the TransportOneSignal resource.

Replaces the TransportOneSignal resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOneSignalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOneSignalApi apiInstance = new TransportOneSignalApi(defaultClient);
    String id = "id_example"; // String | TransportOneSignal identifier
    TransportOneSignalPut transportOneSignalPut = new TransportOneSignalPut(); // TransportOneSignalPut | The updated TransportOneSignal resource
    try {
      TransportOneSignalGet result = apiInstance.apiTransportOneSignalIdPut(id, transportOneSignalPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOneSignalApi#apiTransportOneSignalIdPut");
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
| **id** | **String**| TransportOneSignal identifier | |
| **transportOneSignalPut** | [**TransportOneSignalPut**](TransportOneSignalPut.md)| The updated TransportOneSignal resource | |

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOneSignal resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOneSignalPost"></a>
# **apiTransportOneSignalPost**
> TransportOneSignalGet apiTransportOneSignalPost(transportOneSignalPost)

Creates a TransportOneSignal resource.

Creates a TransportOneSignal resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOneSignalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOneSignalApi apiInstance = new TransportOneSignalApi(defaultClient);
    TransportOneSignalPost transportOneSignalPost = new TransportOneSignalPost(); // TransportOneSignalPost | The new TransportOneSignal resource
    try {
      TransportOneSignalGet result = apiInstance.apiTransportOneSignalPost(transportOneSignalPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOneSignalApi#apiTransportOneSignalPost");
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
| **transportOneSignalPost** | [**TransportOneSignalPost**](TransportOneSignalPost.md)| The new TransportOneSignal resource | |

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportOneSignal resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

