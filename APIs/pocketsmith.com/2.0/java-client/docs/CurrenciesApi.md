# CurrenciesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currenciesGet**](CurrenciesApi.md#currenciesGet) | **GET** /currencies | List currencies |
| [**currenciesIdGet**](CurrenciesApi.md#currenciesIdGet) | **GET** /currencies/{id} | Get currency |


<a id="currenciesGet"></a>
# **currenciesGet**
> List&lt;Currency&gt; currenciesGet()

List currencies

Lists currencies supported by PocketSmith.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    try {
      List<Currency> result = apiInstance.currenciesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesGet");
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

[**List&lt;Currency&gt;**](Currency.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="currenciesIdGet"></a>
# **currenciesIdGet**
> Currency currenciesIdGet(id)

Get currency

Gets a particular currency by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrenciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    CurrenciesApi apiInstance = new CurrenciesApi(defaultClient);
    String id = "nzd"; // String | The unique identifier of the currency.
    try {
      Currency result = apiInstance.currenciesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrenciesApi#currenciesIdGet");
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
| **id** | **String**| The unique identifier of the currency. | |

### Return type

[**Currency**](Currency.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

