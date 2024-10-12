# PriceSimulationsApi.PriceAssociationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vCustomPricesRulesPost**](PriceAssociationApi.md#vCustomPricesRulesPost) | **POST** /_v/custom-prices/rules | Create price association
[**vCustomPricesRulesPriceAssociationIdDelete**](PriceAssociationApi.md#vCustomPricesRulesPriceAssociationIdDelete) | **DELETE** /_v/custom-prices/rules/{priceAssociationId} | Disassociate price association by ID
[**vCustomPricesRulesPriceAssociationIdGet**](PriceAssociationApi.md#vCustomPricesRulesPriceAssociationIdGet) | **GET** /_v/custom-prices/rules/{priceAssociationId} | Get price association by ID
[**vCustomPricesRulesPriceAssociationIdPut**](PriceAssociationApi.md#vCustomPricesRulesPriceAssociationIdPut) | **PUT** /_v/custom-prices/rules/{priceAssociationId} | Update price association by ID



## vCustomPricesRulesPost

> VCustomPricesRulesPost200Response vCustomPricesRulesPost(contentType, accept, opts)

Create price association

Creates a new price association for a shopping scenario

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.PriceAssociationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
let opts = {
  'vCustomPricesRulesPostRequest': new PriceSimulationsApi.VCustomPricesRulesPostRequest() // VCustomPricesRulesPostRequest | 
};
apiInstance.vCustomPricesRulesPost(contentType, accept, opts, (error, data, response) => {
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
 **vCustomPricesRulesPostRequest** | [**VCustomPricesRulesPostRequest**](VCustomPricesRulesPostRequest.md)|  | [optional] 

### Return type

[**VCustomPricesRulesPost200Response**](VCustomPricesRulesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vCustomPricesRulesPriceAssociationIdDelete

> String vCustomPricesRulesPriceAssociationIdDelete(contentType, accept, priceAssociationId)

Disassociate price association by ID

Disassociates a price association from a shopping scenario by its ID

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.PriceAssociationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
let priceAssociationId = 1; // Number | Price Association unique identifier
apiInstance.vCustomPricesRulesPriceAssociationIdDelete(contentType, accept, priceAssociationId, (error, data, response) => {
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
 **priceAssociationId** | **Number**| Price Association unique identifier | [default to 1]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vCustomPricesRulesPriceAssociationIdGet

> VCustomPricesRulesPost200Response vCustomPricesRulesPriceAssociationIdGet(contentType, accept, priceAssociationId)

Get price association by ID

Retrieves price association for a shopping scenario by its ID

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.PriceAssociationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
let priceAssociationId = 1; // Number | Price Association unique identifier
apiInstance.vCustomPricesRulesPriceAssociationIdGet(contentType, accept, priceAssociationId, (error, data, response) => {
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
 **priceAssociationId** | **Number**| Price Association unique identifier | [default to 1]

### Return type

[**VCustomPricesRulesPost200Response**](VCustomPricesRulesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vCustomPricesRulesPriceAssociationIdPut

> VCustomPricesRulesPost200Response vCustomPricesRulesPriceAssociationIdPut(contentType, accept, priceAssociationId, opts)

Update price association by ID

Updates a price association for a shopping scenario by its ID

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.PriceAssociationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
let priceAssociationId = 1; // Number | Price Association unique identifier
let opts = {
  'requestBody': new PriceSimulationsApi.RequestBody() // RequestBody | 
};
apiInstance.vCustomPricesRulesPriceAssociationIdPut(contentType, accept, priceAssociationId, opts, (error, data, response) => {
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
 **priceAssociationId** | **Number**| Price Association unique identifier | [default to 1]
 **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] 

### Return type

[**VCustomPricesRulesPost200Response**](VCustomPricesRulesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

