# TransportSimpleTextinApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSimpleTextinGetCollection**](TransportSimpleTextinApi.md#apiTransportSimpleTextinGetCollection) | **GET** /api/transport-simple-textin | Retrieves the collection of TransportSimpleTextin resources. |
| [**apiTransportSimpleTextinIdDelete**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdDelete) | **DELETE** /api/transport-simple-textin/{id} | Removes the TransportSimpleTextin resource. |
| [**apiTransportSimpleTextinIdGet**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdGet) | **GET** /api/transport-simple-textin/{id} | Retrieves a TransportSimpleTextin resource. |
| [**apiTransportSimpleTextinIdPatch**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdPatch) | **PATCH** /api/transport-simple-textin/{id} | Updates the TransportSimpleTextin resource. |
| [**apiTransportSimpleTextinIdPut**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdPut) | **PUT** /api/transport-simple-textin/{id} | Replaces the TransportSimpleTextin resource. |
| [**apiTransportSimpleTextinPost**](TransportSimpleTextinApi.md#apiTransportSimpleTextinPost) | **POST** /api/transport-simple-textin | Creates a TransportSimpleTextin resource. |


<a id="apiTransportSimpleTextinGetCollection"></a>
# **apiTransportSimpleTextinGetCollection**
> List&lt;TransportSimpleTextinGet&gt; apiTransportSimpleTextinGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSimpleTextin resources.

Retrieves the collection of TransportSimpleTextin resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSimpleTextinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSimpleTextinApi apiInstance = new TransportSimpleTextinApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSimpleTextinGet> result = apiInstance.apiTransportSimpleTextinGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSimpleTextinApi#apiTransportSimpleTextinGetCollection");
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

[**List&lt;TransportSimpleTextinGet&gt;**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSimpleTextin collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSimpleTextinIdDelete"></a>
# **apiTransportSimpleTextinIdDelete**
> apiTransportSimpleTextinIdDelete(id)

Removes the TransportSimpleTextin resource.

Removes the TransportSimpleTextin resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSimpleTextinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSimpleTextinApi apiInstance = new TransportSimpleTextinApi(defaultClient);
    String id = "id_example"; // String | TransportSimpleTextin identifier
    try {
      apiInstance.apiTransportSimpleTextinIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSimpleTextinApi#apiTransportSimpleTextinIdDelete");
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
| **id** | **String**| TransportSimpleTextin identifier | |

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
| **204** | TransportSimpleTextin resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSimpleTextinIdGet"></a>
# **apiTransportSimpleTextinIdGet**
> TransportSimpleTextinGet apiTransportSimpleTextinIdGet(id)

Retrieves a TransportSimpleTextin resource.

Retrieves a TransportSimpleTextin resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSimpleTextinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSimpleTextinApi apiInstance = new TransportSimpleTextinApi(defaultClient);
    String id = "id_example"; // String | TransportSimpleTextin identifier
    try {
      TransportSimpleTextinGet result = apiInstance.apiTransportSimpleTextinIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSimpleTextinApi#apiTransportSimpleTextinIdGet");
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
| **id** | **String**| TransportSimpleTextin identifier | |

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSimpleTextin resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSimpleTextinIdPatch"></a>
# **apiTransportSimpleTextinIdPatch**
> TransportSimpleTextinGet apiTransportSimpleTextinIdPatch(id, transportSimpleTextinPatch)

Updates the TransportSimpleTextin resource.

Updates the TransportSimpleTextin resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSimpleTextinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSimpleTextinApi apiInstance = new TransportSimpleTextinApi(defaultClient);
    String id = "id_example"; // String | TransportSimpleTextin identifier
    TransportSimpleTextinPatch transportSimpleTextinPatch = new TransportSimpleTextinPatch(); // TransportSimpleTextinPatch | The updated TransportSimpleTextin resource
    try {
      TransportSimpleTextinGet result = apiInstance.apiTransportSimpleTextinIdPatch(id, transportSimpleTextinPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSimpleTextinApi#apiTransportSimpleTextinIdPatch");
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
| **id** | **String**| TransportSimpleTextin identifier | |
| **transportSimpleTextinPatch** | [**TransportSimpleTextinPatch**](TransportSimpleTextinPatch.md)| The updated TransportSimpleTextin resource | |

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSimpleTextin resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSimpleTextinIdPut"></a>
# **apiTransportSimpleTextinIdPut**
> TransportSimpleTextinGet apiTransportSimpleTextinIdPut(id, transportSimpleTextinPut)

Replaces the TransportSimpleTextin resource.

Replaces the TransportSimpleTextin resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSimpleTextinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSimpleTextinApi apiInstance = new TransportSimpleTextinApi(defaultClient);
    String id = "id_example"; // String | TransportSimpleTextin identifier
    TransportSimpleTextinPut transportSimpleTextinPut = new TransportSimpleTextinPut(); // TransportSimpleTextinPut | The updated TransportSimpleTextin resource
    try {
      TransportSimpleTextinGet result = apiInstance.apiTransportSimpleTextinIdPut(id, transportSimpleTextinPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSimpleTextinApi#apiTransportSimpleTextinIdPut");
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
| **id** | **String**| TransportSimpleTextin identifier | |
| **transportSimpleTextinPut** | [**TransportSimpleTextinPut**](TransportSimpleTextinPut.md)| The updated TransportSimpleTextin resource | |

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSimpleTextin resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSimpleTextinPost"></a>
# **apiTransportSimpleTextinPost**
> TransportSimpleTextinGet apiTransportSimpleTextinPost(transportSimpleTextinPost)

Creates a TransportSimpleTextin resource.

Creates a TransportSimpleTextin resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSimpleTextinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSimpleTextinApi apiInstance = new TransportSimpleTextinApi(defaultClient);
    TransportSimpleTextinPost transportSimpleTextinPost = new TransportSimpleTextinPost(); // TransportSimpleTextinPost | The new TransportSimpleTextin resource
    try {
      TransportSimpleTextinGet result = apiInstance.apiTransportSimpleTextinPost(transportSimpleTextinPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSimpleTextinApi#apiTransportSimpleTextinPost");
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
| **transportSimpleTextinPost** | [**TransportSimpleTextinPost**](TransportSimpleTextinPost.md)| The new TransportSimpleTextin resource | |

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSimpleTextin resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

