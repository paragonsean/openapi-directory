# TransportSlackApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSlackGetCollection**](TransportSlackApi.md#apiTransportSlackGetCollection) | **GET** /api/transport-slack | Retrieves the collection of TransportSlack resources. |
| [**apiTransportSlackIdDelete**](TransportSlackApi.md#apiTransportSlackIdDelete) | **DELETE** /api/transport-slack/{id} | Removes the TransportSlack resource. |
| [**apiTransportSlackIdGet**](TransportSlackApi.md#apiTransportSlackIdGet) | **GET** /api/transport-slack/{id} | Retrieves a TransportSlack resource. |
| [**apiTransportSlackIdPatch**](TransportSlackApi.md#apiTransportSlackIdPatch) | **PATCH** /api/transport-slack/{id} | Updates the TransportSlack resource. |
| [**apiTransportSlackIdPut**](TransportSlackApi.md#apiTransportSlackIdPut) | **PUT** /api/transport-slack/{id} | Replaces the TransportSlack resource. |
| [**apiTransportSlackPost**](TransportSlackApi.md#apiTransportSlackPost) | **POST** /api/transport-slack | Creates a TransportSlack resource. |


<a id="apiTransportSlackGetCollection"></a>
# **apiTransportSlackGetCollection**
> List&lt;TransportSlackGet&gt; apiTransportSlackGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSlack resources.

Retrieves the collection of TransportSlack resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSlackApi apiInstance = new TransportSlackApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSlackGet> result = apiInstance.apiTransportSlackGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSlackApi#apiTransportSlackGetCollection");
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

[**List&lt;TransportSlackGet&gt;**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSlack collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSlackIdDelete"></a>
# **apiTransportSlackIdDelete**
> apiTransportSlackIdDelete(id)

Removes the TransportSlack resource.

Removes the TransportSlack resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSlackApi apiInstance = new TransportSlackApi(defaultClient);
    String id = "id_example"; // String | TransportSlack identifier
    try {
      apiInstance.apiTransportSlackIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSlackApi#apiTransportSlackIdDelete");
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
| **id** | **String**| TransportSlack identifier | |

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
| **204** | TransportSlack resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSlackIdGet"></a>
# **apiTransportSlackIdGet**
> TransportSlackGet apiTransportSlackIdGet(id)

Retrieves a TransportSlack resource.

Retrieves a TransportSlack resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSlackApi apiInstance = new TransportSlackApi(defaultClient);
    String id = "id_example"; // String | TransportSlack identifier
    try {
      TransportSlackGet result = apiInstance.apiTransportSlackIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSlackApi#apiTransportSlackIdGet");
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
| **id** | **String**| TransportSlack identifier | |

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSlack resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSlackIdPatch"></a>
# **apiTransportSlackIdPatch**
> TransportSlackGet apiTransportSlackIdPatch(id, transportSlackPatch)

Updates the TransportSlack resource.

Updates the TransportSlack resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSlackApi apiInstance = new TransportSlackApi(defaultClient);
    String id = "id_example"; // String | TransportSlack identifier
    TransportSlackPatch transportSlackPatch = new TransportSlackPatch(); // TransportSlackPatch | The updated TransportSlack resource
    try {
      TransportSlackGet result = apiInstance.apiTransportSlackIdPatch(id, transportSlackPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSlackApi#apiTransportSlackIdPatch");
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
| **id** | **String**| TransportSlack identifier | |
| **transportSlackPatch** | [**TransportSlackPatch**](TransportSlackPatch.md)| The updated TransportSlack resource | |

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSlack resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSlackIdPut"></a>
# **apiTransportSlackIdPut**
> TransportSlackGet apiTransportSlackIdPut(id, transportSlackPut)

Replaces the TransportSlack resource.

Replaces the TransportSlack resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSlackApi apiInstance = new TransportSlackApi(defaultClient);
    String id = "id_example"; // String | TransportSlack identifier
    TransportSlackPut transportSlackPut = new TransportSlackPut(); // TransportSlackPut | The updated TransportSlack resource
    try {
      TransportSlackGet result = apiInstance.apiTransportSlackIdPut(id, transportSlackPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSlackApi#apiTransportSlackIdPut");
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
| **id** | **String**| TransportSlack identifier | |
| **transportSlackPut** | [**TransportSlackPut**](TransportSlackPut.md)| The updated TransportSlack resource | |

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSlack resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSlackPost"></a>
# **apiTransportSlackPost**
> TransportSlackGet apiTransportSlackPost(transportSlackPost)

Creates a TransportSlack resource.

Creates a TransportSlack resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSlackApi apiInstance = new TransportSlackApi(defaultClient);
    TransportSlackPost transportSlackPost = new TransportSlackPost(); // TransportSlackPost | The new TransportSlack resource
    try {
      TransportSlackGet result = apiInstance.apiTransportSlackPost(transportSlackPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSlackApi#apiTransportSlackPost");
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
| **transportSlackPost** | [**TransportSlackPost**](TransportSlackPost.md)| The new TransportSlack resource | |

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSlack resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

