# OpenTrialsApi.FdaApplicationsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFDAApplication**](FdaApplicationsApi.md#getFDAApplication) | **GET** /fda_applications/{id} | 
[**listFDAApplications**](FdaApplicationsApi.md#listFDAApplications) | **GET** /fda_applications | 



## getFDAApplication

> FDAApplication getFDAApplication(id)



Returns an FDA application details

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.FdaApplicationsApi();
let id = "id_example"; // String | ID of the FDA application
apiInstance.getFDAApplication(id, (error, data, response) => {
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
 **id** | **String**| ID of the FDA application | 

### Return type

[**FDAApplication**](FDAApplication.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFDAApplications

> FDAApplicationList listFDAApplications(opts)



Returns FDA applications

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.FdaApplicationsApi();
let opts = {
  'page': 1, // Number | The page number
  'perPage': 20 // Number | Number of items per page
};
apiInstance.listFDAApplications(opts, (error, data, response) => {
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
 **page** | **Number**| The page number | [optional] [default to 1]
 **perPage** | **Number**| Number of items per page | [optional] [default to 20]

### Return type

[**FDAApplicationList**](FDAApplicationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

