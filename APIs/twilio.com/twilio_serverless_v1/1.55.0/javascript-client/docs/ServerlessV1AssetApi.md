# TwilioServerless.ServerlessV1AssetApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAsset**](ServerlessV1AssetApi.md#createAsset) | **POST** /v1/Services/{ServiceSid}/Assets | 
[**deleteAsset**](ServerlessV1AssetApi.md#deleteAsset) | **DELETE** /v1/Services/{ServiceSid}/Assets/{Sid} | 
[**fetchAsset**](ServerlessV1AssetApi.md#fetchAsset) | **GET** /v1/Services/{ServiceSid}/Assets/{Sid} | 
[**listAsset**](ServerlessV1AssetApi.md#listAsset) | **GET** /v1/Services/{ServiceSid}/Assets | 
[**updateAsset**](ServerlessV1AssetApi.md#updateAsset) | **POST** /v1/Services/{ServiceSid}/Assets/{Sid} | 



## createAsset

> ServerlessV1ServiceAsset createAsset(serviceSid, friendlyName)



Create a new Asset resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Asset resource under.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
apiInstance.createAsset(serviceSid, friendlyName, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to create the Asset resource under. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters. | 

### Return type

[**ServerlessV1ServiceAsset**](ServerlessV1ServiceAsset.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteAsset

> deleteAsset(serviceSid, sid)



Delete an Asset resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Asset resource from.
let sid = "sid_example"; // String | The SID that identifies the Asset resource to delete.
apiInstance.deleteAsset(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to delete the Asset resource from. | 
 **sid** | **String**| The SID that identifies the Asset resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchAsset

> ServerlessV1ServiceAsset fetchAsset(serviceSid, sid)



Retrieve a specific Asset resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Asset resource from.
let sid = "sid_example"; // String | The SID that identifies the Asset resource to fetch.
apiInstance.fetchAsset(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Asset resource from. | 
 **sid** | **String**| The SID that identifies the Asset resource to fetch. | 

### Return type

[**ServerlessV1ServiceAsset**](ServerlessV1ServiceAsset.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAsset

> ListAssetResponse listAsset(serviceSid, opts)



Retrieve a list of all Assets.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Asset resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAsset(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Asset resources from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAssetResponse**](ListAssetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAsset

> ServerlessV1ServiceAsset updateAsset(serviceSid, sid, friendlyName)



Update a specific Asset resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1AssetApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to update the Asset resource from.
let sid = "sid_example"; // String | The SID that identifies the Asset resource to update.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
apiInstance.updateAsset(serviceSid, sid, friendlyName, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to update the Asset resource from. | 
 **sid** | **String**| The SID that identifies the Asset resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters. | 

### Return type

[**ServerlessV1ServiceAsset**](ServerlessV1ServiceAsset.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

