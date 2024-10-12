# WatchfulLi.SsousersApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSsoUsers**](SsousersApi.md#createSsoUsers) | **POST** /ssousers | Create a SSO User
[**deleteSsoUserById**](SsousersApi.md#deleteSsoUserById) | **DELETE** /ssousers/{id} | Delete a specific SSO User
[**getSsoUsers**](SsousersApi.md#getSsoUsers) | **GET** /ssousers | Get a list of SSO Users
[**getSsoUsersById**](SsousersApi.md#getSsoUsersById) | **GET** /ssousers/{id} | Find SSO User by ID
[**updateSsoUsers**](SsousersApi.md#updateSsoUsers) | **PUT** /ssousers/{id} | Update a SSO User



## createSsoUsers

> SsoUsers createSsoUsers(body)

Create a SSO User

Create a SSO User

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SsousersApi();
let body = new WatchfulLi.SsoUsers(); // SsoUsers | JSON object SsoUsers
apiInstance.createSsoUsers(body, (error, data, response) => {
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
 **body** | [**SsoUsers**](SsoUsers.md)| JSON object SsoUsers | 

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## deleteSsoUserById

> String deleteSsoUserById(id)

Delete a specific SSO User

Delete a specific SSO User

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SsousersApi();
let id = 789; // Number | ID of SSO User that needs to be deleted
apiInstance.deleteSsoUserById(id, (error, data, response) => {
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
 **id** | **Number**| ID of SSO User that needs to be deleted | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getSsoUsers

> SsoUsers getSsoUsers()

Get a list of SSO Users

Returns a list of SSO Users

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SsousersApi();
apiInstance.getSsoUsers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getSsoUsersById

> SsoUsers getSsoUsersById(id, opts)

Find SSO User by ID

Returns a SSO User based on ID

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SsousersApi();
let id = 789; // Number | ID of SSO User that needs to be fetched
let opts = {
  'fields': "fields_example" // String | Fields to return separate by comas: name,id
};
apiInstance.getSsoUsersById(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of SSO User that needs to be fetched | 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## updateSsoUsers

> SsoUsers updateSsoUsers(id, body)

Update a SSO User

Update a SSO User

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SsousersApi();
let id = 789; // Number | ID of SSO User that needs to be updated
let body = new WatchfulLi.SsoUsers(); // SsoUsers | JSON object SsoUsers
apiInstance.updateSsoUsers(id, body, (error, data, response) => {
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
 **id** | **Number**| ID of SSO User that needs to be updated | 
 **body** | [**SsoUsers**](SsoUsers.md)| JSON object SsoUsers | 

### Return type

[**SsoUsers**](SsoUsers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain

