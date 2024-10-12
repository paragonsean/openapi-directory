# TransportSpotHitApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSpotHitGetCollection**](TransportSpotHitApi.md#apiTransportSpotHitGetCollection) | **GET** /api/transport-spot-hit | Retrieves the collection of TransportSpotHit resources. |
| [**apiTransportSpotHitIdDelete**](TransportSpotHitApi.md#apiTransportSpotHitIdDelete) | **DELETE** /api/transport-spot-hit/{id} | Removes the TransportSpotHit resource. |
| [**apiTransportSpotHitIdGet**](TransportSpotHitApi.md#apiTransportSpotHitIdGet) | **GET** /api/transport-spot-hit/{id} | Retrieves a TransportSpotHit resource. |
| [**apiTransportSpotHitIdPatch**](TransportSpotHitApi.md#apiTransportSpotHitIdPatch) | **PATCH** /api/transport-spot-hit/{id} | Updates the TransportSpotHit resource. |
| [**apiTransportSpotHitIdPut**](TransportSpotHitApi.md#apiTransportSpotHitIdPut) | **PUT** /api/transport-spot-hit/{id} | Replaces the TransportSpotHit resource. |
| [**apiTransportSpotHitPost**](TransportSpotHitApi.md#apiTransportSpotHitPost) | **POST** /api/transport-spot-hit | Creates a TransportSpotHit resource. |


<a id="apiTransportSpotHitGetCollection"></a>
# **apiTransportSpotHitGetCollection**
> List&lt;TransportSpotHitGet&gt; apiTransportSpotHitGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSpotHit resources.

Retrieves the collection of TransportSpotHit resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSpotHitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSpotHitApi apiInstance = new TransportSpotHitApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSpotHitGet> result = apiInstance.apiTransportSpotHitGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSpotHitApi#apiTransportSpotHitGetCollection");
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

[**List&lt;TransportSpotHitGet&gt;**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSpotHit collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSpotHitIdDelete"></a>
# **apiTransportSpotHitIdDelete**
> apiTransportSpotHitIdDelete(id)

Removes the TransportSpotHit resource.

Removes the TransportSpotHit resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSpotHitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSpotHitApi apiInstance = new TransportSpotHitApi(defaultClient);
    String id = "id_example"; // String | TransportSpotHit identifier
    try {
      apiInstance.apiTransportSpotHitIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSpotHitApi#apiTransportSpotHitIdDelete");
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
| **id** | **String**| TransportSpotHit identifier | |

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
| **204** | TransportSpotHit resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSpotHitIdGet"></a>
# **apiTransportSpotHitIdGet**
> TransportSpotHitGet apiTransportSpotHitIdGet(id)

Retrieves a TransportSpotHit resource.

Retrieves a TransportSpotHit resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSpotHitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSpotHitApi apiInstance = new TransportSpotHitApi(defaultClient);
    String id = "id_example"; // String | TransportSpotHit identifier
    try {
      TransportSpotHitGet result = apiInstance.apiTransportSpotHitIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSpotHitApi#apiTransportSpotHitIdGet");
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
| **id** | **String**| TransportSpotHit identifier | |

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSpotHit resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSpotHitIdPatch"></a>
# **apiTransportSpotHitIdPatch**
> TransportSpotHitGet apiTransportSpotHitIdPatch(id, transportSpotHitPatch)

Updates the TransportSpotHit resource.

Updates the TransportSpotHit resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSpotHitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSpotHitApi apiInstance = new TransportSpotHitApi(defaultClient);
    String id = "id_example"; // String | TransportSpotHit identifier
    TransportSpotHitPatch transportSpotHitPatch = new TransportSpotHitPatch(); // TransportSpotHitPatch | The updated TransportSpotHit resource
    try {
      TransportSpotHitGet result = apiInstance.apiTransportSpotHitIdPatch(id, transportSpotHitPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSpotHitApi#apiTransportSpotHitIdPatch");
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
| **id** | **String**| TransportSpotHit identifier | |
| **transportSpotHitPatch** | [**TransportSpotHitPatch**](TransportSpotHitPatch.md)| The updated TransportSpotHit resource | |

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSpotHit resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSpotHitIdPut"></a>
# **apiTransportSpotHitIdPut**
> TransportSpotHitGet apiTransportSpotHitIdPut(id, transportSpotHitPut)

Replaces the TransportSpotHit resource.

Replaces the TransportSpotHit resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSpotHitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSpotHitApi apiInstance = new TransportSpotHitApi(defaultClient);
    String id = "id_example"; // String | TransportSpotHit identifier
    TransportSpotHitPut transportSpotHitPut = new TransportSpotHitPut(); // TransportSpotHitPut | The updated TransportSpotHit resource
    try {
      TransportSpotHitGet result = apiInstance.apiTransportSpotHitIdPut(id, transportSpotHitPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSpotHitApi#apiTransportSpotHitIdPut");
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
| **id** | **String**| TransportSpotHit identifier | |
| **transportSpotHitPut** | [**TransportSpotHitPut**](TransportSpotHitPut.md)| The updated TransportSpotHit resource | |

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSpotHit resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSpotHitPost"></a>
# **apiTransportSpotHitPost**
> TransportSpotHitGet apiTransportSpotHitPost(transportSpotHitPost)

Creates a TransportSpotHit resource.

Creates a TransportSpotHit resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSpotHitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSpotHitApi apiInstance = new TransportSpotHitApi(defaultClient);
    TransportSpotHitPost transportSpotHitPost = new TransportSpotHitPost(); // TransportSpotHitPost | The new TransportSpotHit resource
    try {
      TransportSpotHitGet result = apiInstance.apiTransportSpotHitPost(transportSpotHitPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSpotHitApi#apiTransportSpotHitPost");
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
| **transportSpotHitPost** | [**TransportSpotHitPost**](TransportSpotHitPost.md)| The new TransportSpotHit resource | |

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSpotHit resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

