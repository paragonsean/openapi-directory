# MuxApi.PlaybackRestrictionsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPlaybackRestriction**](PlaybackRestrictionsApi.md#createPlaybackRestriction) | **POST** /video/v1/playback-restrictions | Create a Playback Restriction
[**deletePlaybackRestriction**](PlaybackRestrictionsApi.md#deletePlaybackRestriction) | **DELETE** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID} | Delete a Playback Restriction
[**getPlaybackRestriction**](PlaybackRestrictionsApi.md#getPlaybackRestriction) | **GET** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID} | Retrieve a Playback Restriction
[**listPlaybackRestrictions**](PlaybackRestrictionsApi.md#listPlaybackRestrictions) | **GET** /video/v1/playback-restrictions | List Playback Restrictions
[**updateReferrerDomainRestriction**](PlaybackRestrictionsApi.md#updateReferrerDomainRestriction) | **PUT** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID}/referrer | Update the Referrer Playback Restriction



## createPlaybackRestriction

> PlaybackRestrictionResponse createPlaybackRestriction(createPlaybackRestrictionRequest)

Create a Playback Restriction

Create a new Playback Restriction.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.PlaybackRestrictionsApi();
let createPlaybackRestrictionRequest = {"referrer":{"allow_no_referrer":true,"allowed_domains":["*.example.com"]}}; // CreatePlaybackRestrictionRequest | 
apiInstance.createPlaybackRestriction(createPlaybackRestrictionRequest, (error, data, response) => {
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
 **createPlaybackRestrictionRequest** | [**CreatePlaybackRestrictionRequest**](CreatePlaybackRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePlaybackRestriction

> deletePlaybackRestriction(PLAYBACK_RESTRICTION_ID)

Delete a Playback Restriction

Deletes a single Playback Restriction.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.PlaybackRestrictionsApi();
let PLAYBACK_RESTRICTION_ID = "PLAYBACK_RESTRICTION_ID_example"; // String | ID of the Playback Restriction.
apiInstance.deletePlaybackRestriction(PLAYBACK_RESTRICTION_ID, (error, data, response) => {
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
 **PLAYBACK_RESTRICTION_ID** | **String**| ID of the Playback Restriction. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPlaybackRestriction

> PlaybackRestrictionResponse getPlaybackRestriction(PLAYBACK_RESTRICTION_ID)

Retrieve a Playback Restriction

Retrieves a Playback Restriction associated with the unique identifier.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.PlaybackRestrictionsApi();
let PLAYBACK_RESTRICTION_ID = "PLAYBACK_RESTRICTION_ID_example"; // String | ID of the Playback Restriction.
apiInstance.getPlaybackRestriction(PLAYBACK_RESTRICTION_ID, (error, data, response) => {
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
 **PLAYBACK_RESTRICTION_ID** | **String**| ID of the Playback Restriction. | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPlaybackRestrictions

> ListPlaybackRestrictionsResponse listPlaybackRestrictions(opts)

List Playback Restrictions

Returns a list of all Playback Restrictions.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.PlaybackRestrictionsApi();
let opts = {
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'limit': 25 // Number | Number of items to include in the response
};
apiInstance.listPlaybackRestrictions(opts, (error, data, response) => {
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
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]

### Return type

[**ListPlaybackRestrictionsResponse**](ListPlaybackRestrictionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateReferrerDomainRestriction

> PlaybackRestrictionResponse updateReferrerDomainRestriction(PLAYBACK_RESTRICTION_ID, updateReferrerDomainRestrictionRequest)

Update the Referrer Playback Restriction

Allows you to modify the list of domains or change how Mux validates playback requests without the &#x60;Referer&#x60; HTTP header. The Referrer restriction fully replaces the old list with this new list of domains.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.PlaybackRestrictionsApi();
let PLAYBACK_RESTRICTION_ID = "PLAYBACK_RESTRICTION_ID_example"; // String | ID of the Playback Restriction.
let updateReferrerDomainRestrictionRequest = {"allow_no_referrer":true,"allowed_domains":["*.example.com"]}; // UpdateReferrerDomainRestrictionRequest | 
apiInstance.updateReferrerDomainRestriction(PLAYBACK_RESTRICTION_ID, updateReferrerDomainRestrictionRequest, (error, data, response) => {
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
 **PLAYBACK_RESTRICTION_ID** | **String**| ID of the Playback Restriction. | 
 **updateReferrerDomainRestrictionRequest** | [**UpdateReferrerDomainRestrictionRequest**](UpdateReferrerDomainRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

