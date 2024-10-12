# TransportOpsgenieApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportOpsgenieGetCollection**](TransportOpsgenieApi.md#apiTransportOpsgenieGetCollection) | **GET** /api/transport-opsgenie | Retrieves the collection of TransportOpsgenie resources. |
| [**apiTransportOpsgenieIdDelete**](TransportOpsgenieApi.md#apiTransportOpsgenieIdDelete) | **DELETE** /api/transport-opsgenie/{id} | Removes the TransportOpsgenie resource. |
| [**apiTransportOpsgenieIdGet**](TransportOpsgenieApi.md#apiTransportOpsgenieIdGet) | **GET** /api/transport-opsgenie/{id} | Retrieves a TransportOpsgenie resource. |
| [**apiTransportOpsgenieIdPatch**](TransportOpsgenieApi.md#apiTransportOpsgenieIdPatch) | **PATCH** /api/transport-opsgenie/{id} | Updates the TransportOpsgenie resource. |
| [**apiTransportOpsgenieIdPut**](TransportOpsgenieApi.md#apiTransportOpsgenieIdPut) | **PUT** /api/transport-opsgenie/{id} | Replaces the TransportOpsgenie resource. |
| [**apiTransportOpsgeniePost**](TransportOpsgenieApi.md#apiTransportOpsgeniePost) | **POST** /api/transport-opsgenie | Creates a TransportOpsgenie resource. |


<a id="apiTransportOpsgenieGetCollection"></a>
# **apiTransportOpsgenieGetCollection**
> List&lt;TransportOpsgenieGet&gt; apiTransportOpsgenieGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportOpsgenie resources.

Retrieves the collection of TransportOpsgenie resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOpsgenieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOpsgenieApi apiInstance = new TransportOpsgenieApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportOpsgenieGet> result = apiInstance.apiTransportOpsgenieGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOpsgenieApi#apiTransportOpsgenieGetCollection");
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

[**List&lt;TransportOpsgenieGet&gt;**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOpsgenie collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOpsgenieIdDelete"></a>
# **apiTransportOpsgenieIdDelete**
> apiTransportOpsgenieIdDelete(id)

Removes the TransportOpsgenie resource.

Removes the TransportOpsgenie resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOpsgenieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOpsgenieApi apiInstance = new TransportOpsgenieApi(defaultClient);
    String id = "id_example"; // String | TransportOpsgenie identifier
    try {
      apiInstance.apiTransportOpsgenieIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOpsgenieApi#apiTransportOpsgenieIdDelete");
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
| **id** | **String**| TransportOpsgenie identifier | |

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
| **204** | TransportOpsgenie resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOpsgenieIdGet"></a>
# **apiTransportOpsgenieIdGet**
> TransportOpsgenieGet apiTransportOpsgenieIdGet(id)

Retrieves a TransportOpsgenie resource.

Retrieves a TransportOpsgenie resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOpsgenieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOpsgenieApi apiInstance = new TransportOpsgenieApi(defaultClient);
    String id = "id_example"; // String | TransportOpsgenie identifier
    try {
      TransportOpsgenieGet result = apiInstance.apiTransportOpsgenieIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOpsgenieApi#apiTransportOpsgenieIdGet");
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
| **id** | **String**| TransportOpsgenie identifier | |

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOpsgenie resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOpsgenieIdPatch"></a>
# **apiTransportOpsgenieIdPatch**
> TransportOpsgenieGet apiTransportOpsgenieIdPatch(id, transportOpsgeniePatch)

Updates the TransportOpsgenie resource.

Updates the TransportOpsgenie resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOpsgenieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOpsgenieApi apiInstance = new TransportOpsgenieApi(defaultClient);
    String id = "id_example"; // String | TransportOpsgenie identifier
    TransportOpsgeniePatch transportOpsgeniePatch = new TransportOpsgeniePatch(); // TransportOpsgeniePatch | The updated TransportOpsgenie resource
    try {
      TransportOpsgenieGet result = apiInstance.apiTransportOpsgenieIdPatch(id, transportOpsgeniePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOpsgenieApi#apiTransportOpsgenieIdPatch");
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
| **id** | **String**| TransportOpsgenie identifier | |
| **transportOpsgeniePatch** | [**TransportOpsgeniePatch**](TransportOpsgeniePatch.md)| The updated TransportOpsgenie resource | |

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOpsgenie resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOpsgenieIdPut"></a>
# **apiTransportOpsgenieIdPut**
> TransportOpsgenieGet apiTransportOpsgenieIdPut(id, transportOpsgeniePut)

Replaces the TransportOpsgenie resource.

Replaces the TransportOpsgenie resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOpsgenieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOpsgenieApi apiInstance = new TransportOpsgenieApi(defaultClient);
    String id = "id_example"; // String | TransportOpsgenie identifier
    TransportOpsgeniePut transportOpsgeniePut = new TransportOpsgeniePut(); // TransportOpsgeniePut | The updated TransportOpsgenie resource
    try {
      TransportOpsgenieGet result = apiInstance.apiTransportOpsgenieIdPut(id, transportOpsgeniePut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOpsgenieApi#apiTransportOpsgenieIdPut");
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
| **id** | **String**| TransportOpsgenie identifier | |
| **transportOpsgeniePut** | [**TransportOpsgeniePut**](TransportOpsgeniePut.md)| The updated TransportOpsgenie resource | |

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOpsgenie resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOpsgeniePost"></a>
# **apiTransportOpsgeniePost**
> TransportOpsgenieGet apiTransportOpsgeniePost(transportOpsgeniePost)

Creates a TransportOpsgenie resource.

Creates a TransportOpsgenie resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOpsgenieApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOpsgenieApi apiInstance = new TransportOpsgenieApi(defaultClient);
    TransportOpsgeniePost transportOpsgeniePost = new TransportOpsgeniePost(); // TransportOpsgeniePost | The new TransportOpsgenie resource
    try {
      TransportOpsgenieGet result = apiInstance.apiTransportOpsgeniePost(transportOpsgeniePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOpsgenieApi#apiTransportOpsgeniePost");
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
| **transportOpsgeniePost** | [**TransportOpsgeniePost**](TransportOpsgeniePost.md)| The new TransportOpsgenie resource | |

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportOpsgenie resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

