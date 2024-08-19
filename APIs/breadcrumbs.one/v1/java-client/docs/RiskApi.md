# RiskApi

All URIs are relative to *https://api.breadcrumbs.one*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**riskAddressGet**](RiskApi.md#riskAddressGet) | **GET** /risk/address | Will check the risk score for single address |
| [**riskTransactionGet**](RiskApi.md#riskTransactionGet) | **GET** /risk/transaction | Will check the risk score for every addresses in a transaction |


<a id="riskAddressGet"></a>
# **riskAddressGet**
> BreadcrumbsAPIModelsAddressRiskExposureResponse riskAddressGet(chain, address, includeExposure)

Will check the risk score for single address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RiskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.breadcrumbs.one");
    
    // Configure API key authorization: X-API-KEY
    ApiKeyAuth X-API-KEY = (ApiKeyAuth) defaultClient.getAuthentication("X-API-KEY");
    X-API-KEY.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-KEY.setApiKeyPrefix("Token");

    RiskApi apiInstance = new RiskApi(defaultClient);
    String chain = "ETH"; // String | Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX
    String address = "address_example"; // String | Blockchain address
    Boolean includeExposure = false; // Boolean | If set to `true`, will search the one nearest illicit address (incoming and outgoing) from the specified address
    try {
      BreadcrumbsAPIModelsAddressRiskExposureResponse result = apiInstance.riskAddressGet(chain, address, includeExposure);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RiskApi#riskAddressGet");
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
| **chain** | **String**| Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX | [default to ETH] [enum: ETH, BTC, MATIC, RON, SOL, TRX] |
| **address** | **String**| Blockchain address | |
| **includeExposure** | **Boolean**| If set to &#x60;true&#x60;, will search the one nearest illicit address (incoming and outgoing) from the specified address | [optional] [default to false] |

### Return type

[**BreadcrumbsAPIModelsAddressRiskExposureResponse**](BreadcrumbsAPIModelsAddressRiskExposureResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Client Error |  -  |

<a id="riskTransactionGet"></a>
# **riskTransactionGet**
> BreadcrumbsAPIModelsTransactionRiskResponse riskTransactionGet(chain, hash)

Will check the risk score for every addresses in a transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RiskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.breadcrumbs.one");
    
    // Configure API key authorization: X-API-KEY
    ApiKeyAuth X-API-KEY = (ApiKeyAuth) defaultClient.getAuthentication("X-API-KEY");
    X-API-KEY.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-KEY.setApiKeyPrefix("Token");

    RiskApi apiInstance = new RiskApi(defaultClient);
    String chain = "ETH"; // String | Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX
    String hash = "hash_example"; // String | Blockchain hash
    try {
      BreadcrumbsAPIModelsTransactionRiskResponse result = apiInstance.riskTransactionGet(chain, hash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RiskApi#riskTransactionGet");
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
| **chain** | **String**| Blockchain eg: ETH, BTC, MATIC, RON, SOL, TRX | [default to ETH] [enum: ETH, BTC, MATIC, RON, SOL, TRX] |
| **hash** | **String**| Blockchain hash | |

### Return type

[**BreadcrumbsAPIModelsTransactionRiskResponse**](BreadcrumbsAPIModelsTransactionRiskResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Client Error |  -  |

