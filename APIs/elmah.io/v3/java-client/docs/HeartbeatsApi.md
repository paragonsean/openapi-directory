# HeartbeatsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**heartbeatsCreate**](HeartbeatsApi.md#heartbeatsCreate) | **POST** /v3/heartbeats/{logId}/{id} | Create a new heartbeat. |


<a id="heartbeatsCreate"></a>
# **heartbeatsCreate**
> heartbeatsCreate(id, logId, createHeartbeat)

Create a new heartbeat.

Required permission: &#x60;heartbeats_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeartbeatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    HeartbeatsApi apiInstance = new HeartbeatsApi(defaultClient);
    String id = "id_example"; // String | The ID of the heartbeat check.
    String logId = "logId_example"; // String | The ID of the log containing the heartbeat check.
    CreateHeartbeat createHeartbeat = new CreateHeartbeat(); // CreateHeartbeat | The details of the heartbeat.
    try {
      apiInstance.heartbeatsCreate(id, logId, createHeartbeat);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeartbeatsApi#heartbeatsCreate");
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
| **id** | **String**| The ID of the heartbeat check. | |
| **logId** | **String**| The ID of the log containing the heartbeat check. | |
| **createHeartbeat** | [**CreateHeartbeat**](CreateHeartbeat.md)| The details of the heartbeat. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Heartbeat was created. |  -  |
| **400** | Model not valid. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the heartbeats API without heartbeats enabled or trial expired. |  -  |
| **404** | The specified log or heartbeat was not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

