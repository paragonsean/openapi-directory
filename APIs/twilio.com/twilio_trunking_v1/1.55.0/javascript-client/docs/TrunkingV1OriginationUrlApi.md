# TwilioTrunking.TrunkingV1OriginationUrlApi

All URIs are relative to *https://trunking.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOriginationUrl**](TrunkingV1OriginationUrlApi.md#createOriginationUrl) | **POST** /v1/Trunks/{TrunkSid}/OriginationUrls | 
[**deleteOriginationUrl**](TrunkingV1OriginationUrlApi.md#deleteOriginationUrl) | **DELETE** /v1/Trunks/{TrunkSid}/OriginationUrls/{Sid} | 
[**fetchOriginationUrl**](TrunkingV1OriginationUrlApi.md#fetchOriginationUrl) | **GET** /v1/Trunks/{TrunkSid}/OriginationUrls/{Sid} | 
[**listOriginationUrl**](TrunkingV1OriginationUrlApi.md#listOriginationUrl) | **GET** /v1/Trunks/{TrunkSid}/OriginationUrls | 
[**updateOriginationUrl**](TrunkingV1OriginationUrlApi.md#updateOriginationUrl) | **POST** /v1/Trunks/{TrunkSid}/OriginationUrls/{Sid} | 



## createOriginationUrl

> TrunkingV1TrunkOriginationUrl createOriginationUrl(trunkSid, enabled, friendlyName, priority, sipUrl, weight)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1OriginationUrlApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the resource with.
let enabled = true; // Boolean | Whether the URL is enabled. The default is `true`.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
let priority = 56; // Number | The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
let sipUrl = "sipUrl_example"; // String | The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.
let weight = 56; // Number | The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
apiInstance.createOriginationUrl(trunkSid, enabled, friendlyName, priority, sipUrl, weight, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk to associate the resource with. | 
 **enabled** | **Boolean**| Whether the URL is enabled. The default is &#x60;true&#x60;. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | 
 **priority** | **Number**| The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI. | 
 **sipUrl** | **String**| The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema. | 
 **weight** | **Number**| The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority. | 

### Return type

[**TrunkingV1TrunkOriginationUrl**](TrunkingV1TrunkOriginationUrl.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteOriginationUrl

> deleteOriginationUrl(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1OriginationUrlApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the OriginationUrl.
let sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to delete.
apiInstance.deleteOriginationUrl(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to delete the OriginationUrl. | 
 **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchOriginationUrl

> TrunkingV1TrunkOriginationUrl fetchOriginationUrl(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1OriginationUrlApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the OriginationUrl.
let sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to fetch.
apiInstance.fetchOriginationUrl(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to fetch the OriginationUrl. | 
 **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to fetch. | 

### Return type

[**TrunkingV1TrunkOriginationUrl**](TrunkingV1TrunkOriginationUrl.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOriginationUrl

> ListOriginationUrlResponse listOriginationUrl(trunkSid, opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1OriginationUrlApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the OriginationUrl.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listOriginationUrl(trunkSid, opts, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to read the OriginationUrl. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListOriginationUrlResponse**](ListOriginationUrlResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateOriginationUrl

> TrunkingV1TrunkOriginationUrl updateOriginationUrl(trunkSid, sid, opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1OriginationUrlApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to update the OriginationUrl.
let sid = "sid_example"; // String | The unique string that we created to identify the OriginationUrl resource to update.
let opts = {
  'enabled': true, // Boolean | Whether the URL is enabled. The default is `true`.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'priority': 56, // Number | The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
  'sipUrl': "sipUrl_example", // String | The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.
  'weight': 56 // Number | The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
};
apiInstance.updateOriginationUrl(trunkSid, sid, opts, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to update the OriginationUrl. | 
 **sid** | **String**| The unique string that we created to identify the OriginationUrl resource to update. | 
 **enabled** | **Boolean**| Whether the URL is enabled. The default is &#x60;true&#x60;. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **priority** | **Number**| The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI. | [optional] 
 **sipUrl** | **String**| The SIP address you want Twilio to route your Origination calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. | [optional] 
 **weight** | **Number**| The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority. | [optional] 

### Return type

[**TrunkingV1TrunkOriginationUrl**](TrunkingV1TrunkOriginationUrl.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

