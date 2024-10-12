# PriceSimulationsApi.CustomPricesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vCustomPricesSessionSchemaGet**](CustomPricesApi.md#vCustomPricesSessionSchemaGet) | **GET** /_v/custom-prices/session/schema | Get custom prices schema
[**vCustomPricesSessionSchemaPost**](CustomPricesApi.md#vCustomPricesSessionSchemaPost) | **POST** /_v/custom-prices/session/schema | Create or Update custom prices schema



## vCustomPricesSessionSchemaGet

> RequestBody1 vCustomPricesSessionSchemaGet(contentType, accept)

Get custom prices schema

Retrieves all custom price for all shopping scenarios

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.CustomPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
apiInstance.vCustomPricesSessionSchemaGet(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]

### Return type

[**RequestBody1**](RequestBody1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vCustomPricesSessionSchemaPost

> RequestBody1 vCustomPricesSessionSchemaPost(contentType, accept, opts)

Create or Update custom prices schema

Creates a new custom price for a shopping scenario or updates an existing one

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.CustomPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
let opts = {
  'requestBody1': new PriceSimulationsApi.RequestBody1() // RequestBody1 | 
};
apiInstance.vCustomPricesSessionSchemaPost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **requestBody1** | [**RequestBody1**](RequestBody1.md)|  | [optional] 

### Return type

[**RequestBody1**](RequestBody1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

