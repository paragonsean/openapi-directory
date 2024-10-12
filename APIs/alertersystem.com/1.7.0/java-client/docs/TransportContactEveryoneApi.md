# TransportContactEveryoneApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportContactEveryoneGetCollection**](TransportContactEveryoneApi.md#apiTransportContactEveryoneGetCollection) | **GET** /api/transport-contact-everyone | Retrieves the collection of TransportContactEveryone resources. |
| [**apiTransportContactEveryoneIdDelete**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdDelete) | **DELETE** /api/transport-contact-everyone/{id} | Removes the TransportContactEveryone resource. |
| [**apiTransportContactEveryoneIdGet**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdGet) | **GET** /api/transport-contact-everyone/{id} | Retrieves a TransportContactEveryone resource. |
| [**apiTransportContactEveryoneIdPatch**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdPatch) | **PATCH** /api/transport-contact-everyone/{id} | Updates the TransportContactEveryone resource. |
| [**apiTransportContactEveryoneIdPut**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdPut) | **PUT** /api/transport-contact-everyone/{id} | Replaces the TransportContactEveryone resource. |
| [**apiTransportContactEveryonePost**](TransportContactEveryoneApi.md#apiTransportContactEveryonePost) | **POST** /api/transport-contact-everyone | Creates a TransportContactEveryone resource. |


<a id="apiTransportContactEveryoneGetCollection"></a>
# **apiTransportContactEveryoneGetCollection**
> List&lt;TransportContactEveryoneGet&gt; apiTransportContactEveryoneGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportContactEveryone resources.

Retrieves the collection of TransportContactEveryone resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportContactEveryoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportContactEveryoneApi apiInstance = new TransportContactEveryoneApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportContactEveryoneGet> result = apiInstance.apiTransportContactEveryoneGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportContactEveryoneApi#apiTransportContactEveryoneGetCollection");
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

[**List&lt;TransportContactEveryoneGet&gt;**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportContactEveryone collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportContactEveryoneIdDelete"></a>
# **apiTransportContactEveryoneIdDelete**
> apiTransportContactEveryoneIdDelete(id)

Removes the TransportContactEveryone resource.

Removes the TransportContactEveryone resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportContactEveryoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportContactEveryoneApi apiInstance = new TransportContactEveryoneApi(defaultClient);
    String id = "id_example"; // String | TransportContactEveryone identifier
    try {
      apiInstance.apiTransportContactEveryoneIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportContactEveryoneApi#apiTransportContactEveryoneIdDelete");
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
| **id** | **String**| TransportContactEveryone identifier | |

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
| **204** | TransportContactEveryone resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportContactEveryoneIdGet"></a>
# **apiTransportContactEveryoneIdGet**
> TransportContactEveryoneGet apiTransportContactEveryoneIdGet(id)

Retrieves a TransportContactEveryone resource.

Retrieves a TransportContactEveryone resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportContactEveryoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportContactEveryoneApi apiInstance = new TransportContactEveryoneApi(defaultClient);
    String id = "id_example"; // String | TransportContactEveryone identifier
    try {
      TransportContactEveryoneGet result = apiInstance.apiTransportContactEveryoneIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportContactEveryoneApi#apiTransportContactEveryoneIdGet");
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
| **id** | **String**| TransportContactEveryone identifier | |

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportContactEveryone resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportContactEveryoneIdPatch"></a>
# **apiTransportContactEveryoneIdPatch**
> TransportContactEveryoneGet apiTransportContactEveryoneIdPatch(id, transportContactEveryonePatch)

Updates the TransportContactEveryone resource.

Updates the TransportContactEveryone resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportContactEveryoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportContactEveryoneApi apiInstance = new TransportContactEveryoneApi(defaultClient);
    String id = "id_example"; // String | TransportContactEveryone identifier
    TransportContactEveryonePatch transportContactEveryonePatch = new TransportContactEveryonePatch(); // TransportContactEveryonePatch | The updated TransportContactEveryone resource
    try {
      TransportContactEveryoneGet result = apiInstance.apiTransportContactEveryoneIdPatch(id, transportContactEveryonePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportContactEveryoneApi#apiTransportContactEveryoneIdPatch");
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
| **id** | **String**| TransportContactEveryone identifier | |
| **transportContactEveryonePatch** | [**TransportContactEveryonePatch**](TransportContactEveryonePatch.md)| The updated TransportContactEveryone resource | |

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportContactEveryone resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportContactEveryoneIdPut"></a>
# **apiTransportContactEveryoneIdPut**
> TransportContactEveryoneGet apiTransportContactEveryoneIdPut(id, transportContactEveryonePut)

Replaces the TransportContactEveryone resource.

Replaces the TransportContactEveryone resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportContactEveryoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportContactEveryoneApi apiInstance = new TransportContactEveryoneApi(defaultClient);
    String id = "id_example"; // String | TransportContactEveryone identifier
    TransportContactEveryonePut transportContactEveryonePut = new TransportContactEveryonePut(); // TransportContactEveryonePut | The updated TransportContactEveryone resource
    try {
      TransportContactEveryoneGet result = apiInstance.apiTransportContactEveryoneIdPut(id, transportContactEveryonePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportContactEveryoneApi#apiTransportContactEveryoneIdPut");
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
| **id** | **String**| TransportContactEveryone identifier | |
| **transportContactEveryonePut** | [**TransportContactEveryonePut**](TransportContactEveryonePut.md)| The updated TransportContactEveryone resource | |

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportContactEveryone resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportContactEveryonePost"></a>
# **apiTransportContactEveryonePost**
> TransportContactEveryoneGet apiTransportContactEveryonePost(transportContactEveryonePost)

Creates a TransportContactEveryone resource.

Creates a TransportContactEveryone resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportContactEveryoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportContactEveryoneApi apiInstance = new TransportContactEveryoneApi(defaultClient);
    TransportContactEveryonePost transportContactEveryonePost = new TransportContactEveryonePost(); // TransportContactEveryonePost | The new TransportContactEveryone resource
    try {
      TransportContactEveryoneGet result = apiInstance.apiTransportContactEveryonePost(transportContactEveryonePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportContactEveryoneApi#apiTransportContactEveryonePost");
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
| **transportContactEveryonePost** | [**TransportContactEveryonePost**](TransportContactEveryonePost.md)| The new TransportContactEveryone resource | |

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportContactEveryone resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

