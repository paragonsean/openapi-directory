# DictionariesApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCountriesDict**](DictionariesApi.md#getCountriesDict) | **GET** /api/v1/dictionaries/countries | Countries |
| [**getCurrenciesDict**](DictionariesApi.md#getCurrenciesDict) | **GET** /api/v1/dictionaries/currencies | Currencies |
| [**getProductTypesDict**](DictionariesApi.md#getProductTypesDict) | **GET** /api/v1/dictionaries/product_types | Product types |


<a id="getCountriesDict"></a>
# **getCountriesDict**
> GetCountriesDictOut getCountriesDict(taxSupported)

Countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    Boolean taxSupported = true; // Boolean | Should only countries with tax supported be listed?
    try {
      GetCountriesDictOut result = apiInstance.getCountriesDict(taxSupported);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getCountriesDict");
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
| **taxSupported** | **Boolean**| Should only countries with tax supported be listed? | [optional] |

### Return type

[**GetCountriesDictOut**](GetCountriesDictOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getCurrenciesDict"></a>
# **getCurrenciesDict**
> GetCurrenciesDictOut getCurrenciesDict()

Currencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    try {
      GetCurrenciesDictOut result = apiInstance.getCurrenciesDict();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getCurrenciesDict");
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

[**GetCurrenciesDictOut**](GetCurrenciesDictOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="getProductTypesDict"></a>
# **getProductTypesDict**
> GetProductTypesDictOut getProductTypesDict()

Product types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    try {
      GetProductTypesDictOut result = apiInstance.getProductTypesDict();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getProductTypesDict");
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

[**GetProductTypesDictOut**](GetProductTypesDictOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

