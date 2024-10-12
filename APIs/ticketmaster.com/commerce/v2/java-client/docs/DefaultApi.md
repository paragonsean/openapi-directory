# DefaultApi

All URIs are relative to *http://www.ticketmaster.com/commerce/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEventOffers**](DefaultApi.md#getEventOffers) | **GET** /commerce/v2/events/{eventId}/offers | Event Offers |


<a id="getEventOffers"></a>
# **getEventOffers**
> OfferingResponse getEventOffers(eventId, X_SSL_CERT_UID, X_TM_ACCESS_TOKEN, accessToken, apiKey, body)

Event Offers

Returns Event Offers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ticketmaster.com/commerce/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String eventId = "eventId_example"; // String | Event Identifier
    String X_SSL_CERT_UID = "X_SSL_CERT_UID_example"; // String | API Key for external API developer
    String X_TM_ACCESS_TOKEN = "X_TM_ACCESS_TOKEN_example"; // String | Access token for
    String accessToken = "accessToken_example"; // String | Query Param Access Token
    String apiKey = "apiKey_example"; // String | Query Param API Key for external API developer
    String body = "body_example"; // String | displayId to un-hide protected offers
    try {
      OfferingResponse result = apiInstance.getEventOffers(eventId, X_SSL_CERT_UID, X_TM_ACCESS_TOKEN, accessToken, apiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEventOffers");
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
| **eventId** | **String**| Event Identifier | |
| **X_SSL_CERT_UID** | **String**| API Key for external API developer | [optional] |
| **X_TM_ACCESS_TOKEN** | **String**| Access token for | [optional] |
| **accessToken** | **String**| Query Param Access Token | [optional] |
| **apiKey** | **String**| Query Param API Key for external API developer | [optional] |
| **body** | **String**| displayId to un-hide protected offers | [optional] |

### Return type

[**OfferingResponse**](OfferingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

