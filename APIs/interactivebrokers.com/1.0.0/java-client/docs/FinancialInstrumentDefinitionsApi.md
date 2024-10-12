# FinancialInstrumentDefinitionsApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**secdefGet**](FinancialInstrumentDefinitionsApi.md#secdefGet) | **GET** /secdef | Get security definition |


<a id="secdefGet"></a>
# **secdefGet**
> List&lt;SecdefGet200ResponseInner&gt; secdefGet(marketdataSnapshotGetRequestInner)

Get security definition

Fields that compose security definition. Allowed combinations, (1) type and symbol and currency, or (2) type, symbol, exchange, and currency, or (3) conid 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinancialInstrumentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    FinancialInstrumentDefinitionsApi apiInstance = new FinancialInstrumentDefinitionsApi(defaultClient);
    MarketdataSnapshotGetRequestInner marketdataSnapshotGetRequestInner = new MarketdataSnapshotGetRequestInner(); // MarketdataSnapshotGetRequestInner | Order Parameters
    try {
      List<SecdefGet200ResponseInner> result = apiInstance.secdefGet(marketdataSnapshotGetRequestInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinancialInstrumentDefinitionsApi#secdefGet");
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
| **marketdataSnapshotGetRequestInner** | [**MarketdataSnapshotGetRequestInner**](MarketdataSnapshotGetRequestInner.md)| Order Parameters | |

### Return type

[**List&lt;SecdefGet200ResponseInner&gt;**](SecdefGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Financial Instrument Definition |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

