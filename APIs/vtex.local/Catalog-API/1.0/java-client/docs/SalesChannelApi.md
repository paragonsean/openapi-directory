# SalesChannelApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesChannelList**](SalesChannelApi.md#salesChannelList) | **GET** /api/catalog_system/pvt/saleschannel/list | Get Sales Channel List |
| [**salesChannelbyId**](SalesChannelApi.md#salesChannelbyId) | **GET** /api/catalog_system/pub/saleschannel/{salesChannelId} | Get Sales Channel by ID |


<a id="salesChannelList"></a>
# **salesChannelList**
> List&lt;SalesChannelbyId200Response&gt; salesChannelList(contentType, accept)

Get Sales Channel List

Retrieves a list with details about the store&#39;s sales channels.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1,          \&quot;Name\&quot;: \&quot;Loja Principal\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;ProductClusterId\&quot;: null,          \&quot;CountryCode\&quot;: \&quot;BRA\&quot;,          \&quot;CultureInfo\&quot;: \&quot;pt-BR\&quot;,          \&quot;TimeZone\&quot;: \&quot;E. South America Standard Time\&quot;,          \&quot;CurrencyCode\&quot;: \&quot;BRL\&quot;,          \&quot;CurrencySymbol\&quot;: \&quot;R$\&quot;,          \&quot;CurrencyLocale\&quot;: 1046,          \&quot;CurrencyFormatInfo\&quot;: {              \&quot;CurrencyDecimalDigits\&quot;: 1,              \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,              \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,              \&quot;CurrencyGroupSize\&quot;: 3,              \&quot;StartsWithCurrencySymbol\&quot;: true          },          \&quot;Origin\&quot;: null,          \&quot;Position\&quot;: 2,          \&quot;ConditionRule\&quot;: null,          \&quot;CurrencyDecimalDigits\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesChannelApi;

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

    SalesChannelApi apiInstance = new SalesChannelApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      List<SalesChannelbyId200Response> result = apiInstance.salesChannelList(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesChannelApi#salesChannelList");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**List&lt;SalesChannelbyId200Response&gt;**](SalesChannelbyId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesChannelbyId"></a>
# **salesChannelbyId**
> SalesChannelbyId200Response salesChannelbyId(contentType, accept, salesChannelId)

Get Sales Channel by ID

Retrieves a specific sales channel by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Loja Principal\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ProductClusterId\&quot;: null,      \&quot;CountryCode\&quot;: \&quot;BRA\&quot;,      \&quot;CultureInfo\&quot;: \&quot;pt-BR\&quot;,      \&quot;TimeZone\&quot;: \&quot;E. South America Standard Time\&quot;,      \&quot;CurrencyCode\&quot;: \&quot;BRL\&quot;,      \&quot;CurrencySymbol\&quot;: \&quot;R$\&quot;,      \&quot;CurrencyLocale\&quot;: 1046,      \&quot;CurrencyFormatInfo\&quot;: {          \&quot;CurrencyDecimalDigits\&quot;: 1,          \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,          \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,          \&quot;CurrencyGroupSize\&quot;: 3,          \&quot;StartsWithCurrencySymbol\&quot;: true      },      \&quot;Origin\&quot;: null,      \&quot;Position\&quot;: 2,      \&quot;ConditionRule\&quot;: null,      \&quot;CurrencyDecimalDigits\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesChannelApi;

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

    SalesChannelApi apiInstance = new SalesChannelApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String salesChannelId = "1"; // String | 
    try {
      SalesChannelbyId200Response result = apiInstance.salesChannelbyId(contentType, accept, salesChannelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesChannelApi#salesChannelbyId");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **salesChannelId** | **String**|  | |

### Return type

[**SalesChannelbyId200Response**](SalesChannelbyId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

