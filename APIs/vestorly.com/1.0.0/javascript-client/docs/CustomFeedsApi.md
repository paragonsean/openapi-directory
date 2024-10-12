# VestorlyApi.CustomFeedsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomFeed**](CustomFeedsApi.md#createCustomFeed) | **POST** /custom_feeds | 
[**deleteCustomFeed**](CustomFeedsApi.md#deleteCustomFeed) | **DELETE** /custom_feeds/{id} | 
[**duplicateCustomFeed**](CustomFeedsApi.md#duplicateCustomFeed) | **POST** /custom_feeds/{id}/duplicates | 
[**findCustomFeedByID**](CustomFeedsApi.md#findCustomFeedByID) | **GET** /custom_feeds/{id} | 
[**findCustomFeeds**](CustomFeedsApi.md#findCustomFeeds) | **GET** /custom_feeds | 
[**updateCategoryById**](CustomFeedsApi.md#updateCategoryById) | **PUT** /custom_feeds/{id} | 



## createCustomFeed

> CustomFeedresponse createCustomFeed(vestorlyAuth, customFeed, opts)



Creates a new Category

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let customFeed = new VestorlyApi.CustomFeedInput(); // CustomFeedInput | Category to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createCustomFeed(vestorlyAuth, customFeed, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **customFeed** | [**CustomFeedInput**](CustomFeedInput.md)| Category to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCustomFeed

> CustomFeedresponse deleteCustomFeed(vestorlyAuth, id, opts)



Deletes a new Category

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of category to delete
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.deleteCustomFeed(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| id of category to delete | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## duplicateCustomFeed

> CustomFeedresponse duplicateCustomFeed(vestorlyAuth, id, opts)



Duplicates Category

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of category to duplicate
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.duplicateCustomFeed(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| id of category to duplicate | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findCustomFeedByID

> CustomFeedresponse findCustomFeedByID(vestorlyAuth, id, opts)



Returns a single Category

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Custom Feed Id to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findCustomFeedByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| Custom Feed Id to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findCustomFeeds

> CustomFeeds findCustomFeeds(vestorlyAuth, opts)



Returns all Categories

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findCustomFeeds(vestorlyAuth, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeeds**](CustomFeeds.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateCategoryById

> CustomFeedresponse updateCategoryById(vestorlyAuth, id, customFeed, opts)



Updates a Category

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of category to update
let customFeed = new VestorlyApi.CustomFeedInput(); // CustomFeedInput | Category to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateCategoryById(vestorlyAuth, id, customFeed, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| id of category to update | 
 **customFeed** | [**CustomFeedInput**](CustomFeedInput.md)| Category to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

