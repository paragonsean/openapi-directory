# TransportFortySixElksApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportFortySixElksGetCollection**](TransportFortySixElksApi.md#apiTransportFortySixElksGetCollection) | **GET** /api/transport-forty-six-elks | Retrieves the collection of TransportFortySixElks resources. |
| [**apiTransportFortySixElksIdDelete**](TransportFortySixElksApi.md#apiTransportFortySixElksIdDelete) | **DELETE** /api/transport-forty-six-elks/{id} | Removes the TransportFortySixElks resource. |
| [**apiTransportFortySixElksIdGet**](TransportFortySixElksApi.md#apiTransportFortySixElksIdGet) | **GET** /api/transport-forty-six-elks/{id} | Retrieves a TransportFortySixElks resource. |
| [**apiTransportFortySixElksIdPatch**](TransportFortySixElksApi.md#apiTransportFortySixElksIdPatch) | **PATCH** /api/transport-forty-six-elks/{id} | Updates the TransportFortySixElks resource. |
| [**apiTransportFortySixElksIdPut**](TransportFortySixElksApi.md#apiTransportFortySixElksIdPut) | **PUT** /api/transport-forty-six-elks/{id} | Replaces the TransportFortySixElks resource. |
| [**apiTransportFortySixElksPost**](TransportFortySixElksApi.md#apiTransportFortySixElksPost) | **POST** /api/transport-forty-six-elks | Creates a TransportFortySixElks resource. |


<a id="apiTransportFortySixElksGetCollection"></a>
# **apiTransportFortySixElksGetCollection**
> List&lt;TransportFortySixElksGet&gt; apiTransportFortySixElksGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportFortySixElks resources.

Retrieves the collection of TransportFortySixElks resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFortySixElksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFortySixElksApi apiInstance = new TransportFortySixElksApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportFortySixElksGet> result = apiInstance.apiTransportFortySixElksGetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFortySixElksApi#apiTransportFortySixElksGetCollection");
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

[**List&lt;TransportFortySixElksGet&gt;**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFortySixElks collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFortySixElksIdDelete"></a>
# **apiTransportFortySixElksIdDelete**
> apiTransportFortySixElksIdDelete(id)

Removes the TransportFortySixElks resource.

Removes the TransportFortySixElks resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFortySixElksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFortySixElksApi apiInstance = new TransportFortySixElksApi(defaultClient);
    String id = "id_example"; // String | TransportFortySixElks identifier
    try {
      apiInstance.apiTransportFortySixElksIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFortySixElksApi#apiTransportFortySixElksIdDelete");
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
| **id** | **String**| TransportFortySixElks identifier | |

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
| **204** | TransportFortySixElks resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFortySixElksIdGet"></a>
# **apiTransportFortySixElksIdGet**
> TransportFortySixElksGet apiTransportFortySixElksIdGet(id)

Retrieves a TransportFortySixElks resource.

Retrieves a TransportFortySixElks resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFortySixElksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFortySixElksApi apiInstance = new TransportFortySixElksApi(defaultClient);
    String id = "id_example"; // String | TransportFortySixElks identifier
    try {
      TransportFortySixElksGet result = apiInstance.apiTransportFortySixElksIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFortySixElksApi#apiTransportFortySixElksIdGet");
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
| **id** | **String**| TransportFortySixElks identifier | |

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFortySixElks resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFortySixElksIdPatch"></a>
# **apiTransportFortySixElksIdPatch**
> TransportFortySixElksGet apiTransportFortySixElksIdPatch(id, transportFortySixElksPatch)

Updates the TransportFortySixElks resource.

Updates the TransportFortySixElks resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFortySixElksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFortySixElksApi apiInstance = new TransportFortySixElksApi(defaultClient);
    String id = "id_example"; // String | TransportFortySixElks identifier
    TransportFortySixElksPatch transportFortySixElksPatch = new TransportFortySixElksPatch(); // TransportFortySixElksPatch | The updated TransportFortySixElks resource
    try {
      TransportFortySixElksGet result = apiInstance.apiTransportFortySixElksIdPatch(id, transportFortySixElksPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFortySixElksApi#apiTransportFortySixElksIdPatch");
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
| **id** | **String**| TransportFortySixElks identifier | |
| **transportFortySixElksPatch** | [**TransportFortySixElksPatch**](TransportFortySixElksPatch.md)| The updated TransportFortySixElks resource | |

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFortySixElks resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFortySixElksIdPut"></a>
# **apiTransportFortySixElksIdPut**
> TransportFortySixElksGet apiTransportFortySixElksIdPut(id, transportFortySixElksPut)

Replaces the TransportFortySixElks resource.

Replaces the TransportFortySixElks resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFortySixElksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFortySixElksApi apiInstance = new TransportFortySixElksApi(defaultClient);
    String id = "id_example"; // String | TransportFortySixElks identifier
    TransportFortySixElksPut transportFortySixElksPut = new TransportFortySixElksPut(); // TransportFortySixElksPut | The updated TransportFortySixElks resource
    try {
      TransportFortySixElksGet result = apiInstance.apiTransportFortySixElksIdPut(id, transportFortySixElksPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFortySixElksApi#apiTransportFortySixElksIdPut");
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
| **id** | **String**| TransportFortySixElks identifier | |
| **transportFortySixElksPut** | [**TransportFortySixElksPut**](TransportFortySixElksPut.md)| The updated TransportFortySixElks resource | |

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportFortySixElks resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportFortySixElksPost"></a>
# **apiTransportFortySixElksPost**
> TransportFortySixElksGet apiTransportFortySixElksPost(transportFortySixElksPost)

Creates a TransportFortySixElks resource.

Creates a TransportFortySixElks resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportFortySixElksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportFortySixElksApi apiInstance = new TransportFortySixElksApi(defaultClient);
    TransportFortySixElksPost transportFortySixElksPost = new TransportFortySixElksPost(); // TransportFortySixElksPost | The new TransportFortySixElks resource
    try {
      TransportFortySixElksGet result = apiInstance.apiTransportFortySixElksPost(transportFortySixElksPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportFortySixElksApi#apiTransportFortySixElksPost");
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
| **transportFortySixElksPost** | [**TransportFortySixElksPost**](TransportFortySixElksPost.md)| The new TransportFortySixElks resource | |

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportFortySixElks resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

