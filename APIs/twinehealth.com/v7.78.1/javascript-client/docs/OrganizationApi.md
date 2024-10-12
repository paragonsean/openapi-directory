# FitbitPlusApi.OrganizationApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchOrganization**](OrganizationApi.md#fetchOrganization) | **GET** /organization/{id} | Get an organization



## fetchOrganization

> FetchOrganizationResponse fetchOrganization(id)

Get an organization

Get an organization record by id.

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.OrganizationApi();
let id = "id_example"; // String | Organization identifier
apiInstance.fetchOrganization(id, (error, data, response) => {
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
 **id** | **String**| Organization identifier | 

### Return type

[**FetchOrganizationResponse**](FetchOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

