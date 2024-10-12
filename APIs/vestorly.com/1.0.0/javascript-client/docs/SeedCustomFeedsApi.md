# VestorlyApi.SeedCustomFeedsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSeedCustomFeed**](SeedCustomFeedsApi.md#createSeedCustomFeed) | **POST** /seed_custom_feeds | 
[**deleteSeedCustomFeed**](SeedCustomFeedsApi.md#deleteSeedCustomFeed) | **DELETE** /seed_custom_feeds/{id} | 
[**findSeedCustomFeedByID**](SeedCustomFeedsApi.md#findSeedCustomFeedByID) | **GET** /seed_custom_feeds/{id} | 
[**findSeedCustomFeeds**](SeedCustomFeedsApi.md#findSeedCustomFeeds) | **GET** /seed_custom_feeds | 
[**updateSeedCustomFeedById**](SeedCustomFeedsApi.md#updateSeedCustomFeedById) | **PUT** /seed_custom_feeds/{id} | 



## createSeedCustomFeed

> SeedCustomFeedresponse createSeedCustomFeed(vestorlyAuth, seedCustomFeed, opts)



Creates a new Category Keyword

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SeedCustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let seedCustomFeed = new VestorlyApi.SeedCustomFeedInput(); // SeedCustomFeedInput | Category to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createSeedCustomFeed(vestorlyAuth, seedCustomFeed, opts, (error, data, response) => {
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
 **seedCustomFeed** | [**SeedCustomFeedInput**](SeedCustomFeedInput.md)| Category to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSeedCustomFeed

> SeedCustomFeedresponse deleteSeedCustomFeed(vestorlyAuth, id, opts)



Deletes a Category keywords

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SeedCustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of seed category to delete
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.deleteSeedCustomFeed(vestorlyAuth, id, opts, (error, data, response) => {
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
 **id** | **String**| id of seed category to delete | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findSeedCustomFeedByID

> SeedCustomFeedresponse findSeedCustomFeedByID(vestorlyAuth, id, opts)



Returns a single Category keyword

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SeedCustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Seed Custom Feed Id to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findSeedCustomFeedByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **id** | **String**| Seed Custom Feed Id to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findSeedCustomFeeds

> SeedCustomFeeds findSeedCustomFeeds(vestorlyAuth, opts)



Returns all Categories keywords

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SeedCustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findSeedCustomFeeds(vestorlyAuth, opts, (error, data, response) => {
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

[**SeedCustomFeeds**](SeedCustomFeeds.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateSeedCustomFeedById

> SeedCustomFeedresponse updateSeedCustomFeedById(vestorlyAuth, id, seedCustomFeed, opts)



Updates a Category keywords

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.SeedCustomFeedsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of seed category to update
let seedCustomFeed = new VestorlyApi.SeedCustomFeedInput(); // SeedCustomFeedInput | Category keywords to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateSeedCustomFeedById(vestorlyAuth, id, seedCustomFeed, opts, (error, data, response) => {
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
 **id** | **String**| id of seed category to update | 
 **seedCustomFeed** | [**SeedCustomFeedInput**](SeedCustomFeedInput.md)| Category keywords to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

