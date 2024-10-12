# BasicApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMarketingV3MarketingEventsEventsExternalEventIdArchive**](BasicApi.md#deleteMarketingV3MarketingEventsEventsExternalEventIdArchive) | **DELETE** /marketing/v3/marketing-events/events/{externalEventId} | Delete a marketing event |
| [**getMarketingV3MarketingEventsEventsExternalEventIdGetById**](BasicApi.md#getMarketingV3MarketingEventsEventsExternalEventIdGetById) | **GET** /marketing/v3/marketing-events/events/{externalEventId} | Get a marketing event |
| [**patchMarketingV3MarketingEventsEventsExternalEventIdUpdate**](BasicApi.md#patchMarketingV3MarketingEventsEventsExternalEventIdUpdate) | **PATCH** /marketing/v3/marketing-events/events/{externalEventId} | Update a marketing event |
| [**postMarketingV3MarketingEventsEventsCreate**](BasicApi.md#postMarketingV3MarketingEventsEventsCreate) | **POST** /marketing/v3/marketing-events/events | Create a marketing event |
| [**postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel**](BasicApi.md#postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/cancel | Mark a marketing event as cancelled |
| [**putMarketingV3MarketingEventsEventsExternalEventIdReplace**](BasicApi.md#putMarketingV3MarketingEventsEventsExternalEventIdReplace) | **PUT** /marketing/v3/marketing-events/events/{externalEventId} | Create or update a marketing event |


<a id="deleteMarketingV3MarketingEventsEventsExternalEventIdArchive"></a>
# **deleteMarketingV3MarketingEventsEventsExternalEventIdArchive**
> deleteMarketingV3MarketingEventsEventsExternalEventIdArchive(externalEventId, externalAccountId)

Delete a marketing event

Deletes an existing Marketing Event with the specified id, if one exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BasicApi apiInstance = new BasicApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event to delete
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    try {
      apiInstance.deleteMarketingV3MarketingEventsEventsExternalEventIdArchive(externalEventId, externalAccountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasicApi#deleteMarketingV3MarketingEventsEventsExternalEventIdArchive");
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
| **externalEventId** | **String**| The id of the marketing event to delete | |
| **externalAccountId** | **String**| The account id associated with the marketing event | |

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |

<a id="getMarketingV3MarketingEventsEventsExternalEventIdGetById"></a>
# **getMarketingV3MarketingEventsEventsExternalEventIdGetById**
> MarketingEventPublicReadResponse getMarketingV3MarketingEventsEventsExternalEventIdGetById(externalEventId, externalAccountId)

Get a marketing event

Returns the details of the Marketing Event with the specified id, if one exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BasicApi apiInstance = new BasicApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event to return
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    try {
      MarketingEventPublicReadResponse result = apiInstance.getMarketingV3MarketingEventsEventsExternalEventIdGetById(externalEventId, externalAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasicApi#getMarketingV3MarketingEventsEventsExternalEventIdGetById");
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
| **externalEventId** | **String**| The id of the marketing event to return | |
| **externalAccountId** | **String**| The account id associated with the marketing event | |

### Return type

[**MarketingEventPublicReadResponse**](MarketingEventPublicReadResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="patchMarketingV3MarketingEventsEventsExternalEventIdUpdate"></a>
# **patchMarketingV3MarketingEventsEventsExternalEventIdUpdate**
> MarketingEventPublicDefaultResponse patchMarketingV3MarketingEventsEventsExternalEventIdUpdate(externalEventId, externalAccountId, marketingEventUpdateRequestParams)

Update a marketing event

Updates an existing Marketing Event with the specified id, if one exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BasicApi apiInstance = new BasicApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event to update
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    MarketingEventUpdateRequestParams marketingEventUpdateRequestParams = new MarketingEventUpdateRequestParams(); // MarketingEventUpdateRequestParams | The details of the marketing event to update
    try {
      MarketingEventPublicDefaultResponse result = apiInstance.patchMarketingV3MarketingEventsEventsExternalEventIdUpdate(externalEventId, externalAccountId, marketingEventUpdateRequestParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasicApi#patchMarketingV3MarketingEventsEventsExternalEventIdUpdate");
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
| **externalEventId** | **String**| The id of the marketing event to update | |
| **externalAccountId** | **String**| The account id associated with the marketing event | |
| **marketingEventUpdateRequestParams** | [**MarketingEventUpdateRequestParams**](MarketingEventUpdateRequestParams.md)| The details of the marketing event to update | |

### Return type

[**MarketingEventPublicDefaultResponse**](MarketingEventPublicDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postMarketingV3MarketingEventsEventsCreate"></a>
# **postMarketingV3MarketingEventsEventsCreate**
> MarketingEventDefaultResponse postMarketingV3MarketingEventsEventsCreate(marketingEventCreateRequestParams)

Create a marketing event

Creates a new marketing event in HubSpot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BasicApi apiInstance = new BasicApi(defaultClient);
    MarketingEventCreateRequestParams marketingEventCreateRequestParams = new MarketingEventCreateRequestParams(); // MarketingEventCreateRequestParams | The details of the marketing event to create
    try {
      MarketingEventDefaultResponse result = apiInstance.postMarketingV3MarketingEventsEventsCreate(marketingEventCreateRequestParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasicApi#postMarketingV3MarketingEventsEventsCreate");
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
| **marketingEventCreateRequestParams** | [**MarketingEventCreateRequestParams**](MarketingEventCreateRequestParams.md)| The details of the marketing event to create | |

### Return type

[**MarketingEventDefaultResponse**](MarketingEventDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel"></a>
# **postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel**
> MarketingEventDefaultResponse postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel(externalEventId, externalAccountId)

Mark a marketing event as cancelled

Mark a marketing event as cancelled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BasicApi apiInstance = new BasicApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event to mark as cancelled
    String externalAccountId = "externalAccountId_example"; // String | The account id associated with the marketing event
    try {
      MarketingEventDefaultResponse result = apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel(externalEventId, externalAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasicApi#postMarketingV3MarketingEventsEventsExternalEventIdCancelDoCancel");
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
| **externalEventId** | **String**| The id of the marketing event to mark as cancelled | |
| **externalAccountId** | **String**| The account id associated with the marketing event | |

### Return type

[**MarketingEventDefaultResponse**](MarketingEventDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="putMarketingV3MarketingEventsEventsExternalEventIdReplace"></a>
# **putMarketingV3MarketingEventsEventsExternalEventIdReplace**
> MarketingEventPublicDefaultResponse putMarketingV3MarketingEventsEventsExternalEventIdReplace(externalEventId, marketingEventCreateRequestParams)

Create or update a marketing event

Upsets a Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BasicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    BasicApi apiInstance = new BasicApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | The id of the marketing event to upsert
    MarketingEventCreateRequestParams marketingEventCreateRequestParams = new MarketingEventCreateRequestParams(); // MarketingEventCreateRequestParams | The details of the marketing event to upsert
    try {
      MarketingEventPublicDefaultResponse result = apiInstance.putMarketingV3MarketingEventsEventsExternalEventIdReplace(externalEventId, marketingEventCreateRequestParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BasicApi#putMarketingV3MarketingEventsEventsExternalEventIdReplace");
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
| **externalEventId** | **String**| The id of the marketing event to upsert | |
| **marketingEventCreateRequestParams** | [**MarketingEventCreateRequestParams**](MarketingEventCreateRequestParams.md)| The details of the marketing event to upsert | |

### Return type

[**MarketingEventPublicDefaultResponse**](MarketingEventPublicDefaultResponse.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

