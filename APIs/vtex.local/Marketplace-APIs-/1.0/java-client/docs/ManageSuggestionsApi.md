# ManageSuggestionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSuggestion**](ManageSuggestionsApi.md#deleteSuggestion) | **DELETE** /suggestions/{sellerId}/{sellerSkuId} | Delete SKU Suggestion |
| [**saveSuggestion**](ManageSuggestionsApi.md#saveSuggestion) | **PUT** /suggestions/{sellerId}/{sellerSkuId} | Send SKU Suggestion |


<a id="deleteSuggestion"></a>
# **deleteSuggestion**
> deleteSuggestion(accountName, accept, contentType, sellerId, sellerSkuId)

Delete SKU Suggestion

This endpoint deletes a chosen SKU suggestion. Only one SKU should be deleted per request. This request cannot be undone. A workaround to revert its action, is to send the suggestion again, through the Send Suggestion API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageSuggestionsApi;

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

    ManageSuggestionsApi apiInstance = new ManageSuggestionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    String sellerSkuId = "1234"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    try {
      apiInstance.deleteSuggestion(accountName, accept, contentType, sellerId, sellerSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageSuggestionsApi#deleteSuggestion");
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
| **accountName** | **String**| Name of the VTEX account. Used as part of the URL. | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to seller123] |
| **sellerSkuId** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to 1234] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveSuggestion"></a>
# **saveSuggestion**
> saveSuggestion(accountName, accept, contentType, sellerId, sellerSkuId, saveSuggestionRequest)

Send SKU Suggestion

This request is used by the seller when it wants to suggest that one of their SKUs is sold in the marketplace.  Before using this request, the seller should always use the [Change Notification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-seller-sku-notification) request in order to check if the SKU already exists in the marketplace. If it doesn&#39;t, then this is the next call in the SKU integration flow.  In the Send Suggestion request, the seller must send information about the SKU, such as the product and SKU name, the seller ID, and the image URL. All parameters are explained below. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageSuggestionsApi;

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

    ManageSuggestionsApi apiInstance = new ManageSuggestionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account to which the seller wants to suggest a new SKU. It is used as part of the request URL.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    String sellerSkuId = "1234"; // String | A string that identifies the SKU in the seller. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    SaveSuggestionRequest saveSuggestionRequest = new SaveSuggestionRequest(); // SaveSuggestionRequest | 
    try {
      apiInstance.saveSuggestion(accountName, accept, contentType, sellerId, sellerSkuId, saveSuggestionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageSuggestionsApi#saveSuggestion");
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
| **accountName** | **String**| Name of the VTEX account to which the seller wants to suggest a new SKU. It is used as part of the request URL. | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to seller123] |
| **sellerSkuId** | **String**| A string that identifies the SKU in the seller. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to 1234] |
| **saveSuggestionRequest** | [**SaveSuggestionRequest**](SaveSuggestionRequest.md)|  | |

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

