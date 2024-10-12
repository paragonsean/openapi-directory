# OpenTrialsApi.ConditionsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCondition**](ConditionsApi.md#getCondition) | **GET** /conditions/{id} | 



## getCondition

> Condition getCondition(id)



Returns condition details

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.ConditionsApi();
let id = "id_example"; // String | ID of the condition
apiInstance.getCondition(id, (error, data, response) => {
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
 **id** | **String**| ID of the condition | 

### Return type

[**Condition**](Condition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

