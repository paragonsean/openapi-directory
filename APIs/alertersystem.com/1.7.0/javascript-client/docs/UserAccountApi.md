# AlerterSystemApi.UserAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiUserAccountGetCollection**](UserAccountApi.md#apiUserAccountGetCollection) | **GET** /api/user-account | Retrieves the collection of UserAccount resources.
[**apiUserAccountIdGet**](UserAccountApi.md#apiUserAccountIdGet) | **GET** /api/user-account/{id} | Retrieves a UserAccount resource.
[**apiUserAccountIdPatch**](UserAccountApi.md#apiUserAccountIdPatch) | **PATCH** /api/user-account/{id} | Updates the UserAccount resource.
[**apiUserAccountIdPut**](UserAccountApi.md#apiUserAccountIdPut) | **PUT** /api/user-account/{id} | Replaces the UserAccount resource.



## apiUserAccountGetCollection

> [UserAccountGet] apiUserAccountGetCollection(opts)

Retrieves the collection of UserAccount resources.

Retrieves the collection of UserAccount resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.UserAccountApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiUserAccountGetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[UserAccountGet]**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiUserAccountIdGet

> UserAccountGet apiUserAccountIdGet(id)

Retrieves a UserAccount resource.

Retrieves a UserAccount resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.UserAccountApi();
let id = "id_example"; // String | UserAccount identifier
apiInstance.apiUserAccountIdGet(id, (error, data, response) => {
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
 **id** | **String**| UserAccount identifier | 

### Return type

[**UserAccountGet**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiUserAccountIdPatch

> UserAccountGet apiUserAccountIdPatch(id, userAccountPatch)

Updates the UserAccount resource.

Updates the UserAccount resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.UserAccountApi();
let id = "id_example"; // String | UserAccount identifier
let userAccountPatch = new AlerterSystemApi.UserAccountPatch(); // UserAccountPatch | The updated UserAccount resource
apiInstance.apiUserAccountIdPatch(id, userAccountPatch, (error, data, response) => {
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
 **id** | **String**| UserAccount identifier | 
 **userAccountPatch** | [**UserAccountPatch**](UserAccountPatch.md)| The updated UserAccount resource | 

### Return type

[**UserAccountGet**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiUserAccountIdPut

> UserAccountGet apiUserAccountIdPut(id, userAccountPut)

Replaces the UserAccount resource.

Replaces the UserAccount resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.UserAccountApi();
let id = "id_example"; // String | UserAccount identifier
let userAccountPut = new AlerterSystemApi.UserAccountPut(); // UserAccountPut | The updated UserAccount resource
apiInstance.apiUserAccountIdPut(id, userAccountPut, (error, data, response) => {
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
 **id** | **String**| UserAccount identifier | 
 **userAccountPut** | [**UserAccountPut**](UserAccountPut.md)| The updated UserAccount resource | 

### Return type

[**UserAccountGet**](UserAccountGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

