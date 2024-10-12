# TransportExpoApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportExpoGetCollection**](TransportExpoApi.md#apiTransportExpoGetCollection) | **GET** /api/transport-expo | Retrieves the collection of TransportExpo resources. |
| [**apiTransportExpoIdDelete**](TransportExpoApi.md#apiTransportExpoIdDelete) | **DELETE** /api/transport-expo/{id} | Removes the TransportExpo resource. |
| [**apiTransportExpoIdGet**](TransportExpoApi.md#apiTransportExpoIdGet) | **GET** /api/transport-expo/{id} | Retrieves a TransportExpo resource. |
| [**apiTransportExpoIdPatch**](TransportExpoApi.md#apiTransportExpoIdPatch) | **PATCH** /api/transport-expo/{id} | Updates the TransportExpo resource. |
| [**apiTransportExpoIdPut**](TransportExpoApi.md#apiTransportExpoIdPut) | **PUT** /api/transport-expo/{id} | Replaces the TransportExpo resource. |
| [**apiTransportExpoPost**](TransportExpoApi.md#apiTransportExpoPost) | **POST** /api/transport-expo | Creates a TransportExpo resource. |


<a id="apiTransportExpoGetCollection"></a>
# **apiTransportExpoGetCollection**
> List&lt;TransportExpoGet&gt; apiTransportExpoGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportExpo resources.

Retrieves the collection of TransportExpo resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportExpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportExpoApi apiInstance = new TransportExpoApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportExpoGet> result = apiInstance.apiTransportExpoGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportExpoApi#apiTransportExpoGetCollection");
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

[**List&lt;TransportExpoGet&gt;**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportExpo collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportExpoIdDelete"></a>
# **apiTransportExpoIdDelete**
> apiTransportExpoIdDelete(id)

Removes the TransportExpo resource.

Removes the TransportExpo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportExpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportExpoApi apiInstance = new TransportExpoApi(defaultClient);
    String id = "id_example"; // String | TransportExpo identifier
    try {
      apiInstance.apiTransportExpoIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportExpoApi#apiTransportExpoIdDelete");
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
| **id** | **String**| TransportExpo identifier | |

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
| **204** | TransportExpo resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportExpoIdGet"></a>
# **apiTransportExpoIdGet**
> TransportExpoGet apiTransportExpoIdGet(id)

Retrieves a TransportExpo resource.

Retrieves a TransportExpo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportExpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportExpoApi apiInstance = new TransportExpoApi(defaultClient);
    String id = "id_example"; // String | TransportExpo identifier
    try {
      TransportExpoGet result = apiInstance.apiTransportExpoIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportExpoApi#apiTransportExpoIdGet");
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
| **id** | **String**| TransportExpo identifier | |

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportExpo resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportExpoIdPatch"></a>
# **apiTransportExpoIdPatch**
> TransportExpoGet apiTransportExpoIdPatch(id, transportExpoPatch)

Updates the TransportExpo resource.

Updates the TransportExpo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportExpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportExpoApi apiInstance = new TransportExpoApi(defaultClient);
    String id = "id_example"; // String | TransportExpo identifier
    TransportExpoPatch transportExpoPatch = new TransportExpoPatch(); // TransportExpoPatch | The updated TransportExpo resource
    try {
      TransportExpoGet result = apiInstance.apiTransportExpoIdPatch(id, transportExpoPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportExpoApi#apiTransportExpoIdPatch");
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
| **id** | **String**| TransportExpo identifier | |
| **transportExpoPatch** | [**TransportExpoPatch**](TransportExpoPatch.md)| The updated TransportExpo resource | |

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportExpo resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportExpoIdPut"></a>
# **apiTransportExpoIdPut**
> TransportExpoGet apiTransportExpoIdPut(id, transportExpoPut)

Replaces the TransportExpo resource.

Replaces the TransportExpo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportExpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportExpoApi apiInstance = new TransportExpoApi(defaultClient);
    String id = "id_example"; // String | TransportExpo identifier
    TransportExpoPut transportExpoPut = new TransportExpoPut(); // TransportExpoPut | The updated TransportExpo resource
    try {
      TransportExpoGet result = apiInstance.apiTransportExpoIdPut(id, transportExpoPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportExpoApi#apiTransportExpoIdPut");
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
| **id** | **String**| TransportExpo identifier | |
| **transportExpoPut** | [**TransportExpoPut**](TransportExpoPut.md)| The updated TransportExpo resource | |

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportExpo resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportExpoPost"></a>
# **apiTransportExpoPost**
> TransportExpoGet apiTransportExpoPost(transportExpoPost)

Creates a TransportExpo resource.

Creates a TransportExpo resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportExpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportExpoApi apiInstance = new TransportExpoApi(defaultClient);
    TransportExpoPost transportExpoPost = new TransportExpoPost(); // TransportExpoPost | The new TransportExpo resource
    try {
      TransportExpoGet result = apiInstance.apiTransportExpoPost(transportExpoPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportExpoApi#apiTransportExpoPost");
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
| **transportExpoPost** | [**TransportExpoPost**](TransportExpoPost.md)| The new TransportExpo resource | |

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportExpo resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

