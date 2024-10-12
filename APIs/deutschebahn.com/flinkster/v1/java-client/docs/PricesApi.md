# PricesApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPrices**](PricesApi.md#getPrices) | **GET** /providernetworks/{providernetworkUID}/prices | Get information about the prices. |


<a id="getPrices"></a>
# **getPrices**
> RentalObjectJO getPrices(providernetworkUID)

Get information about the prices.

Prices of a rental object by query params. The params depend on the price determination strategy of the provider network. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/flinkster-api-ng/v1");

    PricesApi apiInstance = new PricesApi(defaultClient);
    String providernetworkUID = "providernetworkUID_example"; // String | 
    try {
      RentalObjectJO result = apiInstance.getPrices(providernetworkUID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesApi#getPrices");
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
| **providernetworkUID** | **String**|  | |

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request One or more parameters have invalid values. |  -  |
| **403** | Forbidden Provider is not allowed to use this interface. |  -  |

