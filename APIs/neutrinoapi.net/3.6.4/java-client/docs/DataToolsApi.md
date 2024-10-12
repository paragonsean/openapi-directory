# DataToolsApi

All URIs are relative to *https://neutrinoapi.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**badWordFilter**](DataToolsApi.md#badWordFilter) | **POST** /bad-word-filter | Bad Word Filter |
| [**emailValidate**](DataToolsApi.md#emailValidate) | **GET** /email-validate | Email Validate |
| [**phoneValidate**](DataToolsApi.md#phoneValidate) | **GET** /phone-validate | Phone Validate |
| [**uALookup**](DataToolsApi.md#uALookup) | **GET** /ua-lookup | UA Lookup |


<a id="badWordFilter"></a>
# **badWordFilter**
> BadWordFilterResponse badWordFilter(content, catalog, censorCharacter)

Bad Word Filter

Detect bad words, swear words and profanity in a given text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    DataToolsApi apiInstance = new DataToolsApi(defaultClient);
    String content = "content_example"; // String | The content to scan. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
    String catalog = "strict"; // String | Which catalog of bad words to use, we currently maintain two bad word catalogs: <br> <ul> <li>strict - the largest database of bad words which includes profanity, obscenity, sexual, rude, cuss, dirty, swear and objectionable words and phrases. This catalog is suitable for environments of all ages including educational or children's content</li> <li>obscene - like the strict catalog but does not include any mild profanities, idiomatic phrases or words which are considered formal terminology. This catalog is suitable for adult environments where certain types of bad words are considered OK</li> </ul>
    String censorCharacter = "censorCharacter_example"; // String | The character to use to censor out the bad words found
    try {
      BadWordFilterResponse result = apiInstance.badWordFilter(content, catalog, censorCharacter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataToolsApi#badWordFilter");
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
| **content** | **String**| The content to scan. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string | |
| **catalog** | **String**| Which catalog of bad words to use, we currently maintain two bad word catalogs: &lt;br&gt; &lt;ul&gt; &lt;li&gt;strict - the largest database of bad words which includes profanity, obscenity, sexual, rude, cuss, dirty, swear and objectionable words and phrases. This catalog is suitable for environments of all ages including educational or children&#39;s content&lt;/li&gt; &lt;li&gt;obscene - like the strict catalog but does not include any mild profanities, idiomatic phrases or words which are considered formal terminology. This catalog is suitable for adult environments where certain types of bad words are considered OK&lt;/li&gt; &lt;/ul&gt; | [optional] [default to strict] |
| **censorCharacter** | **String**| The character to use to censor out the bad words found | [optional] |

### Return type

[**BadWordFilterResponse**](BadWordFilterResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="emailValidate"></a>
# **emailValidate**
> EmailValidateResponse emailValidate(email, fixTypos)

Email Validate

Parse, validate and clean an email address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    DataToolsApi apiInstance = new DataToolsApi(defaultClient);
    String email = "email_example"; // String | An email address
    Boolean fixTypos = false; // Boolean | Automatically attempt to fix typos in the address
    try {
      EmailValidateResponse result = apiInstance.emailValidate(email, fixTypos);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataToolsApi#emailValidate");
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
| **email** | **String**| An email address | |
| **fixTypos** | **Boolean**| Automatically attempt to fix typos in the address | [optional] [default to false] |

### Return type

[**EmailValidateResponse**](EmailValidateResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="phoneValidate"></a>
# **phoneValidate**
> PhoneValidateResponse phoneValidate(number, countryCode, ip)

Phone Validate

Parse, validate and get location information about a phone number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    DataToolsApi apiInstance = new DataToolsApi(defaultClient);
    String number = "number_example"; // String | A phone number. This can be in international format (E.164) or local format. If passing local format you must also set either the 'country-code' OR 'ip' options as well
    String countryCode = "countryCode_example"; // String | ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign)
    String ip = "ip_example"; // String | Pass in a users IP address and we will assume numbers are based in the country of the IP address
    try {
      PhoneValidateResponse result = apiInstance.phoneValidate(number, countryCode, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataToolsApi#phoneValidate");
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
| **number** | **String**| A phone number. This can be in international format (E.164) or local format. If passing local format you must also set either the &#39;country-code&#39; OR &#39;ip&#39; options as well | |
| **countryCode** | **String**| ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign) | [optional] |
| **ip** | **String**| Pass in a users IP address and we will assume numbers are based in the country of the IP address | [optional] |

### Return type

[**PhoneValidateResponse**](PhoneValidateResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="uALookup"></a>
# **uALookup**
> UALookupResponse uALookup(ua, uaVersion, uaPlatform, uaPlatformVersion, uaMobile, deviceModel, deviceBrand)

UA Lookup

Parse, validate and get detailed user-agent information from a user agent string or from client hints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    DataToolsApi apiInstance = new DataToolsApi(defaultClient);
    String ua = "ua_example"; // String | The user-agent string to lookup. For client hints use the 'UA' header or the JSON data directly from 'navigator.userAgentData.brands' or 'navigator.userAgentData.getHighEntropyValues()'
    String uaVersion = "uaVersion_example"; // String | For client hints this corresponds to the 'UA-Full-Version' header or 'uaFullVersion' from NavigatorUAData
    String uaPlatform = "uaPlatform_example"; // String | For client hints this corresponds to the 'UA-Platform' header or 'platform' from NavigatorUAData
    String uaPlatformVersion = "uaPlatformVersion_example"; // String | For client hints this corresponds to the 'UA-Platform-Version' header or 'platformVersion' from NavigatorUAData
    String uaMobile = "uaMobile_example"; // String | For client hints this corresponds to the 'UA-Mobile' header or 'mobile' from NavigatorUAData
    String deviceModel = "deviceModel_example"; // String | For client hints this corresponds to the 'UA-Model' header or 'model' from NavigatorUAData. <br>You can also use this parameter to lookup a device directly by its model name, model code or hardware code, on android you can get the model name from: https://developer.android.com/reference/android/os/Build.html#MODEL
    String deviceBrand = "deviceBrand_example"; // String | This parameter is only used in combination with 'device-model' when doing direct device lookups without any user-agent data. Set this to the brand or manufacturer name, this is required for accurate device detection with ambiguous model names. On android you can get the device brand from: https://developer.android.com/reference/android/os/Build#MANUFACTURER
    try {
      UALookupResponse result = apiInstance.uALookup(ua, uaVersion, uaPlatform, uaPlatformVersion, uaMobile, deviceModel, deviceBrand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataToolsApi#uALookup");
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
| **ua** | **String**| The user-agent string to lookup. For client hints use the &#39;UA&#39; header or the JSON data directly from &#39;navigator.userAgentData.brands&#39; or &#39;navigator.userAgentData.getHighEntropyValues()&#39; | |
| **uaVersion** | **String**| For client hints this corresponds to the &#39;UA-Full-Version&#39; header or &#39;uaFullVersion&#39; from NavigatorUAData | [optional] |
| **uaPlatform** | **String**| For client hints this corresponds to the &#39;UA-Platform&#39; header or &#39;platform&#39; from NavigatorUAData | [optional] |
| **uaPlatformVersion** | **String**| For client hints this corresponds to the &#39;UA-Platform-Version&#39; header or &#39;platformVersion&#39; from NavigatorUAData | [optional] |
| **uaMobile** | **String**| For client hints this corresponds to the &#39;UA-Mobile&#39; header or &#39;mobile&#39; from NavigatorUAData | [optional] |
| **deviceModel** | **String**| For client hints this corresponds to the &#39;UA-Model&#39; header or &#39;model&#39; from NavigatorUAData. &lt;br&gt;You can also use this parameter to lookup a device directly by its model name, model code or hardware code, on android you can get the model name from: https://developer.android.com/reference/android/os/Build.html#MODEL | [optional] |
| **deviceBrand** | **String**| This parameter is only used in combination with &#39;device-model&#39; when doing direct device lookups without any user-agent data. Set this to the brand or manufacturer name, this is required for accurate device detection with ambiguous model names. On android you can get the device brand from: https://developer.android.com/reference/android/os/Build#MANUFACTURER | [optional] |

### Return type

[**UALookupResponse**](UALookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

