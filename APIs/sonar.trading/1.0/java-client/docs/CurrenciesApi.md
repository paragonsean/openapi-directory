# CurrenciesApi

All URIs are relative to *https://sonar.trading/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convertGet**](CurrenciesApi.md#convertGet) | **GET** /convert | Convert a currency amount to multiple other currencies |
| [**countryCurrenciesGet**](CurrenciesApi.md#countryCurrenciesGet) | **GET** /country/currencies | Return a list of all currencies of countries, available via service |
| [**digitalCurrenciesGet**](CurrenciesApi.md#digitalCurrenciesGet) | **GET** /digital/currencies | Return a list of all digital currencies, available via service |
| [**historyGet**](CurrenciesApi.md#historyGet) | **GET** /history | Return a historic rate for a currencies |


<a id="convertGet"></a>
# **convertGet**
> convertGet(from, to, amount, decimalPlaces)

Convert a currency amount to multiple other currencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sonar.trading/api/v1");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String from = "from_example"; // String | Currency you want to convert. For example, EUR
    String to = "to_example"; // String | Comma separated list of currencies codes. For example, USD
    String amount = "amount_example"; // String | This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed.
    String decimalPlaces = "decimalPlaces_example"; // String | This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 12 is assumed.
    try {
      apiInstance.convertGet(from, to, amount, decimalPlaces);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#convertGet");
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
| **from** | **String**| Currency you want to convert. For example, EUR | |
| **to** | **String**| Comma separated list of currencies codes. For example, USD | |
| **amount** | **String**| This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed. | [optional] |
| **decimalPlaces** | **String**| This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 12 is assumed. | [optional] |

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
| **200** | Command completed successfully |  -  |
| **422** | Parameter value syntax error / Parameter value range error |  -  |

<a id="countryCurrenciesGet"></a>
# **countryCurrenciesGet**
> countryCurrenciesGet(language)

Return a list of all currencies of countries, available via service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sonar.trading/api/v1");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String language = "language_example"; // String | Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language.
    try {
      apiInstance.countryCurrenciesGet(language);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#countryCurrenciesGet");
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
| **language** | **String**| Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language. | [optional] |

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
| **200** | Command completed successfully |  -  |
| **422** | Parameter value syntax error / Parameter value range error |  -  |

<a id="digitalCurrenciesGet"></a>
# **digitalCurrenciesGet**
> digitalCurrenciesGet(language)

Return a list of all digital currencies, available via service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sonar.trading/api/v1");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String language = "language_example"; // String | Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language.
    try {
      apiInstance.digitalCurrenciesGet(language);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#digitalCurrenciesGet");
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
| **language** | **String**| Parameter used to specify the language in which you would like the currency names to be provided. If not specified, EN is used. Now availeble only EN language. | [optional] |

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
| **200** | Command completed successfully |  -  |
| **422** | Parameter value syntax error / Parameter value range error |  -  |

<a id="historyGet"></a>
# **historyGet**
> historyGet(from, to, date, amount, decimalPlaces)

Return a historic rate for a currencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sonar.trading/api/v1");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String from = "from_example"; // String | Currency you want to convert. For example, EUR
    String to = "to_example"; // String | Comma separated list of currencies codes. For example, USD
    String date = "date_example"; // String | UTC date should be in the form of YYYY-MM-DD, for example, 2018-06-20. Data available from 2018-06-19 only.
    String amount = "amount_example"; // String | This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed.
    String decimalPlaces = "decimalPlaces_example"; // String | This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 4 is assumed.
    try {
      apiInstance.historyGet(from, to, date, amount, decimalPlaces);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#historyGet");
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
| **from** | **String**| Currency you want to convert. For example, EUR | |
| **to** | **String**| Comma separated list of currencies codes. For example, USD | |
| **date** | **String**| UTC date should be in the form of YYYY-MM-DD, for example, 2018-06-20. Data available from 2018-06-19 only. | |
| **amount** | **String**| This parameter can be used to specify the amount you want to convert. If an amount is not specified then 1 is assumed. | [optional] |
| **decimalPlaces** | **String**| This parameter can be used to specify the number of decimal places included in the output. If an amount is not specified then 4 is assumed. | [optional] |

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
| **200** | Command completed successfully |  -  |
| **422** | Parameter value syntax error / Parameter value range error |  -  |

