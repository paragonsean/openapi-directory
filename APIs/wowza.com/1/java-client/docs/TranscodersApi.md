# TranscodersApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addStreamTargetToTranscoderOutput**](TranscodersApi.md#addStreamTargetToTranscoderOutput) | **POST** /transcoders/{transcoder_id}/outputs/{id}/add_stream_target | Deprecated operation |
| [**createTranscoder**](TranscodersApi.md#createTranscoder) | **POST** /transcoders | Create a transcoder |
| [**createTranscoderOutput**](TranscodersApi.md#createTranscoderOutput) | **POST** /transcoders/{transcoder_id}/outputs | Create an output |
| [**createTranscoderOutputOutputStreamTarget**](TranscodersApi.md#createTranscoderOutputOutputStreamTarget) | **POST** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets | Create an output stream target |
| [**createTranscoderProperty**](TranscodersApi.md#createTranscoderProperty) | **POST** /transcoders/{transcoder_id}/properties | Create a property for a transcoder |
| [**deleteTranscoder**](TranscodersApi.md#deleteTranscoder) | **DELETE** /transcoders/{id} | Delete a transcoder |
| [**deleteTranscoderOutput**](TranscodersApi.md#deleteTranscoderOutput) | **DELETE** /transcoders/{transcoder_id}/outputs/{id} | Delete an output |
| [**deleteTranscoderOutputOutputStreamTarget**](TranscodersApi.md#deleteTranscoderOutputOutputStreamTarget) | **DELETE** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id} | Delete an output stream target |
| [**deleteTranscoderProperty**](TranscodersApi.md#deleteTranscoderProperty) | **DELETE** /transcoders/{transcoder_id}/properties/{id} | Delete a transcoder&#39;s property |
| [**disableAllStreamTargetsTranscoder**](TranscodersApi.md#disableAllStreamTargetsTranscoder) | **PUT** /transcoders/{id}/disable_all_stream_targets | Disable a transcoder&#39;s stream targets |
| [**disableTranscoderOutputOutputStreamTarget**](TranscodersApi.md#disableTranscoderOutputOutputStreamTarget) | **PUT** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/disable | Disable an output stream target |
| [**enableAllStreamTargetsTranscoder**](TranscodersApi.md#enableAllStreamTargetsTranscoder) | **PUT** /transcoders/{id}/enable_all_stream_targets | Enable a transcoder&#39;s stream targets |
| [**enableTranscoderOutputOutputStreamTarget**](TranscodersApi.md#enableTranscoderOutputOutputStreamTarget) | **PUT** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/enable | Enable an output stream target |
| [**indexUptimes**](TranscodersApi.md#indexUptimes) | **GET** /transcoders/{transcoder_id}/uptimes | Fetch all uptime records for a transcoder |
| [**listTranscoderOutputOutputStreamTargets**](TranscodersApi.md#listTranscoderOutputOutputStreamTargets) | **GET** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets | Fetch all output stream targets of an output of a transcoder |
| [**listTranscoderOutputs**](TranscodersApi.md#listTranscoderOutputs) | **GET** /transcoders/{transcoder_id}/outputs | Fetch all outputs of a transcoder |
| [**listTranscoderProperties**](TranscodersApi.md#listTranscoderProperties) | **GET** /transcoders/{transcoder_id}/properties | Fetch a transcoder&#39;s properties |
| [**listTranscoderRecordings**](TranscodersApi.md#listTranscoderRecordings) | **GET** /transcoders/{id}/recordings | Fetch a transcoder&#39;s recordings |
| [**listTranscoderSchedules**](TranscodersApi.md#listTranscoderSchedules) | **GET** /transcoders/{id}/schedules | Fetch transcoder&#39;s schedules |
| [**listTranscoders**](TranscodersApi.md#listTranscoders) | **GET** /transcoders | Fetch all transcoders |
| [**removeStreamTargetToTranscoderOutput**](TranscodersApi.md#removeStreamTargetToTranscoderOutput) | **DELETE** /transcoders/{transcoder_id}/outputs/{id}/remove_stream_target | Deprecated operation |
| [**resetTranscoder**](TranscodersApi.md#resetTranscoder) | **PUT** /transcoders/{id}/reset | Reset a transcoder |
| [**restartTranscoderOutputOutputStreamTarget**](TranscodersApi.md#restartTranscoderOutputOutputStreamTarget) | **PUT** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/restart | Restart an output stream target |
| [**showTranscoder**](TranscodersApi.md#showTranscoder) | **GET** /transcoders/{id} | Fetch a transcoder |
| [**showTranscoderOutput**](TranscodersApi.md#showTranscoderOutput) | **GET** /transcoders/{transcoder_id}/outputs/{id} | Fetch an output |
| [**showTranscoderOutputOutputStreamTarget**](TranscodersApi.md#showTranscoderOutputOutputStreamTarget) | **GET** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id} | Fetch an output stream target |
| [**showTranscoderProperty**](TranscodersApi.md#showTranscoderProperty) | **GET** /transcoders/{transcoder_id}/properties/{id} | Fetch a property for a transcoder |
| [**showTranscoderState**](TranscodersApi.md#showTranscoderState) | **GET** /transcoders/{id}/state | Fetch the state and uptime ID of a transcoder |
| [**showTranscoderStats**](TranscodersApi.md#showTranscoderStats) | **GET** /transcoders/{id}/stats | Fetch statistics for a current transcoder |
| [**showTranscoderThumbnailUrl**](TranscodersApi.md#showTranscoderThumbnailUrl) | **GET** /transcoders/{id}/thumbnail_url | Fetch the thumbnail URL of a transcoder |
| [**showUptime**](TranscodersApi.md#showUptime) | **GET** /transcoders/{transcoder_id}/uptimes/{id} | Fetch an uptime record |
| [**showUptimeMetricsCurrent**](TranscodersApi.md#showUptimeMetricsCurrent) | **GET** /transcoders/{transcoder_id}/uptimes/{id}/metrics/current | Fetch current stream health metrics for an active transcoder |
| [**showUptimeMetricsHistoric**](TranscodersApi.md#showUptimeMetricsHistoric) | **GET** /transcoders/{transcoder_id}/uptimes/{id}/metrics/historic | Fetch historic stream health metrics for a transcoder |
| [**startTranscoder**](TranscodersApi.md#startTranscoder) | **PUT** /transcoders/{id}/start | Start a transcoder |
| [**stopTranscoder**](TranscodersApi.md#stopTranscoder) | **PUT** /transcoders/{id}/stop | Stop a transcoder |
| [**updateTranscoder**](TranscodersApi.md#updateTranscoder) | **PATCH** /transcoders/{id} | Update a transcoder |
| [**updateTranscoderOutput**](TranscodersApi.md#updateTranscoderOutput) | **PATCH** /transcoders/{transcoder_id}/outputs/{id} | Update an output |
| [**updateTranscoderOutputOutputStreamTarget**](TranscodersApi.md#updateTranscoderOutputOutputStreamTarget) | **PATCH** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id} | Update an output stream target |


<a id="addStreamTargetToTranscoderOutput"></a>
# **addStreamTargetToTranscoderOutput**
> AddStreamTargetToTranscoderOutput200Response addStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget)

Deprecated operation

The operation POST /transcoders/{transcoder_id}/outputs/{id}/add_stream_target is deprecated. Use POST /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets to add an existing stream target to an output.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
    OutputAddStreamTargetInput outputStreamTarget = new OutputAddStreamTargetInput(); // OutputAddStreamTargetInput | Provide the details of the stream target to add in the body of the request.
    try {
      AddStreamTargetToTranscoderOutput200Response result = apiInstance.addStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#addStreamTargetToTranscoderOutput");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **outputStreamTarget** | [**OutputAddStreamTargetInput**](OutputAddStreamTargetInput.md)| Provide the details of the stream target to add in the body of the request. | |

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

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

<a id="createTranscoder"></a>
# **createTranscoder**
> CreateTranscoder200Response createTranscoder(transcoder)

Create a transcoder

This operation creates a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    TranscoderCreateInput transcoder = new TranscoderCreateInput(); // TranscoderCreateInput | Provide the details of the transcoder to create in the body of the request.
    try {
      CreateTranscoder200Response result = apiInstance.createTranscoder(transcoder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#createTranscoder");
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
| **transcoder** | [**TranscoderCreateInput**](TranscoderCreateInput.md)| Provide the details of the transcoder to create in the body of the request. | |

### Return type

[**CreateTranscoder200Response**](CreateTranscoder200Response.md)

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

<a id="createTranscoderOutput"></a>
# **createTranscoderOutput**
> CreateTranscoderOutput200Response createTranscoderOutput(transcoderId, output)

Create an output

This operation creates an output rendition for a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    OutputCreateInput output = new OutputCreateInput(); // OutputCreateInput | Provide the details of the output rendition to create in the body of the request.
    try {
      CreateTranscoderOutput200Response result = apiInstance.createTranscoderOutput(transcoderId, output);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#createTranscoderOutput");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **output** | [**OutputCreateInput**](OutputCreateInput.md)| Provide the details of the output rendition to create in the body of the request. | |

### Return type

[**CreateTranscoderOutput200Response**](CreateTranscoderOutput200Response.md)

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

<a id="createTranscoderOutputOutputStreamTarget"></a>
# **createTranscoderOutputOutputStreamTarget**
> AddStreamTargetToTranscoderOutput200Response createTranscoderOutputOutputStreamTarget(transcoderId, outputId, outputStreamTarget)

Create an output stream target

This operation creates an output stream target. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    OutputStreamTargetCreateInput outputStreamTarget = new OutputStreamTargetCreateInput(); // OutputStreamTargetCreateInput | Provide the details of the output stream target to create in the body of the request. Targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong> can't be added to output renditions.
    try {
      AddStreamTargetToTranscoderOutput200Response result = apiInstance.createTranscoderOutputOutputStreamTarget(transcoderId, outputId, outputStreamTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#createTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **outputStreamTarget** | [**OutputStreamTargetCreateInput**](OutputStreamTargetCreateInput.md)| Provide the details of the output stream target to create in the body of the request. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions. | |

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

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

<a id="createTranscoderProperty"></a>
# **createTranscoderProperty**
> CreateTranscoderProperty200Response createTranscoderProperty(transcoderId, property)

Create a property for a transcoder

This operation creates a property for a transcoder. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    TranscoderPropertyCreateInput property = new TranscoderPropertyCreateInput(); // TranscoderPropertyCreateInput | Provide the details of the property to create in the body of the request.
    try {
      CreateTranscoderProperty200Response result = apiInstance.createTranscoderProperty(transcoderId, property);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#createTranscoderProperty");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **property** | [**TranscoderPropertyCreateInput**](TranscoderPropertyCreateInput.md)| Provide the details of the property to create in the body of the request. | |

### Return type

[**CreateTranscoderProperty200Response**](CreateTranscoderProperty200Response.md)

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

<a id="deleteTranscoder"></a>
# **deleteTranscoder**
> deleteTranscoder(id)

Delete a transcoder

This operation deletes a transcoder, including all of its assigned output renditions and stream targets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      apiInstance.deleteTranscoder(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#deleteTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

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

<a id="deleteTranscoderOutput"></a>
# **deleteTranscoderOutput**
> deleteTranscoderOutput(transcoderId, id)

Delete an output

This operation deletes an output, including all of its assigned targets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
    try {
      apiInstance.deleteTranscoderOutput(transcoderId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#deleteTranscoderOutput");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the output rendition. | |

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

<a id="deleteTranscoderOutputOutputStreamTarget"></a>
# **deleteTranscoderOutputOutputStreamTarget**
> deleteTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Delete an output stream target

This operation deletes an output stream target, including all of its assigned targets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      apiInstance.deleteTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#deleteTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

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

<a id="deleteTranscoderProperty"></a>
# **deleteTranscoderProperty**
> deleteTranscoderProperty(transcoderId, id)

Delete a transcoder&#39;s property

This operation deletes a specific property from a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset.
    try {
      apiInstance.deleteTranscoderProperty(transcoderId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#deleteTranscoderProperty");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset. | |

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

<a id="disableAllStreamTargetsTranscoder"></a>
# **disableAllStreamTargetsTranscoder**
> DisableAllStreamTargetsTranscoder200Response disableAllStreamTargetsTranscoder(id)

Disable a transcoder&#39;s stream targets

This operation disables all of the stream targets assigned to a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      DisableAllStreamTargetsTranscoder200Response result = apiInstance.disableAllStreamTargetsTranscoder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#disableAllStreamTargetsTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**DisableAllStreamTargetsTranscoder200Response**](DisableAllStreamTargetsTranscoder200Response.md)

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

<a id="disableTranscoderOutputOutputStreamTarget"></a>
# **disableTranscoderOutputOutputStreamTarget**
> DisableTranscoderOutputOutputStreamTarget200Response disableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Disable an output stream target

This operation disables an output stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      DisableTranscoderOutputOutputStreamTarget200Response result = apiInstance.disableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#disableTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**DisableTranscoderOutputOutputStreamTarget200Response**](DisableTranscoderOutputOutputStreamTarget200Response.md)

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

<a id="enableAllStreamTargetsTranscoder"></a>
# **enableAllStreamTargetsTranscoder**
> DisableAllStreamTargetsTranscoder200Response enableAllStreamTargetsTranscoder(id)

Enable a transcoder&#39;s stream targets

This operation enables all of the stream targets assigned to a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      DisableAllStreamTargetsTranscoder200Response result = apiInstance.enableAllStreamTargetsTranscoder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#enableAllStreamTargetsTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**DisableAllStreamTargetsTranscoder200Response**](DisableAllStreamTargetsTranscoder200Response.md)

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

<a id="enableTranscoderOutputOutputStreamTarget"></a>
# **enableTranscoderOutputOutputStreamTarget**
> EnableTranscoderOutputOutputStreamTarget200Response enableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Enable an output stream target

This operation enables an output stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      EnableTranscoderOutputOutputStreamTarget200Response result = apiInstance.enableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#enableTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**EnableTranscoderOutputOutputStreamTarget200Response**](EnableTranscoderOutputOutputStreamTarget200Response.md)

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

<a id="indexUptimes"></a>
# **indexUptimes**
> Uptimes indexUptimes(transcoderId, page, perPage)

Fetch all uptime records for a transcoder

This operation shows all of the uptime records for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a specific transcoding session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    Integer page = 56; // Integer | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
    Integer perPage = 56; // Integer | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
    try {
      Uptimes result = apiInstance.indexUptimes(transcoderId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#indexUptimes");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **page** | **Integer**| Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results. | [optional] |
| **perPage** | **Integer**| For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;. | [optional] |

### Return type

[**Uptimes**](Uptimes.md)

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

<a id="listTranscoderOutputOutputStreamTargets"></a>
# **listTranscoderOutputOutputStreamTargets**
> OutputStreamTarget listTranscoderOutputOutputStreamTargets(transcoderId, outputId)

Fetch all output stream targets of an output of a transcoder

This operation shows the details of all of the output stream targets of an output of a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    try {
      OutputStreamTarget result = apiInstance.listTranscoderOutputOutputStreamTargets(transcoderId, outputId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#listTranscoderOutputOutputStreamTargets");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |

### Return type

[**OutputStreamTarget**](OutputStreamTarget.md)

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

<a id="listTranscoderOutputs"></a>
# **listTranscoderOutputs**
> Outputs listTranscoderOutputs(transcoderId)

Fetch all outputs of a transcoder

This operation shows the details of all of the output renditions of a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      Outputs result = apiInstance.listTranscoderOutputs(transcoderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#listTranscoderOutputs");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**Outputs**](Outputs.md)

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

<a id="listTranscoderProperties"></a>
# **listTranscoderProperties**
> TranscoderProperties listTranscoderProperties(transcoderId)

Fetch a transcoder&#39;s properties

This operation shows all of the properties of a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      TranscoderProperties result = apiInstance.listTranscoderProperties(transcoderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#listTranscoderProperties");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**TranscoderProperties**](TranscoderProperties.md)

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

<a id="listTranscoderRecordings"></a>
# **listTranscoderRecordings**
> ListTranscoderRecordings200Response listTranscoderRecordings(id)

Fetch a transcoder&#39;s recordings

This operation shows the details of all of the recordings for a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      ListTranscoderRecordings200Response result = apiInstance.listTranscoderRecordings(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#listTranscoderRecordings");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**ListTranscoderRecordings200Response**](ListTranscoderRecordings200Response.md)

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

<a id="listTranscoderSchedules"></a>
# **listTranscoderSchedules**
> ListTranscoderSchedules200Response listTranscoderSchedules(id)

Fetch transcoder&#39;s schedules

This operation shows the details of all of the schedules for a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      ListTranscoderSchedules200Response result = apiInstance.listTranscoderSchedules(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#listTranscoderSchedules");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**ListTranscoderSchedules200Response**](ListTranscoderSchedules200Response.md)

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

<a id="listTranscoders"></a>
# **listTranscoders**
> Transcoders listTranscoders(page, perPage)

Fetch all transcoders

This operation shows the details of all of your transcoders.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    Integer page = 56; // Integer | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
    Integer perPage = 56; // Integer | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
    try {
      Transcoders result = apiInstance.listTranscoders(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#listTranscoders");
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

[**Transcoders**](Transcoders.md)

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

<a id="removeStreamTargetToTranscoderOutput"></a>
# **removeStreamTargetToTranscoderOutput**
> removeStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget)

Deprecated operation

The operation DELETE /transcoders/{transcoder_id}/outputs/{id}/remove_stream_target is deprecated. Use DELETE /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{id} to remove a stream target from an output.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
    OutputRemoveStreamTargetInput outputStreamTarget = new OutputRemoveStreamTargetInput(); // OutputRemoveStreamTargetInput | Provide the details of the stream target to remove in the body of the request.
    try {
      apiInstance.removeStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#removeStreamTargetToTranscoderOutput");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **outputStreamTarget** | [**OutputRemoveStreamTargetInput**](OutputRemoveStreamTargetInput.md)| Provide the details of the stream target to remove in the body of the request. | |

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

 - **Content-Type**: application/json
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

<a id="resetTranscoder"></a>
# **resetTranscoder**
> ResetTranscoder200Response resetTranscoder(id)

Reset a transcoder

This operation resets a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      ResetTranscoder200Response result = apiInstance.resetTranscoder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#resetTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**ResetTranscoder200Response**](ResetTranscoder200Response.md)

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

<a id="restartTranscoderOutputOutputStreamTarget"></a>
# **restartTranscoderOutputOutputStreamTarget**
> RestartTranscoderOutputOutputStreamTarget200Response restartTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Restart an output stream target

This operation restarts an output stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      RestartTranscoderOutputOutputStreamTarget200Response result = apiInstance.restartTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#restartTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**RestartTranscoderOutputOutputStreamTarget200Response**](RestartTranscoderOutputOutputStreamTarget200Response.md)

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

<a id="showTranscoder"></a>
# **showTranscoder**
> CreateTranscoder200Response showTranscoder(id)

Fetch a transcoder

This operation shows the details of a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      CreateTranscoder200Response result = apiInstance.showTranscoder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**CreateTranscoder200Response**](CreateTranscoder200Response.md)

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

<a id="showTranscoderOutput"></a>
# **showTranscoderOutput**
> CreateTranscoderOutput200Response showTranscoderOutput(transcoderId, id)

Fetch an output

This operation shows the details of a specific output rendition for a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
    try {
      CreateTranscoderOutput200Response result = apiInstance.showTranscoderOutput(transcoderId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoderOutput");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the output rendition. | |

### Return type

[**CreateTranscoderOutput200Response**](CreateTranscoderOutput200Response.md)

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

<a id="showTranscoderOutputOutputStreamTarget"></a>
# **showTranscoderOutputOutputStreamTarget**
> AddStreamTargetToTranscoderOutput200Response showTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Fetch an output stream target

This operation shows the details of an output stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    try {
      AddStreamTargetToTranscoderOutput200Response result = apiInstance.showTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

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

<a id="showTranscoderProperty"></a>
# **showTranscoderProperty**
> CreateTranscoderProperty200Response showTranscoderProperty(transcoderId, id)

Fetch a property for a transcoder

This operation shows the details of a specific property for a specific transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset.
    try {
      CreateTranscoderProperty200Response result = apiInstance.showTranscoderProperty(transcoderId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoderProperty");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset. | |

### Return type

[**CreateTranscoderProperty200Response**](CreateTranscoderProperty200Response.md)

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

<a id="showTranscoderState"></a>
# **showTranscoderState**
> ShowTranscoderState200Response showTranscoderState(id)

Fetch the state and uptime ID of a transcoder

This operation shows the current state and uptime ID of a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      ShowTranscoderState200Response result = apiInstance.showTranscoderState(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoderState");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**ShowTranscoderState200Response**](ShowTranscoderState200Response.md)

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

<a id="showTranscoderStats"></a>
# **showTranscoderStats**
> ShowTranscoderStats200Response showTranscoderStats(id)

Fetch statistics for a current transcoder

This operation responds with a hash of metrics (keys) for a currently running transcoder. Each key has a &lt;strong&gt;status&lt;/strong&gt;, &lt;strong&gt;text&lt;/strong&gt; (description), &lt;strong&gt;units&lt;/strong&gt;, and &lt;strong&gt;value&lt;/strong&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      ShowTranscoderStats200Response result = apiInstance.showTranscoderStats(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoderStats");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**ShowTranscoderStats200Response**](ShowTranscoderStats200Response.md)

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

<a id="showTranscoderThumbnailUrl"></a>
# **showTranscoderThumbnailUrl**
> ShowTranscoderThumbnailUrl200Response showTranscoderThumbnailUrl(id)

Fetch the thumbnail URL of a transcoder

This operation shows the thumbnail URL of a started transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      ShowTranscoderThumbnailUrl200Response result = apiInstance.showTranscoderThumbnailUrl(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showTranscoderThumbnailUrl");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**ShowTranscoderThumbnailUrl200Response**](ShowTranscoderThumbnailUrl200Response.md)

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

<a id="showUptime"></a>
# **showUptime**
> Uptime showUptime(transcoderId, id)

Fetch an uptime record

This operation shows the details of a specific uptime record for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a transcoding session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the uptime record.
    try {
      Uptime result = apiInstance.showUptime(transcoderId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showUptime");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the uptime record. | |

### Return type

[**Uptime**](Uptime.md)

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

<a id="showUptimeMetricsCurrent"></a>
# **showUptimeMetricsCurrent**
> ShowUptimeMetricsCurrent200Response showUptimeMetricsCurrent(transcoderId, id, fields)

Fetch current stream health metrics for an active transcoder

This operation returns a snapshot of the current source connection and processing details of an active (running) transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the uptime record.
    String fields = "fields_example"; // String | A comma-separated list of fields to return.
    try {
      ShowUptimeMetricsCurrent200Response result = apiInstance.showUptimeMetricsCurrent(transcoderId, id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showUptimeMetricsCurrent");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the uptime record. | |
| **fields** | **String**| A comma-separated list of fields to return. | [optional] |

### Return type

[**ShowUptimeMetricsCurrent200Response**](ShowUptimeMetricsCurrent200Response.md)

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

<a id="showUptimeMetricsHistoric"></a>
# **showUptimeMetricsHistoric**
> ShowUptimeMetricsHistoric200Response showUptimeMetricsHistoric(transcoderId, id, fields, from, to)

Fetch historic stream health metrics for a transcoder

This operation shows the historic source connection and processing details for a transcoding session (uptime record). The transcoder can be running or stopped. Metrics are recorded every 20 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the uptime record.
    String fields = "fields_example"; // String | A comma-separated list of fields to return.
    String from = "from_example"; // String | The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
    String to = "to_example"; // String | The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
    try {
      ShowUptimeMetricsHistoric200Response result = apiInstance.showUptimeMetricsHistoric(transcoderId, id, fields, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#showUptimeMetricsHistoric");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the uptime record. | |
| **fields** | **String**| A comma-separated list of fields to return. | [optional] |
| **from** | **String**| The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] |
| **to** | **String**| The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] |

### Return type

[**ShowUptimeMetricsHistoric200Response**](ShowUptimeMetricsHistoric200Response.md)

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

<a id="startTranscoder"></a>
# **startTranscoder**
> StartTranscoder200Response startTranscoder(id)

Start a transcoder

This operation starts a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      StartTranscoder200Response result = apiInstance.startTranscoder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#startTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**StartTranscoder200Response**](StartTranscoder200Response.md)

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

<a id="stopTranscoder"></a>
# **stopTranscoder**
> StartTranscoder200Response stopTranscoder(id)

Stop a transcoder

This operation stops a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    try {
      StartTranscoder200Response result = apiInstance.stopTranscoder(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#stopTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |

### Return type

[**StartTranscoder200Response**](StartTranscoder200Response.md)

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

<a id="updateTranscoder"></a>
# **updateTranscoder**
> CreateTranscoder200Response updateTranscoder(id, transcoder)

Update a transcoder

This operation updates a transcoder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
    TranscoderUpdateInput transcoder = new TranscoderUpdateInput(); // TranscoderUpdateInput | Provide the details of the transcoder to update in the body of the request.
    try {
      CreateTranscoder200Response result = apiInstance.updateTranscoder(id, transcoder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#updateTranscoder");
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
| **id** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **transcoder** | [**TranscoderUpdateInput**](TranscoderUpdateInput.md)| Provide the details of the transcoder to update in the body of the request. | |

### Return type

[**CreateTranscoder200Response**](CreateTranscoder200Response.md)

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

<a id="updateTranscoderOutput"></a>
# **updateTranscoderOutput**
> CreateTranscoderOutput200Response updateTranscoderOutput(transcoderId, id, output)

Update an output

This operation updates an output rendition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
    OutputUpdateInput output = new OutputUpdateInput(); // OutputUpdateInput | Provide the details of the output rendition to update in the body of the request.
    try {
      CreateTranscoderOutput200Response result = apiInstance.updateTranscoderOutput(transcoderId, id, output);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#updateTranscoderOutput");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **id** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **output** | [**OutputUpdateInput**](OutputUpdateInput.md)| Provide the details of the output rendition to update in the body of the request. | |

### Return type

[**CreateTranscoderOutput200Response**](CreateTranscoderOutput200Response.md)

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

<a id="updateTranscoderOutputOutputStreamTarget"></a>
# **updateTranscoderOutputOutputStreamTarget**
> AddStreamTargetToTranscoderOutput200Response updateTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, outputStreamTarget)

Update an output stream target

This operation updates an output stream target.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TranscodersApi;

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

    TranscodersApi apiInstance = new TranscodersApi(defaultClient);
    String transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
    String outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
    String streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
    OutputStreamTargetUpdateInput outputStreamTarget = new OutputStreamTargetUpdateInput(); // OutputStreamTargetUpdateInput | Provide the details of the output stream target to update in the body of the request.
    try {
      AddStreamTargetToTranscoderOutput200Response result = apiInstance.updateTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, outputStreamTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TranscodersApi#updateTranscoderOutputOutputStreamTarget");
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
| **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | |
| **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | |
| **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | |
| **outputStreamTarget** | [**OutputStreamTargetUpdateInput**](OutputStreamTargetUpdateInput.md)| Provide the details of the output stream target to update in the body of the request. | |

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

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

