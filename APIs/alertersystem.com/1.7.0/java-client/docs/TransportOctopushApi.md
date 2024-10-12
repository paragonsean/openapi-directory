# TransportOctopushApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportOctopushGetCollection**](TransportOctopushApi.md#apiTransportOctopushGetCollection) | **GET** /api/transport-octopush | Retrieves the collection of TransportOctopush resources. |
| [**apiTransportOctopushIdDelete**](TransportOctopushApi.md#apiTransportOctopushIdDelete) | **DELETE** /api/transport-octopush/{id} | Removes the TransportOctopush resource. |
| [**apiTransportOctopushIdGet**](TransportOctopushApi.md#apiTransportOctopushIdGet) | **GET** /api/transport-octopush/{id} | Retrieves a TransportOctopush resource. |
| [**apiTransportOctopushIdPatch**](TransportOctopushApi.md#apiTransportOctopushIdPatch) | **PATCH** /api/transport-octopush/{id} | Updates the TransportOctopush resource. |
| [**apiTransportOctopushIdPut**](TransportOctopushApi.md#apiTransportOctopushIdPut) | **PUT** /api/transport-octopush/{id} | Replaces the TransportOctopush resource. |
| [**apiTransportOctopushPost**](TransportOctopushApi.md#apiTransportOctopushPost) | **POST** /api/transport-octopush | Creates a TransportOctopush resource. |


<a id="apiTransportOctopushGetCollection"></a>
# **apiTransportOctopushGetCollection**
> List&lt;TransportOctopushGet&gt; apiTransportOctopushGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportOctopush resources.

Retrieves the collection of TransportOctopush resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOctopushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOctopushApi apiInstance = new TransportOctopushApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportOctopushGet> result = apiInstance.apiTransportOctopushGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOctopushApi#apiTransportOctopushGetCollection");
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

[**List&lt;TransportOctopushGet&gt;**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOctopush collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOctopushIdDelete"></a>
# **apiTransportOctopushIdDelete**
> apiTransportOctopushIdDelete(id)

Removes the TransportOctopush resource.

Removes the TransportOctopush resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOctopushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOctopushApi apiInstance = new TransportOctopushApi(defaultClient);
    String id = "id_example"; // String | TransportOctopush identifier
    try {
      apiInstance.apiTransportOctopushIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOctopushApi#apiTransportOctopushIdDelete");
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
| **id** | **String**| TransportOctopush identifier | |

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
| **204** | TransportOctopush resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOctopushIdGet"></a>
# **apiTransportOctopushIdGet**
> TransportOctopushGet apiTransportOctopushIdGet(id)

Retrieves a TransportOctopush resource.

Retrieves a TransportOctopush resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOctopushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOctopushApi apiInstance = new TransportOctopushApi(defaultClient);
    String id = "id_example"; // String | TransportOctopush identifier
    try {
      TransportOctopushGet result = apiInstance.apiTransportOctopushIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOctopushApi#apiTransportOctopushIdGet");
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
| **id** | **String**| TransportOctopush identifier | |

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOctopush resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOctopushIdPatch"></a>
# **apiTransportOctopushIdPatch**
> TransportOctopushGet apiTransportOctopushIdPatch(id, transportOctopushPatch)

Updates the TransportOctopush resource.

Updates the TransportOctopush resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOctopushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOctopushApi apiInstance = new TransportOctopushApi(defaultClient);
    String id = "id_example"; // String | TransportOctopush identifier
    TransportOctopushPatch transportOctopushPatch = new TransportOctopushPatch(); // TransportOctopushPatch | The updated TransportOctopush resource
    try {
      TransportOctopushGet result = apiInstance.apiTransportOctopushIdPatch(id, transportOctopushPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOctopushApi#apiTransportOctopushIdPatch");
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
| **id** | **String**| TransportOctopush identifier | |
| **transportOctopushPatch** | [**TransportOctopushPatch**](TransportOctopushPatch.md)| The updated TransportOctopush resource | |

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOctopush resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOctopushIdPut"></a>
# **apiTransportOctopushIdPut**
> TransportOctopushGet apiTransportOctopushIdPut(id, transportOctopushPut)

Replaces the TransportOctopush resource.

Replaces the TransportOctopush resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOctopushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOctopushApi apiInstance = new TransportOctopushApi(defaultClient);
    String id = "id_example"; // String | TransportOctopush identifier
    TransportOctopushPut transportOctopushPut = new TransportOctopushPut(); // TransportOctopushPut | The updated TransportOctopush resource
    try {
      TransportOctopushGet result = apiInstance.apiTransportOctopushIdPut(id, transportOctopushPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOctopushApi#apiTransportOctopushIdPut");
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
| **id** | **String**| TransportOctopush identifier | |
| **transportOctopushPut** | [**TransportOctopushPut**](TransportOctopushPut.md)| The updated TransportOctopush resource | |

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOctopush resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOctopushPost"></a>
# **apiTransportOctopushPost**
> TransportOctopushGet apiTransportOctopushPost(transportOctopushPost)

Creates a TransportOctopush resource.

Creates a TransportOctopush resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOctopushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOctopushApi apiInstance = new TransportOctopushApi(defaultClient);
    TransportOctopushPost transportOctopushPost = new TransportOctopushPost(); // TransportOctopushPost | The new TransportOctopush resource
    try {
      TransportOctopushGet result = apiInstance.apiTransportOctopushPost(transportOctopushPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOctopushApi#apiTransportOctopushPost");
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
| **transportOctopushPost** | [**TransportOctopushPost**](TransportOctopushPost.md)| The new TransportOctopush resource | |

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportOctopush resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

