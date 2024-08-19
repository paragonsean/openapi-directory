# SystemUpdateCampaignsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCampaignEventResult**](SystemUpdateCampaignsApi.md#getCampaignEventResult) | **GET** /systemUpdate/events/{id}/result | Get a campaign event result |
| [**getCampaignEventResultForNode**](SystemUpdateCampaignsApi.md#getCampaignEventResultForNode) | **GET** /systemUpdate/events/{id}/result/{nodeId} | Get detailed campaign event result for a Node |
| [**getCampaignHistory**](SystemUpdateCampaignsApi.md#getCampaignHistory) | **GET** /systemUpdate/campaigns/{id}/history | Get a campaign result history |


<a id="getCampaignEventResult"></a>
# **getCampaignEventResult**
> GetCampaignEventResult200Response getCampaignEventResult(id)

Get a campaign event result

Get a campaign event result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemUpdateCampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SystemUpdateCampaignsApi apiInstance = new SystemUpdateCampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign event
    try {
      GetCampaignEventResult200Response result = apiInstance.getCampaignEventResult(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemUpdateCampaignsApi#getCampaignEventResult");
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
| **id** | **UUID**| Id of the campaign event | |

### Return type

[**GetCampaignEventResult200Response**](GetCampaignEventResult200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign result history result |  -  |

<a id="getCampaignEventResultForNode"></a>
# **getCampaignEventResultForNode**
> GetCampaignEventResultForNode200Response getCampaignEventResultForNode(id, nodeId)

Get detailed campaign event result for a Node

Get detailed campaign event result for a Node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemUpdateCampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SystemUpdateCampaignsApi apiInstance = new SystemUpdateCampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign event
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    try {
      GetCampaignEventResultForNode200Response result = apiInstance.getCampaignEventResultForNode(id, nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemUpdateCampaignsApi#getCampaignEventResultForNode");
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
| **id** | **UUID**| Id of the campaign event | |
| **nodeId** | **String**| Id of the target node | |

### Return type

[**GetCampaignEventResultForNode200Response**](GetCampaignEventResultForNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign event result for a node |  -  |

<a id="getCampaignHistory"></a>
# **getCampaignHistory**
> GetCampaignHistory200Response getCampaignHistory(id, limit, offset, before, after, order, asc)

Get a campaign result history

Get a campaign result history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemUpdateCampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SystemUpdateCampaignsApi apiInstance = new SystemUpdateCampaignsApi(defaultClient);
    UUID id = UUID.fromString("0076a379-f32d-4732-9e91-33ab219d8fde"); // UUID | Id of the campaign
    Integer limit = 56; // Integer | Max number of elements in response
    Integer offset = 56; // Integer | Offset of data in response (skip X elements)
    LocalDate before = LocalDate.now(); // LocalDate | 
    LocalDate after = LocalDate.now(); // LocalDate | 
    String order = "order_example"; // String | 
    String asc = "asc"; // String | 
    try {
      GetCampaignHistory200Response result = apiInstance.getCampaignHistory(id, limit, offset, before, after, order, asc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemUpdateCampaignsApi#getCampaignHistory");
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
| **id** | **UUID**| Id of the campaign | |
| **limit** | **Integer**| Max number of elements in response | [optional] |
| **offset** | **Integer**| Offset of data in response (skip X elements) | [optional] |
| **before** | **LocalDate**|  | [optional] |
| **after** | **LocalDate**|  | [optional] |
| **order** | **String**|  | [optional] |
| **asc** | **String**|  | [optional] [enum: asc, desc] |

### Return type

[**GetCampaignHistory200Response**](GetCampaignHistory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign result history result |  -  |

