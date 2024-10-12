# TransportRingCentralApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportRingCentralGetCollection**](TransportRingCentralApi.md#apiTransportRingCentralGetCollection) | **GET** /api/transport-ring-central | Retrieves the collection of TransportRingCentral resources. |
| [**apiTransportRingCentralIdDelete**](TransportRingCentralApi.md#apiTransportRingCentralIdDelete) | **DELETE** /api/transport-ring-central/{id} | Removes the TransportRingCentral resource. |
| [**apiTransportRingCentralIdGet**](TransportRingCentralApi.md#apiTransportRingCentralIdGet) | **GET** /api/transport-ring-central/{id} | Retrieves a TransportRingCentral resource. |
| [**apiTransportRingCentralIdPatch**](TransportRingCentralApi.md#apiTransportRingCentralIdPatch) | **PATCH** /api/transport-ring-central/{id} | Updates the TransportRingCentral resource. |
| [**apiTransportRingCentralIdPut**](TransportRingCentralApi.md#apiTransportRingCentralIdPut) | **PUT** /api/transport-ring-central/{id} | Replaces the TransportRingCentral resource. |
| [**apiTransportRingCentralPost**](TransportRingCentralApi.md#apiTransportRingCentralPost) | **POST** /api/transport-ring-central | Creates a TransportRingCentral resource. |


<a id="apiTransportRingCentralGetCollection"></a>
# **apiTransportRingCentralGetCollection**
> List&lt;TransportRingCentralGet&gt; apiTransportRingCentralGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportRingCentral resources.

Retrieves the collection of TransportRingCentral resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRingCentralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRingCentralApi apiInstance = new TransportRingCentralApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportRingCentralGet> result = apiInstance.apiTransportRingCentralGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRingCentralApi#apiTransportRingCentralGetCollection");
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

[**List&lt;TransportRingCentralGet&gt;**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRingCentral collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRingCentralIdDelete"></a>
# **apiTransportRingCentralIdDelete**
> apiTransportRingCentralIdDelete(id)

Removes the TransportRingCentral resource.

Removes the TransportRingCentral resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRingCentralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRingCentralApi apiInstance = new TransportRingCentralApi(defaultClient);
    String id = "id_example"; // String | TransportRingCentral identifier
    try {
      apiInstance.apiTransportRingCentralIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRingCentralApi#apiTransportRingCentralIdDelete");
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
| **id** | **String**| TransportRingCentral identifier | |

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
| **204** | TransportRingCentral resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRingCentralIdGet"></a>
# **apiTransportRingCentralIdGet**
> TransportRingCentralGet apiTransportRingCentralIdGet(id)

Retrieves a TransportRingCentral resource.

Retrieves a TransportRingCentral resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRingCentralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRingCentralApi apiInstance = new TransportRingCentralApi(defaultClient);
    String id = "id_example"; // String | TransportRingCentral identifier
    try {
      TransportRingCentralGet result = apiInstance.apiTransportRingCentralIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRingCentralApi#apiTransportRingCentralIdGet");
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
| **id** | **String**| TransportRingCentral identifier | |

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRingCentral resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRingCentralIdPatch"></a>
# **apiTransportRingCentralIdPatch**
> TransportRingCentralGet apiTransportRingCentralIdPatch(id, transportRingCentralPatch)

Updates the TransportRingCentral resource.

Updates the TransportRingCentral resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRingCentralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRingCentralApi apiInstance = new TransportRingCentralApi(defaultClient);
    String id = "id_example"; // String | TransportRingCentral identifier
    TransportRingCentralPatch transportRingCentralPatch = new TransportRingCentralPatch(); // TransportRingCentralPatch | The updated TransportRingCentral resource
    try {
      TransportRingCentralGet result = apiInstance.apiTransportRingCentralIdPatch(id, transportRingCentralPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRingCentralApi#apiTransportRingCentralIdPatch");
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
| **id** | **String**| TransportRingCentral identifier | |
| **transportRingCentralPatch** | [**TransportRingCentralPatch**](TransportRingCentralPatch.md)| The updated TransportRingCentral resource | |

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRingCentral resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRingCentralIdPut"></a>
# **apiTransportRingCentralIdPut**
> TransportRingCentralGet apiTransportRingCentralIdPut(id, transportRingCentralPut)

Replaces the TransportRingCentral resource.

Replaces the TransportRingCentral resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRingCentralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRingCentralApi apiInstance = new TransportRingCentralApi(defaultClient);
    String id = "id_example"; // String | TransportRingCentral identifier
    TransportRingCentralPut transportRingCentralPut = new TransportRingCentralPut(); // TransportRingCentralPut | The updated TransportRingCentral resource
    try {
      TransportRingCentralGet result = apiInstance.apiTransportRingCentralIdPut(id, transportRingCentralPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRingCentralApi#apiTransportRingCentralIdPut");
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
| **id** | **String**| TransportRingCentral identifier | |
| **transportRingCentralPut** | [**TransportRingCentralPut**](TransportRingCentralPut.md)| The updated TransportRingCentral resource | |

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportRingCentral resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportRingCentralPost"></a>
# **apiTransportRingCentralPost**
> TransportRingCentralGet apiTransportRingCentralPost(transportRingCentralPost)

Creates a TransportRingCentral resource.

Creates a TransportRingCentral resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportRingCentralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportRingCentralApi apiInstance = new TransportRingCentralApi(defaultClient);
    TransportRingCentralPost transportRingCentralPost = new TransportRingCentralPost(); // TransportRingCentralPost | The new TransportRingCentral resource
    try {
      TransportRingCentralGet result = apiInstance.apiTransportRingCentralPost(transportRingCentralPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportRingCentralApi#apiTransportRingCentralPost");
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
| **transportRingCentralPost** | [**TransportRingCentralPost**](TransportRingCentralPost.md)| The new TransportRingCentral resource | |

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportRingCentral resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

