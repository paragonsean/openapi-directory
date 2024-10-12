# TransportTrelloApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportTrelloGetCollection**](TransportTrelloApi.md#apiTransportTrelloGetCollection) | **GET** /api/transport-trello | Retrieves the collection of TransportTrello resources. |
| [**apiTransportTrelloIdDelete**](TransportTrelloApi.md#apiTransportTrelloIdDelete) | **DELETE** /api/transport-trello/{id} | Removes the TransportTrello resource. |
| [**apiTransportTrelloIdGet**](TransportTrelloApi.md#apiTransportTrelloIdGet) | **GET** /api/transport-trello/{id} | Retrieves a TransportTrello resource. |
| [**apiTransportTrelloIdPatch**](TransportTrelloApi.md#apiTransportTrelloIdPatch) | **PATCH** /api/transport-trello/{id} | Updates the TransportTrello resource. |
| [**apiTransportTrelloIdPut**](TransportTrelloApi.md#apiTransportTrelloIdPut) | **PUT** /api/transport-trello/{id} | Replaces the TransportTrello resource. |
| [**apiTransportTrelloPost**](TransportTrelloApi.md#apiTransportTrelloPost) | **POST** /api/transport-trello | Creates a TransportTrello resource. |


<a id="apiTransportTrelloGetCollection"></a>
# **apiTransportTrelloGetCollection**
> List&lt;TransportTrelloGet&gt; apiTransportTrelloGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportTrello resources.

Retrieves the collection of TransportTrello resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTrelloApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTrelloApi apiInstance = new TransportTrelloApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportTrelloGet> result = apiInstance.apiTransportTrelloGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTrelloApi#apiTransportTrelloGetCollection");
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

[**List&lt;TransportTrelloGet&gt;**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTrello collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTrelloIdDelete"></a>
# **apiTransportTrelloIdDelete**
> apiTransportTrelloIdDelete(id)

Removes the TransportTrello resource.

Removes the TransportTrello resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTrelloApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTrelloApi apiInstance = new TransportTrelloApi(defaultClient);
    String id = "id_example"; // String | TransportTrello identifier
    try {
      apiInstance.apiTransportTrelloIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTrelloApi#apiTransportTrelloIdDelete");
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
| **id** | **String**| TransportTrello identifier | |

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
| **204** | TransportTrello resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTrelloIdGet"></a>
# **apiTransportTrelloIdGet**
> TransportTrelloGet apiTransportTrelloIdGet(id)

Retrieves a TransportTrello resource.

Retrieves a TransportTrello resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTrelloApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTrelloApi apiInstance = new TransportTrelloApi(defaultClient);
    String id = "id_example"; // String | TransportTrello identifier
    try {
      TransportTrelloGet result = apiInstance.apiTransportTrelloIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTrelloApi#apiTransportTrelloIdGet");
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
| **id** | **String**| TransportTrello identifier | |

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTrello resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTrelloIdPatch"></a>
# **apiTransportTrelloIdPatch**
> TransportTrelloGet apiTransportTrelloIdPatch(id, transportTrelloPatch)

Updates the TransportTrello resource.

Updates the TransportTrello resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTrelloApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTrelloApi apiInstance = new TransportTrelloApi(defaultClient);
    String id = "id_example"; // String | TransportTrello identifier
    TransportTrelloPatch transportTrelloPatch = new TransportTrelloPatch(); // TransportTrelloPatch | The updated TransportTrello resource
    try {
      TransportTrelloGet result = apiInstance.apiTransportTrelloIdPatch(id, transportTrelloPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTrelloApi#apiTransportTrelloIdPatch");
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
| **id** | **String**| TransportTrello identifier | |
| **transportTrelloPatch** | [**TransportTrelloPatch**](TransportTrelloPatch.md)| The updated TransportTrello resource | |

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTrello resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTrelloIdPut"></a>
# **apiTransportTrelloIdPut**
> TransportTrelloGet apiTransportTrelloIdPut(id, transportTrelloPut)

Replaces the TransportTrello resource.

Replaces the TransportTrello resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTrelloApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTrelloApi apiInstance = new TransportTrelloApi(defaultClient);
    String id = "id_example"; // String | TransportTrello identifier
    TransportTrelloPut transportTrelloPut = new TransportTrelloPut(); // TransportTrelloPut | The updated TransportTrello resource
    try {
      TransportTrelloGet result = apiInstance.apiTransportTrelloIdPut(id, transportTrelloPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTrelloApi#apiTransportTrelloIdPut");
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
| **id** | **String**| TransportTrello identifier | |
| **transportTrelloPut** | [**TransportTrelloPut**](TransportTrelloPut.md)| The updated TransportTrello resource | |

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportTrello resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportTrelloPost"></a>
# **apiTransportTrelloPost**
> TransportTrelloGet apiTransportTrelloPost(transportTrelloPost)

Creates a TransportTrello resource.

Creates a TransportTrello resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportTrelloApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportTrelloApi apiInstance = new TransportTrelloApi(defaultClient);
    TransportTrelloPost transportTrelloPost = new TransportTrelloPost(); // TransportTrelloPost | The new TransportTrello resource
    try {
      TransportTrelloGet result = apiInstance.apiTransportTrelloPost(transportTrelloPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportTrelloApi#apiTransportTrelloPost");
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
| **transportTrelloPost** | [**TransportTrelloPost**](TransportTrelloPost.md)| The new TransportTrello resource | |

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportTrello resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

