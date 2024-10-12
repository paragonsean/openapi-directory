# CatalogApi.ProductApi

All URIs are relative to *https://api.ebay.com/commerce/catalog/v1_beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProduct**](ProductApi.md#getProduct) | **GET** /product/{epid} | 



## getProduct

> Product getProduct(epid, opts)



This method retrieves details of the catalog product identified by the eBay product identifier (ePID) specified in the request. These details include the product&#39;s title and description, aspects and their values, associated images, applicable category IDs, and any recognized identifiers that apply to the product. &lt;br /&gt;&lt;br /&gt; For a new listing, you can use the &lt;b&gt;search&lt;/b&gt; method to identify candidate products on which to base the listing, then use the &lt;b&gt;getProduct&lt;/b&gt; method to present the full details of those candidate products to the seller to make a a final selection.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CatalogApi.ProductApi();
let epid = "epid_example"; // String | The ePID of the product being requested. This value can be discovered by issuing the <b>search</b> method and examining the value of the <b>productSummaries.epid</b> field for the desired returned product summary.
let opts = {
  'X_EBAY_C_MARKETPLACE_ID': "X_EBAY_C_MARKETPLACE_ID_example" // String | This method also uses the <code>X-EBAY-C-MARKETPLACE-ID</code> header to identify the seller's eBay marketplace. It is required for all marketplaces except EBAY_US, which is the default. <b>Note:</b> This method is limited to <code>EBAY_US</code>, <code>EBAY_AU</code>, <code>EBAY_CA</code>, and <code>EBAY_GB</code> values.
};
apiInstance.getProduct(epid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **epid** | **String**| The ePID of the product being requested. This value can be discovered by issuing the &lt;b&gt;search&lt;/b&gt; method and examining the value of the &lt;b&gt;productSummaries.epid&lt;/b&gt; field for the desired returned product summary. | 
 **X_EBAY_C_MARKETPLACE_ID** | **String**| This method also uses the &lt;code&gt;X-EBAY-C-MARKETPLACE-ID&lt;/code&gt; header to identify the seller&#39;s eBay marketplace. It is required for all marketplaces except EBAY_US, which is the default. &lt;b&gt;Note:&lt;/b&gt; This method is limited to &lt;code&gt;EBAY_US&lt;/code&gt;, &lt;code&gt;EBAY_AU&lt;/code&gt;, &lt;code&gt;EBAY_CA&lt;/code&gt;, and &lt;code&gt;EBAY_GB&lt;/code&gt; values. | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

