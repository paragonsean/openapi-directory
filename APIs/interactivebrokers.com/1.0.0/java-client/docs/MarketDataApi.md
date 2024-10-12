# MarketDataApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketdataExchangeComponentsGet**](MarketDataApi.md#marketdataExchangeComponentsGet) | **GET** /marketdata/exchange_components | Exchange Components |
| [**marketdataSnapshotGet**](MarketDataApi.md#marketdataSnapshotGet) | **GET** /marketdata/snapshot | Market Data Snapshot |


<a id="marketdataExchangeComponentsGet"></a>
# **marketdataExchangeComponentsGet**
> List&lt;MarketdataExchangeComponentsGet200ResponseInner&gt; marketdataExchangeComponentsGet()

Exchange Components

This endpoint provides a bit mapping for the bid/ask/last &#39;market&#39; values in the snapshot response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    MarketDataApi apiInstance = new MarketDataApi(defaultClient);
    try {
      List<MarketdataExchangeComponentsGet200ResponseInner> result = apiInstance.marketdataExchangeComponentsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApi#marketdataExchangeComponentsGet");
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

[**List&lt;MarketdataExchangeComponentsGet200ResponseInner&gt;**](MarketdataExchangeComponentsGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exchange Components |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="marketdataSnapshotGet"></a>
# **marketdataSnapshotGet**
> List&lt;MarketdataSnapshotGet200ResponseInner&gt; marketdataSnapshotGet(marketdataSnapshotGetRequestInner)

Market Data Snapshot

This endpoint allows the consumer to request a market data snapshot for one or more trading products.  Consumers need to provide unique identifiers (conids) for the products in the IB product database (retrievable using the /secdef endpoint). The &#39;market&#39; values are integers whose bits indicate the exchange(s) making up the quote.   The mapping of bit to exchange is obtained from the marketdata/exchange_component endpoint. For example, if a bid has a &#39;market&#39; value of 5 and the exchange_component result has the map  0 &#x3D;&gt; NYSE, 1 &#x3D;&gt; ISLAND, 2 &#x3D;&gt; ARCA then the exchanges contributing to the bid size are NYSE and ARCA.   Similarly, if market&#x3D;2, then only ISLAND is contributing. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    MarketDataApi apiInstance = new MarketDataApi(defaultClient);
    List<MarketdataSnapshotGetRequestInner> marketdataSnapshotGetRequestInner = Arrays.asList(); // List<MarketdataSnapshotGetRequestInner> | Contract. Allowed combinations are [type and symbol and currency], or [type, symbol, exchange, and currency], or [conid].
    try {
      List<MarketdataSnapshotGet200ResponseInner> result = apiInstance.marketdataSnapshotGet(marketdataSnapshotGetRequestInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketDataApi#marketdataSnapshotGet");
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
| **marketdataSnapshotGetRequestInner** | [**List&lt;MarketdataSnapshotGetRequestInner&gt;**](MarketdataSnapshotGetRequestInner.md)| Contract. Allowed combinations are [type and symbol and currency], or [type, symbol, exchange, and currency], or [conid]. | |

### Return type

[**List&lt;MarketdataSnapshotGet200ResponseInner&gt;**](MarketdataSnapshotGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Financial Instrument Definition |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

