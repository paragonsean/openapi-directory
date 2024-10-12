# RecallSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRecallHistory**](RecallSearchApi.md#getRecallHistory) | **GET** /car/recall/{vin} | Recall info by vin |


<a id="getRecallHistory"></a>
# **getRecallHistory**
> SearchResponse getRecallHistory(vin, apiKey, page)

Recall info by vin

Get a particular recall information for a vin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecallSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RecallSearchApi apiInstance = new RecallSearchApi(defaultClient);
    String vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    BigDecimal page = new BigDecimal(78); // BigDecimal | Page number to fetch the results for the given criteria. Default is 1.
    try {
      SearchResponse result = apiInstance.getRecallHistory(vin, apiKey, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecallSearchApi#getRecallHistory");
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
| **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **page** | **BigDecimal**| Page number to fetch the results for the given criteria. Default is 1. | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reacll info for the given vin |  -  |
| **0** | Error |  -  |

