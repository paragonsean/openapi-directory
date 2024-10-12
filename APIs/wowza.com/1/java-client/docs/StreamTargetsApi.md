# StreamTargetsApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addStreamTarget**](StreamTargetsApi.md#addStreamTarget) | **POST** /stream_targets/add | Deprecated operation |
| [**createStreamTarget**](StreamTargetsApi.md#createStreamTarget) | **POST** /stream_targets | Create a stream target |
| [**createStreamTargetGeoblock**](StreamTargetsApi.md#createStreamTargetGeoblock) | **POST** /stream_targets/{stream_target_id}/geoblock | Create geo-blocking for a stream target |
| [**createStreamTargetProperty**](StreamTargetsApi.md#createStreamTargetProperty) | **POST** /stream_targets/{stream_target_id}/properties | Create a property for a stream target |
| [**createStreamTargetTokenAuth**](StreamTargetsApi.md#createStreamTargetTokenAuth) | **POST** /stream_targets/{stream_target_id}/token_auth | Create token authorization for a stream target |
| [**deleteStreamTarget**](StreamTargetsApi.md#deleteStreamTarget) | **DELETE** /stream_targets/{id} | Delete a stream target |
| [**deleteStreamTargetProperty**](StreamTargetsApi.md#deleteStreamTargetProperty) | **DELETE** /stream_targets/{stream_target_id}/properties/{id} | Delete a stream target property |
| [**listStreamTargetProperties**](StreamTargetsApi.md#listStreamTargetProperties) | **GET** /stream_targets/{stream_target_id}/properties | Fetch all properties of a stream target |
| [**listStreamTargets**](StreamTargetsApi.md#listStreamTargets) | **GET** /stream_targets | Fetch all stream targets |
| [**regenerateConnectionCodeStreamTarget**](StreamTargetsApi.md#regenerateConnectionCodeStreamTarget) | **PUT** /stream_targets/{id}/regenerate_connection_code | Regenerate the connection code for a stream target |
| [**showStreamTarget**](StreamTargetsApi.md#showStreamTarget) | **GET** /stream_targets/{id} | Fetch a stream target |
| [**showStreamTargetGeoblock**](StreamTargetsApi.md#showStreamTargetGeoblock) | **GET** /stream_targets/{stream_target_id}/geoblock | Fetch geo-blocking for a stream target |
| [**showStreamTargetMetricsCurrent**](StreamTargetsApi.md#showStreamTargetMetricsCurrent) | **GET** /stream_targets/{id}/metrics/current | Fetch current health metrics for an active Wowza ultra low latency stream target |
| [**showStreamTargetMetricsHistoric**](StreamTargetsApi.md#showStreamTargetMetricsHistoric) | **GET** /stream_targets/{id}/metrics/historic | Fetch historic health metrics for a Wowza ultra low latency stream target |
| [**showStreamTargetProperty**](StreamTargetsApi.md#showStreamTargetProperty) | **GET** /stream_targets/{stream_target_id}/properties/{id} | Fetch a property of a stream target |
| [**showStreamTargetTokenAuth**](StreamTargetsApi.md#showStreamTargetTokenAuth) | **GET** /stream_targets/{stream_target_id}/token_auth | Fetch token authorization for a stream target |
| [**updateStreamTarget**](StreamTargetsApi.md#updateStreamTarget) | **PATCH** /stream_targets/{id} | Update a stream target |
| [**updateStreamTargetGeoblock**](StreamTargetsApi.md#updateStreamTargetGeoblock) | **PATCH** /stream_targets/{stream_target_id}/geoblock | Update geo-blocking for a stream target |
| [**updateStreamTargetTokenAuth**](StreamTargetsApi.md#updateStreamTargetTokenAuth) | **PATCH** /stream_targets/{stream_target_id}/token_auth | Update token authorization for a stream target |


<a id="addStreamTarget"></a>
# **addStreamTarget**
> CreateStreamTarget200Response addStreamTarget(streamTarget)

Deprecated operation

POST /stream_targets/add/ is deprecated. To add a stream target, use POST /stream_targets instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    WowzaStreamTargetInput streamTarget = new WowzaStreamTargetInput(); // WowzaStreamTargetInput | Provide the details of the stream target to add in the body of the request.
    try {
      CreateStreamTarget200Response result = apiInstance.addStreamTarget(streamTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#addStreamTarget");
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
| **streamTarget** | [**WowzaStreamTargetInput**](WowzaStreamTargetInput.md)| Provide the details of the stream target to add in the body of the request. | |

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="createStreamTarget"></a>
# **createStreamTarget**
> CreateStreamTarget200Response createStreamTarget(streamTarget)

Create a stream target

This operation creates a stream target. There are three types of targets that you can create: &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; for an an external, third-party destination; &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; for a Wowza CDN target; or &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; for an ultra low latency Wowza CDN target. The availability of many parameters depends on the type of target you create.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    StreamTargetCreateInput streamTarget = new StreamTargetCreateInput(); // StreamTargetCreateInput | Provide the details of the stream target to create in the body of the request.
    try {
      CreateStreamTarget200Response result = apiInstance.createStreamTarget(streamTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#createStreamTarget");
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
| **streamTarget** | [**StreamTargetCreateInput**](StreamTargetCreateInput.md)| Provide the details of the stream target to create in the body of the request. | |

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="createStreamTargetGeoblock"></a>
# **createStreamTargetGeoblock**
> ShowStreamTargetGeoblock200Response createStreamTargetGeoblock(streamTargetId, geoblock)

Create geo-blocking for a stream target

This operation allows you to block or whitelist viewing of a stream target by geographic location. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked. For more information see the technical article [How to geo-block stream targets by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-geo-block-stream-targets-by-using-the-wowza-streaming-cloud-rest-api).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    GeoblockCreateInput geoblock = new GeoblockCreateInput(); // GeoblockCreateInput | Provide the details of the geo-blocking to create in the body of the request.
    try {
      ShowStreamTargetGeoblock200Response result = apiInstance.createStreamTargetGeoblock(streamTargetId, geoblock);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#createStreamTargetGeoblock");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **geoblock** | [**GeoblockCreateInput**](GeoblockCreateInput.md)| Provide the details of the geo-blocking to create in the body of the request. | |

### Return type

[**ShowStreamTargetGeoblock200Response**](ShowStreamTargetGeoblock200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="createStreamTargetProperty"></a>
# **createStreamTargetProperty**
> CreateStreamTargetProperty200Response createStreamTargetProperty(streamTargetId, property)

Create a property for a stream target

This operation creates a property for a stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    StreamTargetPropertyCreateInput property = new StreamTargetPropertyCreateInput(); // StreamTargetPropertyCreateInput | Provide the details of the property to create in the body of the request.
    try {
      CreateStreamTargetProperty200Response result = apiInstance.createStreamTargetProperty(streamTargetId, property);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#createStreamTargetProperty");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **property** | [**StreamTargetPropertyCreateInput**](StreamTargetPropertyCreateInput.md)| Provide the details of the property to create in the body of the request. | |

### Return type

[**CreateStreamTargetProperty200Response**](CreateStreamTargetProperty200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="createStreamTargetTokenAuth"></a>
# **createStreamTargetTokenAuth**
> ShowStreamTargetTokenAuth200Response createStreamTargetTokenAuth(streamTargetId, tokenAuth)

Create token authorization for a stream target

This operation creates token authorization for a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization. For more information see the technical article [How to protect stream targets with token authorization by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-protect-streams-with-token-authorization-by-using-the-wowza-streaming-cloud-rest-api).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    TokenAuthCreateInput tokenAuth = new TokenAuthCreateInput(); // TokenAuthCreateInput | Provide the details of the token authorization to create in the body of the request.
    try {
      ShowStreamTargetTokenAuth200Response result = apiInstance.createStreamTargetTokenAuth(streamTargetId, tokenAuth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#createStreamTargetTokenAuth");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **tokenAuth** | [**TokenAuthCreateInput**](TokenAuthCreateInput.md)| Provide the details of the token authorization to create in the body of the request. | |

### Return type

[**ShowStreamTargetTokenAuth200Response**](ShowStreamTargetTokenAuth200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteStreamTarget"></a>
# **deleteStreamTarget**
> deleteStreamTarget(id)

Delete a stream target

This operation deletes a stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      apiInstance.deleteStreamTarget(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#deleteStreamTarget");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteStreamTargetProperty"></a>
# **deleteStreamTargetProperty**
> deleteStreamTargetProperty(streamTargetId, id)

Delete a stream target property

This operation removes a property from a stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    String id = "id_example"; // String | The unique string that identifies the stream target property. The string contains the <em>section</em> and the <em>key</em>, connected by a dash. For example, <strong>hls-chunkSize</strong>.
    try {
      apiInstance.deleteStreamTargetProperty(streamTargetId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#deleteStreamTargetProperty");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **id** | **String**| The unique string that identifies the stream target property. The string contains the &lt;em&gt;section&lt;/em&gt; and the &lt;em&gt;key&lt;/em&gt;, connected by a dash. For example, &lt;strong&gt;hls-chunkSize&lt;/strong&gt;. | |

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="listStreamTargetProperties"></a>
# **listStreamTargetProperties**
> StreamTargetProperties listStreamTargetProperties(streamTargetId)

Fetch all properties of a stream target

This operation shows the details of all of the properties assigned to a specific stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      StreamTargetProperties result = apiInstance.listStreamTargetProperties(streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#listStreamTargetProperties");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**StreamTargetProperties**](StreamTargetProperties.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="listStreamTargets"></a>
# **listStreamTargets**
> StreamTargets listStreamTargets(page, perPage)

Fetch all stream targets

This operation lists the details of all of your stream targets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    Integer page = 56; // Integer | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
    Integer perPage = 56; // Integer | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
    try {
      StreamTargets result = apiInstance.listStreamTargets(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#listStreamTargets");
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
| **page** | **Integer**| Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results. | [optional] |
| **perPage** | **Integer**| For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;. | [optional] |

### Return type

[**StreamTargets**](StreamTargets.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="regenerateConnectionCodeStreamTarget"></a>
# **regenerateConnectionCodeStreamTarget**
> RegenerateConnectionCodeStreamTarget200Response regenerateConnectionCodeStreamTarget(id)

Regenerate the connection code for a stream target

This operation regenerates the connection code of a stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      RegenerateConnectionCodeStreamTarget200Response result = apiInstance.regenerateConnectionCodeStreamTarget(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#regenerateConnectionCodeStreamTarget");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**RegenerateConnectionCodeStreamTarget200Response**](RegenerateConnectionCodeStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="showStreamTarget"></a>
# **showStreamTarget**
> CreateStreamTarget200Response showStreamTarget(id)

Fetch a stream target

This operation shows details of a specific stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      CreateStreamTarget200Response result = apiInstance.showStreamTarget(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#showStreamTarget");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |

<a id="showStreamTargetGeoblock"></a>
# **showStreamTargetGeoblock**
> ShowStreamTargetGeoblock200Response showStreamTargetGeoblock(streamTargetId)

Fetch geo-blocking for a stream target

This operation shows the details of geo-blocking applied to a specific stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      ShowStreamTargetGeoblock200Response result = apiInstance.showStreamTargetGeoblock(streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#showStreamTargetGeoblock");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**ShowStreamTargetGeoblock200Response**](ShowStreamTargetGeoblock200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |

<a id="showStreamTargetMetricsCurrent"></a>
# **showStreamTargetMetricsCurrent**
> ShowStreamTargetMetricsCurrent200Response showStreamTargetMetricsCurrent(id)

Fetch current health metrics for an active Wowza ultra low latency stream target

This operation returns a snapshot of the current connection and throughput details for an active target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. The interval for current metrics is 30 seconds from the moment of the query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      ShowStreamTargetMetricsCurrent200Response result = apiInstance.showStreamTargetMetricsCurrent(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#showStreamTargetMetricsCurrent");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**ShowStreamTargetMetricsCurrent200Response**](ShowStreamTargetMetricsCurrent200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |

<a id="showStreamTargetMetricsHistoric"></a>
# **showStreamTargetMetricsHistoric**
> ShowStreamTargetMetricsHistoric200Response showStreamTargetMetricsHistoric(id, from, to, interval)

Fetch historic health metrics for a Wowza ultra low latency stream target

This operation shows historic connection and throughput details for target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
    String from = "from_example"; // String | The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
    String to = "to_example"; // String | The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
    String interval = "second"; // String | The length of time for a block of metrics. The default is **10m** (10 minutes).
    try {
      ShowStreamTargetMetricsHistoric200Response result = apiInstance.showStreamTargetMetricsHistoric(id, from, to, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#showStreamTargetMetricsHistoric");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **from** | **String**| The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] |
| **to** | **String**| The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] |
| **interval** | **String**| The length of time for a block of metrics. The default is **10m** (10 minutes). | [optional] [enum: second, minute, hour, day, month, #s, #m, #h, #d] |

### Return type

[**ShowStreamTargetMetricsHistoric200Response**](ShowStreamTargetMetricsHistoric200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |

<a id="showStreamTargetProperty"></a>
# **showStreamTargetProperty**
> CreateStreamTargetProperty200Response showStreamTargetProperty(streamTargetId, id)

Fetch a property of a stream target

This operation shows the details of a specific property assigned to a specific stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    String id = "id_example"; // String | The unique string that identifies the stream target property. The string contains the <em>section</em> and the <em>key</em>, connected by a dash. For example, <strong>hls-chunkSize</strong>.
    try {
      CreateStreamTargetProperty200Response result = apiInstance.showStreamTargetProperty(streamTargetId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#showStreamTargetProperty");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **id** | **String**| The unique string that identifies the stream target property. The string contains the &lt;em&gt;section&lt;/em&gt; and the &lt;em&gt;key&lt;/em&gt;, connected by a dash. For example, &lt;strong&gt;hls-chunkSize&lt;/strong&gt;. | |

### Return type

[**CreateStreamTargetProperty200Response**](CreateStreamTargetProperty200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |

<a id="showStreamTargetTokenAuth"></a>
# **showStreamTargetTokenAuth**
> ShowStreamTargetTokenAuth200Response showStreamTargetTokenAuth(streamTargetId)

Fetch token authorization for a stream target

This operation shows the details of the token authorization applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      ShowStreamTargetTokenAuth200Response result = apiInstance.showStreamTargetTokenAuth(streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#showStreamTargetTokenAuth");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**ShowStreamTargetTokenAuth200Response**](ShowStreamTargetTokenAuth200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |

<a id="updateStreamTarget"></a>
# **updateStreamTarget**
> CreateStreamTarget200Response updateStreamTarget(id, streamTarget)

Update a stream target

This operation updates a stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
    StreamTargetUpdateInput streamTarget = new StreamTargetUpdateInput(); // StreamTargetUpdateInput | Provide the details of the stream target to update in the body of the request.
    try {
      CreateStreamTarget200Response result = apiInstance.updateStreamTarget(id, streamTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#updateStreamTarget");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **streamTarget** | [**StreamTargetUpdateInput**](StreamTargetUpdateInput.md)| Provide the details of the stream target to update in the body of the request. | |

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="updateStreamTargetGeoblock"></a>
# **updateStreamTargetGeoblock**
> ShowStreamTargetGeoblock200Response updateStreamTargetGeoblock(streamTargetId, geoblock)

Update geo-blocking for a stream target

This operation updates the geo-blocking applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    GeoblockUpdateInput geoblock = new GeoblockUpdateInput(); // GeoblockUpdateInput | Provide the details of the geo-blocking to update in the body of the request.
    try {
      ShowStreamTargetGeoblock200Response result = apiInstance.updateStreamTargetGeoblock(streamTargetId, geoblock);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#updateStreamTargetGeoblock");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **geoblock** | [**GeoblockUpdateInput**](GeoblockUpdateInput.md)| Provide the details of the geo-blocking to update in the body of the request. | |

### Return type

[**ShowStreamTargetGeoblock200Response**](ShowStreamTargetGeoblock200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="updateStreamTargetTokenAuth"></a>
# **updateStreamTargetTokenAuth**
> ShowStreamTargetTokenAuth200Response updateStreamTargetTokenAuth(streamTargetId, tokenAuth)

Update token authorization for a stream target

This operation updates the token authorization applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamTargetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.cloud.wowza.com/api/v1");
    
    // Configure API key authorization: wsc-api-key
    ApiKeyAuth wsc-api-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-api-key");
    wsc-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: wsc-access-key
    ApiKeyAuth wsc-access-key = (ApiKeyAuth) defaultClient.getAuthentication("wsc-access-key");
    wsc-access-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //wsc-access-key.setApiKeyPrefix("Token");

    StreamTargetsApi apiInstance = new StreamTargetsApi(defaultClient);
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    TokenAuthUpdateInput tokenAuth = new TokenAuthUpdateInput(); // TokenAuthUpdateInput | Provide the details of the token authorization to update in the body of the request.
    try {
      ShowStreamTargetTokenAuth200Response result = apiInstance.updateStreamTargetTokenAuth(streamTargetId, tokenAuth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamTargetsApi#updateStreamTargetTokenAuth");
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
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **tokenAuth** | [**TokenAuthUpdateInput**](TokenAuthUpdateInput.md)| Provide the details of the token authorization to update in the body of the request. | |

### Return type

[**ShowStreamTargetTokenAuth200Response**](ShowStreamTargetTokenAuth200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **410** | Gone |  -  |
| **422** | Unprocessable Entity |  -  |

