# Pims.PriceRangesApi

All URIs are relative to *https://demo.pims.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAllPriceRanges**](PriceRangesApi.md#fetchAllPriceRanges) | **GET** /price-ranges | Find all price ranges
[**fetchOnePriceRange**](PriceRangesApi.md#fetchOnePriceRange) | **GET** /price-ranges/{price_range_id} | Get one price range by ID



## fetchAllPriceRanges

> [PriceRangesEntity] fetchAllPriceRanges(opts)

Find all price ranges

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.PriceRangesApi();
let opts = {
  'label': "label_example", // String | Find only the price ranges whose label contains this value.
  'showIgnored': false, // Boolean | If set to `false`, show only the price ranges which are not ignored. If set to `true`, show all price ranges.
  'sort': "'label'", // String | Sort the price ranges in the corresponding order.
  'pageSize': 25, // Number | Pagination size, i.e. maximum number of items to be displayed in the response.
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchAllPriceRanges(opts, (error, data, response) => {
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
 **label** | **String**| Find only the price ranges whose label contains this value. | [optional] 
 **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the price ranges which are not ignored. If set to &#x60;true&#x60;, show all price ranges. | [optional] [default to false]
 **sort** | **String**| Sort the price ranges in the corresponding order. | [optional] [default to &#39;label&#39;]
 **pageSize** | **Number**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25]
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**[PriceRangesEntity]**](PriceRangesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json


## fetchOnePriceRange

> VenuesEntity fetchOnePriceRange(priceRangeId, opts)

Get one price range by ID

### Example

```javascript
import Pims from 'pims';
let defaultClient = Pims.ApiClient.instance;
// Configure HTTP basic authorization: Basic Auth
let Basic Auth = defaultClient.authentications['Basic Auth'];
Basic Auth.username = 'YOUR USERNAME';
Basic Auth.password = 'YOUR PASSWORD';

let apiInstance = new Pims.PriceRangesApi();
let priceRangeId = 56; // Number | ID of the targeted price range.
let opts = {
  'acceptLanguage': "'en'" // String | Language used for the translatable labels.
};
apiInstance.fetchOnePriceRange(priceRangeId, opts, (error, data, response) => {
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
 **priceRangeId** | **Number**| ID of the targeted price range. | 
 **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to &#39;en&#39;]

### Return type

[**VenuesEntity**](VenuesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json

