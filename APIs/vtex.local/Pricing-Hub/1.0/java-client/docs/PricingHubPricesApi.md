# PricingHubPricesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPricingHubPricesPost**](PricingHubPricesApi.md#apiPricingHubPricesPost) | **POST** /api/pricing-hub/prices | Get Prices |
| [**configExternalPriceSource**](PricingHubPricesApi.md#configExternalPriceSource) | **PUT** /config | Configure External Price Source |


<a id="apiPricingHubPricesPost"></a>
# **apiPricingHubPricesPost**
> Response2 apiPricingHubPricesPost(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject)

Get Prices

This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.     &gt;ℹ️ &gt; This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingHubPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    PricingHubPricesApi apiInstance = new PricingHubPricesApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | The AppKey configured by the merchant
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | The AppToken configured by the merchant
    GetPricesRequestObject getPricesRequestObject = new GetPricesRequestObject(); // GetPricesRequestObject | 
    try {
      Response2 result = apiInstance.apiPricingHubPricesPost(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingHubPricesApi#apiPricingHubPricesPost");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| The AppKey configured by the merchant | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| The AppToken configured by the merchant | [default to {{X-VTEX-API-AppToken}}] |
| **getPricesRequestObject** | [**GetPricesRequestObject**](GetPricesRequestObject.md)|  | |

### Return type

[**Response2**](Response2.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="configExternalPriceSource"></a>
# **configExternalPriceSource**
> configExternalPriceSource(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, an)

Configure External Price Source

This route facilitates setting up an external price source in Pricing Hub. It also allows you to activate or deactivate that source in a given account.     &gt;ℹ️ This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingHubPricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    PricingHubPricesApi apiInstance = new PricingHubPricesApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | The AppKey configured by the merchant
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | The AppToken configured by the merchant
    ConfigExternalPriceSourceRequest configExternalPriceSourceRequest = new ConfigExternalPriceSourceRequest(); // ConfigExternalPriceSourceRequest | 
    String an = "apiexamples"; // String | Name of the VTEX account
    try {
      apiInstance.configExternalPriceSource(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, an);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingHubPricesApi#configExternalPriceSource");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| The AppKey configured by the merchant | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| The AppToken configured by the merchant | [default to {{X-VTEX-API-AppToken}}] |
| **configExternalPriceSourceRequest** | [**ConfigExternalPriceSourceRequest**](ConfigExternalPriceSourceRequest.md)|  | |
| **an** | **String**| Name of the VTEX account | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

