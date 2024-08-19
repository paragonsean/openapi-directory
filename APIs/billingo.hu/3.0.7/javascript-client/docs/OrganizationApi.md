# BillingoApiV3.OrganizationApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationData**](OrganizationApi.md#getOrganizationData) | **GET** /organization | Retrieve a organization data.



## getOrganizationData

> OrganizationData getOrganizationData()

Retrieve a organization data.

Retrieves the data of organization.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.OrganizationApi();
apiInstance.getOrganizationData((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OrganizationData**](OrganizationData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

