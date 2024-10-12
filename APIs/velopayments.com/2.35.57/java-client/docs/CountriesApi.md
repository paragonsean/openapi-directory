# CountriesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listPaymentChannelRulesV1**](CountriesApi.md#listPaymentChannelRulesV1) | **GET** /v1/paymentChannelRules | List Payment Channel Country Rules |
| [**listSupportedCountriesV1**](CountriesApi.md#listSupportedCountriesV1) | **GET** /v1/supportedCountries | List Supported Countries |
| [**listSupportedCountriesV2**](CountriesApi.md#listSupportedCountriesV2) | **GET** /v2/supportedCountries | List Supported Countries |


<a id="listPaymentChannelRulesV1"></a>
# **listPaymentChannelRulesV1**
> PaymentChannelRulesResponse listPaymentChannelRulesV1()

List Payment Channel Country Rules

List the country specific payment channel rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    try {
      PaymentChannelRulesResponse result = apiInstance.listPaymentChannelRulesV1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#listPaymentChannelRulesV1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentChannelRulesResponse**](PaymentChannelRulesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List Payment Channel Country Rules |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |

<a id="listSupportedCountriesV1"></a>
# **listSupportedCountriesV1**
> SupportedCountriesResponse listSupportedCountriesV1()

List Supported Countries

&lt;p&gt;List the supported countries.&lt;/p&gt; &lt;p&gt;This version will be retired in March 2020. Use /v2/supportedCountries&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    try {
      SupportedCountriesResponse result = apiInstance.listSupportedCountriesV1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#listSupportedCountriesV1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedCountriesResponse**](SupportedCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Supported Countries |  -  |

<a id="listSupportedCountriesV2"></a>
# **listSupportedCountriesV2**
> SupportedCountriesResponseV2 listSupportedCountriesV2()

List Supported Countries

List the supported countries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    try {
      SupportedCountriesResponseV2 result = apiInstance.listSupportedCountriesV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#listSupportedCountriesV2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedCountriesResponseV2**](SupportedCountriesResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Supported Countries |  -  |

