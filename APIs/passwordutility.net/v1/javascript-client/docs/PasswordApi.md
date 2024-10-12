# PasswordUtilityWeb.PasswordApi

All URIs are relative to *http://passwordutility.net:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**passwordGenerate**](PasswordApi.md#passwordGenerate) | **POST** /api/password/generate | 
[**passwordValidate**](PasswordApi.md#passwordValidate) | **POST** /api/password/validate | 



## passwordGenerate

> Object passwordGenerate(length, opts)



### Example

```javascript
import PasswordUtilityWeb from 'password_utility_web';

let apiInstance = new PasswordUtilityWeb.PasswordApi();
let length = 56; // Number | 
let opts = {
  'upperCase': true, // Boolean | 
  'digits': true, // Boolean | 
  'specialCharacters': true // Boolean | 
};
apiInstance.passwordGenerate(length, opts, (error, data, response) => {
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
 **length** | **Number**|  | 
 **upperCase** | **Boolean**|  | [optional] 
 **digits** | **Boolean**|  | [optional] 
 **specialCharacters** | **Boolean**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## passwordValidate

> Object passwordValidate(password)



### Example

```javascript
import PasswordUtilityWeb from 'password_utility_web';

let apiInstance = new PasswordUtilityWeb.PasswordApi();
let password = "password_example"; // String | 
apiInstance.passwordValidate(password, (error, data, response) => {
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
 **password** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

