# PricingConfigurationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPricingConfig**](PricingConfigurationApi.md#getPricingConfig) | **GET** /pricing/config | Get Pricing Configuration |
| [**getPricingv2Status**](PricingConfigurationApi.md#getPricingv2Status) | **GET** /pricing/migration | Get Pricing v2 Status |


<a id="getPricingConfig"></a>
# **getPricingConfig**
> PricingConfiguration getPricingConfig(contentType, accept)

Get Pricing Configuration

Retrieves Pricing Configuration.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;hasMigrated\&quot;: true,      \&quot;migrationStatus\&quot;: \&quot;Completed\&quot;,      \&quot;defaultMarkup\&quot;: 100,      \&quot;priceVariation\&quot;: {          \&quot;upperLimit\&quot;: null,          \&quot;lowerLimit\&quot;: null      },      \&quot;minimumMarkups\&quot;: {          \&quot;1\&quot;: 100,          \&quot;2\&quot;: 90      },      \&quot;tradePolicyConfigs\&quot;: [],      \&quot;sellersToOverride\&quot;: [],      \&quot;hasPriceInheritance\&quot;: false,      \&quot;priceInheritance\&quot;: \&quot;never\&quot;,      \&quot;hasOptionalBasePrice\&quot;: false,      \&quot;blockAccount\&quot;: false,      \&quot;blockedRoutes\&quot;: null,      \&quot;priceTableSelectionStrategy\&quot;: \&quot;first\&quot;,      \&quot;priceTableLimit\&quot;: null  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingConfigurationApi;

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

    PricingConfigurationApi apiInstance = new PricingConfigurationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      PricingConfiguration result = apiInstance.getPricingConfig(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingConfigurationApi#getPricingConfig");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |

### Return type

[**PricingConfiguration**](PricingConfiguration.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Access-Control-Allow-Credentials -  <br>  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="getPricingv2Status"></a>
# **getPricingv2Status**
> GetPricingv2Status200Response getPricingv2Status(contentType, accept)

Get Pricing v2 Status

Retrieves Pricing v2 Status.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;isActive\&quot;: true,      \&quot;hasMigrated\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingConfigurationApi;

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

    PricingConfigurationApi apiInstance = new PricingConfigurationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      GetPricingv2Status200Response result = apiInstance.getPricingv2Status(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingConfigurationApi#getPricingv2Status");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |

### Return type

[**GetPricingv2Status200Response**](GetPricingv2Status200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Access-Control-Allow-Credentials -  <br>  * Access-Control-Allow-Origin -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

