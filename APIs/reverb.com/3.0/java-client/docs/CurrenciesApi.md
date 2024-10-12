# CurrenciesApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currenciesDisplayGet**](CurrenciesApi.md#currenciesDisplayGet) | **GET** /currencies/display | List of supported display currencies for browsing listings |
| [**currenciesListingGet**](CurrenciesApi.md#currenciesListingGet) | **GET** /currencies/listing | List of supported listing currencies for shops |


<a id="currenciesDisplayGet"></a>
# **currenciesDisplayGet**
> currenciesDisplayGet()

List of supported display currencies for browsing listings

List of supported display currencies for browsing listings

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    try {
      apiInstance.currenciesDisplayGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesDisplayGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="currenciesListingGet"></a>
# **currenciesListingGet**
> currenciesListingGet()

List of supported listing currencies for shops

List of supported listing currencies for shops

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    try {
      apiInstance.currenciesListingGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesListingGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

