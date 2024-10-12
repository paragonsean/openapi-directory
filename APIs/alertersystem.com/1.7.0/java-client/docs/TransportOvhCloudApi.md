# TransportOvhCloudApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportOvhCloudGetCollection**](TransportOvhCloudApi.md#apiTransportOvhCloudGetCollection) | **GET** /api/transport-ovh-cloud | Retrieves the collection of TransportOvhCloud resources. |
| [**apiTransportOvhCloudIdDelete**](TransportOvhCloudApi.md#apiTransportOvhCloudIdDelete) | **DELETE** /api/transport-ovh-cloud/{id} | Removes the TransportOvhCloud resource. |
| [**apiTransportOvhCloudIdGet**](TransportOvhCloudApi.md#apiTransportOvhCloudIdGet) | **GET** /api/transport-ovh-cloud/{id} | Retrieves a TransportOvhCloud resource. |
| [**apiTransportOvhCloudIdPatch**](TransportOvhCloudApi.md#apiTransportOvhCloudIdPatch) | **PATCH** /api/transport-ovh-cloud/{id} | Updates the TransportOvhCloud resource. |
| [**apiTransportOvhCloudIdPut**](TransportOvhCloudApi.md#apiTransportOvhCloudIdPut) | **PUT** /api/transport-ovh-cloud/{id} | Replaces the TransportOvhCloud resource. |
| [**apiTransportOvhCloudPost**](TransportOvhCloudApi.md#apiTransportOvhCloudPost) | **POST** /api/transport-ovh-cloud | Creates a TransportOvhCloud resource. |


<a id="apiTransportOvhCloudGetCollection"></a>
# **apiTransportOvhCloudGetCollection**
> List&lt;TransportOvhCloudGet&gt; apiTransportOvhCloudGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportOvhCloud resources.

Retrieves the collection of TransportOvhCloud resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOvhCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOvhCloudApi apiInstance = new TransportOvhCloudApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportOvhCloudGet> result = apiInstance.apiTransportOvhCloudGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOvhCloudApi#apiTransportOvhCloudGetCollection");
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

[**List&lt;TransportOvhCloudGet&gt;**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOvhCloud collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOvhCloudIdDelete"></a>
# **apiTransportOvhCloudIdDelete**
> apiTransportOvhCloudIdDelete(id)

Removes the TransportOvhCloud resource.

Removes the TransportOvhCloud resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOvhCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOvhCloudApi apiInstance = new TransportOvhCloudApi(defaultClient);
    String id = "id_example"; // String | TransportOvhCloud identifier
    try {
      apiInstance.apiTransportOvhCloudIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOvhCloudApi#apiTransportOvhCloudIdDelete");
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
| **id** | **String**| TransportOvhCloud identifier | |

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
| **204** | TransportOvhCloud resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOvhCloudIdGet"></a>
# **apiTransportOvhCloudIdGet**
> TransportOvhCloudGet apiTransportOvhCloudIdGet(id)

Retrieves a TransportOvhCloud resource.

Retrieves a TransportOvhCloud resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOvhCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOvhCloudApi apiInstance = new TransportOvhCloudApi(defaultClient);
    String id = "id_example"; // String | TransportOvhCloud identifier
    try {
      TransportOvhCloudGet result = apiInstance.apiTransportOvhCloudIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOvhCloudApi#apiTransportOvhCloudIdGet");
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
| **id** | **String**| TransportOvhCloud identifier | |

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOvhCloud resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOvhCloudIdPatch"></a>
# **apiTransportOvhCloudIdPatch**
> TransportOvhCloudGet apiTransportOvhCloudIdPatch(id, transportOvhCloudPatch)

Updates the TransportOvhCloud resource.

Updates the TransportOvhCloud resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOvhCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOvhCloudApi apiInstance = new TransportOvhCloudApi(defaultClient);
    String id = "id_example"; // String | TransportOvhCloud identifier
    TransportOvhCloudPatch transportOvhCloudPatch = new TransportOvhCloudPatch(); // TransportOvhCloudPatch | The updated TransportOvhCloud resource
    try {
      TransportOvhCloudGet result = apiInstance.apiTransportOvhCloudIdPatch(id, transportOvhCloudPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOvhCloudApi#apiTransportOvhCloudIdPatch");
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
| **id** | **String**| TransportOvhCloud identifier | |
| **transportOvhCloudPatch** | [**TransportOvhCloudPatch**](TransportOvhCloudPatch.md)| The updated TransportOvhCloud resource | |

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOvhCloud resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOvhCloudIdPut"></a>
# **apiTransportOvhCloudIdPut**
> TransportOvhCloudGet apiTransportOvhCloudIdPut(id, transportOvhCloudPut)

Replaces the TransportOvhCloud resource.

Replaces the TransportOvhCloud resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOvhCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOvhCloudApi apiInstance = new TransportOvhCloudApi(defaultClient);
    String id = "id_example"; // String | TransportOvhCloud identifier
    TransportOvhCloudPut transportOvhCloudPut = new TransportOvhCloudPut(); // TransportOvhCloudPut | The updated TransportOvhCloud resource
    try {
      TransportOvhCloudGet result = apiInstance.apiTransportOvhCloudIdPut(id, transportOvhCloudPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOvhCloudApi#apiTransportOvhCloudIdPut");
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
| **id** | **String**| TransportOvhCloud identifier | |
| **transportOvhCloudPut** | [**TransportOvhCloudPut**](TransportOvhCloudPut.md)| The updated TransportOvhCloud resource | |

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportOvhCloud resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportOvhCloudPost"></a>
# **apiTransportOvhCloudPost**
> TransportOvhCloudGet apiTransportOvhCloudPost(transportOvhCloudPost)

Creates a TransportOvhCloud resource.

Creates a TransportOvhCloud resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportOvhCloudApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportOvhCloudApi apiInstance = new TransportOvhCloudApi(defaultClient);
    TransportOvhCloudPost transportOvhCloudPost = new TransportOvhCloudPost(); // TransportOvhCloudPost | The new TransportOvhCloud resource
    try {
      TransportOvhCloudGet result = apiInstance.apiTransportOvhCloudPost(transportOvhCloudPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportOvhCloudApi#apiTransportOvhCloudPost");
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
| **transportOvhCloudPost** | [**TransportOvhCloudPost**](TransportOvhCloudPost.md)| The new TransportOvhCloud resource | |

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportOvhCloud resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

