# SessionManagerApi.SessionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createnewsession**](SessionsApi.md#createnewsession) | **POST** /sessions | Create new session
[**editsession**](SessionsApi.md#editsession) | **PATCH** /sessions | Edit session
[**getSession**](SessionsApi.md#getSession) | **GET** /sessions | Get Session



## createnewsession

> createnewsession(createnewsessionRequest)

Create new session

The response should contain a session cookie. Further &#x60;POST&#x60; or &#x60;PATCH&#x60; requests will edit the existing session rather than creating a new one. All parameters in the body that are not within the public namespace will be ignored. Query string items will automatically be added to the public namespace. Cookies relevant to the session manager execution are also recorded.    &gt; The sessions API uses the &#x60;vtex_session&#x60; cookie to store the data required to identify the user and the session. This cookie is stored in the user&#39;s browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.

### Example

```javascript
import SessionManagerApi from 'session_manager_api';

let apiInstance = new SessionManagerApi.SessionsApi();
let createnewsessionRequest = {"public":{"country":{"value":"BR"},"postalCode":{"value":"12345"}}}; // CreatenewsessionRequest | 
apiInstance.createnewsession(createnewsessionRequest, (error, data, response) => {
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
 **createnewsessionRequest** | [**CreatenewsessionRequest**](CreatenewsessionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## editsession

> editsession(editsessionRequest)

Edit session

This works exactly the same as the POST create session, but when the request is sent with a vtex_session cookie, it retrieves the session first and then applies the changes instead of generating a new one.    As with the &#x60;POST&#x60; method, only keys inside the public namespace on the body are considered, and query parameters are automatically added to the public namespace.    &gt; The sessions API uses the &#x60;vtex_session&#x60; cookie to store the data required to identify the user and the session. This cookie is stored in the user&#39;s browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.

### Example

```javascript
import SessionManagerApi from 'session_manager_api';

let apiInstance = new SessionManagerApi.SessionsApi();
let editsessionRequest = {"public":{"newValue":{"value":"patched"}}}; // EditsessionRequest | 
apiInstance.editsession(editsessionRequest, (error, data, response) => {
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
 **editsessionRequest** | [**EditsessionRequest**](EditsessionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getSession

> getSession(items)

Get Session

Items are the keys of the values you wish to get. It follows the format &#x60;namespace1.key1,namespace2.key2&#x60;. So if you wish to recover the data sent on the previous request, it should be &#x60;public.country,public.postalCode&#x60;.    &gt; The sessions API uses the &#x60;vtex_session&#x60; cookie to store the data required to identify the user and the session. This cookie is stored in the user&#39;s browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.    &gt; If you want to retrieve all keys from Session Manager, you can use the wildcard operator (&#x60;*&#x60;) in your request (i.e. &#x60;?items&#x3D;*&#x60;).

### Example

```javascript
import SessionManagerApi from 'session_manager_api';

let apiInstance = new SessionManagerApi.SessionsApi();
let items = "namespace1.key1,namespace2.key2"; // String | Items are the keys of the values you wish to get. It follows the format `namespace1.key1,namespace2.key2`
apiInstance.getSession(items, (error, data, response) => {
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
 **items** | **String**| Items are the keys of the values you wish to get. It follows the format &#x60;namespace1.key1,namespace2.key2&#x60; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

