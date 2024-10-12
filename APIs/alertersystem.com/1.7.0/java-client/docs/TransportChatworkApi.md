# TransportChatworkApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportChatworkGetCollection**](TransportChatworkApi.md#apiTransportChatworkGetCollection) | **GET** /api/transport-chatwork | Retrieves the collection of TransportChatwork resources. |
| [**apiTransportChatworkIdDelete**](TransportChatworkApi.md#apiTransportChatworkIdDelete) | **DELETE** /api/transport-chatwork/{id} | Removes the TransportChatwork resource. |
| [**apiTransportChatworkIdGet**](TransportChatworkApi.md#apiTransportChatworkIdGet) | **GET** /api/transport-chatwork/{id} | Retrieves a TransportChatwork resource. |
| [**apiTransportChatworkIdPatch**](TransportChatworkApi.md#apiTransportChatworkIdPatch) | **PATCH** /api/transport-chatwork/{id} | Updates the TransportChatwork resource. |
| [**apiTransportChatworkIdPut**](TransportChatworkApi.md#apiTransportChatworkIdPut) | **PUT** /api/transport-chatwork/{id} | Replaces the TransportChatwork resource. |
| [**apiTransportChatworkPost**](TransportChatworkApi.md#apiTransportChatworkPost) | **POST** /api/transport-chatwork | Creates a TransportChatwork resource. |


<a id="apiTransportChatworkGetCollection"></a>
# **apiTransportChatworkGetCollection**
> List&lt;TransportChatworkGet&gt; apiTransportChatworkGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportChatwork resources.

Retrieves the collection of TransportChatwork resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportChatworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportChatworkApi apiInstance = new TransportChatworkApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportChatworkGet> result = apiInstance.apiTransportChatworkGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportChatworkApi#apiTransportChatworkGetCollection");
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

[**List&lt;TransportChatworkGet&gt;**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportChatwork collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportChatworkIdDelete"></a>
# **apiTransportChatworkIdDelete**
> apiTransportChatworkIdDelete(id)

Removes the TransportChatwork resource.

Removes the TransportChatwork resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportChatworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportChatworkApi apiInstance = new TransportChatworkApi(defaultClient);
    String id = "id_example"; // String | TransportChatwork identifier
    try {
      apiInstance.apiTransportChatworkIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportChatworkApi#apiTransportChatworkIdDelete");
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
| **id** | **String**| TransportChatwork identifier | |

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
| **204** | TransportChatwork resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportChatworkIdGet"></a>
# **apiTransportChatworkIdGet**
> TransportChatworkGet apiTransportChatworkIdGet(id)

Retrieves a TransportChatwork resource.

Retrieves a TransportChatwork resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportChatworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportChatworkApi apiInstance = new TransportChatworkApi(defaultClient);
    String id = "id_example"; // String | TransportChatwork identifier
    try {
      TransportChatworkGet result = apiInstance.apiTransportChatworkIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportChatworkApi#apiTransportChatworkIdGet");
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
| **id** | **String**| TransportChatwork identifier | |

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportChatwork resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportChatworkIdPatch"></a>
# **apiTransportChatworkIdPatch**
> TransportChatworkGet apiTransportChatworkIdPatch(id, transportChatworkPatch)

Updates the TransportChatwork resource.

Updates the TransportChatwork resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportChatworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportChatworkApi apiInstance = new TransportChatworkApi(defaultClient);
    String id = "id_example"; // String | TransportChatwork identifier
    TransportChatworkPatch transportChatworkPatch = new TransportChatworkPatch(); // TransportChatworkPatch | The updated TransportChatwork resource
    try {
      TransportChatworkGet result = apiInstance.apiTransportChatworkIdPatch(id, transportChatworkPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportChatworkApi#apiTransportChatworkIdPatch");
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
| **id** | **String**| TransportChatwork identifier | |
| **transportChatworkPatch** | [**TransportChatworkPatch**](TransportChatworkPatch.md)| The updated TransportChatwork resource | |

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportChatwork resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportChatworkIdPut"></a>
# **apiTransportChatworkIdPut**
> TransportChatworkGet apiTransportChatworkIdPut(id, transportChatworkPut)

Replaces the TransportChatwork resource.

Replaces the TransportChatwork resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportChatworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportChatworkApi apiInstance = new TransportChatworkApi(defaultClient);
    String id = "id_example"; // String | TransportChatwork identifier
    TransportChatworkPut transportChatworkPut = new TransportChatworkPut(); // TransportChatworkPut | The updated TransportChatwork resource
    try {
      TransportChatworkGet result = apiInstance.apiTransportChatworkIdPut(id, transportChatworkPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportChatworkApi#apiTransportChatworkIdPut");
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
| **id** | **String**| TransportChatwork identifier | |
| **transportChatworkPut** | [**TransportChatworkPut**](TransportChatworkPut.md)| The updated TransportChatwork resource | |

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportChatwork resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportChatworkPost"></a>
# **apiTransportChatworkPost**
> TransportChatworkGet apiTransportChatworkPost(transportChatworkPost)

Creates a TransportChatwork resource.

Creates a TransportChatwork resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportChatworkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportChatworkApi apiInstance = new TransportChatworkApi(defaultClient);
    TransportChatworkPost transportChatworkPost = new TransportChatworkPost(); // TransportChatworkPost | The new TransportChatwork resource
    try {
      TransportChatworkGet result = apiInstance.apiTransportChatworkPost(transportChatworkPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportChatworkApi#apiTransportChatworkPost");
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
| **transportChatworkPost** | [**TransportChatworkPost**](TransportChatworkPost.md)| The new TransportChatwork resource | |

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportChatwork resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

