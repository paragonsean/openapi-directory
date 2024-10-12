# TransportPushoverApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportPushoverGetCollection**](TransportPushoverApi.md#apiTransportPushoverGetCollection) | **GET** /api/transport-pushover | Retrieves the collection of TransportPushover resources. |
| [**apiTransportPushoverIdDelete**](TransportPushoverApi.md#apiTransportPushoverIdDelete) | **DELETE** /api/transport-pushover/{id} | Removes the TransportPushover resource. |
| [**apiTransportPushoverIdGet**](TransportPushoverApi.md#apiTransportPushoverIdGet) | **GET** /api/transport-pushover/{id} | Retrieves a TransportPushover resource. |
| [**apiTransportPushoverIdPatch**](TransportPushoverApi.md#apiTransportPushoverIdPatch) | **PATCH** /api/transport-pushover/{id} | Updates the TransportPushover resource. |
| [**apiTransportPushoverIdPut**](TransportPushoverApi.md#apiTransportPushoverIdPut) | **PUT** /api/transport-pushover/{id} | Replaces the TransportPushover resource. |
| [**apiTransportPushoverPost**](TransportPushoverApi.md#apiTransportPushoverPost) | **POST** /api/transport-pushover | Creates a TransportPushover resource. |


<a id="apiTransportPushoverGetCollection"></a>
# **apiTransportPushoverGetCollection**
> List&lt;TransportPushoverGet&gt; apiTransportPushoverGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportPushover resources.

Retrieves the collection of TransportPushover resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushoverApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushoverApi apiInstance = new TransportPushoverApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportPushoverGet> result = apiInstance.apiTransportPushoverGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushoverApi#apiTransportPushoverGetCollection");
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

[**List&lt;TransportPushoverGet&gt;**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushover collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushoverIdDelete"></a>
# **apiTransportPushoverIdDelete**
> apiTransportPushoverIdDelete(id)

Removes the TransportPushover resource.

Removes the TransportPushover resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushoverApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushoverApi apiInstance = new TransportPushoverApi(defaultClient);
    String id = "id_example"; // String | TransportPushover identifier
    try {
      apiInstance.apiTransportPushoverIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushoverApi#apiTransportPushoverIdDelete");
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
| **id** | **String**| TransportPushover identifier | |

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
| **204** | TransportPushover resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushoverIdGet"></a>
# **apiTransportPushoverIdGet**
> TransportPushoverGet apiTransportPushoverIdGet(id)

Retrieves a TransportPushover resource.

Retrieves a TransportPushover resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushoverApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushoverApi apiInstance = new TransportPushoverApi(defaultClient);
    String id = "id_example"; // String | TransportPushover identifier
    try {
      TransportPushoverGet result = apiInstance.apiTransportPushoverIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushoverApi#apiTransportPushoverIdGet");
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
| **id** | **String**| TransportPushover identifier | |

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushover resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushoverIdPatch"></a>
# **apiTransportPushoverIdPatch**
> TransportPushoverGet apiTransportPushoverIdPatch(id, transportPushoverPatch)

Updates the TransportPushover resource.

Updates the TransportPushover resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushoverApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushoverApi apiInstance = new TransportPushoverApi(defaultClient);
    String id = "id_example"; // String | TransportPushover identifier
    TransportPushoverPatch transportPushoverPatch = new TransportPushoverPatch(); // TransportPushoverPatch | The updated TransportPushover resource
    try {
      TransportPushoverGet result = apiInstance.apiTransportPushoverIdPatch(id, transportPushoverPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushoverApi#apiTransportPushoverIdPatch");
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
| **id** | **String**| TransportPushover identifier | |
| **transportPushoverPatch** | [**TransportPushoverPatch**](TransportPushoverPatch.md)| The updated TransportPushover resource | |

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushover resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushoverIdPut"></a>
# **apiTransportPushoverIdPut**
> TransportPushoverGet apiTransportPushoverIdPut(id, transportPushoverPut)

Replaces the TransportPushover resource.

Replaces the TransportPushover resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushoverApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushoverApi apiInstance = new TransportPushoverApi(defaultClient);
    String id = "id_example"; // String | TransportPushover identifier
    TransportPushoverPut transportPushoverPut = new TransportPushoverPut(); // TransportPushoverPut | The updated TransportPushover resource
    try {
      TransportPushoverGet result = apiInstance.apiTransportPushoverIdPut(id, transportPushoverPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushoverApi#apiTransportPushoverIdPut");
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
| **id** | **String**| TransportPushover identifier | |
| **transportPushoverPut** | [**TransportPushoverPut**](TransportPushoverPut.md)| The updated TransportPushover resource | |

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportPushover resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportPushoverPost"></a>
# **apiTransportPushoverPost**
> TransportPushoverGet apiTransportPushoverPost(transportPushoverPost)

Creates a TransportPushover resource.

Creates a TransportPushover resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportPushoverApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportPushoverApi apiInstance = new TransportPushoverApi(defaultClient);
    TransportPushoverPost transportPushoverPost = new TransportPushoverPost(); // TransportPushoverPost | The new TransportPushover resource
    try {
      TransportPushoverGet result = apiInstance.apiTransportPushoverPost(transportPushoverPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportPushoverApi#apiTransportPushoverPost");
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
| **transportPushoverPost** | [**TransportPushoverPost**](TransportPushoverPost.md)| The new TransportPushover resource | |

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportPushover resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

