# ChangelogApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offersOfferIdChangelogGet**](ChangelogApi.md#offersOfferIdChangelogGet) | **GET** /offers/{offer_id}/changelog | Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided |


<a id="offersOfferIdChangelogGet"></a>
# **offersOfferIdChangelogGet**
> OffersOfferIdChangelogGet200Response offersOfferIdChangelogGet(offerId)

Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangelogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ChangelogApi apiInstance = new ChangelogApi(defaultClient);
    UUID offerId = UUID.randomUUID(); // UUID | 
    try {
      OffersOfferIdChangelogGet200Response result = apiInstance.offersOfferIdChangelogGet(offerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangelogApi#offersOfferIdChangelogGet");
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
| **offerId** | **UUID**|  | |

### Return type

[**OffersOfferIdChangelogGet200Response**](OffersOfferIdChangelogGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

