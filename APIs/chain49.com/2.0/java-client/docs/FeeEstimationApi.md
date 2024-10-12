# FeeEstimationApi

All URIs are relative to *https://api.chain49.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEstimateFeeV2**](FeeEstimationApi.md#getEstimateFeeV2) | **GET** /{blockchain}/v2/estimatefee/{confirmationTarget} | Estimate transaction fee V2 |


<a id="getEstimateFeeV2"></a>
# **getEstimateFeeV2**
> GetEstimateFeeV2200Response getEstimateFeeV2(blockchain, confirmationTarget)

Estimate transaction fee V2

Returns an estimated transaction fee for a specific confirmation target. If you want your transaction to be included in the next block, then you give 1 as parameter. If it is not urgent, then you can wait a bit longer and get an estimation for the fifth next block.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeeEstimationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    FeeEstimationApi apiInstance = new FeeEstimationApi(defaultClient);
    String blockchain = "bitcoin"; // String | Blockchain name
    Integer confirmationTarget = 1; // Integer | Number of blocks in which the transaction should be confirmed
    try {
      GetEstimateFeeV2200Response result = apiInstance.getEstimateFeeV2(blockchain, confirmationTarget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeeEstimationApi#getEstimateFeeV2");
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
| **blockchain** | **String**| Blockchain name | |
| **confirmationTarget** | **Integer**| Number of blocks in which the transaction should be confirmed | |

### Return type

[**GetEstimateFeeV2200Response**](GetEstimateFeeV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

