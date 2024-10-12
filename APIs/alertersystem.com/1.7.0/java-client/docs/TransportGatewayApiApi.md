# TransportGatewayApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportGatewayApiGetCollection**](TransportGatewayApiApi.md#apiTransportGatewayApiGetCollection) | **GET** /api/transport-gateway-api | Retrieves the collection of TransportGatewayApi resources. |
| [**apiTransportGatewayApiIdDelete**](TransportGatewayApiApi.md#apiTransportGatewayApiIdDelete) | **DELETE** /api/transport-gateway-api/{id} | Removes the TransportGatewayApi resource. |
| [**apiTransportGatewayApiIdGet**](TransportGatewayApiApi.md#apiTransportGatewayApiIdGet) | **GET** /api/transport-gateway-api/{id} | Retrieves a TransportGatewayApi resource. |
| [**apiTransportGatewayApiIdPatch**](TransportGatewayApiApi.md#apiTransportGatewayApiIdPatch) | **PATCH** /api/transport-gateway-api/{id} | Updates the TransportGatewayApi resource. |
| [**apiTransportGatewayApiIdPut**](TransportGatewayApiApi.md#apiTransportGatewayApiIdPut) | **PUT** /api/transport-gateway-api/{id} | Replaces the TransportGatewayApi resource. |
| [**apiTransportGatewayApiPost**](TransportGatewayApiApi.md#apiTransportGatewayApiPost) | **POST** /api/transport-gateway-api | Creates a TransportGatewayApi resource. |


<a id="apiTransportGatewayApiGetCollection"></a>
# **apiTransportGatewayApiGetCollection**
> List&lt;TransportGatewayApiGet&gt; apiTransportGatewayApiGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportGatewayApi resources.

Retrieves the collection of TransportGatewayApi resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGatewayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGatewayApiApi apiInstance = new TransportGatewayApiApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportGatewayApiGet> result = apiInstance.apiTransportGatewayApiGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGatewayApiApi#apiTransportGatewayApiGetCollection");
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

[**List&lt;TransportGatewayApiGet&gt;**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGatewayApi collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGatewayApiIdDelete"></a>
# **apiTransportGatewayApiIdDelete**
> apiTransportGatewayApiIdDelete(id)

Removes the TransportGatewayApi resource.

Removes the TransportGatewayApi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGatewayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGatewayApiApi apiInstance = new TransportGatewayApiApi(defaultClient);
    String id = "id_example"; // String | TransportGatewayApi identifier
    try {
      apiInstance.apiTransportGatewayApiIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGatewayApiApi#apiTransportGatewayApiIdDelete");
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
| **id** | **String**| TransportGatewayApi identifier | |

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
| **204** | TransportGatewayApi resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGatewayApiIdGet"></a>
# **apiTransportGatewayApiIdGet**
> TransportGatewayApiGet apiTransportGatewayApiIdGet(id)

Retrieves a TransportGatewayApi resource.

Retrieves a TransportGatewayApi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGatewayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGatewayApiApi apiInstance = new TransportGatewayApiApi(defaultClient);
    String id = "id_example"; // String | TransportGatewayApi identifier
    try {
      TransportGatewayApiGet result = apiInstance.apiTransportGatewayApiIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGatewayApiApi#apiTransportGatewayApiIdGet");
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
| **id** | **String**| TransportGatewayApi identifier | |

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGatewayApi resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGatewayApiIdPatch"></a>
# **apiTransportGatewayApiIdPatch**
> TransportGatewayApiGet apiTransportGatewayApiIdPatch(id, transportGatewayApiPatch)

Updates the TransportGatewayApi resource.

Updates the TransportGatewayApi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGatewayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGatewayApiApi apiInstance = new TransportGatewayApiApi(defaultClient);
    String id = "id_example"; // String | TransportGatewayApi identifier
    TransportGatewayApiPatch transportGatewayApiPatch = new TransportGatewayApiPatch(); // TransportGatewayApiPatch | The updated TransportGatewayApi resource
    try {
      TransportGatewayApiGet result = apiInstance.apiTransportGatewayApiIdPatch(id, transportGatewayApiPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGatewayApiApi#apiTransportGatewayApiIdPatch");
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
| **id** | **String**| TransportGatewayApi identifier | |
| **transportGatewayApiPatch** | [**TransportGatewayApiPatch**](TransportGatewayApiPatch.md)| The updated TransportGatewayApi resource | |

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGatewayApi resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGatewayApiIdPut"></a>
# **apiTransportGatewayApiIdPut**
> TransportGatewayApiGet apiTransportGatewayApiIdPut(id, transportGatewayApiPut)

Replaces the TransportGatewayApi resource.

Replaces the TransportGatewayApi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGatewayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGatewayApiApi apiInstance = new TransportGatewayApiApi(defaultClient);
    String id = "id_example"; // String | TransportGatewayApi identifier
    TransportGatewayApiPut transportGatewayApiPut = new TransportGatewayApiPut(); // TransportGatewayApiPut | The updated TransportGatewayApi resource
    try {
      TransportGatewayApiGet result = apiInstance.apiTransportGatewayApiIdPut(id, transportGatewayApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGatewayApiApi#apiTransportGatewayApiIdPut");
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
| **id** | **String**| TransportGatewayApi identifier | |
| **transportGatewayApiPut** | [**TransportGatewayApiPut**](TransportGatewayApiPut.md)| The updated TransportGatewayApi resource | |

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportGatewayApi resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportGatewayApiPost"></a>
# **apiTransportGatewayApiPost**
> TransportGatewayApiGet apiTransportGatewayApiPost(transportGatewayApiPost)

Creates a TransportGatewayApi resource.

Creates a TransportGatewayApi resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportGatewayApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportGatewayApiApi apiInstance = new TransportGatewayApiApi(defaultClient);
    TransportGatewayApiPost transportGatewayApiPost = new TransportGatewayApiPost(); // TransportGatewayApiPost | The new TransportGatewayApi resource
    try {
      TransportGatewayApiGet result = apiInstance.apiTransportGatewayApiPost(transportGatewayApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportGatewayApiApi#apiTransportGatewayApiPost");
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
| **transportGatewayApiPost** | [**TransportGatewayApiPost**](TransportGatewayApiPost.md)| The new TransportGatewayApi resource | |

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportGatewayApi resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

