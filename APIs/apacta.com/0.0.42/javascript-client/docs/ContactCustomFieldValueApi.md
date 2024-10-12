# Apacta.ContactCustomFieldValueApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactsContactIdContactCustomFieldValuesGet**](ContactCustomFieldValueApi.md#contactsContactIdContactCustomFieldValuesGet) | **GET** /contacts/{contact_id}/contact_custom_field_values | Get a list of contact custom field values



## contactsContactIdContactCustomFieldValuesGet

> ContactsContactIdContactCustomFieldValuesGet200Response contactsContactIdContactCustomFieldValuesGet(contactId)

Get a list of contact custom field values

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ContactCustomFieldValueApi();
let contactId = "contactId_example"; // String | Automatically added
apiInstance.contactsContactIdContactCustomFieldValuesGet(contactId, (error, data, response) => {
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
 **contactId** | **String**| Automatically added | 

### Return type

[**ContactsContactIdContactCustomFieldValuesGet200Response**](ContactsContactIdContactCustomFieldValuesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

