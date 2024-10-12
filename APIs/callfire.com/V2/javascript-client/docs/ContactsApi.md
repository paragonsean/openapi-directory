# CallFireApiDocumentation.ContactsApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addContactListItems**](ContactsApi.md#addContactListItems) | **POST** /contacts/lists/{id}/items | Add contacts to a contact list
[**addDoNotContacts**](ContactsApi.md#addDoNotContacts) | **POST** /contacts/dncs | Add do not contact (dnc) numbers
[**createContactList**](ContactsApi.md#createContactList) | **POST** /contacts/lists | Create contact lists
[**createContactListFromFile**](ContactsApi.md#createContactListFromFile) | **POST** /contacts/lists/upload | Create contact list from file
[**createContacts**](ContactsApi.md#createContacts) | **POST** /contacts | Create contacts
[**deleteContact**](ContactsApi.md#deleteContact) | **DELETE** /contacts/{id} | Delete a contact
[**deleteContactList**](ContactsApi.md#deleteContactList) | **DELETE** /contacts/lists/{id} | Delete a contact list
[**deleteDoNotContact**](ContactsApi.md#deleteDoNotContact) | **DELETE** /contacts/dncs/{number} | Delete do not contact (dnc) number. If number contains commas treat as list of numbers
[**deleteDoNotContactsBySource**](ContactsApi.md#deleteDoNotContactsBySource) | **DELETE** /contacts/dncs/sources/{source} | Delete do not contact (dnc) numbers contained in source.
[**findContactLists**](ContactsApi.md#findContactLists) | **GET** /contacts/lists | Find contact lists
[**findContacts**](ContactsApi.md#findContacts) | **GET** /contacts | Find contacts
[**findDoNotContacts**](ContactsApi.md#findDoNotContacts) | **GET** /contacts/dncs | Find do not contact (dnc) items
[**getContact**](ContactsApi.md#getContact) | **GET** /contacts/{id} | Find a specific contact
[**getContactHistory**](ContactsApi.md#getContactHistory) | **GET** /contacts/{id}/history | Find a contact&#39;s history
[**getContactList**](ContactsApi.md#getContactList) | **GET** /contacts/lists/{id} | Find a specific contact list
[**getContactListItems**](ContactsApi.md#getContactListItems) | **GET** /contacts/lists/{id}/items | Find contacts in a contact list
[**getDoNotContact**](ContactsApi.md#getDoNotContact) | **GET** /contacts/dncs/{number} | Get do not contact (dnc)
[**getUniversalDoNotContacts**](ContactsApi.md#getUniversalDoNotContacts) | **GET** /contacts/dncs/universals/{toNumber} | Find universal do not contacts (udnc) associated with toNumber
[**removeContactListItem**](ContactsApi.md#removeContactListItem) | **DELETE** /contacts/lists/{id}/items/{contactId} | Delete a contact from a contact list
[**removeContactListItems**](ContactsApi.md#removeContactListItems) | **DELETE** /contacts/lists/{id}/items | Delete contacts from a contact list
[**updateContact**](ContactsApi.md#updateContact) | **PUT** /contacts/{id} | Update a contact
[**updateContactList**](ContactsApi.md#updateContactList) | **PUT** /contacts/lists/{id} | Update a contact list
[**updateDoNotContact**](ContactsApi.md#updateDoNotContact) | **PUT** /contacts/dncs/{number} | Update an individual do not contact (dnc) number



## addContactListItems

> addContactListItems(id, opts)

Add contacts to a contact list

Adds contacts to a contact list. Available contact sources are: list of the contact entities, list of ids of existing contacts in user&#39;s account, list of phone numbers in E.164 format (11-digits)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of a contact list
let opts = {
  'addContactListContactsRequest': new CallFireApiDocumentation.AddContactListContactsRequest() // AddContactListContactsRequest | A request object
};
apiInstance.addContactListItems(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a contact list | 
 **addContactListContactsRequest** | [**AddContactListContactsRequest**](AddContactListContactsRequest.md)| A request object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addDoNotContacts

> addDoNotContacts(opts)

Add do not contact (dnc) numbers

Add or update a list of Do Not Contact (DNC) contact entries. Can toggle whether the DNCs are enabled for calls/texts.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let opts = {
  'addDoNotContactRequest': new CallFireApiDocumentation.AddDoNotContactRequest() // AddDoNotContactRequest | AddDoNotContactsRequest object
};
apiInstance.addDoNotContacts(opts, (error, data, response) => {
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
 **addDoNotContactRequest** | [**AddDoNotContactRequest**](AddDoNotContactRequest.md)| AddDoNotContactsRequest object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactList

> ContactList createContactList(opts)

Create contact lists

Creates a contact list for use with campaigns using 1 of 3 inputs. A List of Contact objects, a list of String E.164 numbers, or a list of CallFire contactIds can be used as the data source for the created contact list. After contact list is added into the CallFire system, contact lists goes through seven system safeguards that check the accuracy and consistency of the data. For example, our system checks that contact number is formatted correctly, is valid, is not duplicated in another contact list, or is not added on a specific DNC list. You can configure to keep/merge or remove contacts which do not complies these rules. If contacts were not added to a contact list after the validation, this means the data needs to be properly formatted and corrected before calling this API

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'createContactListRequest': new CallFireApiDocumentation.CreateContactListRequest() // CreateContactListRequest | A request object
};
apiInstance.createContactList(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **createContactListRequest** | [**CreateContactListRequest**](CreateContactListRequest.md)| A request object | [optional] 

### Return type

[**ContactList**](ContactList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactListFromFile

> ResourceId createContactListFromFile(file, opts)

Create contact list from file

Creates a contact list to be used with campaigns through uploading a .csv file. Returns the id of created list

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let file = "/path/to/file"; // File | CSV file to be uploaded
let opts = {
  'name': "name_example", // String | A name of a contact list
  'useCustomFields': true // Boolean | A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc
};
apiInstance.createContactListFromFile(file, opts, (error, data, response) => {
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
 **file** | **File**| CSV file to be uploaded | 
 **name** | **String**| A name of a contact list | [optional] 
 **useCustomFields** | **Boolean**| A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## createContacts

> ResourceIdList createContacts(opts)

Create contacts

Creates contacts in CallFire system. Only values from the next list can be used as external system parameter in contact creation: **NATION_BUILDER, SALES_FORCE_CONTACTS, SALES_FORCE_LEADS, SALES_FORCE_REPORTS, ZOHO, MAIL_CHIMP**. See [contacts validation rules](https://www.callfire.com/help/docs/getting-started/managing-contacts/validating-contacts#section1)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let opts = {
  'contact': [new CallFireApiDocumentation.Contact()] // [Contact] | A list of a contact objects
};
apiInstance.createContacts(opts, (error, data, response) => {
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
 **contact** | [**[Contact]**](Contact.md)| A list of a contact objects | [optional] 

### Return type

[**ResourceIdList**](ResourceIdList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteContact

> deleteContact(id)

Delete a contact

Deletes a contact instance from account

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An Id of a contact
apiInstance.deleteContact(id, (error, data, response) => {
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
 **id** | **Number**| An Id of a contact | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteContactList

> deleteContactList(id)

Delete a contact list

Deletes a contact list, included contacts will not be deleted.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of the contact list to be deleted
apiInstance.deleteContactList(id, (error, data, response) => {
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
 **id** | **Number**| An id of the contact list to be deleted | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDoNotContact

> deleteDoNotContact(number)

Delete do not contact (dnc) number. If number contains commas treat as list of numbers

Delete a Do Not Contact (DNC) contact entry.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let number = "number_example"; // String | Number associated with Do Not Contact (DNC) entry.
apiInstance.deleteDoNotContact(number, (error, data, response) => {
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
 **number** | **String**| Number associated with Do Not Contact (DNC) entry. | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDoNotContactsBySource

> deleteDoNotContactsBySource(source)

Delete do not contact (dnc) numbers contained in source.

Delete Do Not Contact (DNC) contact entries contained in source.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let source = "source_example"; // String | Source associated with Do Not Contact (DNC) entry.
apiInstance.deleteDoNotContactsBySource(source, (error, data, response) => {
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
 **source** | **String**| Source associated with Do Not Contact (DNC) entry. | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findContactLists

> ContactListPage findContactLists(opts)

Find contact lists

Searches for all contact lists which are available for the current user. Returns a paged list of contact lists

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'name': "name_example", // String | A name or a partial name of a contact list
  'exactMatch': true, // Boolean | ~
  'contactCount': 56, // Number | ~
  'orderBy': "orderBy_example" // String | ~
};
apiInstance.findContactLists(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **name** | **String**| A name or a partial name of a contact list | [optional] 
 **exactMatch** | **Boolean**| ~ | [optional] 
 **contactCount** | **Number**| ~ | [optional] 
 **orderBy** | **String**| ~ | [optional] 

### Return type

[**ContactListPage**](ContactListPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findContacts

> ContactPage findContacts(opts)

Find contacts

Find user&#39;s contacts by id, contact list, or on any property name. Returns a paged list of contacts

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'id': [null], // [Number] | A list of contact IDs. If the id parameter is included, the other query parameters are ignored.
  'number': ["null"], // [String] | Multiple contact numbers can be specified. If the number parameter is included, the other query parameters are ignored.
  'contactListId': 789, // Number | Filters contacts by a particular contact list
  'propertyName': "propertyName_example", // String | Name of a contact property to search by
  'propertyValue': "propertyValue_example" // String | Value of a contact property to search by
};
apiInstance.findContacts(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **id** | [**[Number]**](Number.md)| A list of contact IDs. If the id parameter is included, the other query parameters are ignored. | [optional] 
 **number** | [**[String]**](String.md)| Multiple contact numbers can be specified. If the number parameter is included, the other query parameters are ignored. | [optional] 
 **contactListId** | **Number**| Filters contacts by a particular contact list | [optional] 
 **propertyName** | **String**| Name of a contact property to search by | [optional] 
 **propertyValue** | **String**| Value of a contact property to search by | [optional] 

### Return type

[**ContactPage**](ContactPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findDoNotContacts

> DoNotContactPage findDoNotContacts(opts)

Find do not contact (dnc) items

Searches for all Do Not Contact (DNC) objects created by user. These DoNotContact entries only affect calls/texts/campaigns on this account. Returns a paged list of DoNotContact objects

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'prefix': "prefix_example", // String | Prefix (1-10 digits) of phone numbers
  'campaignId': 789, // Number | A campaign id which was used to send a message to a DNC number
  'source': "source_example", // String | A DNC source name to search for DNCs
  'call': true, // Boolean | Show only Do-Not-Call numbers
  'text': true, // Boolean | Show only Do-Not-Text numbers
  'inboundCall': true, // Boolean | ~
  'inboundText': true, // Boolean | ~
  'number': ["null"] // [String] | ~
};
apiInstance.findDoNotContacts(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **prefix** | **String**| Prefix (1-10 digits) of phone numbers | [optional] 
 **campaignId** | **Number**| A campaign id which was used to send a message to a DNC number | [optional] 
 **source** | **String**| A DNC source name to search for DNCs | [optional] 
 **call** | **Boolean**| Show only Do-Not-Call numbers | [optional] 
 **text** | **Boolean**| Show only Do-Not-Text numbers | [optional] 
 **inboundCall** | **Boolean**| ~ | [optional] 
 **inboundText** | **Boolean**| ~ | [optional] 
 **number** | [**[String]**](String.md)| ~ | [optional] 

### Return type

[**DoNotContactPage**](DoNotContactPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContact

> Contact getContact(id, opts)

Find a specific contact

Returns a Contact instance for a given contact id. Deleted contacts can be still retrieved but will be marked as deleted. Deleted contacts will not be shown in search request.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of a contact
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getContact(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a contact | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactHistory

> ContactHistory getContactHistory(id, opts)

Find a contact&#39;s history

Searches for all texts and calls attributed to a contact. Returns a list of calls and texts a contact has been involved with

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An Id of a contact
let opts = {
  'limit': 56, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 56, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getContactHistory(id, opts, (error, data, response) => {
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
 **id** | **Number**| An Id of a contact | 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] 
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**ContactHistory**](ContactHistory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactList

> ContactList getContactList(id, opts)

Find a specific contact list

Returns a single ContactList instance for a given contact list id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of a contact list to return
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getContactList(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a contact list to return | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**ContactList**](ContactList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactListItems

> ContactPage getContactListItems(id, opts)

Find contacts in a contact list

Searches for all entries in a contact list with specified id. Returns a paged list of contact entries

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of a contact list
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 56, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 56 // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
};
apiInstance.getContactListItems(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a contact list | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] 
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] 

### Return type

[**ContactPage**](ContactPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDoNotContact

> DoNotContact getDoNotContact(number)

Get do not contact (dnc)

Get Do Not Contact (DNC) object create by user. This DoNotContact entry only affects calls/texts/campaigns on this account.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let number = "number_example"; // String | Number associated with Do Not Contact (DNC) entry.
apiInstance.getDoNotContact(number, (error, data, response) => {
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
 **number** | **String**| Number associated with Do Not Contact (DNC) entry. | 

### Return type

[**DoNotContact**](DoNotContact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUniversalDoNotContacts

> ItemListUniversalDoNotContact getUniversalDoNotContacts(toNumber, opts)

Find universal do not contacts (udnc) associated with toNumber

Searches for a UniversalDoNotContact object for a given phone number. Shows whether inbound/outbound actions are allowed for a given number

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let toNumber = "toNumber_example"; // String | A required destination phone number in E.164 format (11-digit). Example: 12132000384
let opts = {
  'fromNumber': "fromNumber_example", // String | An optional destination/source number for DNC, specified in E.164 format (11-digit). Example: 12132000384
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getUniversalDoNotContacts(toNumber, opts, (error, data, response) => {
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
 **toNumber** | **String**| A required destination phone number in E.164 format (11-digit). Example: 12132000384 | 
 **fromNumber** | **String**| An optional destination/source number for DNC, specified in E.164 format (11-digit). Example: 12132000384 | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**ItemListUniversalDoNotContact**](ItemListUniversalDoNotContact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeContactListItem

> removeContactListItem(id, contactId)

Delete a contact from a contact list

Deletes a single contact from a contact list

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of a contact list
let contactId = 789; // Number | An id of a contact
apiInstance.removeContactListItem(id, contactId, (error, data, response) => {
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
 **id** | **Number**| An id of a contact list | 
 **contactId** | **Number**| An id of a contact | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeContactListItems

> removeContactListItems(id, opts)

Delete contacts from a contact list

Deletes contacts from a contact list. List the contact ids in request to delete multiple contacts with one request.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | A id of a contact list
let opts = {
  'contactId': [null] // [Number] | An id of a contact entity in the CallFire system
};
apiInstance.removeContactListItems(id, opts, (error, data, response) => {
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
 **id** | **Number**| A id of a contact list | 
 **contactId** | [**[Number]**](Number.md)| An id of a contact entity in the CallFire system | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateContact

> updateContact(id, opts)

Update a contact

Updates a single contact instance with id specified. See [contact validation rules](https://www.callfire.com/help/docs/getting-started/managing-contacts/validating-contacts#section1)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of a contact
let opts = {
  'contact': new CallFireApiDocumentation.Contact() // Contact | A contact object
};
apiInstance.updateContact(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a contact | 
 **contact** | [**Contact**](Contact.md)| A contact object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactList

> updateContactList(id, opts)

Update a contact list

Updates contact list instance.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let id = 789; // Number | An id of contact list to update
let opts = {
  'updateContactListRequest': new CallFireApiDocumentation.UpdateContactListRequest() // UpdateContactListRequest | A request object
};
apiInstance.updateContactList(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of contact list to update | 
 **updateContactListRequest** | [**UpdateContactListRequest**](UpdateContactListRequest.md)| A request object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDoNotContact

> updateDoNotContact(number, opts)

Update an individual do not contact (dnc) number

Update a Do Not Contact (DNC) contact entry. Can toggle whether the DNC is enabled for calls/texts.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.ContactsApi();
let number = "number_example"; // String | ~
let opts = {
  'doNotContact': new CallFireApiDocumentation.DoNotContact() // DoNotContact | DoNotContact object
};
apiInstance.updateDoNotContact(number, opts, (error, data, response) => {
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
 **number** | **String**| ~ | 
 **doNotContact** | [**DoNotContact**](DoNotContact.md)| DoNotContact object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

