# TransportEmailApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportEmailGetCollection**](TransportEmailApi.md#apiTransportEmailGetCollection) | **GET** /api/transport-email | Retrieves the collection of TransportEmail resources. |
| [**apiTransportEmailIdDelete**](TransportEmailApi.md#apiTransportEmailIdDelete) | **DELETE** /api/transport-email/{id} | Removes the TransportEmail resource. |
| [**apiTransportEmailIdGet**](TransportEmailApi.md#apiTransportEmailIdGet) | **GET** /api/transport-email/{id} | Retrieves a TransportEmail resource. |
| [**apiTransportEmailIdPatch**](TransportEmailApi.md#apiTransportEmailIdPatch) | **PATCH** /api/transport-email/{id} | Updates the TransportEmail resource. |
| [**apiTransportEmailIdPut**](TransportEmailApi.md#apiTransportEmailIdPut) | **PUT** /api/transport-email/{id} | Replaces the TransportEmail resource. |
| [**apiTransportEmailPost**](TransportEmailApi.md#apiTransportEmailPost) | **POST** /api/transport-email | Creates a TransportEmail resource. |


<a id="apiTransportEmailGetCollection"></a>
# **apiTransportEmailGetCollection**
> List&lt;TransportEmailGet&gt; apiTransportEmailGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportEmail resources.

Retrieves the collection of TransportEmail resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEmailApi apiInstance = new TransportEmailApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportEmailGet> result = apiInstance.apiTransportEmailGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEmailApi#apiTransportEmailGetCollection");
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

[**List&lt;TransportEmailGet&gt;**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEmail collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEmailIdDelete"></a>
# **apiTransportEmailIdDelete**
> apiTransportEmailIdDelete(id)

Removes the TransportEmail resource.

Removes the TransportEmail resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEmailApi apiInstance = new TransportEmailApi(defaultClient);
    String id = "id_example"; // String | TransportEmail identifier
    try {
      apiInstance.apiTransportEmailIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEmailApi#apiTransportEmailIdDelete");
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
| **id** | **String**| TransportEmail identifier | |

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
| **204** | TransportEmail resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEmailIdGet"></a>
# **apiTransportEmailIdGet**
> TransportEmailGet apiTransportEmailIdGet(id)

Retrieves a TransportEmail resource.

Retrieves a TransportEmail resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEmailApi apiInstance = new TransportEmailApi(defaultClient);
    String id = "id_example"; // String | TransportEmail identifier
    try {
      TransportEmailGet result = apiInstance.apiTransportEmailIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEmailApi#apiTransportEmailIdGet");
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
| **id** | **String**| TransportEmail identifier | |

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEmail resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEmailIdPatch"></a>
# **apiTransportEmailIdPatch**
> TransportEmailGet apiTransportEmailIdPatch(id, transportEmailPatch)

Updates the TransportEmail resource.

Updates the TransportEmail resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEmailApi apiInstance = new TransportEmailApi(defaultClient);
    String id = "id_example"; // String | TransportEmail identifier
    TransportEmailPatch transportEmailPatch = new TransportEmailPatch(); // TransportEmailPatch | The updated TransportEmail resource
    try {
      TransportEmailGet result = apiInstance.apiTransportEmailIdPatch(id, transportEmailPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEmailApi#apiTransportEmailIdPatch");
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
| **id** | **String**| TransportEmail identifier | |
| **transportEmailPatch** | [**TransportEmailPatch**](TransportEmailPatch.md)| The updated TransportEmail resource | |

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEmail resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEmailIdPut"></a>
# **apiTransportEmailIdPut**
> TransportEmailGet apiTransportEmailIdPut(id, transportEmailPut)

Replaces the TransportEmail resource.

Replaces the TransportEmail resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEmailApi apiInstance = new TransportEmailApi(defaultClient);
    String id = "id_example"; // String | TransportEmail identifier
    TransportEmailPut transportEmailPut = new TransportEmailPut(); // TransportEmailPut | The updated TransportEmail resource
    try {
      TransportEmailGet result = apiInstance.apiTransportEmailIdPut(id, transportEmailPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEmailApi#apiTransportEmailIdPut");
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
| **id** | **String**| TransportEmail identifier | |
| **transportEmailPut** | [**TransportEmailPut**](TransportEmailPut.md)| The updated TransportEmail resource | |

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportEmail resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportEmailPost"></a>
# **apiTransportEmailPost**
> TransportEmailGet apiTransportEmailPost(transportEmailPost)

Creates a TransportEmail resource.

Creates a TransportEmail resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportEmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportEmailApi apiInstance = new TransportEmailApi(defaultClient);
    TransportEmailPost transportEmailPost = new TransportEmailPost(); // TransportEmailPost | The new TransportEmail resource
    try {
      TransportEmailGet result = apiInstance.apiTransportEmailPost(transportEmailPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportEmailApi#apiTransportEmailPost");
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
| **transportEmailPost** | [**TransportEmailPost**](TransportEmailPost.md)| The new TransportEmail resource | |

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportEmail resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

