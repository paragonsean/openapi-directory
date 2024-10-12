# Mailsquad.ListsApi

All URIs are relative to *https://api.inboxroute.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactsListsGet**](ListsApi.md#contactsListsGet) | **GET** /contacts/lists | 
[**contactsListsListidDelete**](ListsApi.md#contactsListsListidDelete) | **DELETE** /contacts/lists/{listid} | 
[**contactsListsListidPut**](ListsApi.md#contactsListsListidPut) | **PUT** /contacts/lists/{listid} | 
[**contactsListsPost**](ListsApi.md#contactsListsPost) | **POST** /contacts/lists | 



## contactsListsGet

> ContactListPage contactsListsGet(opts)



Get a paged result of contact lists.

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ListsApi();
let opts = {
  'offset': 56, // Number | Skip that many records
  'limit': 56, // Number | Maximum number of items in page
  'sort': "sort_example" // String | Property to sort by. Append '-' for descending order.
};
apiInstance.contactsListsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Skip that many records | [optional] 
 **limit** | **Number**| Maximum number of items in page | [optional] 
 **sort** | **String**| Property to sort by. Append &#39;-&#39; for descending order. | [optional] 

### Return type

[**ContactListPage**](ContactListPage.md)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsListsListidDelete

> contactsListsListidDelete(listid)



Delete an existing contact list

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ListsApi();
let listid = "listid_example"; // String | Unique 16 characters ID of the contact list
apiInstance.contactsListsListidDelete(listid, (error, data, response) => {
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
 **listid** | **String**| Unique 16 characters ID of the contact list | 

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsListsListidPut

> contactsListsListidPut(listid, opts)



Update an existing contact list

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ListsApi();
let listid = "listid_example"; // String | Unique 16 characters ID of the contact list
let opts = {
  'contactlist': new Mailsquad.ContactListUpdate() // ContactListUpdate | Contact list properties to update
};
apiInstance.contactsListsListidPut(listid, opts, (error, data, response) => {
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
 **listid** | **String**| Unique 16 characters ID of the contact list | 
 **contactlist** | [**ContactListUpdate**](ContactListUpdate.md)| Contact list properties to update | [optional] 

### Return type

null (empty response body)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsListsPost

> NewId contactsListsPost(opts)



Add a new contact list

### Example

```javascript
import Mailsquad from 'mailsquad';
let defaultClient = Mailsquad.ApiClient.instance;
// Configure API key authorization: mqApiKey
let mqApiKey = defaultClient.authentications['mqApiKey'];
mqApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//mqApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Mailsquad.ListsApi();
let opts = {
  'contactlist': new Mailsquad.ContactListUpdate() // ContactListUpdate | Contact list initial properties
};
apiInstance.contactsListsPost(opts, (error, data, response) => {
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
 **contactlist** | [**ContactListUpdate**](ContactListUpdate.md)| Contact list initial properties | [optional] 

### Return type

[**NewId**](NewId.md)

### Authorization

[mqApiKey](../README.md#mqApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

