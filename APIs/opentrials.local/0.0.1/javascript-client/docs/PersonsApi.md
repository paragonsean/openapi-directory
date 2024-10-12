# OpenTrialsApi.PersonsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPerson**](PersonsApi.md#getPerson) | **GET** /persons/{id} | 



## getPerson

> Person getPerson(id)



Returns person details

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.PersonsApi();
let id = "id_example"; // String | ID of the person
apiInstance.getPerson(id, (error, data, response) => {
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
 **id** | **String**| ID of the person | 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

