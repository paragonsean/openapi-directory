# StreamSourcesApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addStreamSource**](StreamSourcesApi.md#addStreamSource) | **POST** /stream_sources/add | Deprecated operation |
| [**createStreamSource**](StreamSourcesApi.md#createStreamSource) | **POST** /stream_sources | Add a stream source |
| [**deleteStreamSource**](StreamSourcesApi.md#deleteStreamSource) | **DELETE** /stream_sources/{id} | Delete a stream source |
| [**listStreamSources**](StreamSourcesApi.md#listStreamSources) | **GET** /stream_sources | Fetch all stream sources |
| [**showStreamSource**](StreamSourcesApi.md#showStreamSource) | **GET** /stream_sources/{id} | Fetch a stream source |
| [**updateStreamSource**](StreamSourcesApi.md#updateStreamSource) | **PATCH** /stream_sources/{id} | Update a stream source |


<a id="addStreamSource"></a>
# **addStreamSource**
> CreateStreamSource200Response addStreamSource(streamSource)

Deprecated operation

POST /stream_sources/add/ is deprecated. To add a stream source, use POST /stream_sources instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSourcesApi;

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

    StreamSourcesApi apiInstance = new StreamSourcesApi(defaultClient);
    StreamSourceCreateInput streamSource = new StreamSourceCreateInput(); // StreamSourceCreateInput | Provide the details of the stream source to add in the body of the request.
    try {
      CreateStreamSource200Response result = apiInstance.addStreamSource(streamSource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSourcesApi#addStreamSource");
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
| **streamSource** | [**StreamSourceCreateInput**](StreamSourceCreateInput.md)| Provide the details of the stream source to add in the body of the request. | |

### Return type

[**CreateStreamSource200Response**](CreateStreamSource200Response.md)

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

<a id="createStreamSource"></a>
# **createStreamSource**
> CreateStreamSource200Response createStreamSource(streamSource)

Add a stream source

This operation adds a stream source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSourcesApi;

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

    StreamSourcesApi apiInstance = new StreamSourcesApi(defaultClient);
    StreamSourceCreateInput streamSource = new StreamSourceCreateInput(); // StreamSourceCreateInput | Provide the details of the stream source to add in the body of the request.
    try {
      CreateStreamSource200Response result = apiInstance.createStreamSource(streamSource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSourcesApi#createStreamSource");
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
| **streamSource** | [**StreamSourceCreateInput**](StreamSourceCreateInput.md)| Provide the details of the stream source to add in the body of the request. | |

### Return type

[**CreateStreamSource200Response**](CreateStreamSource200Response.md)

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

<a id="deleteStreamSource"></a>
# **deleteStreamSource**
> deleteStreamSource(id)

Delete a stream source

This operation deletes a stream source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSourcesApi;

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

    StreamSourcesApi apiInstance = new StreamSourcesApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream source.
    try {
      apiInstance.deleteStreamSource(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSourcesApi#deleteStreamSource");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream source. | |

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

<a id="listStreamSources"></a>
# **listStreamSources**
> StreamSources listStreamSources(page, perPage)

Fetch all stream sources

This operation shows the details of all of your stream sources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSourcesApi;

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

    StreamSourcesApi apiInstance = new StreamSourcesApi(defaultClient);
    Integer page = 56; // Integer | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
    Integer perPage = 56; // Integer | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
    try {
      StreamSources result = apiInstance.listStreamSources(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSourcesApi#listStreamSources");
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

[**StreamSources**](StreamSources.md)

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

<a id="showStreamSource"></a>
# **showStreamSource**
> CreateStreamSource200Response showStreamSource(id)

Fetch a stream source

This operation shows details of a specific stream source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSourcesApi;

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

    StreamSourcesApi apiInstance = new StreamSourcesApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream source.
    try {
      CreateStreamSource200Response result = apiInstance.showStreamSource(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSourcesApi#showStreamSource");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream source. | |

### Return type

[**CreateStreamSource200Response**](CreateStreamSource200Response.md)

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

<a id="updateStreamSource"></a>
# **updateStreamSource**
> CreateStreamSource200Response updateStreamSource(id, streamSource)

Update a stream source

This operation updates a stream source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreamSourcesApi;

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

    StreamSourcesApi apiInstance = new StreamSourcesApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the stream source.
    StreamSourceUpdateInput streamSource = new StreamSourceUpdateInput(); // StreamSourceUpdateInput | Provide the details of the stream source to update in the body of the request.
    try {
      CreateStreamSource200Response result = apiInstance.updateStreamSource(id, streamSource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreamSourcesApi#updateStreamSource");
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
| **id** | **String**| The unique alphanumeric string that identifies the stream source. | |
| **streamSource** | [**StreamSourceUpdateInput**](StreamSourceUpdateInput.md)| Provide the details of the stream source to update in the body of the request. | |

### Return type

[**CreateStreamSource200Response**](CreateStreamSource200Response.md)

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

