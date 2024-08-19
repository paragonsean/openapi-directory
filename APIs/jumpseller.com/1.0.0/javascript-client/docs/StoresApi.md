# JumpsellerApi.StoresApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storeInfoJsonGet**](StoresApi.md#storeInfoJsonGet) | **GET** /store/info.json | Retrieve Store Information.
[**storeLanguagesJsonGet**](StoresApi.md#storeLanguagesJsonGet) | **GET** /store/languages.json | Retrieve Store Languages.



## storeInfoJsonGet

> Store storeInfoJsonGet(login, authtoken)

Retrieve Store Information.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.StoresApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.storeInfoJsonGet(login, authtoken, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 

### Return type

[**Store**](Store.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeLanguagesJsonGet

> [Language] storeLanguagesJsonGet(login, authtoken)

Retrieve Store Languages.



### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.StoresApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.storeLanguagesJsonGet(login, authtoken, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 

### Return type

[**[Language]**](Language.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

