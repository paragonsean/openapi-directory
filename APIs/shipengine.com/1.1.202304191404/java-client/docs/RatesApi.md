# RatesApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calculateRates**](RatesApi.md#calculateRates) | **POST** /v1/rates | Get Shipping Rates |
| [**compareBulkRates**](RatesApi.md#compareBulkRates) | **POST** /v1/rates/bulk | Get Bulk Rates |
| [**estimateRates**](RatesApi.md#estimateRates) | **POST** /v1/rates/estimate | Estimate Rates |
| [**getRateById**](RatesApi.md#getRateById) | **GET** /v1/rates/{rate_id} | Get Rate By ID |


<a id="calculateRates"></a>
# **calculateRates**
> CalculateRatesResponseBody calculateRates(calculateRatesRequestBody)

Get Shipping Rates

It&#39;s not uncommon that you want to give your customer the choice between whether they want to ship the fastest, cheapest, or the most trusted route. Most companies don&#39;t solely ship things using a single shipping option; so we provide functionality to show you all your options! 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RatesApi apiInstance = new RatesApi(defaultClient);
    CalculateRatesRequestBody calculateRatesRequestBody = new CalculateRatesRequestBody(); // CalculateRatesRequestBody | 
    try {
      CalculateRatesResponseBody result = apiInstance.calculateRates(calculateRatesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatesApi#calculateRates");
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
| **calculateRatesRequestBody** | [**CalculateRatesRequestBody**](CalculateRatesRequestBody.md)|  | |

### Return type

[**CalculateRatesResponseBody**](CalculateRatesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="compareBulkRates"></a>
# **compareBulkRates**
> List&lt;BulkRate&gt; compareBulkRates(compareBulkRatesRequestBody)

Get Bulk Rates

Get Bulk Shipment Rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RatesApi apiInstance = new RatesApi(defaultClient);
    CompareBulkRatesRequestBody compareBulkRatesRequestBody = new CompareBulkRatesRequestBody(); // CompareBulkRatesRequestBody | 
    try {
      List<BulkRate> result = apiInstance.compareBulkRates(compareBulkRatesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatesApi#compareBulkRates");
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
| **compareBulkRatesRequestBody** | [**CompareBulkRatesRequestBody**](CompareBulkRatesRequestBody.md)|  | |

### Return type

[**List&lt;BulkRate&gt;**](BulkRate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="estimateRates"></a>
# **estimateRates**
> List&lt;RateEstimate&gt; estimateRates(estimateRatesRequestBody)

Estimate Rates

Get Rate Estimates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RatesApi apiInstance = new RatesApi(defaultClient);
    EstimateRatesRequestBody estimateRatesRequestBody = new EstimateRatesRequestBody(); // EstimateRatesRequestBody | 
    try {
      List<RateEstimate> result = apiInstance.estimateRates(estimateRatesRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatesApi#estimateRates");
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
| **estimateRatesRequestBody** | [**EstimateRatesRequestBody**](EstimateRatesRequestBody.md)|  | |

### Return type

[**List&lt;RateEstimate&gt;**](RateEstimate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getRateById"></a>
# **getRateById**
> GetRateByIdResponseBody getRateById(rateId)

Get Rate By ID

Retrieve a previously queried rate by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RatesApi apiInstance = new RatesApi(defaultClient);
    String rateId = "rateId_example"; // String | Rate ID
    try {
      GetRateByIdResponseBody result = apiInstance.getRateById(rateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatesApi#getRateById");
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
| **rateId** | **String**| Rate ID | |

### Return type

[**GetRateByIdResponseBody**](GetRateByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

