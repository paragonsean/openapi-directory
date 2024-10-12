# EtMdbRestApiV1.PeopleApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peopleSearchRead**](PeopleApi.md#peopleSearchRead) | **GET** /api/v1/people/search/{user} | Return cast search result



## peopleSearchRead

> peopleSearchRead(user)

Return cast search result

Return cast search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username  For more details on how cast are listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.PeopleApi();
let user = "user_example"; // String | 
apiInstance.peopleSearchRead(user, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

