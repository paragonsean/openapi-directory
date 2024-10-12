# MarketplaceApi.SellersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getListSellers**](SellersApi.md#getListSellers) | **GET** /seller-register/pvt/sellers | List Sellers
[**getRetrieveSeller**](SellersApi.md#getRetrieveSeller) | **GET** /seller-register/pvt/sellers/{sellerId} | Get Seller data by ID
[**updateSeller**](SellersApi.md#updateSeller) | **PATCH** /seller-register/pvt/sellers/{sellerId} | Update Seller by Seller ID
[**upsertSellerRequest**](SellersApi.md#upsertSellerRequest) | **POST** /seller-register/pvt/sellers | Configure Seller Account



## getListSellers

> getListSellers(accountName, environment, accept, contentType, opts)

List Sellers

This endpoint lists all Sellers. This call&#39;s results can be filtered by [trade policies](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data) through the &#x60;sc&#x60; query param.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellersApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let opts = {
  'from': 0, // Number | The start number of pagination, being `0` the default value.
  'to': 100, // Number | The end number of pagination, being `100` the default value.
  'keyword': "'keyword'", // String | Search sellers by a keyword in `sellerId` or `sellerName`.
  'integration': "'vtex-seller'", // String | Filters sellers by the name of who made the integration, if VTEX or an external hub. The possible values for VTEX integrations are: `vtex-sellerportal`, `vtex-seller` and `vtex-franchise`.
  'group': "'Group'", // String | Groups are defined by keywords that group sellers into categories defined by the marketplace.
  'isActive': false, // Boolean | Enables to filter sellers that are active (`true`) or unactive (`false`) in the marketplace.
  'isBetterScope': false, // Boolean | The flag `isBetterScope` is used by the VTEX Checkout to simulate shopping carts, products, and shipping only in sellers with the field set as `true`, avoiding performance issues. When used as a query param, `isBetterScope` filters sellers that have the flag set as `true` or `false`.
  'isVtex': false, // Boolean | When set as `true`, the list returned will be of sellers who have a VTEX store configured. When set as `false`, the list will be of sellers who do not have a VTEX store configured.
  'sc': "'1'", // String | Filters sellers available for the marketplace's sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) indicated in this field.
  'sellerType': 1, // Number | Filters sellers by their type, which can be regular seller (`1`) or whitelabel seller (`2`).
  'sort': "'id:asc'" // String | Narrow the search filtering by the fields: `id`, `name` or `pendingoffers`. The list retrieved can be organized in an ascending (`asc`) or descending (`desc`) order. The standardized format is `{field}:{order}`, and the default value is `id:asc`.
};
apiInstance.getListSellers(accountName, environment, accept, contentType, opts, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **from** | **Number**| The start number of pagination, being &#x60;0&#x60; the default value. | [optional] [default to 0]
 **to** | **Number**| The end number of pagination, being &#x60;100&#x60; the default value. | [optional] [default to 100]
 **keyword** | **String**| Search sellers by a keyword in &#x60;sellerId&#x60; or &#x60;sellerName&#x60;. | [optional] [default to &#39;keyword&#39;]
 **integration** | **String**| Filters sellers by the name of who made the integration, if VTEX or an external hub. The possible values for VTEX integrations are: &#x60;vtex-sellerportal&#x60;, &#x60;vtex-seller&#x60; and &#x60;vtex-franchise&#x60;. | [optional] [default to &#39;vtex-seller&#39;]
 **group** | **String**| Groups are defined by keywords that group sellers into categories defined by the marketplace. | [optional] [default to &#39;Group&#39;]
 **isActive** | **Boolean**| Enables to filter sellers that are active (&#x60;true&#x60;) or unactive (&#x60;false&#x60;) in the marketplace. | [optional] [default to false]
 **isBetterScope** | **Boolean**| The flag &#x60;isBetterScope&#x60; is used by the VTEX Checkout to simulate shopping carts, products, and shipping only in sellers with the field set as &#x60;true&#x60;, avoiding performance issues. When used as a query param, &#x60;isBetterScope&#x60; filters sellers that have the flag set as &#x60;true&#x60; or &#x60;false&#x60;. | [optional] [default to false]
 **isVtex** | **Boolean**| When set as &#x60;true&#x60;, the list returned will be of sellers who have a VTEX store configured. When set as &#x60;false&#x60;, the list will be of sellers who do not have a VTEX store configured. | [optional] [default to false]
 **sc** | **String**| Filters sellers available for the marketplace&#39;s sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) indicated in this field. | [optional] [default to &#39;1&#39;]
 **sellerType** | **Number**| Filters sellers by their type, which can be regular seller (&#x60;1&#x60;) or whitelabel seller (&#x60;2&#x60;). | [optional] [default to 1]
 **sort** | **String**| Narrow the search filtering by the fields: &#x60;id&#x60;, &#x60;name&#x60; or &#x60;pendingoffers&#x60;. The list retrieved can be organized in an ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order. The standardized format is &#x60;{field}:{order}&#x60;, and the default value is &#x60;id:asc&#x60;. | [optional] [default to &#39;id:asc&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRetrieveSeller

> getRetrieveSeller(accountName, environment, sellerId, accept, contentType, opts)

Get Seller data by ID

Marketplace operator may call this endpoint to retrieve information about a specific seller by filtering by ID. It is also possible to filter results by sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) through the &#x60;sc&#x60; query param.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellersApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let opts = {
  'sc': "'1'" // String | Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) associated to the seller account created.
};
apiInstance.getRetrieveSeller(accountName, environment, sellerId, accept, contentType, opts, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace | [default to &#39;seller123&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **sc** | **String**| Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) associated to the seller account created. | [optional] [default to &#39;1&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateSeller

> updateSeller(accountName, environment, accept, contentType, sellerId, opts)

Update Seller by Seller ID

This endpoint allows marketplace operators to update the information of sellers connected to their account. You can replace a path&#39;s value with another value in order to update that single information. There is no need to fill all the body params available, only the one you wish to update.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellersApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account that belongs to the marketplace.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace
let opts = {
  'requestBodyInner': [new MarketplaceApi.RequestBodyInner()] // [RequestBodyInner] | array of objects
};
apiInstance.updateSeller(accountName, environment, accept, contentType, sellerId, opts, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace | [default to &#39;seller123&#39;]
 **requestBodyInner** | [**[RequestBodyInner]**](RequestBodyInner.md)| array of objects | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## upsertSellerRequest

> upsertSellerRequest(accountName, environment, accept, contentType, upsertSellerRequest)

Configure Seller Account

This endpoint is used by marketplace operators to configure the accounts of sellers that have already accepted the invitation to join their marketplaces.   For marketplaces to [add sellers](https://help.vtex.com/en/tutorial/adding-a-seller--tutorials_392) without the [Seller Invite](https://help.vtex.com/en/tutorial/marketplace-invited-sellers--6rb2FkcslmDueJ689Ulb9A) feature, call this endpoint directly.   This call includes all the information a seller needs to activate their account.

### Example

```javascript
import MarketplaceApi from 'marketplace_api';
let defaultClient = MarketplaceApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MarketplaceApi.SellersApi();
let accountName = "'apiexamples'"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let upsertSellerRequest = {"CSCIdentification":"cscidentification 123","account":"partner01","allowHybridPayments":false,"availableSalesChannels":[{"id":1,"isSelected":true,"name":"Loja Principal"},{"id":2,"isSelected":true,"name":"Terceira"},{"id":3,"isSelected":true,"name":"Marketplaces"}],"catalogSystemEndpoint":"https://pedrostore.vtexcommercestable.com.br/api/catalog_system/","channel":"marketplaceA","deliveryPolicy":"Describe delivery policy","description":"Seller A, from the B industry.","email":"seller@email.com","exchangeReturnPolicy":"Describe exchange and returns policy","fulfillmentEndpoint":"http://fulfillment.vtexcommerce.com.br/api/fulfillment?an=parceiro01","fulfillmentSellerId":"seller1","groups":[{"groups":[{"id":"8d845239bf1448dc8bc3ed3121837511","name":"long tail"},{"id":"b9bcd348ab9c4cec8285ff9485c27a72","name":"franchise accounts"}]}],"id":"testeMARCUS123","isActive":true,"isBetterScope":false,"isVtex":true,"name":"qamarketplace","password":null,"salesChannel":"1","score":0,"securityPrivacyPolicy":null,"sellerCommissionConfiguration":{"categoriesCommissionConfiguration":[],"freightCommissionPercentage":4,"productCommissionPercentage":3},"sellerType":1,"taxCode":"34444","trustPolicy":"Default","user":null}; // UpsertSellerRequest | 
apiInstance.upsertSellerRequest(accountName, environment, accept, contentType, upsertSellerRequest, (error, data, response) => {
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
 **accountName** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **upsertSellerRequest** | [**UpsertSellerRequest**](UpsertSellerRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

