# EcosystemApi.ListingApi

All URIs are relative to *https://api.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listingsAll**](ListingApi.md#listingsAll) | **GET** /ecosystems/{ecosystem_id}/listings | List listings
[**listingsOne**](ListingApi.md#listingsOne) | **GET** /ecosystems/{ecosystem_id}/listings/{id} | Get listing



## listingsAll

> GetListingsResponse listingsAll(ecosystemId, opts)

List listings

List listings

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.ListingApi();
let ecosystemId = "ecosystemId_example"; // String | 
let opts = {
  'cursor': "cursor_example", // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
  'limit': 50, // Number | Number of records to return
  'externalId': "externalId_example" // String | Filter on external_id
};
apiInstance.listingsAll(ecosystemId, opts, (error, data, response) => {
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
 **ecosystemId** | **String**|  | 
 **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] 
 **limit** | **Number**| Number of records to return | [optional] [default to 50]
 **externalId** | **String**| Filter on external_id | [optional] 

### Return type

[**GetListingsResponse**](GetListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingsOne

> GetListingResponse listingsOne(ecosystemId, id)

Get listing

Get listing

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.ListingApi();
let ecosystemId = "ecosystemId_example"; // String | 
let id = "id_example"; // String | ID of the record you are acting upon.
apiInstance.listingsOne(ecosystemId, id, (error, data, response) => {
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
 **ecosystemId** | **String**|  | 
 **id** | **String**| ID of the record you are acting upon. | 

### Return type

[**GetListingResponse**](GetListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

