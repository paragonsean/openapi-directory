# PeerTube.AccountBlocksApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1BlocklistStatusGet**](AccountBlocksApi.md#apiV1BlocklistStatusGet) | **GET** /api/v1/blocklist/status | Get block status of accounts/hosts
[**apiV1ServerBlocklistAccountsAccountNameDelete**](AccountBlocksApi.md#apiV1ServerBlocklistAccountsAccountNameDelete) | **DELETE** /api/v1/server/blocklist/accounts/{accountName} | Unblock an account by its handle
[**apiV1ServerBlocklistAccountsGet**](AccountBlocksApi.md#apiV1ServerBlocklistAccountsGet) | **GET** /api/v1/server/blocklist/accounts | List account blocks
[**apiV1ServerBlocklistAccountsPost**](AccountBlocksApi.md#apiV1ServerBlocklistAccountsPost) | **POST** /api/v1/server/blocklist/accounts | Block an account



## apiV1BlocklistStatusGet

> BlockStatus apiV1BlocklistStatusGet(opts)

Get block status of accounts/hosts

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.AccountBlocksApi();
let opts = {
  'accounts': ["null"], // [String] | Check if these accounts are blocked
  'hosts': ["null"] // [String] | Check if these hosts are blocked
};
apiInstance.apiV1BlocklistStatusGet(opts, (error, data, response) => {
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
 **accounts** | [**[String]**](String.md)| Check if these accounts are blocked | [optional] 
 **hosts** | [**[String]**](String.md)| Check if these hosts are blocked | [optional] 

### Return type

[**BlockStatus**](BlockStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1ServerBlocklistAccountsAccountNameDelete

> apiV1ServerBlocklistAccountsAccountNameDelete(accountName)

Unblock an account by its handle

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AccountBlocksApi();
let accountName = "accountName_example"; // String | account to unblock, in the form `username@domain`
apiInstance.apiV1ServerBlocklistAccountsAccountNameDelete(accountName, (error, data, response) => {
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
 **accountName** | **String**| account to unblock, in the form &#x60;username@domain&#x60; | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerBlocklistAccountsGet

> apiV1ServerBlocklistAccountsGet(opts)

List account blocks

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AccountBlocksApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1ServerBlocklistAccountsGet(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ServerBlocklistAccountsPost

> apiV1ServerBlocklistAccountsPost(opts)

Block an account

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AccountBlocksApi();
let opts = {
  'apiV1ServerBlocklistAccountsPostRequest': new PeerTube.ApiV1ServerBlocklistAccountsPostRequest() // ApiV1ServerBlocklistAccountsPostRequest | 
};
apiInstance.apiV1ServerBlocklistAccountsPost(opts, (error, data, response) => {
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
 **apiV1ServerBlocklistAccountsPostRequest** | [**ApiV1ServerBlocklistAccountsPostRequest**](ApiV1ServerBlocklistAccountsPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

