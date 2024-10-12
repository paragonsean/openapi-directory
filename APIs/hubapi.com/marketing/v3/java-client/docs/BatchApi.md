# BatchApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postMarketingV3MarketingEventsEventsDeleteArchive**](BatchApi.md#postMarketingV3MarketingEventsEventsDeleteArchive) | **POST** /marketing/v3/marketing-events/events/delete | Delete multiple marketing events |
| [**postMarketingV3MarketingEventsEventsUpsertDoUpsert**](BatchApi.md#postMarketingV3MarketingEventsEventsUpsertDoUpsert) | **POST** /marketing/v3/marketing-events/events/upsert | Create or update multiple marketing events |


<a id="postMarketingV3MarketingEventsEventsDeleteArchive"></a>
# **postMarketingV3MarketingEventsEventsDeleteArchive**
> Error postMarketingV3MarketingEventsEventsDeleteArchive(batchInputMarketingEventExternalUniqueIdentifier)

Delete multiple marketing events

Bulk delete a number of marketing events in HubSpot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchApi;

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

    BatchApi apiInstance = new BatchApi(defaultClient);
    BatchInputMarketingEventExternalUniqueIdentifier batchInputMarketingEventExternalUniqueIdentifier = new BatchInputMarketingEventExternalUniqueIdentifier(); // BatchInputMarketingEventExternalUniqueIdentifier | The details of the marketing events to delete
    try {
      Error result = apiInstance.postMarketingV3MarketingEventsEventsDeleteArchive(batchInputMarketingEventExternalUniqueIdentifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchApi#postMarketingV3MarketingEventsEventsDeleteArchive");
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
| **batchInputMarketingEventExternalUniqueIdentifier** | [**BatchInputMarketingEventExternalUniqueIdentifier**](BatchInputMarketingEventExternalUniqueIdentifier.md)| The details of the marketing events to delete | |

### Return type

[**Error**](Error.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | An error occurred. |  -  |

<a id="postMarketingV3MarketingEventsEventsUpsertDoUpsert"></a>
# **postMarketingV3MarketingEventsEventsUpsertDoUpsert**
> BatchResponseMarketingEventPublicDefaultResponse postMarketingV3MarketingEventsEventsUpsertDoUpsert(batchInputMarketingEventCreateRequestParams)

Create or update multiple marketing events

Upset multiple Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchApi;

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

    BatchApi apiInstance = new BatchApi(defaultClient);
    BatchInputMarketingEventCreateRequestParams batchInputMarketingEventCreateRequestParams = new BatchInputMarketingEventCreateRequestParams(); // BatchInputMarketingEventCreateRequestParams | The details of the marketing events to upsert
    try {
      BatchResponseMarketingEventPublicDefaultResponse result = apiInstance.postMarketingV3MarketingEventsEventsUpsertDoUpsert(batchInputMarketingEventCreateRequestParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchApi#postMarketingV3MarketingEventsEventsUpsertDoUpsert");
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
| **batchInputMarketingEventCreateRequestParams** | [**BatchInputMarketingEventCreateRequestParams**](BatchInputMarketingEventCreateRequestParams.md)| The details of the marketing events to upsert | |

### Return type

[**BatchResponseMarketingEventPublicDefaultResponse**](BatchResponseMarketingEventPublicDefaultResponse.md)

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

