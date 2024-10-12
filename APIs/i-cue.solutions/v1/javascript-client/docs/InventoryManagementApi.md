# GrowthServices.InventoryManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventoryAmazonIpiPost**](InventoryManagementApi.md#inventoryAmazonIpiPost) | **POST** /inventory/amazon-ipi | Calculate Amazon Inventory Performance Index (IPI)
[**inventoryCaryyingCostPost**](InventoryManagementApi.md#inventoryCaryyingCostPost) | **POST** /inventory/caryying-cost | Carrying Cost
[**inventoryEoqPost**](InventoryManagementApi.md#inventoryEoqPost) | **POST** /inventory/eoq | Calculate economic order quantity
[**inventoryFillRatePost**](InventoryManagementApi.md#inventoryFillRatePost) | **POST** /inventory/fill-rate | Calculate fill rate
[**inventoryFinancialImapctForecastAccuracyPost**](InventoryManagementApi.md#inventoryFinancialImapctForecastAccuracyPost) | **POST** /inventory/financial-imapct-forecast-accuracy | Calculate financial impact of forecast accuracy
[**inventoryInventoryTurnoverPost**](InventoryManagementApi.md#inventoryInventoryTurnoverPost) | **POST** /inventory/inventory-turnover | Inventroy Turn-over
[**inventoryLtdPost**](InventoryManagementApi.md#inventoryLtdPost) | **POST** /inventory/ltd | Calculate lead time demand
[**inventoryMoqPost**](InventoryManagementApi.md#inventoryMoqPost) | **POST** /inventory/moq | Calculate minimum order quantity
[**inventoryOptimalServiceLevelPost**](InventoryManagementApi.md#inventoryOptimalServiceLevelPost) | **POST** /inventory/optimal-service-level | Calculate optimal service level
[**inventoryReorderPointPost**](InventoryManagementApi.md#inventoryReorderPointPost) | **POST** /inventory/reorder-point | Re-order Point
[**inventorySafetyStockPost**](InventoryManagementApi.md#inventorySafetyStockPost) | **POST** /inventory/safety-stock | Safety Stock
[**inventoryServiceLevelPost**](InventoryManagementApi.md#inventoryServiceLevelPost) | **POST** /inventory/service-level | Calculate service level
[**inventoryTurnsPost**](InventoryManagementApi.md#inventoryTurnsPost) | **POST** /inventory/turns | Calculate inventory turns



## inventoryAmazonIpiPost

> inventoryAmazonIpiPost(opts)

Calculate Amazon Inventory Performance Index (IPI)

Calculate Amazon Inventory Performance Index (IPI)

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryAmazonIpiPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryCaryyingCostPost

> inventoryCaryyingCostPost(opts)

Carrying Cost

Carrying Cost

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryCaryyingCostPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryEoqPost

> inventoryEoqPost(opts)

Calculate economic order quantity

Calculate economic order quantity

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryEoqPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryFillRatePost

> inventoryFillRatePost(opts)

Calculate fill rate

Calculate fill rate

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryFillRatePost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryFinancialImapctForecastAccuracyPost

> inventoryFinancialImapctForecastAccuracyPost(opts)

Calculate financial impact of forecast accuracy

Calculate financial impact of forecast accuracy

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryFinancialImapctForecastAccuracyPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryInventoryTurnoverPost

> inventoryInventoryTurnoverPost(opts)

Inventroy Turn-over

Inventroy Turn-over

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryInventoryTurnoverPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryLtdPost

> inventoryLtdPost(opts)

Calculate lead time demand

Calculate lead time demand

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryLtdPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryMoqPost

> inventoryMoqPost(opts)

Calculate minimum order quantity

Calculate minimum order quantity

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryMoqPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryOptimalServiceLevelPost

> inventoryOptimalServiceLevelPost(opts)

Calculate optimal service level

Calculate optimal service level

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryOptimalServiceLevelPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryReorderPointPost

> inventoryReorderPointPost(opts)

Re-order Point

Re-order Point

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryReorderPointPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventorySafetyStockPost

> inventorySafetyStockPost(opts)

Safety Stock

Safety Stock

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventorySafetyStockPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryServiceLevelPost

> inventoryServiceLevelPost(opts)

Calculate service level

Calculate service level

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryServiceLevelPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## inventoryTurnsPost

> inventoryTurnsPost(opts)

Calculate inventory turns

Calculate inventory turns

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InventoryManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.inventoryTurnsPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

