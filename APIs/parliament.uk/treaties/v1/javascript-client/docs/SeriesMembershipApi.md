# TreatiesApi.SeriesMembershipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSeriesMemberships**](SeriesMembershipApi.md#getSeriesMemberships) | **GET** /api/SeriesMembership | Returns all series memberships.



## getSeriesMemberships

> SeriesMembershipResourceCollection getSeriesMemberships()

Returns all series memberships.

### Example

```javascript
import TreatiesApi from 'treaties_api';

let apiInstance = new TreatiesApi.SeriesMembershipApi();
apiInstance.getSeriesMemberships((error, data, response) => {
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

[**SeriesMembershipResourceCollection**](SeriesMembershipResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

