# Mailsquad.ContactsApi

All URIs are relative to *https://api.inboxroute.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactsContactidDelete**](ContactsApi.md#contactsContactidDelete) | **DELETE** /contacts/{contactid} | 
[**contactsContactidPut**](ContactsApi.md#contactsContactidPut) | **PUT** /contacts/{contactid} | 
[**contactsGet**](ContactsApi.md#contactsGet) | **GET** /contacts | 



## contactsContactidDelete

> contactsContactidDelete(contactid)



Delete an existing contact

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ContactsApi();
let contactid = "contactid_example"; // String | Unique 16 characters ID of the contact
apiInstance.contactsContactidDelete(contactid, (error, data, response) => {
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
 **contactid** | **String**| Unique 16 characters ID of the contact | 

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsContactidPut

> contactsContactidPut(contactid, contact)



Update an existing contact

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ContactsApi();
let contactid = "contactid_example"; // String | Unique 16 characters ID of the contact
let contact = new Mailsquad.ContactUpdate(); // ContactUpdate | Contact properties to update
apiInstance.contactsContactidPut(contactid, contact, (error, data, response) => {
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
 **contactid** | **String**| Unique 16 characters ID of the contact | 
 **contact** | [**ContactUpdate**](ContactUpdate.md)| Contact properties to update | 

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsGet

> ContactPage contactsGet(opts)



Get a paged result of contacts from a list

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ContactsApi();
let opts = {
  'listid': "listid_example", // String | Unique 16 characters ID of the contact list to get contacts of
  'offset': 56, // Number | Skip that many records
  'limit': 56, // Number | Maximum number of items in page
  'sort': "sort_example" // String | Property to sort by. Append '-' for descending order.
};
apiInstance.contactsGet(opts, (error, data, response) => {
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
 **listid** | **String**| Unique 16 characters ID of the contact list to get contacts of | [optional] 
 **offset** | **Number**| Skip that many records | [optional] 
 **limit** | **Number**| Maximum number of items in page | [optional] 
 **sort** | **String**| Property to sort by. Append &#39;-&#39; for descending order. | [optional] 

### Return type

[**ContactPage**](ContactPage.md)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

