# GitHubV3RestApi.CodesOfConductApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codesOfConductGetAllCodesOfConduct**](CodesOfConductApi.md#codesOfConductGetAllCodesOfConduct) | **GET** /codes_of_conduct | Get all codes of conduct
[**codesOfConductGetConductCode**](CodesOfConductApi.md#codesOfConductGetConductCode) | **GET** /codes_of_conduct/{key} | Get a code of conduct



## codesOfConductGetAllCodesOfConduct

> [CodeOfConduct] codesOfConductGetAllCodesOfConduct()

Get all codes of conduct



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodesOfConductApi();
apiInstance.codesOfConductGetAllCodesOfConduct((error, data, response) => {
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

[**[CodeOfConduct]**](CodeOfConduct.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codesOfConductGetConductCode

> CodeOfConduct codesOfConductGetConductCode(key)

Get a code of conduct



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.CodesOfConductApi();
let key = "key_example"; // String | 
apiInstance.codesOfConductGetConductCode(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

[**CodeOfConduct**](CodeOfConduct.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

