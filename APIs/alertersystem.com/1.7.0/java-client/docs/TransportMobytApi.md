# TransportMobytApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportMobytGetCollection**](TransportMobytApi.md#apiTransportMobytGetCollection) | **GET** /api/transport-mobyt | Retrieves the collection of TransportMobyt resources. |
| [**apiTransportMobytIdDelete**](TransportMobytApi.md#apiTransportMobytIdDelete) | **DELETE** /api/transport-mobyt/{id} | Removes the TransportMobyt resource. |
| [**apiTransportMobytIdGet**](TransportMobytApi.md#apiTransportMobytIdGet) | **GET** /api/transport-mobyt/{id} | Retrieves a TransportMobyt resource. |
| [**apiTransportMobytIdPatch**](TransportMobytApi.md#apiTransportMobytIdPatch) | **PATCH** /api/transport-mobyt/{id} | Updates the TransportMobyt resource. |
| [**apiTransportMobytIdPut**](TransportMobytApi.md#apiTransportMobytIdPut) | **PUT** /api/transport-mobyt/{id} | Replaces the TransportMobyt resource. |
| [**apiTransportMobytPost**](TransportMobytApi.md#apiTransportMobytPost) | **POST** /api/transport-mobyt | Creates a TransportMobyt resource. |


<a id="apiTransportMobytGetCollection"></a>
# **apiTransportMobytGetCollection**
> List&lt;TransportMobytGet&gt; apiTransportMobytGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportMobyt resources.

Retrieves the collection of TransportMobyt resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMobytApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMobytApi apiInstance = new TransportMobytApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportMobytGet> result = apiInstance.apiTransportMobytGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMobytApi#apiTransportMobytGetCollection");
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

[**List&lt;TransportMobytGet&gt;**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMobyt collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMobytIdDelete"></a>
# **apiTransportMobytIdDelete**
> apiTransportMobytIdDelete(id)

Removes the TransportMobyt resource.

Removes the TransportMobyt resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMobytApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMobytApi apiInstance = new TransportMobytApi(defaultClient);
    String id = "id_example"; // String | TransportMobyt identifier
    try {
      apiInstance.apiTransportMobytIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMobytApi#apiTransportMobytIdDelete");
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
| **id** | **String**| TransportMobyt identifier | |

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
| **204** | TransportMobyt resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMobytIdGet"></a>
# **apiTransportMobytIdGet**
> TransportMobytGet apiTransportMobytIdGet(id)

Retrieves a TransportMobyt resource.

Retrieves a TransportMobyt resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMobytApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMobytApi apiInstance = new TransportMobytApi(defaultClient);
    String id = "id_example"; // String | TransportMobyt identifier
    try {
      TransportMobytGet result = apiInstance.apiTransportMobytIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMobytApi#apiTransportMobytIdGet");
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
| **id** | **String**| TransportMobyt identifier | |

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMobyt resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMobytIdPatch"></a>
# **apiTransportMobytIdPatch**
> TransportMobytGet apiTransportMobytIdPatch(id, transportMobytPatch)

Updates the TransportMobyt resource.

Updates the TransportMobyt resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMobytApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMobytApi apiInstance = new TransportMobytApi(defaultClient);
    String id = "id_example"; // String | TransportMobyt identifier
    TransportMobytPatch transportMobytPatch = new TransportMobytPatch(); // TransportMobytPatch | The updated TransportMobyt resource
    try {
      TransportMobytGet result = apiInstance.apiTransportMobytIdPatch(id, transportMobytPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMobytApi#apiTransportMobytIdPatch");
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
| **id** | **String**| TransportMobyt identifier | |
| **transportMobytPatch** | [**TransportMobytPatch**](TransportMobytPatch.md)| The updated TransportMobyt resource | |

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMobyt resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMobytIdPut"></a>
# **apiTransportMobytIdPut**
> TransportMobytGet apiTransportMobytIdPut(id, transportMobytPut)

Replaces the TransportMobyt resource.

Replaces the TransportMobyt resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMobytApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMobytApi apiInstance = new TransportMobytApi(defaultClient);
    String id = "id_example"; // String | TransportMobyt identifier
    TransportMobytPut transportMobytPut = new TransportMobytPut(); // TransportMobytPut | The updated TransportMobyt resource
    try {
      TransportMobytGet result = apiInstance.apiTransportMobytIdPut(id, transportMobytPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMobytApi#apiTransportMobytIdPut");
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
| **id** | **String**| TransportMobyt identifier | |
| **transportMobytPut** | [**TransportMobytPut**](TransportMobytPut.md)| The updated TransportMobyt resource | |

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportMobyt resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportMobytPost"></a>
# **apiTransportMobytPost**
> TransportMobytGet apiTransportMobytPost(transportMobytPost)

Creates a TransportMobyt resource.

Creates a TransportMobyt resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportMobytApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportMobytApi apiInstance = new TransportMobytApi(defaultClient);
    TransportMobytPost transportMobytPost = new TransportMobytPost(); // TransportMobytPost | The new TransportMobyt resource
    try {
      TransportMobytGet result = apiInstance.apiTransportMobytPost(transportMobytPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportMobytApi#apiTransportMobytPost");
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
| **transportMobytPost** | [**TransportMobytPost**](TransportMobytPost.md)| The new TransportMobyt resource | |

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportMobyt resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

