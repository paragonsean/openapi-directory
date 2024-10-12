# TwilioServerless.ServerlessV1AssetVersionApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAssetVersion**](ServerlessV1AssetVersionApi.md#fetchAssetVersion) | **GET** /v1/Services/{ServiceSid}/Assets/{AssetSid}/Versions/{Sid} | 
[**listAssetVersion**](ServerlessV1AssetVersionApi.md#listAssetVersion) | **GET** /v1/Services/{ServiceSid}/Assets/{AssetSid}/Versions | 



## fetchAssetVersion

> ServerlessV1ServiceAssetAssetVersion fetchAssetVersion(serviceSid, assetSid, sid)



Retrieve a specific Asset Version.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetVersionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Asset Version resource from.
let assetSid = "assetSid_example"; // String | The SID of the Asset resource that is the parent of the Asset Version resource to fetch.
let sid = "sid_example"; // String | The SID of the Asset Version resource to fetch.
apiInstance.fetchAssetVersion(serviceSid, assetSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Asset Version resource from. | 
 **assetSid** | **String**| The SID of the Asset resource that is the parent of the Asset Version resource to fetch. | 
 **sid** | **String**| The SID of the Asset Version resource to fetch. | 

### Return type

[**ServerlessV1ServiceAssetAssetVersion**](ServerlessV1ServiceAssetAssetVersion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssetVersion

> ListAssetVersionResponse listAssetVersion(serviceSid, assetSid, opts)



Retrieve a list of all Asset Versions.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetVersionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Asset Version resource from.
let assetSid = "assetSid_example"; // String | The SID of the Asset resource that is the parent of the Asset Version resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAssetVersion(serviceSid, assetSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Asset Version resource from. | 
 **assetSid** | **String**| The SID of the Asset resource that is the parent of the Asset Version resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAssetVersionResponse**](ListAssetVersionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

