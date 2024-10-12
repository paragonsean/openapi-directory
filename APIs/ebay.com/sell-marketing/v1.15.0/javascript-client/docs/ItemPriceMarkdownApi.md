# MarketingApi.ItemPriceMarkdownApi

All URIs are relative to *https://api.ebay.com/sell/marketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createItemPriceMarkdownPromotion**](ItemPriceMarkdownApi.md#createItemPriceMarkdownPromotion) | **POST** /item_price_markdown | 
[**deleteItemPriceMarkdownPromotion**](ItemPriceMarkdownApi.md#deleteItemPriceMarkdownPromotion) | **DELETE** /item_price_markdown/{promotion_id} | 
[**getItemPriceMarkdownPromotion**](ItemPriceMarkdownApi.md#getItemPriceMarkdownPromotion) | **GET** /item_price_markdown/{promotion_id} | 
[**updateItemPriceMarkdownPromotion**](ItemPriceMarkdownApi.md#updateItemPriceMarkdownPromotion) | **PUT** /item_price_markdown/{promotion_id} | 



## createItemPriceMarkdownPromotion

> Object createItemPriceMarkdownPromotion(opts)



This method creates an &lt;b&gt;item price markdown promotion&lt;/b&gt; (know simply as a \&quot;markdown promotion\&quot;) where a discount amount is applied directly to the items included the promotion. Discounts can be specified as either a monetary amount or a percentage off the standard sales price. eBay highlights promoted items by placing teasers for the items throughout the online sales flows.  &lt;p&gt;Unlike an &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/item_promotion/methods/createItemPromotion\&quot;&gt;item promotion&lt;/a&gt;, a markdown promotion does not require the buyer meet a \&quot;threshold\&quot; before the offer takes effect. With markdown promotions, all the buyer needs to do is purchase the item to receive the promotion benefit.&lt;/p&gt;  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Important:&lt;/b&gt; There are some restrictions for which listings are available for price markdown promotions. For details, see &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/static/overview.html#PM-requirements\&quot;&gt;Promotions Manager requirements and restrictions&lt;/a&gt;. &lt;br&gt;&lt;br&gt;In addition, we recommend you list items at competitive prices before including them in your markdown promotions. For an extensive list of pricing recommendations, see the &lt;b&gt;Growth&lt;/b&gt; tab in Seller Hub.&lt;/p&gt; &lt;p&gt;There are two ways to add items to markdown promotions:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;b&gt;Key-based promotions&lt;/b&gt; select items using either the listing IDs or inventory reference IDs of the items you want to promote. Note that if you use inventory reference IDs, you must specify both the &lt;b&gt;inventoryReferenceId&lt;/b&gt; and the associated &lt;b&gt;inventoryReferenceType&lt;/b&gt; of the item(s) you want to include the promotion.&lt;/li&gt;  &lt;li&gt;&lt;b&gt;Rule-based promotions&lt;/b&gt; select items using a list of eBay category IDs or seller Store category IDs. Rules can further constrain items in a promotion by minimum and maximum prices, brands, and item conditions.&lt;/li&gt;&lt;/ul&gt;  &lt;p&gt;New promotions must be created in either a &lt;code&gt;DRAFT&lt;/code&gt; or a &lt;code&gt;SCHEDULED&lt;/code&gt; state. Use the DRAFT state when you are initially creating a promotion and you want to be sure it&#39;s correctly configured before scheduling it to run. When you create a promotion, the promotion ID is returned in the &lt;b&gt;Location&lt;/b&gt; response header. Use this ID to reference the promotion in subsequent requests (such as to schedule a promotion that&#39;s in a DRAFT state).&lt;/p&gt;  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; Refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/promotions-manager.html\&quot;&gt;Promotions Manager&lt;/a&gt; in the &lt;i&gt;Selling Integration Guide&lt;/i&gt; for details and examples showing how to create and manage seller promotions.&lt;/p&gt;  &lt;p&gt;Markdown promotions are available on all eBay marketplaces. For more information, see &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/static/overview.html#PM-requirements\&quot;&gt;Promotions Manager requirements and restrictions&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.ItemPriceMarkdownApi();
let opts = {
  'itemPriceMarkdown': new MarketingApi.ItemPriceMarkdown() // ItemPriceMarkdown | This type defines the fields that describe an item price markdown promotion.
};
apiInstance.createItemPriceMarkdownPromotion(opts, (error, data, response) => {
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
 **itemPriceMarkdown** | [**ItemPriceMarkdown**](ItemPriceMarkdown.md)| This type defines the fields that describe an item price markdown promotion. | [optional] 

### Return type

**Object**

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteItemPriceMarkdownPromotion

> deleteItemPriceMarkdownPromotion(promotionId)



This method deletes the item price markdown promotion specified by the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.  &lt;br&gt;&lt;br&gt;You can delete any promotion with the exception of those that are currently active (RUNNING). To end a running promotion, call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/item_price_markdown/methods/updateItemPriceMarkdownPromotion\&quot;&gt;updateItemPriceMarkdownPromotion&lt;/a&gt; and adjust the &lt;b&gt;endDate&lt;/b&gt; field as appropriate.

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.ItemPriceMarkdownApi();
let promotionId = "promotionId_example"; // String | This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code>
apiInstance.deleteItemPriceMarkdownPromotion(promotionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotionId** | **String**| This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt; | 

### Return type

null (empty response body)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getItemPriceMarkdownPromotion

> ItemPriceMarkdown getItemPriceMarkdownPromotion(promotionId)



This method returns the complete details of the item price markdown promotion that&#39;s indicated by the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. &lt;br&gt;&lt;br&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.ItemPriceMarkdownApi();
let promotionId = "promotionId_example"; // String | This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code>
apiInstance.getItemPriceMarkdownPromotion(promotionId, (error, data, response) => {
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
 **promotionId** | **String**| This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt; | 

### Return type

[**ItemPriceMarkdown**](ItemPriceMarkdown.md)

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateItemPriceMarkdownPromotion

> Object updateItemPriceMarkdownPromotion(promotionId, opts)



This method updates the specified item price markdown promotion with the new configuration that you supply in the payload of the request. Specify the promotion you want to update using the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.  &lt;br&gt;&lt;br&gt;When updating a promotion, supply all the fields that you used to configure the original promotion (and not just the fields you are updating). eBay replaces the specified promotion with the values you supply in the update request and if you don&#39;t pass a field that currently has a value, the update request fails.  &lt;br&gt;&lt;br&gt;The parameters you are allowed to update with this request depend on the status of the promotion you&#39;re updating:  &lt;ul&gt;&lt;li&gt;DRAFT or SCHEDULED promotions: You can update any of the parameters in these promotions that have not yet started to run, including the &lt;b&gt;discountRules&lt;/b&gt;.&lt;/li&gt; &lt;li&gt;RUNNING promotions: You can change the &lt;b&gt;endDate&lt;/b&gt; and the item&#39;s inventory but you cannot change the promotional discount or the promotion&#39;s start date.&lt;/li&gt; &lt;li&gt;ENDED promotions: Nothing can be changed.&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import MarketingApi from 'marketing_api';
let defaultClient = MarketingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MarketingApi.ItemPriceMarkdownApi();
let promotionId = "promotionId_example"; // String | This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \"at sign\" (<b>@</b>).  <br><br>The ID of the promotion (<b>promotionId</b>) is a unique eBay-assigned value that's generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. <br><br><b>Example:</b> <code>1********5@EBAY_US</code>
let opts = {
  'itemPriceMarkdown': new MarketingApi.ItemPriceMarkdown() // ItemPriceMarkdown | This type defines the fields that describe an item price markdown promotion.
};
apiInstance.updateItemPriceMarkdownPromotion(promotionId, opts, (error, data, response) => {
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
 **promotionId** | **String**| This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt; | 
 **itemPriceMarkdown** | [**ItemPriceMarkdown**](ItemPriceMarkdown.md)| This type defines the fields that describe an item price markdown promotion. | [optional] 

### Return type

**Object**

### Authorization

[api_auth](../README.md#api_auth), [api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

