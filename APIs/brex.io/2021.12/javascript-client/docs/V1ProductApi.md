# KycApiDocumentation.V1ProductApi

All URIs are relative to *https://api.kompany.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productAvailability**](V1ProductApi.md#productAvailability) | **GET** /api/v1/product/availability/{sku}/{subjectId} | Retrieves a document availability result
[**productCatalog**](V1ProductApi.md#productCatalog) | **GET** /api/v1/product/catalog/{country} | Returns a catalog of products
[**productNotifier**](V1ProductApi.md#productNotifier) | **GET** /api/v1/product/notifier/{notifierId} | Returns metadata for a notifier
[**productNotifierCreate**](V1ProductApi.md#productNotifierCreate) | **POST** /api/v1/product/notifier/{orderId}/{type}/{uri} | Creates a notifier for an order
[**productOrder**](V1ProductApi.md#productOrder) | **POST** /api/v1/product/order/{sku}/{subjectId} | Places a product order
[**productOrderConcierge**](V1ProductApi.md#productOrderConcierge) | **POST** /api/v1/product/order/concierge | Places a concierge order
[**productOrderUbo**](V1ProductApi.md#productOrderUbo) | **POST** /api/v1/product/order/ubo | Places a UBO order
[**productOrderWithOption**](V1ProductApi.md#productOrderWithOption) | **POST** /api/v1/product/order/{sku}/{option}/{subjectId} | Places a product order
[**productRetrieve**](V1ProductApi.md#productRetrieve) | **GET** /api/v1/product/{orderId} | Retrieves the result of an order
[**productSearch**](V1ProductApi.md#productSearch) | **GET** /api/v1/product/search/{subjectId} | Returns a list of products
[**productStatus**](V1ProductApi.md#productStatus) | **GET** /api/v1/product/status/{orderId} | Returns metadata for a order
[**productUpdateAction**](V1ProductApi.md#productUpdateAction) | **POST** /api/v1/product/update/{action}/{orderId} | Updates metadata of an order



## productAvailability

> ProductAvailability200Response productAvailability(sku, subjectId)

Retrieves a document availability result

Check availability and valid options for a particular product for a particular company identfied by its id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let sku = "sku_example"; // String | SKU - 9 character value from a Product object
let subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
apiInstance.productAvailability(sku, subjectId, (error, data, response) => {
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
 **sku** | **String**| SKU - 9 character value from a Product object | 
 **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | 

### Return type

[**ProductAvailability200Response**](ProductAvailability200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCatalog

> ProductCatalog200Response productCatalog(country)

Returns a catalog of products

Returns a catalog of purchasable products available with some metadata for a particular country

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let country = "country_example"; // String | two letter country code in upper case
apiInstance.productCatalog(country, (error, data, response) => {
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
 **country** | **String**| two letter country code in upper case | 

### Return type

[**ProductCatalog200Response**](ProductCatalog200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productNotifier

> productNotifier(notifierId)

Returns metadata for a notifier

Queries and returns all metadata associated with a notifier identified by its notifer id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let notifierId = "notifierId_example"; // String | ID of the ProductOrderNotifier as returned from a /notifier POST call - 32 character hex value
apiInstance.productNotifier(notifierId, (error, data, response) => {
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
 **notifierId** | **String**| ID of the ProductOrderNotifier as returned from a /notifier POST call - 32 character hex value | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productNotifierCreate

> ProductNotifierCreate200Response productNotifierCreate(orderId, type, uri)

Creates a notifier for an order

Create a notifier for a particular order. Parameters can be supplied in the path

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
let type = "type_example"; // String | Type of the notifier - indicates the action the notifier will perform. Currently GET and POST are supported which performs an http(s) GET/POST to the supplied uri with appended notifierId= and orderId= parameters when the order processing is completed. Upon the POST request the order object is sent as a JSON body
let uri = "uri_example"; // String | URI of the notifier for the 'complete' action. Currently only a GET method HTTP(s) URL is supported. 1 to 250 characters long. Every slash in the URI must be replaced by a ~
apiInstance.productNotifierCreate(orderId, type, uri, (error, data, response) => {
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
 **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | 
 **type** | **String**| Type of the notifier - indicates the action the notifier will perform. Currently GET and POST are supported which performs an http(s) GET/POST to the supplied uri with appended notifierId&#x3D; and orderId&#x3D; parameters when the order processing is completed. Upon the POST request the order object is sent as a JSON body | 
 **uri** | **String**| URI of the notifier for the &#39;complete&#39; action. Currently only a GET method HTTP(s) URL is supported. 1 to 250 characters long. Every slash in the URI must be replaced by a ~ | 

### Return type

[**ProductNotifierCreate200Response**](ProductNotifierCreate200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOrder

> ProductOrder200Response productOrder(sku, subjectId)

Places a product order

Place an order for a particular product identified by its SKU for a particular company identified by its id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let sku = "sku_example"; // String | SKU - 9 character value from a Product object
let subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
apiInstance.productOrder(sku, subjectId, (error, data, response) => {
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
 **sku** | **String**| SKU - 9 character value from a Product object | 
 **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | 

### Return type

[**ProductOrder200Response**](ProductOrder200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOrderConcierge

> productOrderConcierge(opts)

Places a concierge order

Place an order for a concierge product

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let opts = {
  'companyName': "companyName_example", // String | Name of the company for which a document should be ordered. (Not required if subjectId is given)
  'contactEmail': "contactEmail_example", // String | Contact E-Mail, will be contacted if concierge costs are exceeding the threshhold configured on your plan
  'contactPhone': "contactPhone_example", // String | Contact phone, will be contacted if concierge costs are exceeding the threshhold configured on your plan
  'costConfirmation': true, // Boolean | If the concierge cost should require additional confirmation if a threshold is reached (configured on your plan)
  'country': "country_example", // String | Two letter ISO code of the country of the company
  'financialData': true, // Boolean | If you want financial data of the company to be retrieved
  'historicInformation': true, // Boolean | If you want historical data of the company to be retrieved
  'informationRequirements': "informationRequirements_example", // String | Requirements on what document or information should be provided. Please be very precise
  'locationInvestigation': true, // Boolean | If the companies residency should be investigated
  'priority': "priority_example", // String | Priority of order: standard/express are allowed
  'registerData': true, // Boolean | If you want register data of the company to be retrieved
  'registerNumber': "registerNumber_example", // String | Registration number of the company for which a document should be ordered. (Not required if subjectId is given)
  'subjectId': "subjectId_example" // String | Kompanyid of the company you want to place the order for
};
apiInstance.productOrderConcierge(opts, (error, data, response) => {
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
 **companyName** | **String**| Name of the company for which a document should be ordered. (Not required if subjectId is given) | [optional] 
 **contactEmail** | **String**| Contact E-Mail, will be contacted if concierge costs are exceeding the threshhold configured on your plan | [optional] 
 **contactPhone** | **String**| Contact phone, will be contacted if concierge costs are exceeding the threshhold configured on your plan | [optional] 
 **costConfirmation** | **Boolean**| If the concierge cost should require additional confirmation if a threshold is reached (configured on your plan) | [optional] 
 **country** | **String**| Two letter ISO code of the country of the company | [optional] 
 **financialData** | **Boolean**| If you want financial data of the company to be retrieved | [optional] 
 **historicInformation** | **Boolean**| If you want historical data of the company to be retrieved | [optional] 
 **informationRequirements** | **String**| Requirements on what document or information should be provided. Please be very precise | [optional] 
 **locationInvestigation** | **Boolean**| If the companies residency should be investigated | [optional] 
 **priority** | **String**| Priority of order: standard/express are allowed | [optional] 
 **registerData** | **Boolean**| If you want register data of the company to be retrieved | [optional] 
 **registerNumber** | **String**| Registration number of the company for which a document should be ordered. (Not required if subjectId is given) | [optional] 
 **subjectId** | **String**| Kompanyid of the company you want to place the order for | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## productOrderUbo

> productOrderUbo(subjectId, opts)

Places a UBO order

Place an order for a UBO (ultimate beneficial owner) discovery report

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let subjectId = "subjectId_example"; // String | KYC API Id (32 byte hexid) of the company you want to place the order for
let opts = {
  'callbackUrl': "callbackUrl_example", // String | An optional callback URL to which updates about the order will be sent (for instance if credits are exceeded)
  'credits': 3.4, // Number | Specify a maximum amount of credits which should be used. To disable use -1
  'includeDocs': true, // Boolean | Include purchase of register document to ubo report
  'levels': "levels_example", // String | Define a threshold for different levels of crawling
  'strategy': "strategy_example" // String | Choose a matching strategy. Available options (FULL,LEVELS)
};
apiInstance.productOrderUbo(subjectId, opts, (error, data, response) => {
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
 **subjectId** | **String**| KYC API Id (32 byte hexid) of the company you want to place the order for | 
 **callbackUrl** | **String**| An optional callback URL to which updates about the order will be sent (for instance if credits are exceeded) | [optional] 
 **credits** | **Number**| Specify a maximum amount of credits which should be used. To disable use -1 | [optional] 
 **includeDocs** | **Boolean**| Include purchase of register document to ubo report | [optional] 
 **levels** | **String**| Define a threshold for different levels of crawling | [optional] 
 **strategy** | **String**| Choose a matching strategy. Available options (FULL,LEVELS) | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## productOrderWithOption

> productOrderWithOption(sku, option, subjectId)

Places a product order

Place an order for a particular product identified by its SKU with a particular option for a particular company identified by its id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let sku = "sku_example"; // String | SKU - 9 character value from a Product object
let option = "option_example"; // String | Product option (e.g. Accounts year) from a previous Availability call
let subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
apiInstance.productOrderWithOption(sku, option, subjectId, (error, data, response) => {
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
 **sku** | **String**| SKU - 9 character value from a Product object | 
 **option** | **String**| Product option (e.g. Accounts year) from a previous Availability call | 
 **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productRetrieve

> ProductRetrieve200Response productRetrieve(orderId)

Retrieves the result of an order

Retrieves the document or structured data associated with a completed order identified with its order id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
apiInstance.productRetrieve(orderId, (error, data, response) => {
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
 **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | 

### Return type

[**ProductRetrieve200Response**](ProductRetrieve200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSearch

> [ProductSearch200ResponseInner] productSearch(subjectId)

Returns a list of products

Search for possible products for a particular company identified by its id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let subjectId = "subjectId_example"; // String | Subject (e.g. Company) ID - 32 character hex value
apiInstance.productSearch(subjectId, (error, data, response) => {
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
 **subjectId** | **String**| Subject (e.g. Company) ID - 32 character hex value | 

### Return type

[**[ProductSearch200ResponseInner]**](ProductSearch200ResponseInner.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productStatus

> productStatus(orderId)

Returns metadata for a order

Retrieve the current status of an order identified by its order id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
apiInstance.productStatus(orderId, (error, data, response) => {
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
 **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productUpdateAction

> productUpdateAction(action, orderId, opts)

Updates metadata of an order

Update an existing order identified by its order id

### Example

```javascript
import KycApiDocumentation from 'kyc_api_documentation';
let defaultClient = KycApiDocumentation.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new KycApiDocumentation.V1ProductApi();
let action = "action_example"; // String | The action you want to perform for the order
let orderId = "orderId_example"; // String | ID of the ProductOrder as returned from a /product/buy call - 32 character hex value
let opts = {
  'credits': 3.4 // Number | Specify an amount of credits which should be added to the order
};
apiInstance.productUpdateAction(action, orderId, opts, (error, data, response) => {
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
 **action** | **String**| The action you want to perform for the order | 
 **orderId** | **String**| ID of the ProductOrder as returned from a /product/buy call - 32 character hex value | 
 **credits** | **Number**| Specify an amount of credits which should be added to the order | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

