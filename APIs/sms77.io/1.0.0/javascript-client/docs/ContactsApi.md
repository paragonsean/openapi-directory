# SevenIoApi.ContactsApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactsGet**](ContactsApi.md#contactsGet) | **GET** /contacts | 
[**contactsPOST**](ContactsApi.md#contactsPOST) | **POST** /contacts | 



## contactsGet

> String contactsGet(action, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.ContactsApi();
let action = "action_example"; // String | Determines the action to execute.
let opts = {
  'json': 0 // Number | Defines whether to return the response as JSON or CSV separated by semicolon.
};
apiInstance.contactsGet(action, opts, (error, data, response) => {
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
 **action** | **String**| Determines the action to execute. | 
 **json** | **Number**| Defines whether to return the response as JSON or CSV separated by semicolon. | [optional] [default to 0]

### Return type

**String**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## contactsPOST

> String contactsPOST(action, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.ContactsApi();
let action = "action_example"; // String | Determines the action to execute.
let opts = {
  'json': 0, // Number | Defines whether to return the response as JSON or CSV separated by semicolon.
  'id': "id_example", // String | The contact ID for editing/deletion.
  'nick': "nick_example", // String | The contacts name.
  'empfaenger': "empfaenger_example", // String | The contacts phone number.
  'email': "email_example" // String | The contacts email address.
};
apiInstance.contactsPOST(action, opts, (error, data, response) => {
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
 **action** | **String**| Determines the action to execute. | 
 **json** | **Number**| Defines whether to return the response as JSON or CSV separated by semicolon. | [optional] [default to 0]
 **id** | **String**| The contact ID for editing/deletion. | [optional] 
 **nick** | **String**| The contacts name. | [optional] 
 **empfaenger** | **String**| The contacts phone number. | [optional] 
 **email** | **String**| The contacts email address. | [optional] 

### Return type

**String**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

