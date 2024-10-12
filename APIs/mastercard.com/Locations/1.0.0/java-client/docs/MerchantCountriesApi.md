# MerchantCountriesApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**merchantsV1CountryGet**](MerchantCountriesApi.md#merchantsV1CountryGet) | **GET** /merchants/v1/country | Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card.  |


<a id="merchantsV1CountryGet"></a>
# **merchantsV1CountryGet**
> CountriesResponse merchantsV1CountryGet(details)

Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

Returns countries that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantCountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantCountriesApi apiInstance = new MerchantCountriesApi(defaultClient);
    String details = "acceptance.paypass"; // String | This is the type of merchant location. Options  \"acceptance.paypass\" \"topup.repower\"  \"products.prepaidtravelcard\"  and \"offers.easysavings\"
    try {
      CountriesResponse result = apiInstance.merchantsV1CountryGet(details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantCountriesApi#merchantsV1CountryGet");
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
| **details** | **String**| This is the type of merchant location. Options  \&quot;acceptance.paypass\&quot; \&quot;topup.repower\&quot;  \&quot;products.prepaidtravelcard\&quot;  and \&quot;offers.easysavings\&quot; | |

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all the countries have a certain category |  -  |
| **0** | Unexpected error |  -  |

