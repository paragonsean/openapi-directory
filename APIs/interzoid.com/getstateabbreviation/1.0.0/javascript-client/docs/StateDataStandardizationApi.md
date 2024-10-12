# InterzoidStateDataStandardizationApi.StateDataStandardizationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getstateabbreviation**](StateDataStandardizationApi.md#getstateabbreviation) | **GET** /getstateabbreviation | Gets a two-letter abbreviation for a state or province name data



## getstateabbreviation

> Getstateabbreviation200Response getstateabbreviation(license, state)

Gets a two-letter abbreviation for a state or province name data

Gets a two-letter abbreviation for a state or province given a permutation of state or province data.

### Example

```javascript
import InterzoidStateDataStandardizationApi from 'interzoid_state_data_standardization_api';

let apiInstance = new InterzoidStateDataStandardizationApi.StateDataStandardizationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let state = "state_example"; // String | State (or province) name from which to retrieve the two letter abbreviation.
apiInstance.getstateabbreviation(license, state, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **state** | **String**| State (or province) name from which to retrieve the two letter abbreviation. | 

### Return type

[**Getstateabbreviation200Response**](Getstateabbreviation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

