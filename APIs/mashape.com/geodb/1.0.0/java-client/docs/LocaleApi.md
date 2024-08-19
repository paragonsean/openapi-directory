# LocaleApi

All URIs are relative to *https://wft-geo-db.p.rapidapi.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCurrenciesUsingGET**](LocaleApi.md#getCurrenciesUsingGET) | **GET** /locale/currencies | Find currencies |
| [**getLanguagesUsingGET**](LocaleApi.md#getLanguagesUsingGET) | **GET** /locale/languages | Get languages |
| [**getLocalesUsingGET**](LocaleApi.md#getLocalesUsingGET) | **GET** /locale/locales | Get locales |
| [**getTimeZoneDateTimeUsingGET**](LocaleApi.md#getTimeZoneDateTimeUsingGET) | **GET** /locale/timezones/{zoneId}/dateTime | Get time-zone date-time |
| [**getTimeZoneTimeUsingGET**](LocaleApi.md#getTimeZoneTimeUsingGET) | **GET** /locale/timezones/{zoneId}/time | Get time-zone time |
| [**getTimeZoneUsingGET**](LocaleApi.md#getTimeZoneUsingGET) | **GET** /locale/timezones/{zoneId} | Get time-zone |
| [**getTimezonesUsingGET**](LocaleApi.md#getTimezonesUsingGET) | **GET** /locale/timezones | Get time-zones |


<a id="getCurrenciesUsingGET"></a>
# **getCurrenciesUsingGET**
> CurrenciesResponse getCurrenciesUsingGET(countryId, hateoasMode, limit, offset)

Find currencies

Find currencies, filtering by optional criteria. If no criteria are set, you will get back all known currencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    String countryId = "countryId_example"; // String | Currencies for this country id
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    try {
      CurrenciesResponse result = apiInstance.getCurrenciesUsingGET(countryId, hateoasMode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getCurrenciesUsingGET");
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
| **countryId** | **String**| Currencies for this country id | |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of currencies |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="getLanguagesUsingGET"></a>
# **getLanguagesUsingGET**
> LanguagesResponse getLanguagesUsingGET(hateoasMode, limit, offset)

Get languages

Get all supported languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    try {
      LanguagesResponse result = apiInstance.getLanguagesUsingGET(hateoasMode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getLanguagesUsingGET");
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
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |

### Return type

[**LanguagesResponse**](LanguagesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of languages supported by the system |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="getLocalesUsingGET"></a>
# **getLocalesUsingGET**
> LocalesResponse getLocalesUsingGET(hateoasMode, limit, offset)

Get locales

Get all known locales

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    try {
      LocalesResponse result = apiInstance.getLocalesUsingGET(hateoasMode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getLocalesUsingGET");
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
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |

### Return type

[**LocalesResponse**](LocalesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of locales |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="getTimeZoneDateTimeUsingGET"></a>
# **getTimeZoneDateTimeUsingGET**
> DateTimeResponse getTimeZoneDateTimeUsingGET(zoneId)

Get time-zone date-time

Get time-zone date-time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    String zoneId = "zoneId_example"; // String | A time-zone id
    try {
      DateTimeResponse result = apiInstance.getTimeZoneDateTimeUsingGET(zoneId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getTimeZoneDateTimeUsingGET");
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
| **zoneId** | **String**| A time-zone id | |

### Return type

[**DateTimeResponse**](DateTimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An ISO-6801 date-time |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getTimeZoneTimeUsingGET"></a>
# **getTimeZoneTimeUsingGET**
> TimeResponse getTimeZoneTimeUsingGET(zoneId)

Get time-zone time

Get time-zone time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    String zoneId = "zoneId_example"; // String | A time-zone id
    try {
      TimeResponse result = apiInstance.getTimeZoneTimeUsingGET(zoneId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getTimeZoneTimeUsingGET");
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
| **zoneId** | **String**| A time-zone id | |

### Return type

[**TimeResponse**](TimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An ISO-8601 time response |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getTimeZoneUsingGET"></a>
# **getTimeZoneUsingGET**
> TimeZoneResponse getTimeZoneUsingGET(zoneId)

Get time-zone

Get time-zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    String zoneId = "zoneId_example"; // String | A time-zone id
    try {
      TimeZoneResponse result = apiInstance.getTimeZoneUsingGET(zoneId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getTimeZoneUsingGET");
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
| **zoneId** | **String**| A time-zone id | |

### Return type

[**TimeZoneResponse**](TimeZoneResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A time-zone |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getTimezonesUsingGET"></a>
# **getTimezonesUsingGET**
> TimeZonesResponse getTimezonesUsingGET(hateoasMode, limit, offset)

Get time-zones

Get all known time-zones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    LocaleApi apiInstance = new LocaleApi(defaultClient);
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    try {
      TimeZonesResponse result = apiInstance.getTimezonesUsingGET(hateoasMode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocaleApi#getTimezonesUsingGET");
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
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |

### Return type

[**TimeZonesResponse**](TimeZonesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of time-zones |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

