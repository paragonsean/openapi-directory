# MarketplaceApi.MatchedOffersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProductoffers**](MatchedOffersApi.md#getProductoffers) | **GET** /offer-manager/pvt/product/{productId} | Get Matched Offer&#39;s Data by Product ID
[**getSKUoffers**](MatchedOffersApi.md#getSKUoffers) | **GET** /offer-manager/pvt/product/{productId}/sku/{skuId} | Get Matched Offer&#39;s Data by SKU ID
[**getofferslist**](MatchedOffersApi.md#getofferslist) | **GET** /offer-manager/pvt/offers | Get Matched Offers List



## getProductoffers

> getProductoffers(accountName, environment, contentType, accept, productId)

Get Matched Offer&#39;s Data by Product ID

Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.   This endpoint retrieves the available offers for a speciic Product ID in the marketplace&#39;s catalog. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace operator, and are currently active in its catalog.   The call returns a list of offers for that ID, that contain the following data:   - Seller that sells the SKU   - Correspondent SKU ID   - SKU&#39;s price value   - Inventory level   - Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) that it is available at.

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

let apiInstance = new MarketplaceApi.MatchedOffersApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let productId = "'123456'"; // String | A string that identifies the seller's product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications.
apiInstance.getProductoffers(accountName, environment, contentType, accept, productId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications. | [default to &#39;123456&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSKUoffers

> getSKUoffers(accountName, environment, contentType, accept, productId, skuId)

Get Matched Offer&#39;s Data by SKU ID

Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.   This endpoint retrieves the available offers for a speciic SKU ID in the marketplace&#39;s catalog. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace operator, and are currently active in its catalog.   The call returns a list of offers for that ID, that contain the following data:   - Seller that sells the SKU   - Correspondent SKU ID   - SKU&#39;s price value   - Inventory level   - Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) that it is available at.

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

let apiInstance = new MarketplaceApi.MatchedOffersApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let productId = "'123456'"; // String | A string that identifies the seller's product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications.
let skuId = "'1234'"; // String | A string that identifies the seller's SKU. This is the ID that the marketplace will use for all references to this SKU, such as price and inventory notifications.
apiInstance.getSKUoffers(accountName, environment, contentType, accept, productId, skuId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL. | [default to &#39;apiexamples&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications. | [default to &#39;123456&#39;]
 **skuId** | **String**| A string that identifies the seller&#39;s SKU. This is the ID that the marketplace will use for all references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getofferslist

> [GetMatchedOffersResponse] getofferslist(accountName, contentType, environment, accept, opts)

Get Matched Offers List

Offers are seller&#39;s products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.    This endpoint retrieves the available offers in a marketplace. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace, and are currently in its catalog.   It is possible to filter the search through the following parameters:   - rows  - sort   - start   - fq

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

let apiInstance = new MarketplaceApi.MatchedOffersApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let environment = "'vtexcommercestable'"; // String | Environment to use. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'sort': "availability,desc", // String | Criteria used to sort the list of offers. For sorting values in ascending order, use `asc`, while for descending order, use `desc`. To fill in the field, insert the sorting criteria, followed by 'asc', or 'desc', separated by a comma. You can sort by the following criteria:   - **price:** sorts offers by price. *Ascending* goes from lowest to highest price, while *Descending* goes from highest to lowest price.   - **name:** sorts offers by *productName*, in alphabetical order. *Ascending* goes from *A* to *Z*, while *Descending* goes from *Z* to *A*.   - **availability:** availability in the sales channel (sc). The default value is 1.   Ex. sort=availability,desc   Ex. sort=name,asc   Ex. price,desc
  'rows': 20, // Number | Number of rows included in the response. Each row corresponds to a single offer. The default amount of rows in the response is 1, and the maximum amount is 50. To have more than one offer listed in the response, please add the `rows` parameter with a number greater than 1.
  'start': 21, // Number | Number corresponding to the row from which the offer list will begin, used for pagination. Filters the list of offers by retrieving the offers starting from the row defined. The default value is 0, if the param is not included in the call.
  'fq': "skuId:172" // String | This filter query can be used to filter offers by the criteria described below. It should be filled in by following the format: `fq={{criteriaName}}:{{criteriaValue}}`.   - **productId:** integer of the product ID   - **productName:** string of the product's name   - **skuId:** integer of the SKU ID   - **eanId:** string of the EAN ID   - **refId:** string of the Ref ID   - **categoryId:** integer of the category ID   - **brandId:** integer of the brand ID   - **sellerId:** string of the seller ID   - **sc:** integer of the sales channel's ID (trade policy in VTEX)   Ex: skuId:172   Ex: categoryId:13   Ex. productName:Product example-123
};
apiInstance.getofferslist(accountName, contentType, environment, accept, opts, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to &#39;apiexamples&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **environment** | **String**| Environment to use. Used as part of the URL. | [default to &#39;vtexcommercestable&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **sort** | **String**| Criteria used to sort the list of offers. For sorting values in ascending order, use &#x60;asc&#x60;, while for descending order, use &#x60;desc&#x60;. To fill in the field, insert the sorting criteria, followed by &#39;asc&#39;, or &#39;desc&#39;, separated by a comma. You can sort by the following criteria:   - **price:** sorts offers by price. *Ascending* goes from lowest to highest price, while *Descending* goes from highest to lowest price.   - **name:** sorts offers by *productName*, in alphabetical order. *Ascending* goes from *A* to *Z*, while *Descending* goes from *Z* to *A*.   - **availability:** availability in the sales channel (sc). The default value is 1.   Ex. sort&#x3D;availability,desc   Ex. sort&#x3D;name,asc   Ex. price,desc | [optional] 
 **rows** | **Number**| Number of rows included in the response. Each row corresponds to a single offer. The default amount of rows in the response is 1, and the maximum amount is 50. To have more than one offer listed in the response, please add the &#x60;rows&#x60; parameter with a number greater than 1. | [optional] [default to 20]
 **start** | **Number**| Number corresponding to the row from which the offer list will begin, used for pagination. Filters the list of offers by retrieving the offers starting from the row defined. The default value is 0, if the param is not included in the call. | [optional] [default to 21]
 **fq** | **String**| This filter query can be used to filter offers by the criteria described below. It should be filled in by following the format: &#x60;fq&#x3D;{{criteriaName}}:{{criteriaValue}}&#x60;.   - **productId:** integer of the product ID   - **productName:** string of the product&#39;s name   - **skuId:** integer of the SKU ID   - **eanId:** string of the EAN ID   - **refId:** string of the Ref ID   - **categoryId:** integer of the category ID   - **brandId:** integer of the brand ID   - **sellerId:** string of the seller ID   - **sc:** integer of the sales channel&#39;s ID (trade policy in VTEX)   Ex: skuId:172   Ex: categoryId:13   Ex. productName:Product example-123 | [optional] 

### Return type

[**[GetMatchedOffersResponse]**](GetMatchedOffersResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

