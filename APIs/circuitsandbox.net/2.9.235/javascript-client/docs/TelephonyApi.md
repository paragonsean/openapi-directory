# RestApiVersion2.TelephonyApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJournalEntries**](TelephonyApi.md#getJournalEntries) | **GET** /telephony/{telephonyConversationId}/journal | Get journal
[**v2GetDeviceInfos**](TelephonyApi.md#v2GetDeviceInfos) | **GET** /telephony/deviceInfos | Get devices infos
[**v2GetTelephonyConversationId**](TelephonyApi.md#v2GetTelephonyConversationId) | **GET** /telephony/telephonyConversationId | Get telephony conversation id



## getJournalEntries

> [ConversationItem] getJournalEntries(telephonyConversationId, opts)

Get journal

Get telephony journal OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.TelephonyApi();
let telephonyConversationId = "telephonyConversationId_example"; // String | The id of the telephony conversation
let opts = {
  'timestamp': 0, // Number | A timestamp, default = 0
  'numberOfEntries': 25, // Number | The number of entries, between 1 and 100, default = 25
  'direction': "'AFTER'", // String | The direction (BEFORE||AFTER||BOTH), default = AFTER
  'journalFilter': "'ALL'" // String | The filter, ALL||MISSED||DIALED||RECEIVED||DIVERTED||VOICEMAILS||UNHERAD_VOICEMAILS. default = ALL
};
apiInstance.getJournalEntries(telephonyConversationId, opts, (error, data, response) => {
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
 **telephonyConversationId** | **String**| The id of the telephony conversation | 
 **timestamp** | **Number**| A timestamp, default &#x3D; 0 | [optional] [default to 0]
 **numberOfEntries** | **Number**| The number of entries, between 1 and 100, default &#x3D; 25 | [optional] [default to 25]
 **direction** | **String**| The direction (BEFORE||AFTER||BOTH), default &#x3D; AFTER | [optional] [default to &#39;AFTER&#39;]
 **journalFilter** | **String**| The filter, ALL||MISSED||DIALED||RECEIVED||DIVERTED||VOICEMAILS||UNHERAD_VOICEMAILS. default &#x3D; ALL | [optional] [default to &#39;ALL&#39;]

### Return type

[**[ConversationItem]**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v2GetDeviceInfos

> [V2DistributedClientInfo] v2GetDeviceInfos()

Get devices infos

Get the device infos of the requesting user OauthScopes: READ_USER_PROFILE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.TelephonyApi();
apiInstance.v2GetDeviceInfos((error, data, response) => {
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

[**[V2DistributedClientInfo]**](V2DistributedClientInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2GetTelephonyConversationId

> v2GetTelephonyConversationId()

Get telephony conversation id

Get telephony conversation id for requesting client OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.TelephonyApi();
apiInstance.v2GetTelephonyConversationId((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

