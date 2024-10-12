# GetSuggestionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSuggestion**](GetSuggestionsApi.md#getSuggestion) | **GET** /suggestions/{sellerId}/{sellerSkuId} | Get SKU Suggestion by ID |
| [**getsuggestions**](GetSuggestionsApi.md#getsuggestions) | **GET** /suggestions | Get all SKU suggestions |


<a id="getSuggestion"></a>
# **getSuggestion**
> getSuggestion(accountName, accept, contentType, sellerId, sellerSkuId)

Get SKU Suggestion by ID

This endpoint retrieves the data of a specific SKU sent by the seller, to the marketplace. Marketplaces or external matchers can call this endpoint when they want to check the information about a single SKU.   Note that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint&#39;s response is given by the Matcher.   Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetSuggestionsApi;

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

    GetSuggestionsApi apiInstance = new GetSuggestionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    String sellerSkuId = "1234"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    try {
      apiInstance.getSuggestion(accountName, accept, contentType, sellerId, sellerSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetSuggestionsApi#getSuggestion");
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

<a id="getsuggestions"></a>
# **getsuggestions**
> getsuggestions(accountName, accept, contentType, q, type, seller, status, hasmapping, matcherid, from, to)

Get all SKU suggestions

This endpoint retrieves a list of all SKUs sent by the seller for the Marketplace&#39;s approval. Marketplace operators should use this endpoint whenever they want to check the full list of received SKUs and their  information.   Note that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint&#39;s response is given by the Matcher.   Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetSuggestionsApi;

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

    GetSuggestionsApi apiInstance = new GetSuggestionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account. Used as part of the URL
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String q = ""; // String | This field allows you to customize your search. You can fill in this query param if you want to narrow down your search using the available filters on Received SKU modules.
    String type = "new"; // String | This field allows users to filter SKU suggestions, by searching only the new suggestions that were just sent, and suggestions that have already been sent, but were updated. Possible values for this field include `new` and `update`.
    String seller = ""; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller so it can call this endpoint.
    String status = "accepted"; // String | Narrow down you search, filtering by status. Values allowed on this field include: `accepted`, `pending` and `denied.`
    String hasmapping = "true"; // String | This field allows you to filter SKUs that have mapping or not. Insert `true` to filter SKUs that have mapping, or `false` to retrieve SKUs that aren't mapped.
    String matcherid = "vtex-matcher"; // String | Identifies the matching entity. It can be either VTEX's matcher, or an external matcher developed by partners, for example. The `matcherId`'s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint.
    Integer from = 1; // Integer | Define your pagination range, by adding the pagination starting value. Values should be bigger than 0, with a maximum of 50 records per page.
    Integer to = 50; // Integer | Define your pagination range, by adding the pagination ending value. Values should be bigger than 0, with a maximum of 50 records per page.
    try {
      apiInstance.getsuggestions(accountName, accept, contentType, q, type, seller, status, hasmapping, matcherid, from, to);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetSuggestionsApi#getsuggestions");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **q** | **String**| This field allows you to customize your search. You can fill in this query param if you want to narrow down your search using the available filters on Received SKU modules. | [optional] |
| **type** | **String**| This field allows users to filter SKU suggestions, by searching only the new suggestions that were just sent, and suggestions that have already been sent, but were updated. Possible values for this field include &#x60;new&#x60; and &#x60;update&#x60;. | [optional] |
| **seller** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller so it can call this endpoint. | [optional] |
| **status** | **String**| Narrow down you search, filtering by status. Values allowed on this field include: &#x60;accepted&#x60;, &#x60;pending&#x60; and &#x60;denied.&#x60; | [optional] |
| **hasmapping** | **String**| This field allows you to filter SKUs that have mapping or not. Insert &#x60;true&#x60; to filter SKUs that have mapping, or &#x60;false&#x60; to retrieve SKUs that aren&#39;t mapped. | [optional] |
| **matcherid** | **String**| Identifies the matching entity. It can be either VTEX&#39;s matcher, or an external matcher developed by partners, for example. The &#x60;matcherId&#x60;&#39;s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint. | [optional] [default to vtex-matcher] |
| **from** | **Integer**| Define your pagination range, by adding the pagination starting value. Values should be bigger than 0, with a maximum of 50 records per page. | [optional] [default to 1] |
| **to** | **Integer**| Define your pagination range, by adding the pagination ending value. Values should be bigger than 0, with a maximum of 50 records per page. | [optional] [default to 50] |

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

