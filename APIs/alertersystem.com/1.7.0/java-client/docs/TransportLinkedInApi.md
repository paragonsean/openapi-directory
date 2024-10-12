# TransportLinkedInApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportLinkedInGetCollection**](TransportLinkedInApi.md#apiTransportLinkedInGetCollection) | **GET** /api/transport-linked-in | Retrieves the collection of TransportLinkedIn resources. |
| [**apiTransportLinkedInIdDelete**](TransportLinkedInApi.md#apiTransportLinkedInIdDelete) | **DELETE** /api/transport-linked-in/{id} | Removes the TransportLinkedIn resource. |
| [**apiTransportLinkedInIdGet**](TransportLinkedInApi.md#apiTransportLinkedInIdGet) | **GET** /api/transport-linked-in/{id} | Retrieves a TransportLinkedIn resource. |
| [**apiTransportLinkedInIdPatch**](TransportLinkedInApi.md#apiTransportLinkedInIdPatch) | **PATCH** /api/transport-linked-in/{id} | Updates the TransportLinkedIn resource. |
| [**apiTransportLinkedInIdPut**](TransportLinkedInApi.md#apiTransportLinkedInIdPut) | **PUT** /api/transport-linked-in/{id} | Replaces the TransportLinkedIn resource. |
| [**apiTransportLinkedInPost**](TransportLinkedInApi.md#apiTransportLinkedInPost) | **POST** /api/transport-linked-in | Creates a TransportLinkedIn resource. |


<a id="apiTransportLinkedInGetCollection"></a>
# **apiTransportLinkedInGetCollection**
> List&lt;TransportLinkedInGet&gt; apiTransportLinkedInGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportLinkedIn resources.

Retrieves the collection of TransportLinkedIn resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLinkedInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLinkedInApi apiInstance = new TransportLinkedInApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportLinkedInGet> result = apiInstance.apiTransportLinkedInGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLinkedInApi#apiTransportLinkedInGetCollection");
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

[**List&lt;TransportLinkedInGet&gt;**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLinkedIn collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLinkedInIdDelete"></a>
# **apiTransportLinkedInIdDelete**
> apiTransportLinkedInIdDelete(id)

Removes the TransportLinkedIn resource.

Removes the TransportLinkedIn resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLinkedInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLinkedInApi apiInstance = new TransportLinkedInApi(defaultClient);
    String id = "id_example"; // String | TransportLinkedIn identifier
    try {
      apiInstance.apiTransportLinkedInIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLinkedInApi#apiTransportLinkedInIdDelete");
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
| **id** | **String**| TransportLinkedIn identifier | |

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
| **204** | TransportLinkedIn resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLinkedInIdGet"></a>
# **apiTransportLinkedInIdGet**
> TransportLinkedInGet apiTransportLinkedInIdGet(id)

Retrieves a TransportLinkedIn resource.

Retrieves a TransportLinkedIn resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLinkedInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLinkedInApi apiInstance = new TransportLinkedInApi(defaultClient);
    String id = "id_example"; // String | TransportLinkedIn identifier
    try {
      TransportLinkedInGet result = apiInstance.apiTransportLinkedInIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLinkedInApi#apiTransportLinkedInIdGet");
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
| **id** | **String**| TransportLinkedIn identifier | |

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLinkedIn resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLinkedInIdPatch"></a>
# **apiTransportLinkedInIdPatch**
> TransportLinkedInGet apiTransportLinkedInIdPatch(id, transportLinkedInPatch)

Updates the TransportLinkedIn resource.

Updates the TransportLinkedIn resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLinkedInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLinkedInApi apiInstance = new TransportLinkedInApi(defaultClient);
    String id = "id_example"; // String | TransportLinkedIn identifier
    TransportLinkedInPatch transportLinkedInPatch = new TransportLinkedInPatch(); // TransportLinkedInPatch | The updated TransportLinkedIn resource
    try {
      TransportLinkedInGet result = apiInstance.apiTransportLinkedInIdPatch(id, transportLinkedInPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLinkedInApi#apiTransportLinkedInIdPatch");
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
| **id** | **String**| TransportLinkedIn identifier | |
| **transportLinkedInPatch** | [**TransportLinkedInPatch**](TransportLinkedInPatch.md)| The updated TransportLinkedIn resource | |

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLinkedIn resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLinkedInIdPut"></a>
# **apiTransportLinkedInIdPut**
> TransportLinkedInGet apiTransportLinkedInIdPut(id, transportLinkedInPut)

Replaces the TransportLinkedIn resource.

Replaces the TransportLinkedIn resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLinkedInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLinkedInApi apiInstance = new TransportLinkedInApi(defaultClient);
    String id = "id_example"; // String | TransportLinkedIn identifier
    TransportLinkedInPut transportLinkedInPut = new TransportLinkedInPut(); // TransportLinkedInPut | The updated TransportLinkedIn resource
    try {
      TransportLinkedInGet result = apiInstance.apiTransportLinkedInIdPut(id, transportLinkedInPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLinkedInApi#apiTransportLinkedInIdPut");
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
| **id** | **String**| TransportLinkedIn identifier | |
| **transportLinkedInPut** | [**TransportLinkedInPut**](TransportLinkedInPut.md)| The updated TransportLinkedIn resource | |

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportLinkedIn resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportLinkedInPost"></a>
# **apiTransportLinkedInPost**
> TransportLinkedInGet apiTransportLinkedInPost(transportLinkedInPost)

Creates a TransportLinkedIn resource.

Creates a TransportLinkedIn resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportLinkedInApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportLinkedInApi apiInstance = new TransportLinkedInApi(defaultClient);
    TransportLinkedInPost transportLinkedInPost = new TransportLinkedInPost(); // TransportLinkedInPost | The new TransportLinkedIn resource
    try {
      TransportLinkedInGet result = apiInstance.apiTransportLinkedInPost(transportLinkedInPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportLinkedInApi#apiTransportLinkedInPost");
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
| **transportLinkedInPost** | [**TransportLinkedInPost**](TransportLinkedInPost.md)| The new TransportLinkedIn resource | |

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportLinkedIn resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

