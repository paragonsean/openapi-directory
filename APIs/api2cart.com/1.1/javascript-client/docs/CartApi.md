# SwaggerApi2Cart.CartApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bridgeDownload**](CartApi.md#bridgeDownload) | **GET** /bridge.download.file | 
[**cartBridge**](CartApi.md#cartBridge) | **GET** /cart.bridge.json | 
[**cartCatalogPriceRulesCount**](CartApi.md#cartCatalogPriceRulesCount) | **GET** /cart.catalog_price_rules.count.json | 
[**cartCatalogPriceRulesList**](CartApi.md#cartCatalogPriceRulesList) | **GET** /cart.catalog_price_rules.list.json | 
[**cartClearCache**](CartApi.md#cartClearCache) | **POST** /cart.clear_cache.json | 
[**cartConfig**](CartApi.md#cartConfig) | **GET** /cart.config.json | 
[**cartConfigUpdate**](CartApi.md#cartConfigUpdate) | **PUT** /cart.config.update.json | 
[**cartCouponAdd**](CartApi.md#cartCouponAdd) | **POST** /cart.coupon.add.json | 
[**cartCouponConditionAdd**](CartApi.md#cartCouponConditionAdd) | **POST** /cart.coupon.condition.add.json | 
[**cartCouponCount**](CartApi.md#cartCouponCount) | **GET** /cart.coupon.count.json | 
[**cartCouponDelete**](CartApi.md#cartCouponDelete) | **DELETE** /cart.coupon.delete.json | 
[**cartCouponList**](CartApi.md#cartCouponList) | **GET** /cart.coupon.list.json | 
[**cartCreate**](CartApi.md#cartCreate) | **POST** /cart.create.json | 
[**cartDelete**](CartApi.md#cartDelete) | **DELETE** /cart.delete.json | 
[**cartDisconnect**](CartApi.md#cartDisconnect) | **GET** /cart.disconnect.json | 
[**cartGiftcardAdd**](CartApi.md#cartGiftcardAdd) | **POST** /cart.giftcard.add.json | 
[**cartGiftcardCount**](CartApi.md#cartGiftcardCount) | **GET** /cart.giftcard.count.json | 
[**cartGiftcardList**](CartApi.md#cartGiftcardList) | **GET** /cart.giftcard.list.json | 
[**cartInfo**](CartApi.md#cartInfo) | **GET** /cart.info.json | 
[**cartList**](CartApi.md#cartList) | **GET** /cart.list.json | 
[**cartMetaDataList**](CartApi.md#cartMetaDataList) | **GET** /cart.meta_data.list.json | 
[**cartMetaDataSet**](CartApi.md#cartMetaDataSet) | **POST** /cart.meta_data.set.json | 
[**cartMetaDataUnset**](CartApi.md#cartMetaDataUnset) | **DELETE** /cart.meta_data.unset.json | 
[**cartMethods**](CartApi.md#cartMethods) | **GET** /cart.methods.json | 
[**cartPluginList**](CartApi.md#cartPluginList) | **GET** /cart.plugin.list.json | 
[**cartScriptAdd**](CartApi.md#cartScriptAdd) | **POST** /cart.script.add.json | 
[**cartScriptDelete**](CartApi.md#cartScriptDelete) | **DELETE** /cart.script.delete.json | 
[**cartScriptList**](CartApi.md#cartScriptList) | **GET** /cart.script.list.json | 
[**cartShippingZonesList**](CartApi.md#cartShippingZonesList) | **GET** /cart.shipping_zones.list.json | 
[**cartValidate**](CartApi.md#cartValidate) | **GET** /cart.validate.json | 



## bridgeDownload

> File bridgeDownload(opts)



Download bridge for store

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'whitelabel': false // Boolean | Identifies if there is a necessity to download whitelabel bridge.
};
apiInstance.bridgeDownload(opts, (error, data, response) => {
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
 **whitelabel** | **Boolean**| Identifies if there is a necessity to download whitelabel bridge. | [optional] [default to false]

### Return type

**File**

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip


## cartBridge

> CartBridge200Response cartBridge()



Get bridge key and store key

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
apiInstance.cartBridge((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CartBridge200Response**](CartBridge200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartCatalogPriceRulesCount

> CartCatalogPriceRulesCount200Response cartCatalogPriceRulesCount()



Get count of cart catalog price rules discounts.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
apiInstance.cartCatalogPriceRulesCount((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CartCatalogPriceRulesCount200Response**](CartCatalogPriceRulesCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartCatalogPriceRulesList

> ModelResponseCartCatalogPriceRulesList cartCatalogPriceRulesList(opts)



Get cart catalog price rules discounts.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'ids': "ids_example", // String | Retrieves  catalog_price_rules by ids
  'params': "'id,name,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartCatalogPriceRulesList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **ids** | **String**| Retrieves  catalog_price_rules by ids | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartCatalogPriceRulesList**](ModelResponseCartCatalogPriceRulesList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartClearCache

> CartClearCache200Response cartClearCache(cacheType)



Clear cache on store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let cacheType = "cacheType_example"; // String | Defines which cache should be cleared.
apiInstance.cartClearCache(cacheType, (error, data, response) => {
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
 **cacheType** | **String**| Defines which cache should be cleared. | 

### Return type

[**CartClearCache200Response**](CartClearCache200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartConfig

> CartConfig200Response cartConfig(opts)



Get list of cart configs

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'params': "'store_name,store_url,db_prefix'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartConfig(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;store_name,store_url,db_prefix&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**CartConfig200Response**](CartConfig200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartConfigUpdate

> CartConfigUpdate200Response cartConfigUpdate(cartConfigUpdate)



Use this API method to update custom data in client database.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let cartConfigUpdate = new SwaggerApi2Cart.CartConfigUpdate(); // CartConfigUpdate | 
apiInstance.cartConfigUpdate(cartConfigUpdate, (error, data, response) => {
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
 **cartConfigUpdate** | [**CartConfigUpdate**](CartConfigUpdate.md)|  | 

### Return type

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cartCouponAdd

> CartCouponAdd200Response cartCouponAdd(cartCouponAdd)



Create new coupon

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let cartCouponAdd = new SwaggerApi2Cart.CartCouponAdd(); // CartCouponAdd | 
apiInstance.cartCouponAdd(cartCouponAdd, (error, data, response) => {
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
 **cartCouponAdd** | [**CartCouponAdd**](CartCouponAdd.md)|  | 

### Return type

[**CartCouponAdd200Response**](CartCouponAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cartCouponConditionAdd

> BasketLiveShippingServiceDelete200Response cartCouponConditionAdd(couponId, entity, key, operator, value, opts)



Create new coupon condition

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let couponId = "couponId_example"; // String | Coupon Id
let entity = "entity_example"; // String | Defines condition entity type
let key = "key_example"; // String | Defines condition entity attribute key
let operator = "operator_example"; // String | Defines condition operator
let value = "value_example"; // String | Defines condition value, can be comma separated according to the operator.
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'target': "'coupon_prerequisite'" // String | Defines condition operator
};
apiInstance.cartCouponConditionAdd(couponId, entity, key, operator, value, opts, (error, data, response) => {
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
 **couponId** | **String**| Coupon Id | 
 **entity** | **String**| Defines condition entity type | 
 **key** | **String**| Defines condition entity attribute key | 
 **operator** | **String**| Defines condition operator | 
 **value** | **String**| Defines condition value, can be comma separated according to the operator. | 
 **storeId** | **String**| Store Id | [optional] 
 **target** | **String**| Defines condition operator | [optional] [default to &#39;coupon_prerequisite&#39;]

### Return type

[**BasketLiveShippingServiceDelete200Response**](BasketLiveShippingServiceDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartCouponCount

> CartCouponCount200Response cartCouponCount(opts)



Get cart coupons count.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'dateStartFrom': "dateStartFrom_example", // String | Filter entity by date_start (greater or equal)
  'dateStartTo': "dateStartTo_example", // String | Filter entity by date_start (less or equal)
  'dateEndFrom': "dateEndFrom_example", // String | Filter entity by date_end (greater or equal)
  'dateEndTo': "dateEndTo_example", // String | Filter entity by date_end (less or equal)
  'avail': true // Boolean | Defines category's visibility status
};
apiInstance.cartCouponCount(opts, (error, data, response) => {
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
 **storeId** | **String**| Store Id | [optional] 
 **dateStartFrom** | **String**| Filter entity by date_start (greater or equal) | [optional] 
 **dateStartTo** | **String**| Filter entity by date_start (less or equal) | [optional] 
 **dateEndFrom** | **String**| Filter entity by date_end (greater or equal) | [optional] 
 **dateEndTo** | **String**| Filter entity by date_end (less or equal) | [optional] 
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true]

### Return type

[**CartCouponCount200Response**](CartCouponCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartCouponDelete

> AttributeDelete200Response cartCouponDelete(id, opts)



Delete coupon

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.cartCouponDelete(id, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartCouponList

> ModelResponseCartCouponList cartCouponList(opts)



Get cart coupon discounts.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'couponsIds': "couponsIds_example", // String | Filter coupons by ids
  'storeId': "storeId_example", // String | Filter coupons by store id
  'dateStartFrom': "dateStartFrom_example", // String | Filter entity by date_start (greater or equal)
  'dateStartTo': "dateStartTo_example", // String | Filter entity by date_start (less or equal)
  'dateEndFrom': "dateEndFrom_example", // String | Filter entity by date_end (greater or equal)
  'dateEndTo': "dateEndTo_example", // String | Filter entity by date_end (less or equal)
  'avail': true, // Boolean | Filter coupons by avail status
  'langId': "langId_example", // String | Language id
  'params': "'id,code,name,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartCouponList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **couponsIds** | **String**| Filter coupons by ids | [optional] 
 **storeId** | **String**| Filter coupons by store id | [optional] 
 **dateStartFrom** | **String**| Filter entity by date_start (greater or equal) | [optional] 
 **dateStartTo** | **String**| Filter entity by date_start (less or equal) | [optional] 
 **dateEndFrom** | **String**| Filter entity by date_end (greater or equal) | [optional] 
 **dateEndTo** | **String**| Filter entity by date_end (less or equal) | [optional] 
 **avail** | **Boolean**| Filter coupons by avail status | [optional] 
 **langId** | **String**| Language id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,code,name,description&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartCouponList**](ModelResponseCartCouponList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartCreate

> AccountCartAdd200Response cartCreate(cartId, storeUrl, etsyClientId, etsyRefreshToken, storeId, opts)



Add store to the account

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let cartId = "cartId_example"; // String | Store’s identifier which you can get from cart_list method
let storeUrl = "storeUrl_example"; // String | A web address of a store that you would like to connect to API2Cart
let etsyClientId = "etsyClientId_example"; // String | Etsy Client Id
let etsyRefreshToken = "etsyRefreshToken_example"; // String | Etsy Refresh token
let storeId = "storeId_example"; // String | Store Id
let opts = {
  'bridgeUrl': "bridgeUrl_example", // String | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store)
  'storeRoot': "storeRoot_example", // String | Absolute path to the store root directory (used with \"bridge_url\" parameter)
  'storeKey': "storeKey_example", // String | Set this parameter if bridge is already uploaded to store
  'sharedSecret': "sharedSecret_example", // String | Shared secret
  'validateVersion': false, // Boolean | Specify if api2cart should validate cart version
  'verify': true, // Boolean | Enables or disables cart's verification
  'dbTablesPrefix': "dbTablesPrefix_example", // String | DB tables prefix
  'ftpHost': "ftpHost_example", // String | FTP connection host
  'ftpUser': "ftpUser_example", // String | FTP User
  'ftpPassword': "ftpPassword_example", // String | FTP Password
  'ftpPort': 56, // Number | FTP Port
  'ftpStoreDir': "ftpStoreDir_example", // String | FTP Store dir
  'apiKey3dcart': "apiKey3dcart_example", // String | 3DCart API Key
  'adminAccount': "adminAccount_example", // String | It's a BigCommerce account for which API is enabled
  'apiPath': "apiPath_example", // String | BigCommerce API URL
  'apiKey': "apiKey_example", // String | Bigcommerce API Key
  'clientId': "clientId_example", // String | Client ID of the requesting app
  'accessToken': "accessToken_example", // String | Access token authorizing the app to access resources on behalf of a user
  'context': "context_example", // String | API Path section unique to the store
  'accessToken2': "accessToken_example", // String | Access token authorizing the app to access resources on behalf of a user
  'apiKeyShopify': "apiKeyShopify_example", // String | Shopify API Key
  'apiPassword': "apiPassword_example", // String | Shopify API Password
  'accessTokenShopify': "accessTokenShopify_example", // String | Access token authorizing the app to access resources on behalf of a user
  'apiKey2': "apiKey_example", // String | Neto API Key
  'apiUsername': "apiUsername_example", // String | Neto User Name
  'encryptedPassword': "encryptedPassword_example", // String | Volusion API Password
  'login': "login_example", // String | It's a Volusion account for which API is enabled
  'apiUserAdnsf': "apiUserAdnsf_example", // String | It's a AspDotNetStorefront account for which API is available
  'apiPass': "apiPass_example", // String | AspDotNetStorefront API Password
  'privateKey': "privateKey_example", // String | 3DCart Application Private Key
  'appToken': "appToken_example", // String | 3DCart Token from Application
  'etsyKeystring': "etsyKeystring_example", // String | Etsy keystring
  'etsySharedSecret': "etsySharedSecret_example", // String | Etsy shared secret
  'tokenSecret': "tokenSecret_example", // String | Secret token authorizing the app to access resources on behalf of a user
  'ebayClientId': "ebayClientId_example", // String | Application ID (AppID).
  'ebayClientSecret': "ebayClientSecret_example", // String | Shared Secret from eBay application
  'ebayRuname': "ebayRuname_example", // String | The RuName value that eBay assigns to your application.
  'ebayAccessToken': "ebayAccessToken_example", // String | Used to authenticate API requests.
  'ebayRefreshToken': "ebayRefreshToken_example", // String | Used to renew the access token.
  'ebayEnvironment': "'production'", // String | eBay environment
  'ebaySiteId': 0, // Number | eBay global ID
  'dwClientId': "dwClientId_example", // String | Demandware client id
  'dwApiPass': "dwApiPass_example", // String | Demandware api password
  'demandwareUserName': "demandwareUserName_example", // String | Demandware user name
  'demandwareUserPassword': "demandwareUserPassword_example", // String | Demandware user password
  'sellerId': "sellerId_example", // String | Seller Id
  'amazonSecretKey': "amazonSecretKey_example", // String | Amazon Secret Key
  'amazonAccessKeyId': "amazonAccessKeyId_example", // String | Amazon Secret Key Id
  'marketplacesIds': "marketplacesIds_example", // String | Comma separated marketplaces ids
  'environment': "'production'", // String | 
  'hybrisClientId': "hybrisClientId_example", // String | Omni Commerce Connector Client ID
  'hybrisClientSecret': "hybrisClientSecret_example", // String | Omni Commerce Connector Client Secret
  'hybrisUsername': "hybrisUsername_example", // String | User Name
  'hybrisPassword': "hybrisPassword_example", // String | User password
  'hybrisWebsites': ["null"], // [String] | Websites to stores mapping data
  'walmartClientId': "walmartClientId_example", // String | Walmart client ID
  'walmartClientSecret': "walmartClientSecret_example", // String | Walmart client secret
  'walmartEnvironment': "'production'", // String | Walmart environment
  'walmartChannelType': "walmartChannelType_example", // String | Walmart WM_CONSUMER.CHANNEL.TYPE header
  'lightspeedApiKey': "lightspeedApiKey_example", // String | LightSpeed api key
  'lightspeedApiSecret': "lightspeedApiSecret_example", // String | LightSpeed api secret
  'shopwareAccessKey': "shopwareAccessKey_example", // String | Shopware access key
  'shopwareApiKey': "shopwareApiKey_example", // String | Shopware api key
  'shopwareApiSecret': "shopwareApiSecret_example", // String | Shopware client secret access key
  'commercehqApiKey': "commercehqApiKey_example", // String | CommerceHQ api key
  'commercehqApiPassword': "commercehqApiPassword_example", // String | CommerceHQ api password
  '_3dcartPrivateKey': "_3dcartPrivateKey_example", // String | 3DCart Private Key
  '_3dcartAccessToken': "_3dcartAccessToken_example", // String | 3DCart Token
  'wcConsumerKey': "wcConsumerKey_example", // String | Woocommerce consumer key
  'wcConsumerSecret': "wcConsumerSecret_example", // String | Woocommerce consumer secret
  'magentoConsumerKey': "magentoConsumerKey_example", // String | Magento Consumer Key
  'magentoConsumerSecret': "magentoConsumerSecret_example", // String | Magento Consumer Secret
  'magentoAccessToken': "magentoAccessToken_example", // String | Magento Access Token
  'magentoTokenSecret': "magentoTokenSecret_example", // String | Magento Token Secret
  'prestashopWebserviceKey': "prestashopWebserviceKey_example", // String | Prestashop webservice key
  'wixAppId': "wixAppId_example", // String | Wix App ID
  'wixAppSecretKey': "wixAppSecretKey_example", // String | Wix App Secret Key
  'wixRefreshToken': "wixRefreshToken_example", // String | Wix refresh token
  'mercadoLibreAppId': "mercadoLibreAppId_example", // String | Mercado Libre App ID
  'mercadoLibreAppSecretKey': "mercadoLibreAppSecretKey_example", // String | Mercado Libre App Secret Key
  'mercadoLibreRefreshToken': "mercadoLibreRefreshToken_example", // String | Mercado Libre Refresh Token
  'zidClientId': 56, // Number | Zid Client ID
  'zidClientSecret': "zidClientSecret_example", // String | Zid Client Secret
  'zidAccessToken': "zidAccessToken_example", // String | Zid Access Token
  'zidAuthorization': "zidAuthorization_example", // String | Zid Authorization
  'zidRefreshToken': "zidRefreshToken_example" // String | Zid refresh token
};
apiInstance.cartCreate(cartId, storeUrl, etsyClientId, etsyRefreshToken, storeId, opts, (error, data, response) => {
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
 **cartId** | **String**| Store’s identifier which you can get from cart_list method | 
 **storeUrl** | **String**| A web address of a store that you would like to connect to API2Cart | 
 **etsyClientId** | **String**| Etsy Client Id | 
 **etsyRefreshToken** | **String**| Etsy Refresh token | 
 **storeId** | **String**| Store Id | 
 **bridgeUrl** | **String**| This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] 
 **storeRoot** | **String**| Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] 
 **storeKey** | **String**| Set this parameter if bridge is already uploaded to store | [optional] 
 **sharedSecret** | **String**| Shared secret | [optional] 
 **validateVersion** | **Boolean**| Specify if api2cart should validate cart version | [optional] [default to false]
 **verify** | **Boolean**| Enables or disables cart&#39;s verification | [optional] [default to true]
 **dbTablesPrefix** | **String**| DB tables prefix | [optional] 
 **ftpHost** | **String**| FTP connection host | [optional] 
 **ftpUser** | **String**| FTP User | [optional] 
 **ftpPassword** | **String**| FTP Password | [optional] 
 **ftpPort** | **Number**| FTP Port | [optional] 
 **ftpStoreDir** | **String**| FTP Store dir | [optional] 
 **apiKey3dcart** | **String**| 3DCart API Key | [optional] 
 **adminAccount** | **String**| It&#39;s a BigCommerce account for which API is enabled | [optional] 
 **apiPath** | **String**| BigCommerce API URL | [optional] 
 **apiKey** | **String**| Bigcommerce API Key | [optional] 
 **clientId** | **String**| Client ID of the requesting app | [optional] 
 **accessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **context** | **String**| API Path section unique to the store | [optional] 
 **accessToken2** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **apiKeyShopify** | **String**| Shopify API Key | [optional] 
 **apiPassword** | **String**| Shopify API Password | [optional] 
 **accessTokenShopify** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **apiKey2** | **String**| Neto API Key | [optional] 
 **apiUsername** | **String**| Neto User Name | [optional] 
 **encryptedPassword** | **String**| Volusion API Password | [optional] 
 **login** | **String**| It&#39;s a Volusion account for which API is enabled | [optional] 
 **apiUserAdnsf** | **String**| It&#39;s a AspDotNetStorefront account for which API is available | [optional] 
 **apiPass** | **String**| AspDotNetStorefront API Password | [optional] 
 **privateKey** | **String**| 3DCart Application Private Key | [optional] 
 **appToken** | **String**| 3DCart Token from Application | [optional] 
 **etsyKeystring** | **String**| Etsy keystring | [optional] 
 **etsySharedSecret** | **String**| Etsy shared secret | [optional] 
 **tokenSecret** | **String**| Secret token authorizing the app to access resources on behalf of a user | [optional] 
 **ebayClientId** | **String**| Application ID (AppID). | [optional] 
 **ebayClientSecret** | **String**| Shared Secret from eBay application | [optional] 
 **ebayRuname** | **String**| The RuName value that eBay assigns to your application. | [optional] 
 **ebayAccessToken** | **String**| Used to authenticate API requests. | [optional] 
 **ebayRefreshToken** | **String**| Used to renew the access token. | [optional] 
 **ebayEnvironment** | **String**| eBay environment | [optional] [default to &#39;production&#39;]
 **ebaySiteId** | **Number**| eBay global ID | [optional] [default to 0]
 **dwClientId** | **String**| Demandware client id | [optional] 
 **dwApiPass** | **String**| Demandware api password | [optional] 
 **demandwareUserName** | **String**| Demandware user name | [optional] 
 **demandwareUserPassword** | **String**| Demandware user password | [optional] 
 **sellerId** | **String**| Seller Id | [optional] 
 **amazonSecretKey** | **String**| Amazon Secret Key | [optional] 
 **amazonAccessKeyId** | **String**| Amazon Secret Key Id | [optional] 
 **marketplacesIds** | **String**| Comma separated marketplaces ids | [optional] 
 **environment** | **String**|  | [optional] [default to &#39;production&#39;]
 **hybrisClientId** | **String**| Omni Commerce Connector Client ID | [optional] 
 **hybrisClientSecret** | **String**| Omni Commerce Connector Client Secret | [optional] 
 **hybrisUsername** | **String**| User Name | [optional] 
 **hybrisPassword** | **String**| User password | [optional] 
 **hybrisWebsites** | [**[String]**](String.md)| Websites to stores mapping data | [optional] 
 **walmartClientId** | **String**| Walmart client ID | [optional] 
 **walmartClientSecret** | **String**| Walmart client secret | [optional] 
 **walmartEnvironment** | **String**| Walmart environment | [optional] [default to &#39;production&#39;]
 **walmartChannelType** | **String**| Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] 
 **lightspeedApiKey** | **String**| LightSpeed api key | [optional] 
 **lightspeedApiSecret** | **String**| LightSpeed api secret | [optional] 
 **shopwareAccessKey** | **String**| Shopware access key | [optional] 
 **shopwareApiKey** | **String**| Shopware api key | [optional] 
 **shopwareApiSecret** | **String**| Shopware client secret access key | [optional] 
 **commercehqApiKey** | **String**| CommerceHQ api key | [optional] 
 **commercehqApiPassword** | **String**| CommerceHQ api password | [optional] 
 **_3dcartPrivateKey** | **String**| 3DCart Private Key | [optional] 
 **_3dcartAccessToken** | **String**| 3DCart Token | [optional] 
 **wcConsumerKey** | **String**| Woocommerce consumer key | [optional] 
 **wcConsumerSecret** | **String**| Woocommerce consumer secret | [optional] 
 **magentoConsumerKey** | **String**| Magento Consumer Key | [optional] 
 **magentoConsumerSecret** | **String**| Magento Consumer Secret | [optional] 
 **magentoAccessToken** | **String**| Magento Access Token | [optional] 
 **magentoTokenSecret** | **String**| Magento Token Secret | [optional] 
 **prestashopWebserviceKey** | **String**| Prestashop webservice key | [optional] 
 **wixAppId** | **String**| Wix App ID | [optional] 
 **wixAppSecretKey** | **String**| Wix App Secret Key | [optional] 
 **wixRefreshToken** | **String**| Wix refresh token | [optional] 
 **mercadoLibreAppId** | **String**| Mercado Libre App ID | [optional] 
 **mercadoLibreAppSecretKey** | **String**| Mercado Libre App Secret Key | [optional] 
 **mercadoLibreRefreshToken** | **String**| Mercado Libre Refresh Token | [optional] 
 **zidClientId** | **Number**| Zid Client ID | [optional] 
 **zidClientSecret** | **String**| Zid Client Secret | [optional] 
 **zidAccessToken** | **String**| Zid Access Token | [optional] 
 **zidAuthorization** | **String**| Zid Authorization | [optional] 
 **zidRefreshToken** | **String**| Zid refresh token | [optional] 

### Return type

[**AccountCartAdd200Response**](AccountCartAdd200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartDelete

> CartDelete200Response cartDelete(opts)



Remove store from API2Cart

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'deleteBridge': true // Boolean | Identifies if there is a necessity to delete bridge
};
apiInstance.cartDelete(opts, (error, data, response) => {
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
 **deleteBridge** | **Boolean**| Identifies if there is a necessity to delete bridge | [optional] [default to true]

### Return type

[**CartDelete200Response**](CartDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartDisconnect

> CartDisconnect200Response cartDisconnect(opts)



Disconnect with the store and clear store session data.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'deleteBridge': false // Boolean | Identifies if there is a necessity to delete bridge
};
apiInstance.cartDisconnect(opts, (error, data, response) => {
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
 **deleteBridge** | **Boolean**| Identifies if there is a necessity to delete bridge | [optional] [default to false]

### Return type

[**CartDisconnect200Response**](CartDisconnect200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartGiftcardAdd

> CartGiftcardAdd200Response cartGiftcardAdd(amount, opts)



Create new gift card

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let amount = 3.4; // Number | Defines the gift card amount value.
let opts = {
  'code': "code_example", // String | Gift card code
  'ownerEmail': "ownerEmail_example", // String | Gift card owner email
  'recipientEmail': "recipientEmail_example" // String | Gift card recipient email
};
apiInstance.cartGiftcardAdd(amount, opts, (error, data, response) => {
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
 **amount** | **Number**| Defines the gift card amount value. | 
 **code** | **String**| Gift card code | [optional] 
 **ownerEmail** | **String**| Gift card owner email | [optional] 
 **recipientEmail** | **String**| Gift card recipient email | [optional] 

### Return type

[**CartGiftcardAdd200Response**](CartGiftcardAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartGiftcardCount

> CartGiftcardCount200Response cartGiftcardCount(opts)



Get gift cards count.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.cartGiftcardCount(opts, (error, data, response) => {
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
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CartGiftcardCount200Response**](CartGiftcardCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartGiftcardList

> ModelResponseCartGiftCardList cartGiftcardList(opts)



Get gift cards list.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'storeId': "storeId_example", // String | Store Id
  'params': "'id,code,name'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartGiftcardList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **storeId** | **String**| Store Id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,code,name&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartGiftCardList**](ModelResponseCartGiftCardList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartInfo

> CartInfo200Response cartInfo(opts)



Get cart information

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'params': "'store_name,store_url,db_prefix'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.cartInfo(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;store_name,store_url,db_prefix&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CartInfo200Response**](CartInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartList

> CartList200Response cartList()



Get list of supported carts

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
apiInstance.cartList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CartList200Response**](CartList200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartMetaDataList

> ModelResponseCartMetaDataList cartMetaDataList(entityId, opts)



Get entity meta data

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let entityId = "entityId_example"; // String | Entity Id
let opts = {
  'entity': "'product'", // String | Entity
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'key': "key_example", // String | Key
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'params': "'key,value'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartMetaDataList(entityId, opts, (error, data, response) => {
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
 **entityId** | **String**| Entity Id | 
 **entity** | **String**| Entity | [optional] [default to &#39;product&#39;]
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **key** | **String**| Key | [optional] 
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;key,value&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartMetaDataList**](ModelResponseCartMetaDataList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartMetaDataSet

> AttributeAdd200Response cartMetaDataSet(entityId, key, value, namespace, opts)



Set meta data for a specific entity

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let entityId = "entityId_example"; // String | Entity Id
let key = "key_example"; // String | Key
let value = "value_example"; // String | Value
let namespace = "namespace_example"; // String | Metafield namespace
let opts = {
  'entity': "'product'", // String | Entity
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example" // String | Language id
};
apiInstance.cartMetaDataSet(entityId, key, value, namespace, opts, (error, data, response) => {
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
 **entityId** | **String**| Entity Id | 
 **key** | **String**| Key | 
 **value** | **String**| Value | 
 **namespace** | **String**| Metafield namespace | 
 **entity** | **String**| Entity | [optional] [default to &#39;product&#39;]
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 

### Return type

[**AttributeAdd200Response**](AttributeAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartMetaDataUnset

> BasketLiveShippingServiceDelete200Response cartMetaDataUnset(entityId, key, id, opts)



Unset meta data for a specific entity

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let entityId = "entityId_example"; // String | Entity Id
let key = "key_example"; // String | Key
let id = "id_example"; // String | Entity id
let opts = {
  'entity': "'product'", // String | Entity
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.cartMetaDataUnset(entityId, key, id, opts, (error, data, response) => {
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
 **entityId** | **String**| Entity Id | 
 **key** | **String**| Key | 
 **id** | **String**| Entity id | 
 **entity** | **String**| Entity | [optional] [default to &#39;product&#39;]
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**BasketLiveShippingServiceDelete200Response**](BasketLiveShippingServiceDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartMethods

> CartMethods200Response cartMethods()



Get list of cart methods

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
apiInstance.cartMethods((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CartMethods200Response**](CartMethods200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartPluginList

> CartPluginList200Response cartPluginList(opts)



Get list of installed plugins

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'storeKey': "storeKey_example", // String | Set this parameter if bridge is already uploaded to store
  'storeId': "storeId_example", // String | Store Id
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10 // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
};
apiInstance.cartPluginList(opts, (error, data, response) => {
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
 **storeKey** | **String**| Set this parameter if bridge is already uploaded to store | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]

### Return type

[**CartPluginList200Response**](CartPluginList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartScriptAdd

> CartScriptAdd200Response cartScriptAdd(opts)



Add new script to the storefront

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'name': "name_example", // String | The user-friendly script name
  'description': "description_example", // String | The user-friendly description
  'html': "html_example", // String | An html string containing exactly one `script` tag.
  'src': "src_example", // String | The URL of the remote script
  'loadMethod': "loadMethod_example", // String | The load method to use for the script
  'scope': "'storefront'", // String | The page or pages on the online store where the script should be included
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.cartScriptAdd(opts, (error, data, response) => {
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
 **name** | **String**| The user-friendly script name | [optional] 
 **description** | **String**| The user-friendly description | [optional] 
 **html** | **String**| An html string containing exactly one &#x60;script&#x60; tag. | [optional] 
 **src** | **String**| The URL of the remote script | [optional] 
 **loadMethod** | **String**| The load method to use for the script | [optional] 
 **scope** | **String**| The page or pages on the online store where the script should be included | [optional] [default to &#39;storefront&#39;]
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CartScriptAdd200Response**](CartScriptAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartScriptDelete

> BridgeDelete200Response cartScriptDelete(id, opts)



Remove script from the storefront

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.cartScriptDelete(id, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**BridgeDelete200Response**](BridgeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartScriptList

> ModelResponseCartScriptList cartScriptList(opts)



Get scripts installed to the storefront

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'scriptIds': "scriptIds_example", // String | Retrieves only scripts with specific ids
  'storeId': "storeId_example", // String | Store Id
  'params': "'id,name,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartScriptList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **scriptIds** | **String**| Retrieves only scripts with specific ids | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseCartScriptList**](ModelResponseCartScriptList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartShippingZonesList

> CartShippingZonesList200Response cartShippingZonesList(opts)



Get list of shipping zones

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,name,enabled'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.cartShippingZonesList(opts, (error, data, response) => {
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
 **storeId** | **String**| Store Id | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,enabled&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**CartShippingZonesList200Response**](CartShippingZonesList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cartValidate

> CartValidate200Response cartValidate(opts)



Check store availability, bridge connection for the downloadable carts, identify DB prefix, validate API accesses for API carts.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CartApi();
let opts = {
  'validateVersion': false // Boolean | Specify if api2cart should validate cart version
};
apiInstance.cartValidate(opts, (error, data, response) => {
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
 **validateVersion** | **Boolean**| Specify if api2cart should validate cart version | [optional] [default to false]

### Return type

[**CartValidate200Response**](CartValidate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

