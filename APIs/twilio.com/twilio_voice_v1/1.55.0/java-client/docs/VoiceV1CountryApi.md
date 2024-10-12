# VoiceV1CountryApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDialingPermissionsCountry**](VoiceV1CountryApi.md#fetchDialingPermissionsCountry) | **GET** /v1/DialingPermissions/Countries/{IsoCode} |  |
| [**listDialingPermissionsCountry**](VoiceV1CountryApi.md#listDialingPermissionsCountry) | **GET** /v1/DialingPermissions/Countries |  |


<a id="fetchDialingPermissionsCountry"></a>
# **fetchDialingPermissionsCountry**
> VoiceV1DialingPermissionsDialingPermissionsCountryInstance fetchDialingPermissionsCountry(isoCode)



Retrieve voice dialing country permissions identified by the given ISO country code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1CountryApi apiInstance = new VoiceV1CountryApi(defaultClient);
    String isoCode = "isoCode_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch
    try {
      VoiceV1DialingPermissionsDialingPermissionsCountryInstance result = apiInstance.fetchDialingPermissionsCountry(isoCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1CountryApi#fetchDialingPermissionsCountry");
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
| **isoCode** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch | |

### Return type

[**VoiceV1DialingPermissionsDialingPermissionsCountryInstance**](VoiceV1DialingPermissionsDialingPermissionsCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDialingPermissionsCountry"></a>
# **listDialingPermissionsCountry**
> ListDialingPermissionsCountryResponse listDialingPermissionsCountry(isoCode, continent, countryCode, lowRiskNumbersEnabled, highRiskSpecialNumbersEnabled, highRiskTollfraudNumbersEnabled, pageSize, page, pageToken)



Retrieve all voice dialing country permissions for this account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1CountryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1CountryApi apiInstance = new VoiceV1CountryApi(defaultClient);
    String isoCode = "isoCode_example"; // String | Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
    String continent = "continent_example"; // String | Filter to retrieve the country permissions by specifying the continent
    String countryCode = "countryCode_example"; // String | Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
    Boolean lowRiskNumbersEnabled = true; // Boolean | Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.
    Boolean highRiskSpecialNumbersEnabled = true; // Boolean | Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`
    Boolean highRiskTollfraudNumbersEnabled = true; // Boolean | Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers enabled. Can be: `true` or `false`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDialingPermissionsCountryResponse result = apiInstance.listDialingPermissionsCountry(isoCode, continent, countryCode, lowRiskNumbersEnabled, highRiskSpecialNumbersEnabled, highRiskTollfraudNumbersEnabled, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1CountryApi#listDialingPermissionsCountry");
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
| **isoCode** | **String**| Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] |
| **continent** | **String**| Filter to retrieve the country permissions by specifying the continent | [optional] |
| **countryCode** | **String**| Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html) | [optional] |
| **lowRiskNumbersEnabled** | **Boolean**| Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **highRiskSpecialNumbersEnabled** | **Boolean**| Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60; | [optional] |
| **highRiskTollfraudNumbersEnabled** | **Boolean**| Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDialingPermissionsCountryResponse**](ListDialingPermissionsCountryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

