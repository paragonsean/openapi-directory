# BeezUpMerchantApi.UserListOfValuesLOVApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserListOfValues**](UserListOfValuesLOVApi.md#getUserListOfValues) | **GET** /v2/user/lov/{listName} | Get the list of values related to this list name
[**getUserLovIndex**](UserListOfValuesLOVApi.md#getUserLovIndex) | **GET** /v2/user/lov/ | Get all list names



## getUserListOfValues

> UserListOfValuesResponse getUserListOfValues(listName, opts)

Get the list of values related to this list name

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.UserListOfValuesLOVApi();
let listName = "listName_example"; // String | The list of value name your want to get
let opts = {
  'acceptLanguage': ["null"], // [String] | Indicates that the client accepts the following languages.
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getUserListOfValues(listName, opts, (error, data, response) => {
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
 **listName** | **String**| The list of value name your want to get | 
 **acceptLanguage** | [**[String]**](String.md)| Indicates that the client accepts the following languages. | [optional] 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**UserListOfValuesResponse**](UserListOfValuesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserLovIndex

> UserLovIndex getUserLovIndex()

Get all list names

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.UserListOfValuesLOVApi();
apiInstance.getUserLovIndex((error, data, response) => {
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

[**UserLovIndex**](UserLovIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

