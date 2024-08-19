# TokenPricesApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTokenPrice**](TokenPricesApi.md#getTokenPrice) | **GET** /tokens/prices/{tokenId} | Lists price and available volume for a certain token |
| [**getTokenPrices**](TokenPricesApi.md#getTokenPrices) | **GET** /tokens/prices/all | Lists all token prices and available volume |


<a id="getTokenPrice"></a>
# **getTokenPrice**
> TokenPrice getTokenPrice(tokenId)

Lists price and available volume for a certain token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    TokenPricesApi apiInstance = new TokenPricesApi(defaultClient);
    String tokenId = "tokenId_example"; // String | 
    try {
      TokenPrice result = apiInstance.getTokenPrice(tokenId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenPricesApi#getTokenPrice");
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
| **tokenId** | **String**|  | |

### Return type

[**TokenPrice**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getTokenPrices"></a>
# **getTokenPrices**
> List&lt;TokenPrice&gt; getTokenPrices()

Lists all token prices and available volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    TokenPricesApi apiInstance = new TokenPricesApi(defaultClient);
    try {
      List<TokenPrice> result = apiInstance.getTokenPrices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenPricesApi#getTokenPrices");
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

[**List&lt;TokenPrice&gt;**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

