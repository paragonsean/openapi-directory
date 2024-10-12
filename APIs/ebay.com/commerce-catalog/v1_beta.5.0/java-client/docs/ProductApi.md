# ProductApi

All URIs are relative to *https://api.ebay.com/commerce/catalog/v1_beta*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProduct**](ProductApi.md#getProduct) | **GET** /product/{epid} |  |


<a id="getProduct"></a>
# **getProduct**
> Product getProduct(epid, X_EBAY_C_MARKETPLACE_ID)



This method retrieves details of the catalog product identified by the eBay product identifier (ePID) specified in the request. These details include the product&#39;s title and description, aspects and their values, associated images, applicable category IDs, and any recognized identifiers that apply to the product. &lt;br /&gt;&lt;br /&gt; For a new listing, you can use the &lt;b&gt;search&lt;/b&gt; method to identify candidate products on which to base the listing, then use the &lt;b&gt;getProduct&lt;/b&gt; method to present the full details of those candidate products to the seller to make a a final selection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/catalog/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductApi apiInstance = new ProductApi(defaultClient);
    String epid = "epid_example"; // String | The ePID of the product being requested. This value can be discovered by issuing the <b>search</b> method and examining the value of the <b>productSummaries.epid</b> field for the desired returned product summary.
    String X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | This method also uses the <code>X-EBAY-C-MARKETPLACE-ID</code> header to identify the seller's eBay marketplace. It is required for all marketplaces except EBAY_US, which is the default. <b>Note:</b> This method is limited to <code>EBAY_US</code>, <code>EBAY_AU</code>, <code>EBAY_CA</code>, and <code>EBAY_GB</code> values.
    try {
      Product result = apiInstance.getProduct(epid, X_EBAY_C_MARKETPLACE_ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApi#getProduct");
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
| **epid** | **String**| The ePID of the product being requested. This value can be discovered by issuing the &lt;b&gt;search&lt;/b&gt; method and examining the value of the &lt;b&gt;productSummaries.epid&lt;/b&gt; field for the desired returned product summary. | |
| **X_EBAY_C_MARKETPLACE_ID** | **String**| This method also uses the &lt;code&gt;X-EBAY-C-MARKETPLACE-ID&lt;/code&gt; header to identify the seller&#39;s eBay marketplace. It is required for all marketplaces except EBAY_US, which is the default. &lt;b&gt;Note:&lt;/b&gt; This method is limited to &lt;code&gt;EBAY_US&lt;/code&gt;, &lt;code&gt;EBAY_AU&lt;/code&gt;, &lt;code&gt;EBAY_CA&lt;/code&gt;, and &lt;code&gt;EBAY_GB&lt;/code&gt; values. | [optional] |

### Return type

[**Product**](Product.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

