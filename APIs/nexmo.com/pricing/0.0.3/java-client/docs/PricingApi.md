# PricingApi

All URIs are relative to *https://rest.nexmo.com/account*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrievePrefixPricing**](PricingApi.md#retrievePrefixPricing) | **GET** /get-prefix-pricing/outbound/{type} | Retrieve outbound pricing for a specific dialing prefix. |
| [**retrievePricingAllCountries**](PricingApi.md#retrievePricingAllCountries) | **GET** /get-full-pricing/outbound/{type} | Retrieve outbound pricing for all countries. |
| [**retrievePricingCountry**](PricingApi.md#retrievePricingCountry) | **GET** /get-pricing/outbound/{type} | Retrieve outbound pricing for a specific country. |


<a id="retrievePrefixPricing"></a>
# **retrievePrefixPricing**
> PricingCountriesResponse retrievePrefixPricing(type, apiKey, apiSecret, prefix)

Retrieve outbound pricing for a specific dialing prefix.

Retrieves the pricing information based on the dialing prefix. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com/account");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String type = "sms"; // String | The type of service you wish to retrieve data about: either `sms`, `sms-transit` or `voice`.
    String apiKey = "apiKey_example"; // String | Your Nexmo API key.
    String apiSecret = "apiSecret_example"; // String | Your Nexmo API secret.
    String prefix = "prefix_example"; // String | The numerical dialing prefix to look up pricing for. Examples include 44, 1 and so on.
    try {
      PricingCountriesResponse result = apiInstance.retrievePrefixPricing(type, apiKey, apiSecret, prefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#retrievePrefixPricing");
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
| **type** | **String**| The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;. | |
| **apiKey** | **String**| Your Nexmo API key. | |
| **apiSecret** | **String**| Your Nexmo API secret. | |
| **prefix** | **String**| The numerical dialing prefix to look up pricing for. Examples include 44, 1 and so on. | |

### Return type

[**PricingCountriesResponse**](PricingCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing countries response |  -  |
| **400** | Bad request. You probably provided an invalid parameter. |  -  |
| **401** | You did not provide valid credentials |  -  |
| **404** | The page you requested was not found |  -  |
| **429** | You made too many requests. The API is rate limited to one request per second. |  -  |

<a id="retrievePricingAllCountries"></a>
# **retrievePricingAllCountries**
> PricingCountriesResponse retrievePricingAllCountries(type, apiKey, apiSecret)

Retrieve outbound pricing for all countries.

Retrieves the pricing information for all countries. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com/account");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String type = "sms"; // String | The type of service you wish to retrieve data about: either `sms`, `sms-transit` or `voice`.
    String apiKey = "apiKey_example"; // String | Your Nexmo API key.
    String apiSecret = "apiSecret_example"; // String | Your Nexmo API secret.
    try {
      PricingCountriesResponse result = apiInstance.retrievePricingAllCountries(type, apiKey, apiSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#retrievePricingAllCountries");
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
| **type** | **String**| The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;. | |
| **apiKey** | **String**| Your Nexmo API key. | |
| **apiSecret** | **String**| Your Nexmo API secret. | |

### Return type

[**PricingCountriesResponse**](PricingCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing response |  -  |
| **400** | Bad request. You probably provided an invalid parameter. |  -  |
| **401** | You did not provide valid credentials |  -  |
| **404** | The page you requested was not found |  -  |
| **429** | You made too many requests. The API is rate limited to one request per second. |  -  |

<a id="retrievePricingCountry"></a>
# **retrievePricingCountry**
> PricingCountryResponse retrievePricingCountry(type, apiKey, apiSecret, country)

Retrieve outbound pricing for a specific country.

Retrieves the pricing information based on the specified country. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com/account");

    PricingApi apiInstance = new PricingApi(defaultClient);
    String type = "sms"; // String | The type of service you wish to retrieve data about: either `sms`, `sms-transit` or `voice`.
    String apiKey = "apiKey_example"; // String | Your Nexmo API key.
    String apiSecret = "apiSecret_example"; // String | Your Nexmo API secret.
    String country = "country_example"; // String | A two letter [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). For example, `CA`.
    try {
      PricingCountryResponse result = apiInstance.retrievePricingCountry(type, apiKey, apiSecret, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#retrievePricingCountry");
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
| **type** | **String**| The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;. | |
| **apiKey** | **String**| Your Nexmo API key. | |
| **apiSecret** | **String**| Your Nexmo API secret. | |
| **country** | **String**| A two letter [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). For example, &#x60;CA&#x60;. | |

### Return type

[**PricingCountryResponse**](PricingCountryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing information for a specific country. |  -  |
| **400** | Bad request. You probably provided an invalid parameter. |  -  |
| **401** | You did not provide valid credentials |  -  |
| **404** | The page you requested was not found |  -  |
| **429** | You made too many requests. The API is rate limited to one request per second. |  -  |

