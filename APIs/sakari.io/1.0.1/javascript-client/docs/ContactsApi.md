# Sakari.ContactsApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contactsCreate**](ContactsApi.md#contactsCreate) | **POST** /v1/accounts/{accountId}/contacts | Create contact
[**contactsFetch**](ContactsApi.md#contactsFetch) | **GET** /v1/accounts/{accountId}/contacts/{contactId} | Fetch contact by ID
[**contactsFetchAll**](ContactsApi.md#contactsFetchAll) | **GET** /v1/accounts/{accountId}/contacts | Fetch contacts
[**contactsRemove**](ContactsApi.md#contactsRemove) | **DELETE** /v1/accounts/{accountId}/contacts/{contactId} | Deletes a contact
[**contactsUpdate**](ContactsApi.md#contactsUpdate) | **PUT** /v1/accounts/{accountId}/contacts/{contactId} | Updates a contact



## contactsCreate

> ContactsCreate201Response contactsCreate(accountId, opts)

Create contact

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ContactsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'mergeStrategy': "mergeStrategy_example", // String | Determines how existing contacts with matching mobile numbers are treated
  'contactRequest': new Sakari.ContactRequest() // ContactRequest | 
};
apiInstance.contactsCreate(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **mergeStrategy** | **String**| Determines how existing contacts with matching mobile numbers are treated | [optional] 
 **contactRequest** | [**ContactRequest**](ContactRequest.md)|  | [optional] 

### Return type

[**ContactsCreate201Response**](ContactsCreate201Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: application/json, text/csv
- **Accept**: application/json


## contactsFetch

> ContactResponse contactsFetch(accountId, contactId)

Fetch contact by ID

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ContactsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let contactId = "contactId_example"; // String | ID of contact to return
apiInstance.contactsFetch(accountId, contactId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **contactId** | **String**| ID of contact to return | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsFetchAll

> ContactsResponse contactsFetchAll(accountId, opts)

Fetch contacts

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ContactsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let opts = {
  'offset': 789, // Number | Results to skip when paginating through a result set
  'limit': 789, // Number | Maximum number of results to return
  'firstName': "firstName_example", // String | Filter by first name or part of
  'lastName': "lastName_example", // String | Filter by last name or part of
  'mobile': "mobile_example", // String | Filter by mobile or part of
  'email': "email_example", // String | Filter by email or part of
  'tags': "tags_example" // String | Filter by tag(s)
};
apiInstance.contactsFetchAll(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **offset** | **Number**| Results to skip when paginating through a result set | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] 
 **firstName** | **String**| Filter by first name or part of | [optional] 
 **lastName** | **String**| Filter by last name or part of | [optional] 
 **mobile** | **String**| Filter by mobile or part of | [optional] 
 **email** | **String**| Filter by email or part of | [optional] 
 **tags** | **String**| Filter by tag(s) | [optional] 

### Return type

[**ContactsResponse**](ContactsResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsRemove

> CampaignsRemove200Response contactsRemove(accountId, contactId)

Deletes a contact

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ContactsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let contactId = "contactId_example"; // String | Contact id to delete
apiInstance.contactsRemove(accountId, contactId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **contactId** | **String**| Contact id to delete | 

### Return type

[**CampaignsRemove200Response**](CampaignsRemove200Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsUpdate

> ContactResponse contactsUpdate(accountId, contactId)

Updates a contact

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.ContactsApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let contactId = "contactId_example"; // String | ID of contact
apiInstance.contactsUpdate(accountId, contactId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **contactId** | **String**| ID of contact | 

### Return type

[**ContactResponse**](ContactResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

