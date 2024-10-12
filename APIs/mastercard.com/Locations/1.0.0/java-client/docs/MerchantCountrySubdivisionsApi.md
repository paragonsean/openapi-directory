# MerchantCountrySubdivisionsApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**merchantsV1CountrysubdivisionGet**](MerchantCountrySubdivisionsApi.md#merchantsV1CountrysubdivisionGet) | **GET** /merchants/v1/countrysubdivision | Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada.  |


<a id="merchantsV1CountrysubdivisionGet"></a>
# **merchantsV1CountrysubdivisionGet**
> CountrySubdivisionResponse merchantsV1CountrysubdivisionGet(details, country)

Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 

Returns country subdivisions that have Merchants offering the following services: accept contactless-enabled cards and devices, allow customers to add money to an eligible MasterCard or Maestro prepaid card, issue MasterCard Prepaid Travel cards, offer cash at checkout when paying with a Debit MasterCard or Maestro Card. A country subdivision is a segment within a country (ex  state or province).  Please note country subdivisions are only available for the US and Canada. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantCountrySubdivisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    MerchantCountrySubdivisionsApi apiInstance = new MerchantCountrySubdivisionsApi(defaultClient);
    String details = "topup.repower"; // String | This is the type of merchant location. Options  \"acceptance.paypass\" \"topup.repower\"  \"products.prepaidtravelcard\"  and \"offers.easysavings\"
    String country = "USA"; // String | Any three digit country code as defined in ISO 3166-1. For example \"USA or \"CAN\"
    try {
      CountrySubdivisionResponse result = apiInstance.merchantsV1CountrysubdivisionGet(details, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantCountrySubdivisionsApi#merchantsV1CountrysubdivisionGet");
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
| **country** | **String**| Any three digit country code as defined in ISO 3166-1. For example \&quot;USA or \&quot;CAN\&quot; | |

### Return type

[**CountrySubdivisionResponse**](CountrySubdivisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all the CountrySubdivisions |  -  |
| **0** | Unexpected error |  -  |

