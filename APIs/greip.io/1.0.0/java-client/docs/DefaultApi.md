# DefaultApi

All URIs are relative to *https://gregeoip.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aSNLookupGet**](DefaultApi.md#aSNLookupGet) | **GET** /ASNLookup |  |
| [**bINLookupGet**](DefaultApi.md#bINLookupGet) | **GET** /BINLookup |  |
| [**badWordsGet**](DefaultApi.md#badWordsGet) | **GET** /badWords |  |
| [**bulkLookupGet**](DefaultApi.md#bulkLookupGet) | **GET** /BulkLookup |  |
| [**countryGet**](DefaultApi.md#countryGet) | **GET** /Country |  |
| [**geoIPGet**](DefaultApi.md#geoIPGet) | **GET** /GeoIP |  |
| [**iPLookupGet**](DefaultApi.md#iPLookupGet) | **GET** /IPLookup |  |
| [**validateEmailGet**](DefaultApi.md#validateEmailGet) | **GET** /validateEmail |  |
| [**validatePhoneGet**](DefaultApi.md#validatePhoneGet) | **GET** /validatePhone |  |


<a id="aSNLookupGet"></a>
# **aSNLookupGet**
> aSNLookupGet(key, asn, isList, format)



ASNLookup endpoint: This method helps you lookup any AS Number. It returns the type, organisation details, routes, etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String asn = "15169"; // String | The AS Number you want to lookup
    String isList = "false"; // String | Set this to true if you want to list all routes of both IPv4 and IPv6.
    String format = "JSON"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.aSNLookupGet(key, asn, isList, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#aSNLookupGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **asn** | **String**| The AS Number you want to lookup | |
| **isList** | **String**| Set this to true if you want to list all routes of both IPv4 and IPv6. | [optional] |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="bINLookupGet"></a>
# **bINLookupGet**
> bINLookupGet(key, bin, format)



This method helps you validate any BIN/IIN number and retrieve the full details related to the bank, brand, type, scheme, country, etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String bin = "489022"; // String | The BIN/IIN you want to lookup/validate.
    String format = "JSON"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.bINLookupGet(key, bin, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#bINLookupGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **bin** | **String**| The BIN/IIN you want to lookup/validate. | |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="badWordsGet"></a>
# **badWordsGet**
> badWordsGet(key, text, listBadWords, scoreOnly, format)



badWords endpoint: Detects whether user inputs contain profanity or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String text = "This is a sample text without profanity!"; // String | The text you want to check.
    String listBadWords = "false"; // String | Set to `yes` to list the bad-words as an Array.
    String scoreOnly = "false"; // String | Set to `yes` to return only the score of the text and whether it's safe or not.
    String format = "JSON"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.badWordsGet(key, text, listBadWords, scoreOnly, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#badWordsGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **text** | **String**| The text you want to check. | |
| **listBadWords** | **String**| Set to &#x60;yes&#x60; to list the bad-words as an Array. | [optional] |
| **scoreOnly** | **String**| Set to &#x60;yes&#x60; to return only the score of the text and whether it&#39;s safe or not. | [optional] |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="bulkLookupGet"></a>
# **bulkLookupGet**
> bulkLookupGet(key, ips, params, lang, format)



BulkLookup endpoint: Returns the geolocation data of multiple IP Addresses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String ips = "1.1.1.1,2.2.2.2"; // String | The IP Addresses you want to lookup. It's a CSV (Comma Separated Values)
    String params = "currency"; // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
    String lang = "AR"; // String | Used to inform the API to retrieve the response in your native language.
    String format = "XML"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.bulkLookupGet(key, ips, params, lang, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#bulkLookupGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **ips** | **String**| The IP Addresses you want to lookup. It&#39;s a CSV (Comma Separated Values) | |
| **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] |
| **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="countryGet"></a>
# **countryGet**
> countryGet(key, countryCode, params, lang, format)



Country endpoint: Returns the information of a specific country by passing the &#x60;countrCode&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String countryCode = "PS"; // String | The Country Code of the country you want to fetch it's data.
    String params = "language"; // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
    String lang = "AR"; // String | Used to inform the API to retrieve the response in your native language.
    String format = "XML"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.countryGet(key, countryCode, params, lang, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#countryGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **countryCode** | **String**| The Country Code of the country you want to fetch it&#39;s data. | |
| **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] |
| **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="geoIPGet"></a>
# **geoIPGet**
> geoIPGet(key, params, lang, format)



Returns the geolocation data of the visitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String params = "currency"; // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
    String lang = "AR"; // String | Used to inform the API to retrieve the response in your native language.
    String format = "XML"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.geoIPGet(key, params, lang, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#geoIPGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] |
| **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="iPLookupGet"></a>
# **iPLookupGet**
> iPLookupGet(key, ip, params, lang, format)



Returns the geolocation data of a specific IP Address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String ip = "1.1.1.1"; // String | The IP Address you want to lookup.
    String params = "currency"; // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
    String lang = "AR"; // String | Used to inform the API to retrieve the response in your native language.
    String format = "XML"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.iPLookupGet(key, ip, params, lang, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iPLookupGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **ip** | **String**| The IP Address you want to lookup. | |
| **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] |
| **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="validateEmailGet"></a>
# **validateEmailGet**
> validateEmailGet(key, email, format)



This method can be used as an extra-layer of your system for validating email addresses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String email = "name@domain.com"; // String | The Email Address you want to validate.
    String format = "JSON"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.validateEmailGet(key, email, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validateEmailGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **email** | **String**| The Email Address you want to validate. | |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="validatePhoneGet"></a>
# **validatePhoneGet**
> validatePhoneGet(key, phone, countryCode, format)



This method can be used as an extra-layer of your system for validating phone numbers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gregeoip.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
    String phone = "1234567890"; // String | The Phone Number you want to validate.
    String countryCode = "US"; // String | The ISO 3166-1 alpha-2 format of the country code of the phone number.
    String format = "JSON"; // String | Sets the format of the API response. JSON is the default format.
    try {
      apiInstance.validatePhoneGet(key, phone, countryCode, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validatePhoneGet");
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
| **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | |
| **phone** | **String**| The Phone Number you want to validate. | |
| **countryCode** | **String**| The ISO 3166-1 alpha-2 format of the country code of the phone number. | |
| **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

