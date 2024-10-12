# MarketDataApiApi

All URIs are relative to *https://api.tradematic.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketdataMarketsGet**](MarketDataApiApi.md#marketdataMarketsGet) | **GET** /marketdata/markets | Get markets list |
| [**marketdataMarketsMarketidGet**](MarketDataApiApi.md#marketdataMarketsMarketidGet) | **GET** /marketdata/markets/{marketid} | Get market by ID |
| [**marketdataSymbolsGet**](MarketDataApiApi.md#marketdataSymbolsGet) | **GET** /marketdata/symbols | Get symbols list |
| [**marketdataSymbolsSymbolidGet**](MarketDataApiApi.md#marketdataSymbolsSymbolidGet) | **GET** /marketdata/symbols/{symbolid} | Get symbol by ID |
| [**marketdataSymbolsSymbolidHistdataGet**](MarketDataApiApi.md#marketdataSymbolsSymbolidHistdataGet) | **GET** /marketdata/symbols/{symbolid}/histdata | Get historical data for instrument |


<a id="marketdataMarketsGet"></a>
# **marketdataMarketsGet**
> List&lt;Market&gt; marketdataMarketsGet()

Get markets list

Get markets list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    MarketDataApiApi apiInstance = new MarketDataApiApi(defaultClient);
    try {
      List<Market> result = apiInstance.marketdataMarketsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApiApi#marketdataMarketsGet");
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

[**List&lt;Market&gt;**](Market.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="marketdataMarketsMarketidGet"></a>
# **marketdataMarketsMarketidGet**
> Market marketdataMarketsMarketidGet(marketid)

Get market by ID

Get market by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    MarketDataApiApi apiInstance = new MarketDataApiApi(defaultClient);
    Long marketid = 56L; // Long | 
    try {
      Market result = apiInstance.marketdataMarketsMarketidGet(marketid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApiApi#marketdataMarketsMarketidGet");
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
| **marketid** | **Long**|  | |

### Return type

[**Market**](Market.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="marketdataSymbolsGet"></a>
# **marketdataSymbolsGet**
> List&lt;String&gt; marketdataSymbolsGet(marketid, filter)

Get symbols list

Get symbols list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    MarketDataApiApi apiInstance = new MarketDataApiApi(defaultClient);
    Long marketid = 56L; // Long | 
    Long filter = 56L; // Long | 
    try {
      List<String> result = apiInstance.marketdataSymbolsGet(marketid, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApiApi#marketdataSymbolsGet");
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
| **marketid** | **Long**|  | |
| **filter** | **Long**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="marketdataSymbolsSymbolidGet"></a>
# **marketdataSymbolsSymbolidGet**
> String marketdataSymbolsSymbolidGet(symbolid)

Get symbol by ID

Get symbol by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    MarketDataApiApi apiInstance = new MarketDataApiApi(defaultClient);
    Long symbolid = 56L; // Long | 
    try {
      String result = apiInstance.marketdataSymbolsSymbolidGet(symbolid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApiApi#marketdataSymbolsSymbolidGet");
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
| **symbolid** | **Long**|  | |

### Return type

**String**

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="marketdataSymbolsSymbolidHistdataGet"></a>
# **marketdataSymbolsSymbolidHistdataGet**
> MarketdataSymbolsSymbolidHistdataGet200Response marketdataSymbolsSymbolidHistdataGet(symbolid, tf, from, to)

Get historical data for instrument

Get historical data for instrument

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    MarketDataApiApi apiInstance = new MarketDataApiApi(defaultClient);
    Long symbolid = 56L; // Long | 
    Long tf = 56L; // Long | 
    Long from = 56L; // Long | 
    Long to = 56L; // Long | 
    try {
      MarketdataSymbolsSymbolidHistdataGet200Response result = apiInstance.marketdataSymbolsSymbolidHistdataGet(symbolid, tf, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApiApi#marketdataSymbolsSymbolidHistdataGet");
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
| **symbolid** | **Long**|  | |
| **tf** | **Long**|  | |
| **from** | **Long**|  | |
| **to** | **Long**|  | |

### Return type

[**MarketdataSymbolsSymbolidHistdataGet200Response**](MarketdataSymbolsSymbolidHistdataGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

