# Apacta.ContactPersonsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addContactPerson**](ContactPersonsApi.md#addContactPerson) | **POST** /contacts/{contact_id}/contact_persons | Add a new contact person to a contact
[**contactsContactIdContactPersonsContactPersonIdDelete**](ContactPersonsApi.md#contactsContactIdContactPersonsContactPersonIdDelete) | **DELETE** /contacts/{contact_id}/contact_persons/{contact_person_id} | Delete a contact person
[**editContactPerson**](ContactPersonsApi.md#editContactPerson) | **PUT** /contacts/{contact_id}/contact_persons/{contact_person_id} | Edit a contact person
[**getContactPerson**](ContactPersonsApi.md#getContactPerson) | **GET** /contacts/{contact_id}/contact_persons/{contact_person_id} | Get a contact person
[**getContactPersonsList**](ContactPersonsApi.md#getContactPersonsList) | **GET** /contacts/{contact_id}/contact_persons | Get a list of contact people



## addContactPerson

> ClockingRecordsPost201Response addContactPerson(contactId, opts)

Add a new contact person to a contact

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

let apiInstance = new Apacta.ContactPersonsApi();
let contactId = "contactId_example"; // String | 
let opts = {
  'addContactPersonRequest': new Apacta.AddContactPersonRequest() // AddContactPersonRequest | 
};
apiInstance.addContactPerson(contactId, opts, (error, data, response) => {
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
 **addContactPersonRequest** | [**AddContactPersonRequest**](AddContactPersonRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsContactIdContactPersonsContactPersonIdDelete

> ClockingRecordsClockingRecordIdDelete200Response contactsContactIdContactPersonsContactPersonIdDelete(contactId, contactPersonId)

Delete a contact person

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

let apiInstance = new Apacta.ContactPersonsApi();
let contactId = "contactId_example"; // String | 
let contactPersonId = "contactPersonId_example"; // String | 
apiInstance.contactsContactIdContactPersonsContactPersonIdDelete(contactId, contactPersonId, (error, data, response) => {
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
 **contactPersonId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editContactPerson

> ClockingRecordsClockingRecordIdPut200Response editContactPerson(contactId, contactPersonId, opts)

Edit a contact person

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

let apiInstance = new Apacta.ContactPersonsApi();
let contactId = "contactId_example"; // String | 
let contactPersonId = "contactPersonId_example"; // String | 
let opts = {
  'addContactPersonRequest': new Apacta.AddContactPersonRequest() // AddContactPersonRequest | 
};
apiInstance.editContactPerson(contactId, contactPersonId, opts, (error, data, response) => {
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
 **contactPersonId** | **String**|  | 
 **addContactPersonRequest** | [**AddContactPersonRequest**](AddContactPersonRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContactPerson

> GetContactPerson200Response getContactPerson(contactId, contactPersonId)

Get a contact person

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

let apiInstance = new Apacta.ContactPersonsApi();
let contactId = "contactId_example"; // String | 
let contactPersonId = "contactPersonId_example"; // String | 
apiInstance.getContactPerson(contactId, contactPersonId, (error, data, response) => {
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
 **contactPersonId** | **String**|  | 

### Return type

[**GetContactPerson200Response**](GetContactPerson200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactPersonsList

> GetContactPersonsList200Response getContactPersonsList(contactId, opts)

Get a list of contact people

Get a list of contact people associated with a contact

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

let apiInstance = new Apacta.ContactPersonsApi();
let contactId = "contactId_example"; // String | 
let opts = {
  'q': "q_example", // String | 
  'createdGte': new Date("2013-10-20"), // Date | 
  'createdLte': new Date("2013-10-20") // Date | 
};
apiInstance.getContactPersonsList(contactId, opts, (error, data, response) => {
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
 **q** | **String**|  | [optional] 
 **createdGte** | **Date**|  | [optional] 
 **createdLte** | **Date**|  | [optional] 

### Return type

[**GetContactPersonsList200Response**](GetContactPersonsList200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

