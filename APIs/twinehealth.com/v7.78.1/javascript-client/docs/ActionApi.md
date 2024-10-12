# FitbitPlusApi.ActionApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAction**](ActionApi.md#createAction) | **POST** /action | Create action
[**fetchAction**](ActionApi.md#fetchAction) | **GET** /action/{id} | Get an action
[**updateAction**](ActionApi.md#updateAction) | **PATCH** /action/{id} | Update an action



## createAction

> CreateActionResponse createAction(createActionRequest)

Create action

Create a plan action

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.ActionApi();
let createActionRequest = new FitbitPlusApi.CreateActionRequest(); // CreateActionRequest | 
apiInstance.createAction(createActionRequest, (error, data, response) => {
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
 **createActionRequest** | [**CreateActionRequest**](CreateActionRequest.md)|  | 

### Return type

[**CreateActionResponse**](CreateActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json


## fetchAction

> FetchActionResponse fetchAction(id)

Get an action

Get a health action from a patient&#39;s plan.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.ActionApi();
let id = "id_example"; // String | Action identifier
apiInstance.fetchAction(id, (error, data, response) => {
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
 **id** | **String**| Action identifier | 

### Return type

[**FetchActionResponse**](FetchActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## updateAction

> UpdateActionResponse updateAction(id, updateActionRequest)

Update an action

Update a health action from a patient&#39;s plan.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.ActionApi();
let id = "id_example"; // String | Action identifier
let updateActionRequest = new FitbitPlusApi.UpdateActionRequest(); // UpdateActionRequest | 
apiInstance.updateAction(id, updateActionRequest, (error, data, response) => {
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
 **id** | **String**| Action identifier | 
 **updateActionRequest** | [**UpdateActionRequest**](UpdateActionRequest.md)|  | 

### Return type

[**UpdateActionResponse**](UpdateActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.api+json
- **Accept**: application/vnd.api+json

