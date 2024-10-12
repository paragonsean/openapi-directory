# RedeemedOffersApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**redeemedoffersGet**](RedeemedOffersApi.md#redeemedoffersGet) | **GET** /redeemedoffers | Returns Redeemed Offers |


<a id="redeemedoffersGet"></a>
# **redeemedoffersGet**
> RedeemedOffersResponse redeemedoffersGet(fid, userToken, lang, pageNumber, itemsPerPage)

Returns Redeemed Offers

This resource returns offers that have been fulfilled by the user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedeemedOffersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    RedeemedOffersApi apiInstance = new RedeemedOffersApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
    String lang = "en_US"; // String | When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format.
    Integer pageNumber = 1; // Integer | Segment of offers to return.
    Integer itemsPerPage = 1; // Integer | Segment size of offer to be returned. Default is 25.
    try {
      RedeemedOffersResponse result = apiInstance.redeemedoffersGet(fid, userToken, lang, pageNumber, itemsPerPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedeemedOffersApi#redeemedoffersGet");
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
| **fid** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | |
| **userToken** | **String**| Session identifier as returned by the UserToken resource. | |
| **lang** | **String**| When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format. | [optional] |
| **pageNumber** | **Integer**| Segment of offers to return. | [optional] |
| **itemsPerPage** | **Integer**| Segment size of offer to be returned. Default is 25. | [optional] |

### Return type

[**RedeemedOffersResponse**](RedeemedOffersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns offers that have been fulfilled by the user. |  -  |
| **0** | Unexpected error |  -  |

