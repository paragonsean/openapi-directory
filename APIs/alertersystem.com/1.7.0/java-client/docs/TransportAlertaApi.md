# TransportAlertaApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportAlertaGetCollection**](TransportAlertaApi.md#apiTransportAlertaGetCollection) | **GET** /api/transport-alerta | Retrieves the collection of TransportAlerta resources. |
| [**apiTransportAlertaIdDelete**](TransportAlertaApi.md#apiTransportAlertaIdDelete) | **DELETE** /api/transport-alerta/{id} | Removes the TransportAlerta resource. |
| [**apiTransportAlertaIdGet**](TransportAlertaApi.md#apiTransportAlertaIdGet) | **GET** /api/transport-alerta/{id} | Retrieves a TransportAlerta resource. |
| [**apiTransportAlertaIdPatch**](TransportAlertaApi.md#apiTransportAlertaIdPatch) | **PATCH** /api/transport-alerta/{id} | Updates the TransportAlerta resource. |
| [**apiTransportAlertaIdPut**](TransportAlertaApi.md#apiTransportAlertaIdPut) | **PUT** /api/transport-alerta/{id} | Replaces the TransportAlerta resource. |
| [**apiTransportAlertaPost**](TransportAlertaApi.md#apiTransportAlertaPost) | **POST** /api/transport-alerta | Creates a TransportAlerta resource. |


<a id="apiTransportAlertaGetCollection"></a>
# **apiTransportAlertaGetCollection**
> List&lt;TransportAlertaGet&gt; apiTransportAlertaGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportAlerta resources.

Retrieves the collection of TransportAlerta resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAlertaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAlertaApi apiInstance = new TransportAlertaApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportAlertaGet> result = apiInstance.apiTransportAlertaGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAlertaApi#apiTransportAlertaGetCollection");
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

[**List&lt;TransportAlertaGet&gt;**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAlerta collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAlertaIdDelete"></a>
# **apiTransportAlertaIdDelete**
> apiTransportAlertaIdDelete(id)

Removes the TransportAlerta resource.

Removes the TransportAlerta resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAlertaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAlertaApi apiInstance = new TransportAlertaApi(defaultClient);
    String id = "id_example"; // String | TransportAlerta identifier
    try {
      apiInstance.apiTransportAlertaIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAlertaApi#apiTransportAlertaIdDelete");
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
| **id** | **String**| TransportAlerta identifier | |

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
| **204** | TransportAlerta resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAlertaIdGet"></a>
# **apiTransportAlertaIdGet**
> TransportAlertaGet apiTransportAlertaIdGet(id)

Retrieves a TransportAlerta resource.

Retrieves a TransportAlerta resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAlertaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAlertaApi apiInstance = new TransportAlertaApi(defaultClient);
    String id = "id_example"; // String | TransportAlerta identifier
    try {
      TransportAlertaGet result = apiInstance.apiTransportAlertaIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAlertaApi#apiTransportAlertaIdGet");
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
| **id** | **String**| TransportAlerta identifier | |

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAlerta resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAlertaIdPatch"></a>
# **apiTransportAlertaIdPatch**
> TransportAlertaGet apiTransportAlertaIdPatch(id, transportAlertaPatch)

Updates the TransportAlerta resource.

Updates the TransportAlerta resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAlertaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAlertaApi apiInstance = new TransportAlertaApi(defaultClient);
    String id = "id_example"; // String | TransportAlerta identifier
    TransportAlertaPatch transportAlertaPatch = new TransportAlertaPatch(); // TransportAlertaPatch | The updated TransportAlerta resource
    try {
      TransportAlertaGet result = apiInstance.apiTransportAlertaIdPatch(id, transportAlertaPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAlertaApi#apiTransportAlertaIdPatch");
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
| **id** | **String**| TransportAlerta identifier | |
| **transportAlertaPatch** | [**TransportAlertaPatch**](TransportAlertaPatch.md)| The updated TransportAlerta resource | |

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAlerta resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAlertaIdPut"></a>
# **apiTransportAlertaIdPut**
> TransportAlertaGet apiTransportAlertaIdPut(id, transportAlertaPut)

Replaces the TransportAlerta resource.

Replaces the TransportAlerta resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAlertaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAlertaApi apiInstance = new TransportAlertaApi(defaultClient);
    String id = "id_example"; // String | TransportAlerta identifier
    TransportAlertaPut transportAlertaPut = new TransportAlertaPut(); // TransportAlertaPut | The updated TransportAlerta resource
    try {
      TransportAlertaGet result = apiInstance.apiTransportAlertaIdPut(id, transportAlertaPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAlertaApi#apiTransportAlertaIdPut");
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
| **id** | **String**| TransportAlerta identifier | |
| **transportAlertaPut** | [**TransportAlertaPut**](TransportAlertaPut.md)| The updated TransportAlerta resource | |

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportAlerta resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportAlertaPost"></a>
# **apiTransportAlertaPost**
> TransportAlertaGet apiTransportAlertaPost(transportAlertaPost)

Creates a TransportAlerta resource.

Creates a TransportAlerta resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportAlertaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportAlertaApi apiInstance = new TransportAlertaApi(defaultClient);
    TransportAlertaPost transportAlertaPost = new TransportAlertaPost(); // TransportAlertaPost | The new TransportAlerta resource
    try {
      TransportAlertaGet result = apiInstance.apiTransportAlertaPost(transportAlertaPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportAlertaApi#apiTransportAlertaPost");
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
| **transportAlertaPost** | [**TransportAlertaPost**](TransportAlertaPost.md)| The new TransportAlerta resource | |

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportAlerta resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

