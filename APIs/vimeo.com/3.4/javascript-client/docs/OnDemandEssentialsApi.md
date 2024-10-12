# Vimeo.OnDemandEssentialsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVod**](OnDemandEssentialsApi.md#createVod) | **POST** /users/{user_id}/ondemand/pages | Create an On Demand page
[**createVodAlt1**](OnDemandEssentialsApi.md#createVodAlt1) | **POST** /me/ondemand/pages | Create an On Demand page
[**deleteVodDraft**](OnDemandEssentialsApi.md#deleteVodDraft) | **DELETE** /ondemand/pages/{ondemand_id} | Delete a draft of an On Demand page
[**editVod**](OnDemandEssentialsApi.md#editVod) | **PATCH** /ondemand/pages/{ondemand_id} | Edit an On Demand page
[**getUserVods**](OnDemandEssentialsApi.md#getUserVods) | **GET** /users/{user_id}/ondemand/pages | Get all the On Demand pages of a user
[**getUserVodsAlt1**](OnDemandEssentialsApi.md#getUserVodsAlt1) | **GET** /me/ondemand/pages | Get all the On Demand pages of a user
[**getVod**](OnDemandEssentialsApi.md#getVod) | **GET** /ondemand/pages/{ondemand_id} | Get a specific On Demand page



## createVod

> OnDemandPage createVod(userId, createVodAlt1Request)

Create an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let createVodAlt1Request = new Vimeo.CreateVodAlt1Request(); // CreateVodAlt1Request | 
apiInstance.createVod(userId, createVodAlt1Request, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **createVodAlt1Request** | [**CreateVodAlt1Request**](CreateVodAlt1Request.md)|  | 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVodAlt1

> OnDemandPage createVodAlt1(createVodAlt1Request)

Create an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let createVodAlt1Request = new Vimeo.CreateVodAlt1Request(); // CreateVodAlt1Request | 
apiInstance.createVodAlt1(createVodAlt1Request, (error, data, response) => {
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
 **createVodAlt1Request** | [**CreateVodAlt1Request**](CreateVodAlt1Request.md)|  | 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVodDraft

> deleteVodDraft(ondemandId)

Delete a draft of an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.deleteVodDraft(ondemandId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## editVod

> OnDemandPage editVod(ondemandId, opts)

Edit an On Demand page

Enable preorders or publish the page.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let opts = {
  'editVodRequest': new Vimeo.EditVodRequest() // EditVodRequest | 
};
apiInstance.editVod(ondemandId, opts, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **editVodRequest** | [**EditVodRequest**](EditVodRequest.md)|  | [optional] 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.ondemand.page+json
- **Accept**: application/vnd.vimeo.ondemand.page+json


## getUserVods

> [OnDemandPage] getUserVods(userId, opts)

Get all the On Demand pages of a user

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The type of On Demand pages to return.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getUserVods(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The type of On Demand pages to return. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[OnDemandPage]**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## getUserVodsAlt1

> [OnDemandPage] getUserVodsAlt1(opts)

Get all the On Demand pages of a user

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The type of On Demand pages to return.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getUserVodsAlt1(opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The type of On Demand pages to return. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[OnDemandPage]**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## getVod

> OnDemandPage getVod(ondemandId)

Get a specific On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandEssentialsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getVod(ondemandId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json

