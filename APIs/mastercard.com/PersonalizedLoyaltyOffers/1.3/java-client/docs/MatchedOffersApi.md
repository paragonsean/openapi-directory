# MatchedOffersApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**matchedoffersGet**](MatchedOffersApi.md#matchedoffersGet) | **GET** /matchedoffers | Returns Matched Offers |


<a id="matchedoffersGet"></a>
# **matchedoffersGet**
> MatchedOffersResponse matchedoffersGet(fid, userToken, lang, merchantName, category, offerType, pageNumber, itemsPerPage)

Returns Matched Offers

This resource returns offers that are available to the user and conform to the search criteria (if specified). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MatchedOffersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    MatchedOffersApi apiInstance = new MatchedOffersApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
    String lang = "en_US"; // String | When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format.
    String merchantName = "Example.com"; // String | Fuzzy term to search retailers with offers for the user. In general, searching of Matched Offers is not advised as users generally have a modest selection of highly relevant promotions.
    String category = "DEPARTMENTSTORE"; // String | Offer Categories.
    String offerType = "POSTPAIDCREDIT"; // String | The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase.
    Integer pageNumber = 1; // Integer | Segment of offers to return.
    Integer itemsPerPage = 1; // Integer | Segment size of offer to be returned. Default is 25.
    try {
      MatchedOffersResponse result = apiInstance.matchedoffersGet(fid, userToken, lang, merchantName, category, offerType, pageNumber, itemsPerPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MatchedOffersApi#matchedoffersGet");
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
| **merchantName** | **String**| Fuzzy term to search retailers with offers for the user. In general, searching of Matched Offers is not advised as users generally have a modest selection of highly relevant promotions. | [optional] |
| **category** | **String**| Offer Categories. | [optional] |
| **offerType** | **String**| The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase. | [optional] |
| **pageNumber** | **Integer**| Segment of offers to return. | [optional] |
| **itemsPerPage** | **Integer**| Segment size of offer to be returned. Default is 25. | [optional] |

### Return type

[**MatchedOffersResponse**](MatchedOffersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns offers that are available to the user and conform to the search criteria (if specified). |  -  |
| **0** | Unexpected error |  -  |

