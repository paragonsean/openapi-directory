# MerchantIdsApi

All URIs are relative to *http://api.mastercard.com/merchant-id/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMerchantIdentifiers**](MerchantIdsApi.md#getMerchantIdentifiers) | **GET** /merchant-ids | Returns merchant descriptor and locator information based on the criteria you provide.  Information returned includes merchant DBA name, merchant category code (MCC), street address, city, state, postal code, country, and sales channels. |


<a id="getMerchantIdentifiers"></a>
# **getMerchantIdentifiers**
> MerchantIds getMerchantIdentifiers(merchantId, type)

Returns merchant descriptor and locator information based on the criteria you provide.  Information returned includes merchant DBA name, merchant category code (MCC), street address, city, state, postal code, country, and sales channels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantIdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.mastercard.com/merchant-id/v2");

    MerchantIdsApi apiInstance = new MerchantIdsApi(defaultClient);
    String merchantId = "DOLIUMPTYLTDWELSHPOOLWA"; // String | Merchant's name as provided by the issuer found on a cardholder statement. __Important: Please remove all spaces before submitting a API request.__   
    String type = "ExactMatch"; // String | Determines how the search is performed.              ExactMatch returns either the one merchant that best fits the description or no results at all.              FuzzyMatch returns 0-20 merchants that are similar to the transaction descriptor.               If Type is not provided, defaults to ExactMatch.              Example: FuzzyMatch
    try {
      MerchantIds result = apiInstance.getMerchantIdentifiers(merchantId, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantIdsApi#getMerchantIdentifiers");
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
| **merchantId** | **String**| Merchant&#39;s name as provided by the issuer found on a cardholder statement. __Important: Please remove all spaces before submitting a API request.__    | [optional] |
| **type** | **String**| Determines how the search is performed.              ExactMatch returns either the one merchant that best fits the description or no results at all.              FuzzyMatch returns 0-20 merchants that are similar to the transaction descriptor.               If Type is not provided, defaults to ExactMatch.              Example: FuzzyMatch | [optional] [default to ExactMatch] |

### Return type

[**MerchantIds**](MerchantIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **500** | Server Error |  -  |

