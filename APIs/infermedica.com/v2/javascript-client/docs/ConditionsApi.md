# InfermedicaApi.ConditionsApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllConditions**](ConditionsApi.md#getAllConditions) | **GET** /conditions | List all conditions
[**getCondition**](ConditionsApi.md#getCondition) | **GET** /conditions/{id} | Get condition by id



## getAllConditions

> [ConditionPublic] getAllConditions(opts)

List all conditions

Returns a list of all available conditions.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.ConditionsApi();
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year", // String | unit in which age value was provided
  'enableTriage5': true // Boolean | enable 5-level triage values
};
apiInstance.getAllConditions(opts, (error, data, response) => {
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
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]
 **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] 

### Return type

[**[ConditionPublic]**](ConditionPublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCondition

> ConditionDetails getCondition(id, opts)

Get condition by id

Returns details of a single condition specified by id parameter.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.ConditionsApi();
let id = "id_example"; // String | condition id
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year", // String | unit in which age value was provided
  'enableTriage5': true // Boolean | enable 5-level triage values
};
apiInstance.getCondition(id, opts, (error, data, response) => {
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
 **id** | **String**| condition id | 
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]
 **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] 

### Return type

[**ConditionDetails**](ConditionDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

