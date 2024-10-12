# ItemDraftApi

All URIs are relative to *https://api.ebay.com/sell/listing/v1_beta*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createItemDraft**](ItemDraftApi.md#createItemDraft) | **POST** /item_draft/ |  |


<a id="createItemDraft"></a>
# **createItemDraft**
> ItemDraftResponse createItemDraft(X_EBAY_C_MARKETPLACE_ID, contentLanguage, itemDraft)



This call gives Partners the ability to create an eBay draft of a item for their seller using information from their site. This lets the Partner increase the exposure of items on their site and leverage the eBay user listing experience seamlessly. This experience provides guidance on pricing, aspects, etc. and recommendations that help create a listing that is complete and improves the exposure of the listing in search results. After the listing draft is created, the seller logs into their eBay account and uses the listing experience to finish the listing and publish the item on eBay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItemDraftApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/listing/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    ItemDraftApi apiInstance = new ItemDraftApi(defaultClient);
    String X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | Use this header to specify an eBay marketplace ID. For a list of supported sites, see API Restrictions in the Listing API overview.
    String contentLanguage = "contentLanguage_example"; // String | Use this header to specify the natural language of the seller. For details, see Content-Language in HTTP request headers. Required: For EBAY_CA in French. (Content-Language = fr-CA)
    ItemDraft itemDraft = new ItemDraft(); // ItemDraft | 
    try {
      ItemDraftResponse result = apiInstance.createItemDraft(X_EBAY_C_MARKETPLACE_ID, contentLanguage, itemDraft);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItemDraftApi#createItemDraft");
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
| **X_EBAY_C_MARKETPLACE_ID** | **String**| Use this header to specify an eBay marketplace ID. For a list of supported sites, see API Restrictions in the Listing API overview. | |
| **contentLanguage** | **String**| Use this header to specify the natural language of the seller. For details, see Content-Language in HTTP request headers. Required: For EBAY_CA in French. (Content-Language &#x3D; fr-CA) | [optional] |
| **itemDraft** | [**ItemDraft**](ItemDraft.md)|  | [optional] |

### Return type

[**ItemDraftResponse**](ItemDraftResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

