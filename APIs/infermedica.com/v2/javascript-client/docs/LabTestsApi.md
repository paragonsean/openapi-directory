# InfermedicaApi.LabTestsApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllLabTests**](LabTestsApi.md#getAllLabTests) | **GET** /lab_tests | List all lab tests
[**getLabTest**](LabTestsApi.md#getLabTest) | **GET** /lab_tests/{id} | Get lab test by id



## getAllLabTests

> [LabTestPublic] getAllLabTests(opts)

List all lab tests

Returns a list of all available lab tests.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.LabTestsApi();
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year" // String | unit in which age value was provided
};
apiInstance.getAllLabTests(opts, (error, data, response) => {
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

### Return type

[**[LabTestPublic]**](LabTestPublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLabTest

> LabTestDetails getLabTest(id, opts)

Get lab test by id

Returns details of a single lab test specified by id parameter.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.LabTestsApi();
let id = "id_example"; // String | lab test id
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year" // String | unit in which age value was provided
};
apiInstance.getLabTest(id, opts, (error, data, response) => {
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
 **id** | **String**| lab test id | 
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]

### Return type

[**LabTestDetails**](LabTestDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

