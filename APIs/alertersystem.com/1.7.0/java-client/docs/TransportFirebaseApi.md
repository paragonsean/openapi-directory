# TransportFirebaseApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportFirebaseGetCollection**](TransportFirebaseApi.md#apiTransportFirebaseGetCollection) | **GET** /api/transport-firebase | Retrieves the collection of TransportFirebase resources. |
| [**apiTransportFirebaseIdDelete**](TransportFirebaseApi.md#apiTransportFirebaseIdDelete) | **DELETE** /api/transport-firebase/{id} | Removes the TransportFirebase resource. |
| [**apiTransportFirebaseIdGet**](TransportFirebaseApi.md#apiTransportFirebaseIdGet) | **GET** /api/transport-firebase/{id} | Retrieves a TransportFirebase resource. |
| [**apiTransportFirebaseIdPatch**](TransportFirebaseApi.md#apiTransportFirebaseIdPatch) | **PATCH** /api/transport-firebase/{id} | Updates the TransportFirebase resource. |
| [**apiTransportFirebaseIdPut**](TransportFirebaseApi.md#apiTransportFirebaseIdPut) | **PUT** /api/transport-firebase/{id} | Replaces the TransportFirebase resource. |
| [**apiTransportFirebasePost**](TransportFirebaseApi.md#apiTransportFirebasePost) | **POST** /api/transport-firebase | Creates a TransportFirebase resource. |


<a id="apiTransportFirebaseGetCollection"></a>
# **apiTransportFirebaseGetCollection**
> List&lt;TransportFirebaseGet&gt; apiTransportFirebaseGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportFirebase resources.

Retrieves the collection of TransportFirebase resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFirebaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFirebaseApi apiInstance = new TransportFirebaseApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportFirebaseGet> result = apiInstance.apiTransportFirebaseGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFirebaseApi#apiTransportFirebaseGetCollection");
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

[**List&lt;TransportFirebaseGet&gt;**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFirebase collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFirebaseIdDelete"></a>
# **apiTransportFirebaseIdDelete**
> apiTransportFirebaseIdDelete(id)

Removes the TransportFirebase resource.

Removes the TransportFirebase resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFirebaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFirebaseApi apiInstance = new TransportFirebaseApi(defaultClient);
    String id = "id_example"; // String | TransportFirebase identifier
    try {
      apiInstance.apiTransportFirebaseIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFirebaseApi#apiTransportFirebaseIdDelete");
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
| **id** | **String**| TransportFirebase identifier | |

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
| **204** | TransportFirebase resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFirebaseIdGet"></a>
# **apiTransportFirebaseIdGet**
> TransportFirebaseGet apiTransportFirebaseIdGet(id)

Retrieves a TransportFirebase resource.

Retrieves a TransportFirebase resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFirebaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFirebaseApi apiInstance = new TransportFirebaseApi(defaultClient);
    String id = "id_example"; // String | TransportFirebase identifier
    try {
      TransportFirebaseGet result = apiInstance.apiTransportFirebaseIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFirebaseApi#apiTransportFirebaseIdGet");
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
| **id** | **String**| TransportFirebase identifier | |

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFirebase resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFirebaseIdPatch"></a>
# **apiTransportFirebaseIdPatch**
> TransportFirebaseGet apiTransportFirebaseIdPatch(id, transportFirebasePatch)

Updates the TransportFirebase resource.

Updates the TransportFirebase resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFirebaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFirebaseApi apiInstance = new TransportFirebaseApi(defaultClient);
    String id = "id_example"; // String | TransportFirebase identifier
    TransportFirebasePatch transportFirebasePatch = new TransportFirebasePatch(); // TransportFirebasePatch | The updated TransportFirebase resource
    try {
      TransportFirebaseGet result = apiInstance.apiTransportFirebaseIdPatch(id, transportFirebasePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFirebaseApi#apiTransportFirebaseIdPatch");
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
| **id** | **String**| TransportFirebase identifier | |
| **transportFirebasePatch** | [**TransportFirebasePatch**](TransportFirebasePatch.md)| The updated TransportFirebase resource | |

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFirebase resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFirebaseIdPut"></a>
# **apiTransportFirebaseIdPut**
> TransportFirebaseGet apiTransportFirebaseIdPut(id, transportFirebasePut)

Replaces the TransportFirebase resource.

Replaces the TransportFirebase resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFirebaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFirebaseApi apiInstance = new TransportFirebaseApi(defaultClient);
    String id = "id_example"; // String | TransportFirebase identifier
    TransportFirebasePut transportFirebasePut = new TransportFirebasePut(); // TransportFirebasePut | The updated TransportFirebase resource
    try {
      TransportFirebaseGet result = apiInstance.apiTransportFirebaseIdPut(id, transportFirebasePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFirebaseApi#apiTransportFirebaseIdPut");
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
| **id** | **String**| TransportFirebase identifier | |
| **transportFirebasePut** | [**TransportFirebasePut**](TransportFirebasePut.md)| The updated TransportFirebase resource | |

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFirebase resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFirebasePost"></a>
# **apiTransportFirebasePost**
> TransportFirebaseGet apiTransportFirebasePost(transportFirebasePost)

Creates a TransportFirebase resource.

Creates a TransportFirebase resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFirebaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFirebaseApi apiInstance = new TransportFirebaseApi(defaultClient);
    TransportFirebasePost transportFirebasePost = new TransportFirebasePost(); // TransportFirebasePost | The new TransportFirebase resource
    try {
      TransportFirebaseGet result = apiInstance.apiTransportFirebasePost(transportFirebasePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFirebaseApi#apiTransportFirebasePost");
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
| **transportFirebasePost** | [**TransportFirebasePost**](TransportFirebasePost.md)| The new TransportFirebase resource | |

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportFirebase resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

