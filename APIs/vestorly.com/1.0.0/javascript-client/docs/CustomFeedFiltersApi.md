# VestorlyApi.CustomFeedFiltersApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomFeedFilter**](CustomFeedFiltersApi.md#createCustomFeedFilter) | **POST** /custom_feed_filters | 
[**deleteCustomFeedFilter**](CustomFeedFiltersApi.md#deleteCustomFeedFilter) | **DELETE** /custom_feed_filters/{id} | 
[**findCustomFeedFilterByID**](CustomFeedFiltersApi.md#findCustomFeedFilterByID) | **GET** /custom_feed_filters/{id} | 
[**findCustomFeedFilters**](CustomFeedFiltersApi.md#findCustomFeedFilters) | **GET** /custom_feed_filters | 
[**updateCustomFeedFilterById**](CustomFeedFiltersApi.md#updateCustomFeedFilterById) | **PUT** /custom_feed_filters/{id} | 



## createCustomFeedFilter

> CustomFeedFilterresponse createCustomFeedFilter(vestorlyAuth, customFeedFilter, opts)



Creates a new Category filter

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedFiltersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let customFeedFilter = new VestorlyApi.CustomFeedFilterInput(); // CustomFeedFilterInput | Category filter to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createCustomFeedFilter(vestorlyAuth, customFeedFilter, opts, (error, data, response) => {
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
 **customFeedFilter** | [**CustomFeedFilterInput**](CustomFeedFilterInput.md)| Category filter to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCustomFeedFilter

> CustomFeedFilterresponse deleteCustomFeedFilter(vestorlyAuth, id, opts)



Deletes the Category&#39;s filter

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedFiltersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of category filter to delete
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.deleteCustomFeedFilter(vestorlyAuth, id, opts, (error, data, response) => {
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
 **id** | **String**| id of category filter to delete | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCustomFeedFilterByID

> CustomFeedFilterresponse findCustomFeedFilterByID(vestorlyAuth, id, opts)



Returns a single Category&#39;s filter

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedFiltersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Custom Feed Filter Id to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findCustomFeedFilterByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **id** | **String**| Custom Feed Filter Id to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findCustomFeedFilters

> CustomFeedFilters findCustomFeedFilters(vestorlyAuth, opts)



Returns all Categorie&#39;s filters

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedFiltersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findCustomFeedFilters(vestorlyAuth, opts, (error, data, response) => {
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

[**CustomFeedFilters**](CustomFeedFilters.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateCustomFeedFilterById

> CustomFeedFilterresponse updateCustomFeedFilterById(vestorlyAuth, id, customFeedFilter, opts)



Updates a Category Feed Filter

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.CustomFeedFiltersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of category filter to update
let customFeedFilter = new VestorlyApi.CustomFeedFilterInput(); // CustomFeedFilterInput | Category filter to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateCustomFeedFilterById(vestorlyAuth, id, customFeedFilter, opts, (error, data, response) => {
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
 **id** | **String**| id of category filter to update | 
 **customFeedFilter** | [**CustomFeedFilterInput**](CustomFeedFilterInput.md)| Category filter to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

