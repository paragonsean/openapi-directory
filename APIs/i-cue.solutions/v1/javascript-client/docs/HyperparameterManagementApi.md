# GrowthServices.HyperparameterManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hyperparameterGet**](HyperparameterManagementApi.md#hyperparameterGet) | **GET** /hyperparameter | Get hyperparameters
[**hyperparameterPost**](HyperparameterManagementApi.md#hyperparameterPost) | **POST** /hyperparameter | Set hyperparameters



## hyperparameterGet

> HyperparameterModel hyperparameterGet(opts)

Get hyperparameters

Get entity global hyperparameters.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.HyperparameterManagementApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.hyperparameterGet(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

[**HyperparameterModel**](HyperparameterModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## hyperparameterPost

> hyperparameterPost(opts)

Set hyperparameters

Set entity global hyperparameters. Hyperparameters can be overwritten by user and planning level (add to JSON body).

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.HyperparameterManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'hyperparameterModel': new GrowthServices.HyperparameterModel() // HyperparameterModel | 
};
apiInstance.hyperparameterPost(opts, (error, data, response) => {
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
 **hyperparameterModel** | [**HyperparameterModel**](HyperparameterModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

