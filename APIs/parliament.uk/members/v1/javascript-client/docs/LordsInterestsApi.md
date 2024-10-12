# MembersApi.LordsInterestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiLordsInterestsRegisterGet**](LordsInterestsApi.md#apiLordsInterestsRegisterGet) | **GET** /api/LordsInterests/Register | Returns a list of registered interests
[**apiLordsInterestsStaffGet**](LordsInterestsApi.md#apiLordsInterestsStaffGet) | **GET** /api/LordsInterests/Staff | Returns a list of staff



## apiLordsInterestsRegisterGet

> MembersInterestsMembersServiceSearchResult apiLordsInterestsRegisterGet(opts)

Returns a list of registered interests

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LordsInterestsApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | Registered interests containing search term
  'page': 56, // Number | Page of results to return, default 0. Results per page 20.
  'includeDeleted': false // Boolean | Registered interests that have been deleted
};
apiInstance.apiLordsInterestsRegisterGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Registered interests containing search term | [optional] 
 **page** | **Number**| Page of results to return, default 0. Results per page 20. | [optional] 
 **includeDeleted** | **Boolean**| Registered interests that have been deleted | [optional] [default to false]

### Return type

[**MembersInterestsMembersServiceSearchResult**](MembersInterestsMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLordsInterestsStaffGet

> MembersStaffMembersServiceSearchResult apiLordsInterestsStaffGet(opts)

Returns a list of staff

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LordsInterestsApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | Staff containing search term
  'page': 56 // Number | Page of results to return, default 0. Results per page 20.
};
apiInstance.apiLordsInterestsStaffGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Staff containing search term | [optional] 
 **page** | **Number**| Page of results to return, default 0. Results per page 20. | [optional] 

### Return type

[**MembersStaffMembersServiceSearchResult**](MembersStaffMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

