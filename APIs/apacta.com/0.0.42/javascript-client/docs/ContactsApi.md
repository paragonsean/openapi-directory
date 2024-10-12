# Apacta.ContactsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteContacts**](ContactsApi.md#bulkDeleteContacts) | **DELETE** /contacts/bulkDelete | Bulk delete contacts
[**contactsContactIdDelete**](ContactsApi.md#contactsContactIdDelete) | **DELETE** /contacts/{contact_id} | Delete a contact
[**contactsContactIdGet**](ContactsApi.md#contactsContactIdGet) | **GET** /contacts/{contact_id} | Details of 1 contact
[**contactsContactIdPut**](ContactsApi.md#contactsContactIdPut) | **PUT** /contacts/{contact_id} | Edit a contact
[**contactsGet**](ContactsApi.md#contactsGet) | **GET** /contacts | Get a list of contacts
[**contactsPost**](ContactsApi.md#contactsPost) | **POST** /contacts | Add a new contact



## bulkDeleteContacts

> EmptySuccessResponse bulkDeleteContacts(bulkActionRequestBody)

Bulk delete contacts

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

let apiInstance = new Apacta.ContactsApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Contact ids
apiInstance.bulkDeleteContacts(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Contact ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsContactIdDelete

> ClockingRecordsClockingRecordIdDelete200Response contactsContactIdDelete(contactId)

Delete a contact

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

let apiInstance = new Apacta.ContactsApi();
let contactId = "contactId_example"; // String | 
apiInstance.contactsContactIdDelete(contactId, (error, data, response) => {
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
 **contactId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsContactIdGet

> ContactsContactIdGet200Response contactsContactIdGet(contactId)

Details of 1 contact

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

let apiInstance = new Apacta.ContactsApi();
let contactId = "contactId_example"; // String | 
apiInstance.contactsContactIdGet(contactId, (error, data, response) => {
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
 **contactId** | **String**|  | 

### Return type

[**ContactsContactIdGet200Response**](ContactsContactIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsContactIdPut

> ClockingRecordsClockingRecordIdPut200Response contactsContactIdPut(contactId, opts)

Edit a contact

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

let apiInstance = new Apacta.ContactsApi();
let contactId = "contactId_example"; // String | 
let opts = {
  'contactsPostRequest': new Apacta.ContactsPostRequest() // ContactsPostRequest | 
};
apiInstance.contactsContactIdPut(contactId, opts, (error, data, response) => {
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
 **contactId** | **String**|  | 
 **contactsPostRequest** | [**ContactsPostRequest**](ContactsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsGet

> ContactsGet200Response contactsGet(opts)

Get a list of contacts

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

let apiInstance = new Apacta.ContactsApi();
let opts = {
  'name': "name_example", // String | Used to search for a contact with a specific name
  'cvr': "cvr_example", // String | Search for values in CVR field
  'ean': "ean_example", // String | Search for values in EAN field
  'erpId': "erpId_example", // String | Search for values in ERP id field
  'contactType': "contactType_example", // String | Used to show only contacts with with one specific `ContactType`
  'city': "city_example", // String | Used to show only contacts with with one specific `City`
  'modifiedGte': "modifiedGte_example" // String | 
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
 **name** | **String**| Used to search for a contact with a specific name | [optional] 
 **cvr** | **String**| Search for values in CVR field | [optional] 
 **ean** | **String**| Search for values in EAN field | [optional] 
 **erpId** | **String**| Search for values in ERP id field | [optional] 
 **contactType** | **String**| Used to show only contacts with with one specific &#x60;ContactType&#x60; | [optional] 
 **city** | **String**| Used to show only contacts with with one specific &#x60;City&#x60; | [optional] 
 **modifiedGte** | **String**|  | [optional] 

### Return type

[**ContactsGet200Response**](ContactsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsPost

> ClockingRecordsPost201Response contactsPost(opts)

Add a new contact

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

let apiInstance = new Apacta.ContactsApi();
let opts = {
  'contactsPostRequest': new Apacta.ContactsPostRequest() // ContactsPostRequest | 
};
apiInstance.contactsPost(opts, (error, data, response) => {
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
 **contactsPostRequest** | [**ContactsPostRequest**](ContactsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

