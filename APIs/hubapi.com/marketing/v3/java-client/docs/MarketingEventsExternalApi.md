# MarketingEventsExternalApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete**](MarketingEventsExternalApi.md#postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete) | **POST** /marketing/v3/marketing-events/events/{externalEventId}/complete |  |


<a id="postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete"></a>
# **postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete**
> MarketingEventDefaultResponse postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete(externalEventId, externalAccountId, marketingEventCompleteRequestParams)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketingEventsExternalApi;

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

    MarketingEventsExternalApi apiInstance = new MarketingEventsExternalApi(defaultClient);
    String externalEventId = "externalEventId_example"; // String | 
    String externalAccountId = "externalAccountId_example"; // String | 
    MarketingEventCompleteRequestParams marketingEventCompleteRequestParams = new MarketingEventCompleteRequestParams(); // MarketingEventCompleteRequestParams | 
    try {
      MarketingEventDefaultResponse result = apiInstance.postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete(externalEventId, externalAccountId, marketingEventCompleteRequestParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketingEventsExternalApi#postMarketingV3MarketingEventsEventsExternalEventIdCompleteComplete");
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
| **externalEventId** | **String**|  | |
| **externalAccountId** | **String**|  | |
| **marketingEventCompleteRequestParams** | [**MarketingEventCompleteRequestParams**](MarketingEventCompleteRequestParams.md)|  | |

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

