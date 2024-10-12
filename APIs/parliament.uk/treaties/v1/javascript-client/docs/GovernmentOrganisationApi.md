# TreatiesApi.GovernmentOrganisationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganisations**](GovernmentOrganisationApi.md#getOrganisations) | **GET** /api/GovernmentOrganisation | Returns all government organisations.



## getOrganisations

> GovernmentOrganisationResourceCollection getOrganisations()

Returns all government organisations.

### Example

```javascript
import TreatiesApi from 'treaties_api';

let apiInstance = new TreatiesApi.GovernmentOrganisationApi();
apiInstance.getOrganisations((error, data, response) => {
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

[**GovernmentOrganisationResourceCollection**](GovernmentOrganisationResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

