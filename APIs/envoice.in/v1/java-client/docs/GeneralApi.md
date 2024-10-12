# GeneralApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generalApiCountries**](GeneralApi.md#generalApiCountries) | **GET** /api/general/countries | Return all of the platform supported countries |
| [**generalApiCurrencies**](GeneralApi.md#generalApiCurrencies) | **GET** /api/general/currencies | Return all of the platform supported currencies |
| [**generalApiDateFormats**](GeneralApi.md#generalApiDateFormats) | **GET** /api/general/dateformats | Return all of the platform supported Date Formats |
| [**generalApiUiLanguages**](GeneralApi.md#generalApiUiLanguages) | **GET** /api/general/uilanguages | Return all of the platform supported UI languages |


<a id="generalApiCountries"></a>
# **generalApiCountries**
> List&lt;CountryDetailsApiModel&gt; generalApiCountries(xAuthKey, xAuthSecret)

Return all of the platform supported countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<CountryDetailsApiModel> result = apiInstance.generalApiCountries(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#generalApiCountries");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**List&lt;CountryDetailsApiModel&gt;**](CountryDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generalApiCurrencies"></a>
# **generalApiCurrencies**
> List&lt;CurrencyDetailsApiModel&gt; generalApiCurrencies(xAuthKey, xAuthSecret)

Return all of the platform supported currencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<CurrencyDetailsApiModel> result = apiInstance.generalApiCurrencies(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#generalApiCurrencies");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**List&lt;CurrencyDetailsApiModel&gt;**](CurrencyDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generalApiDateFormats"></a>
# **generalApiDateFormats**
> List&lt;String&gt; generalApiDateFormats(xAuthKey, xAuthSecret)

Return all of the platform supported Date Formats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<String> result = apiInstance.generalApiDateFormats(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#generalApiDateFormats");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generalApiUiLanguages"></a>
# **generalApiUiLanguages**
> List&lt;UILanguageDetailsApiModel&gt; generalApiUiLanguages(xAuthKey, xAuthSecret)

Return all of the platform supported UI languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<UILanguageDetailsApiModel> result = apiInstance.generalApiUiLanguages(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#generalApiUiLanguages");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**List&lt;UILanguageDetailsApiModel&gt;**](UILanguageDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

