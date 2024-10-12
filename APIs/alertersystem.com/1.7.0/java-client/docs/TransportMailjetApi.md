# TransportMailjetApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMailjetGetCollection**](TransportMailjetApi.md#apiTransportMailjetGetCollection) | **GET** /api/transport-mailjet | Retrieves the collection of TransportMailjet resources. |
| [**apiTransportMailjetIdDelete**](TransportMailjetApi.md#apiTransportMailjetIdDelete) | **DELETE** /api/transport-mailjet/{id} | Removes the TransportMailjet resource. |
| [**apiTransportMailjetIdGet**](TransportMailjetApi.md#apiTransportMailjetIdGet) | **GET** /api/transport-mailjet/{id} | Retrieves a TransportMailjet resource. |
| [**apiTransportMailjetIdPatch**](TransportMailjetApi.md#apiTransportMailjetIdPatch) | **PATCH** /api/transport-mailjet/{id} | Updates the TransportMailjet resource. |
| [**apiTransportMailjetIdPut**](TransportMailjetApi.md#apiTransportMailjetIdPut) | **PUT** /api/transport-mailjet/{id} | Replaces the TransportMailjet resource. |
| [**apiTransportMailjetPost**](TransportMailjetApi.md#apiTransportMailjetPost) | **POST** /api/transport-mailjet | Creates a TransportMailjet resource. |


<a id="apiTransportMailjetGetCollection"></a>
# **apiTransportMailjetGetCollection**
> List&lt;TransportMailjetGet&gt; apiTransportMailjetGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMailjet resources.

Retrieves the collection of TransportMailjet resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMailjetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMailjetApi apiInstance = new TransportMailjetApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMailjetGet> result = apiInstance.apiTransportMailjetGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMailjetApi#apiTransportMailjetGetCollection");
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

[**List&lt;TransportMailjetGet&gt;**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMailjet collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMailjetIdDelete"></a>
# **apiTransportMailjetIdDelete**
> apiTransportMailjetIdDelete(id)

Removes the TransportMailjet resource.

Removes the TransportMailjet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMailjetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMailjetApi apiInstance = new TransportMailjetApi(defaultClient);
    String id = "id_example"; // String | TransportMailjet identifier
    try {
      apiInstance.apiTransportMailjetIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMailjetApi#apiTransportMailjetIdDelete");
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
| **id** | **String**| TransportMailjet identifier | |

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
| **204** | TransportMailjet resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMailjetIdGet"></a>
# **apiTransportMailjetIdGet**
> TransportMailjetGet apiTransportMailjetIdGet(id)

Retrieves a TransportMailjet resource.

Retrieves a TransportMailjet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMailjetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMailjetApi apiInstance = new TransportMailjetApi(defaultClient);
    String id = "id_example"; // String | TransportMailjet identifier
    try {
      TransportMailjetGet result = apiInstance.apiTransportMailjetIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMailjetApi#apiTransportMailjetIdGet");
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
| **id** | **String**| TransportMailjet identifier | |

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMailjet resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMailjetIdPatch"></a>
# **apiTransportMailjetIdPatch**
> TransportMailjetGet apiTransportMailjetIdPatch(id, transportMailjetPatch)

Updates the TransportMailjet resource.

Updates the TransportMailjet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMailjetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMailjetApi apiInstance = new TransportMailjetApi(defaultClient);
    String id = "id_example"; // String | TransportMailjet identifier
    TransportMailjetPatch transportMailjetPatch = new TransportMailjetPatch(); // TransportMailjetPatch | The updated TransportMailjet resource
    try {
      TransportMailjetGet result = apiInstance.apiTransportMailjetIdPatch(id, transportMailjetPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMailjetApi#apiTransportMailjetIdPatch");
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
| **id** | **String**| TransportMailjet identifier | |
| **transportMailjetPatch** | [**TransportMailjetPatch**](TransportMailjetPatch.md)| The updated TransportMailjet resource | |

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMailjet resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMailjetIdPut"></a>
# **apiTransportMailjetIdPut**
> TransportMailjetGet apiTransportMailjetIdPut(id, transportMailjetPut)

Replaces the TransportMailjet resource.

Replaces the TransportMailjet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMailjetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMailjetApi apiInstance = new TransportMailjetApi(defaultClient);
    String id = "id_example"; // String | TransportMailjet identifier
    TransportMailjetPut transportMailjetPut = new TransportMailjetPut(); // TransportMailjetPut | The updated TransportMailjet resource
    try {
      TransportMailjetGet result = apiInstance.apiTransportMailjetIdPut(id, transportMailjetPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMailjetApi#apiTransportMailjetIdPut");
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
| **id** | **String**| TransportMailjet identifier | |
| **transportMailjetPut** | [**TransportMailjetPut**](TransportMailjetPut.md)| The updated TransportMailjet resource | |

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMailjet resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMailjetPost"></a>
# **apiTransportMailjetPost**
> TransportMailjetGet apiTransportMailjetPost(transportMailjetPost)

Creates a TransportMailjet resource.

Creates a TransportMailjet resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMailjetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMailjetApi apiInstance = new TransportMailjetApi(defaultClient);
    TransportMailjetPost transportMailjetPost = new TransportMailjetPost(); // TransportMailjetPost | The new TransportMailjet resource
    try {
      TransportMailjetGet result = apiInstance.apiTransportMailjetPost(transportMailjetPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMailjetApi#apiTransportMailjetPost");
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
| **transportMailjetPost** | [**TransportMailjetPost**](TransportMailjetPost.md)| The new TransportMailjet resource | |

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMailjet resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

