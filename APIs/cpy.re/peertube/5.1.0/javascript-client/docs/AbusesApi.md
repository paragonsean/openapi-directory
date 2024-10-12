# PeerTube.AbusesApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1AbusesAbuseIdDelete**](AbusesApi.md#apiV1AbusesAbuseIdDelete) | **DELETE** /api/v1/abuses/{abuseId} | Delete an abuse
[**apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete**](AbusesApi.md#apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete) | **DELETE** /api/v1/abuses/{abuseId}/messages/{abuseMessageId} | Delete an abuse message
[**apiV1AbusesAbuseIdMessagesGet**](AbusesApi.md#apiV1AbusesAbuseIdMessagesGet) | **GET** /api/v1/abuses/{abuseId}/messages | List messages of an abuse
[**apiV1AbusesAbuseIdMessagesPost**](AbusesApi.md#apiV1AbusesAbuseIdMessagesPost) | **POST** /api/v1/abuses/{abuseId}/messages | Add message to an abuse
[**apiV1AbusesAbuseIdPut**](AbusesApi.md#apiV1AbusesAbuseIdPut) | **PUT** /api/v1/abuses/{abuseId} | Update an abuse
[**apiV1AbusesPost**](AbusesApi.md#apiV1AbusesPost) | **POST** /api/v1/abuses | Report an abuse
[**getAbuses**](AbusesApi.md#getAbuses) | **GET** /api/v1/abuses | List abuses
[**getMyAbuses**](AbusesApi.md#getMyAbuses) | **GET** /api/v1/users/me/abuses | List my abuses



## apiV1AbusesAbuseIdDelete

> apiV1AbusesAbuseIdDelete(abuseId)

Delete an abuse

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let abuseId = 56; // Number | Abuse id
apiInstance.apiV1AbusesAbuseIdDelete(abuseId, (error, data, response) => {
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
 **abuseId** | **Number**| Abuse id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete

> apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(abuseId, abuseMessageId)

Delete an abuse message

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let abuseId = 56; // Number | Abuse id
let abuseMessageId = 56; // Number | Abuse message id
apiInstance.apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(abuseId, abuseMessageId, (error, data, response) => {
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
 **abuseId** | **Number**| Abuse id | 
 **abuseMessageId** | **Number**| Abuse message id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1AbusesAbuseIdMessagesGet

> ApiV1AbusesAbuseIdMessagesGet200Response apiV1AbusesAbuseIdMessagesGet(abuseId)

List messages of an abuse

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let abuseId = 56; // Number | Abuse id
apiInstance.apiV1AbusesAbuseIdMessagesGet(abuseId, (error, data, response) => {
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
 **abuseId** | **Number**| Abuse id | 

### Return type

[**ApiV1AbusesAbuseIdMessagesGet200Response**](ApiV1AbusesAbuseIdMessagesGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1AbusesAbuseIdMessagesPost

> apiV1AbusesAbuseIdMessagesPost(abuseId, apiV1AbusesAbuseIdMessagesPostRequest)

Add message to an abuse

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let abuseId = 56; // Number | Abuse id
let apiV1AbusesAbuseIdMessagesPostRequest = new PeerTube.ApiV1AbusesAbuseIdMessagesPostRequest(); // ApiV1AbusesAbuseIdMessagesPostRequest | 
apiInstance.apiV1AbusesAbuseIdMessagesPost(abuseId, apiV1AbusesAbuseIdMessagesPostRequest, (error, data, response) => {
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
 **abuseId** | **Number**| Abuse id | 
 **apiV1AbusesAbuseIdMessagesPostRequest** | [**ApiV1AbusesAbuseIdMessagesPostRequest**](ApiV1AbusesAbuseIdMessagesPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1AbusesAbuseIdPut

> apiV1AbusesAbuseIdPut(abuseId, opts)

Update an abuse

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let abuseId = 56; // Number | Abuse id
let opts = {
  'apiV1AbusesAbuseIdPutRequest': new PeerTube.ApiV1AbusesAbuseIdPutRequest() // ApiV1AbusesAbuseIdPutRequest | 
};
apiInstance.apiV1AbusesAbuseIdPut(abuseId, opts, (error, data, response) => {
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
 **abuseId** | **Number**| Abuse id | 
 **apiV1AbusesAbuseIdPutRequest** | [**ApiV1AbusesAbuseIdPutRequest**](ApiV1AbusesAbuseIdPutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1AbusesPost

> ApiV1AbusesPost200Response apiV1AbusesPost(apiV1AbusesPostRequest)

Report an abuse

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let apiV1AbusesPostRequest = new PeerTube.ApiV1AbusesPostRequest(); // ApiV1AbusesPostRequest | 
apiInstance.apiV1AbusesPost(apiV1AbusesPostRequest, (error, data, response) => {
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
 **apiV1AbusesPostRequest** | [**ApiV1AbusesPostRequest**](ApiV1AbusesPostRequest.md)|  | 

### Return type

[**ApiV1AbusesPost200Response**](ApiV1AbusesPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAbuses

> GetAbuses200Response getAbuses(opts)

List abuses

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let opts = {
  'id': 56, // Number | only list the report with this id
  'predefinedReason': ["null"], // [String] | predefined reason the listed reports should contain
  'search': "search_example", // String | plain search that will match with video titles, reporter names and more
  'state': new PeerTube.AbuseStateSet(), // AbuseStateSet | 
  'searchReporter': "searchReporter_example", // String | only list reports of a specific reporter
  'searchReportee': "searchReportee_example", // String | only list reports of a specific reportee
  'searchVideo': "searchVideo_example", // String | only list reports of a specific video
  'searchVideoChannel': "searchVideoChannel_example", // String | only list reports of a specific video channel
  'videoIs': "videoIs_example", // String | only list deleted or blocklisted videos
  'filter': "filter_example", // String | only list account, comment or video reports
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "sort_example" // String | Sort abuses by criteria
};
apiInstance.getAbuses(opts, (error, data, response) => {
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
 **id** | **Number**| only list the report with this id | [optional] 
 **predefinedReason** | [**[String]**](String.md)| predefined reason the listed reports should contain | [optional] 
 **search** | **String**| plain search that will match with video titles, reporter names and more | [optional] 
 **state** | [**AbuseStateSet**](.md)|  | [optional] 
 **searchReporter** | **String**| only list reports of a specific reporter | [optional] 
 **searchReportee** | **String**| only list reports of a specific reportee | [optional] 
 **searchVideo** | **String**| only list reports of a specific video | [optional] 
 **searchVideoChannel** | **String**| only list reports of a specific video channel | [optional] 
 **videoIs** | **String**| only list deleted or blocklisted videos | [optional] 
 **filter** | **String**| only list account, comment or video reports | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort abuses by criteria | [optional] 

### Return type

[**GetAbuses200Response**](GetAbuses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMyAbuses

> GetAbuses200Response getMyAbuses(opts)

List my abuses

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.AbusesApi();
let opts = {
  'id': 56, // Number | only list the report with this id
  'state': new PeerTube.AbuseStateSet(), // AbuseStateSet | 
  'sort': "sort_example", // String | Sort abuses by criteria
  'start': 56, // Number | Offset used to paginate results
  'count': 15 // Number | Number of items to return
};
apiInstance.getMyAbuses(opts, (error, data, response) => {
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
 **id** | **Number**| only list the report with this id | [optional] 
 **state** | [**AbuseStateSet**](.md)|  | [optional] 
 **sort** | **String**| Sort abuses by criteria | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]

### Return type

[**GetAbuses200Response**](GetAbuses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

