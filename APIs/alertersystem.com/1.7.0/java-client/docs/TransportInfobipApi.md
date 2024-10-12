# TransportInfobipApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportInfobipGetCollection**](TransportInfobipApi.md#apiTransportInfobipGetCollection) | **GET** /api/transport-infobip | Retrieves the collection of TransportInfobip resources. |
| [**apiTransportInfobipIdDelete**](TransportInfobipApi.md#apiTransportInfobipIdDelete) | **DELETE** /api/transport-infobip/{id} | Removes the TransportInfobip resource. |
| [**apiTransportInfobipIdGet**](TransportInfobipApi.md#apiTransportInfobipIdGet) | **GET** /api/transport-infobip/{id} | Retrieves a TransportInfobip resource. |
| [**apiTransportInfobipIdPatch**](TransportInfobipApi.md#apiTransportInfobipIdPatch) | **PATCH** /api/transport-infobip/{id} | Updates the TransportInfobip resource. |
| [**apiTransportInfobipIdPut**](TransportInfobipApi.md#apiTransportInfobipIdPut) | **PUT** /api/transport-infobip/{id} | Replaces the TransportInfobip resource. |
| [**apiTransportInfobipPost**](TransportInfobipApi.md#apiTransportInfobipPost) | **POST** /api/transport-infobip | Creates a TransportInfobip resource. |


<a id="apiTransportInfobipGetCollection"></a>
# **apiTransportInfobipGetCollection**
> List&lt;TransportInfobipGet&gt; apiTransportInfobipGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportInfobip resources.

Retrieves the collection of TransportInfobip resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportInfobipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportInfobipApi apiInstance = new TransportInfobipApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportInfobipGet> result = apiInstance.apiTransportInfobipGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportInfobipApi#apiTransportInfobipGetCollection");
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

[**List&lt;TransportInfobipGet&gt;**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportInfobip collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportInfobipIdDelete"></a>
# **apiTransportInfobipIdDelete**
> apiTransportInfobipIdDelete(id)

Removes the TransportInfobip resource.

Removes the TransportInfobip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportInfobipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportInfobipApi apiInstance = new TransportInfobipApi(defaultClient);
    String id = "id_example"; // String | TransportInfobip identifier
    try {
      apiInstance.apiTransportInfobipIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportInfobipApi#apiTransportInfobipIdDelete");
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
| **id** | **String**| TransportInfobip identifier | |

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
| **204** | TransportInfobip resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportInfobipIdGet"></a>
# **apiTransportInfobipIdGet**
> TransportInfobipGet apiTransportInfobipIdGet(id)

Retrieves a TransportInfobip resource.

Retrieves a TransportInfobip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportInfobipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportInfobipApi apiInstance = new TransportInfobipApi(defaultClient);
    String id = "id_example"; // String | TransportInfobip identifier
    try {
      TransportInfobipGet result = apiInstance.apiTransportInfobipIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportInfobipApi#apiTransportInfobipIdGet");
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
| **id** | **String**| TransportInfobip identifier | |

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportInfobip resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportInfobipIdPatch"></a>
# **apiTransportInfobipIdPatch**
> TransportInfobipGet apiTransportInfobipIdPatch(id, transportInfobipPatch)

Updates the TransportInfobip resource.

Updates the TransportInfobip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportInfobipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportInfobipApi apiInstance = new TransportInfobipApi(defaultClient);
    String id = "id_example"; // String | TransportInfobip identifier
    TransportInfobipPatch transportInfobipPatch = new TransportInfobipPatch(); // TransportInfobipPatch | The updated TransportInfobip resource
    try {
      TransportInfobipGet result = apiInstance.apiTransportInfobipIdPatch(id, transportInfobipPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportInfobipApi#apiTransportInfobipIdPatch");
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
| **id** | **String**| TransportInfobip identifier | |
| **transportInfobipPatch** | [**TransportInfobipPatch**](TransportInfobipPatch.md)| The updated TransportInfobip resource | |

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportInfobip resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportInfobipIdPut"></a>
# **apiTransportInfobipIdPut**
> TransportInfobipGet apiTransportInfobipIdPut(id, transportInfobipPut)

Replaces the TransportInfobip resource.

Replaces the TransportInfobip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportInfobipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportInfobipApi apiInstance = new TransportInfobipApi(defaultClient);
    String id = "id_example"; // String | TransportInfobip identifier
    TransportInfobipPut transportInfobipPut = new TransportInfobipPut(); // TransportInfobipPut | The updated TransportInfobip resource
    try {
      TransportInfobipGet result = apiInstance.apiTransportInfobipIdPut(id, transportInfobipPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportInfobipApi#apiTransportInfobipIdPut");
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
| **id** | **String**| TransportInfobip identifier | |
| **transportInfobipPut** | [**TransportInfobipPut**](TransportInfobipPut.md)| The updated TransportInfobip resource | |

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportInfobip resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportInfobipPost"></a>
# **apiTransportInfobipPost**
> TransportInfobipGet apiTransportInfobipPost(transportInfobipPost)

Creates a TransportInfobip resource.

Creates a TransportInfobip resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportInfobipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportInfobipApi apiInstance = new TransportInfobipApi(defaultClient);
    TransportInfobipPost transportInfobipPost = new TransportInfobipPost(); // TransportInfobipPost | The new TransportInfobip resource
    try {
      TransportInfobipGet result = apiInstance.apiTransportInfobipPost(transportInfobipPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportInfobipApi#apiTransportInfobipPost");
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
| **transportInfobipPost** | [**TransportInfobipPost**](TransportInfobipPost.md)| The new TransportInfobip resource | |

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportInfobip resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

