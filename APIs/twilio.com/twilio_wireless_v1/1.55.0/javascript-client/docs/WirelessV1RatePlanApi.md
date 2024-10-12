# TwilioWireless.WirelessV1RatePlanApi

All URIs are relative to *https://wireless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRatePlan**](WirelessV1RatePlanApi.md#createRatePlan) | **POST** /v1/RatePlans | 
[**deleteRatePlan**](WirelessV1RatePlanApi.md#deleteRatePlan) | **DELETE** /v1/RatePlans/{Sid} | 
[**fetchRatePlan**](WirelessV1RatePlanApi.md#fetchRatePlan) | **GET** /v1/RatePlans/{Sid} | 
[**listRatePlan**](WirelessV1RatePlanApi.md#listRatePlan) | **GET** /v1/RatePlans | 
[**updateRatePlan**](WirelessV1RatePlanApi.md#updateRatePlan) | **POST** /v1/RatePlans/{Sid} | 



## createRatePlan

> WirelessV1RatePlan createRatePlan(opts)





### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1RatePlanApi();
let opts = {
  'dataEnabled': true, // Boolean | Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
  'dataLimit': 56, // Number | The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is `1000`.
  'dataMetering': "dataMetering_example", // String | The model used to meter data usage. Can be: `payg` and `quota-1`, `quota-10`, and `quota-50`. Learn more about the available [data metering models](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#payg-vs-quota-data-plans).
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It does not have to be unique.
  'internationalRoaming': ["null"], // [String] | The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: `data` and `messaging`.
  'internationalRoamingDataLimit': 56, // Number | The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB.
  'messagingEnabled': true, // Boolean | Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/iot/wireless/api/command-resource).
  'nationalRoamingDataLimit': 56, // Number | The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming) for more info.
  'nationalRoamingEnabled': true, // Boolean | Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming).
  'uniqueName': "uniqueName_example", // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
  'voiceEnabled': true // Boolean | Deprecated.
};
apiInstance.createRatePlan(opts, (error, data, response) => {
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
 **dataEnabled** | **Boolean**| Whether SIMs can use GPRS/3G/4G/LTE data connectivity. | [optional] 
 **dataLimit** | **Number**| The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is &#x60;1000&#x60;. | [optional] 
 **dataMetering** | **String**| The model used to meter data usage. Can be: &#x60;payg&#x60; and &#x60;quota-1&#x60;, &#x60;quota-10&#x60;, and &#x60;quota-50&#x60;. Learn more about the available [data metering models](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#payg-vs-quota-data-plans). | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It does not have to be unique. | [optional] 
 **internationalRoaming** | [**[String]**](String.md)| The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: &#x60;data&#x60; and &#x60;messaging&#x60;. | [optional] 
 **internationalRoamingDataLimit** | **Number**| The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB. | [optional] 
 **messagingEnabled** | **Boolean**| Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/iot/wireless/api/command-resource). | [optional] 
 **nationalRoamingDataLimit** | **Number**| The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming) for more info. | [optional] 
 **nationalRoamingEnabled** | **Boolean**| Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming). | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] 
 **voiceEnabled** | **Boolean**| Deprecated. | [optional] 

### Return type

[**WirelessV1RatePlan**](WirelessV1RatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteRatePlan

> deleteRatePlan(sid)





### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1RatePlanApi();
let sid = "sid_example"; // String | The SID of the RatePlan resource to delete.
apiInstance.deleteRatePlan(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the RatePlan resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRatePlan

> WirelessV1RatePlan fetchRatePlan(sid)





### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1RatePlanApi();
let sid = "sid_example"; // String | The SID of the RatePlan resource to fetch.
apiInstance.fetchRatePlan(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the RatePlan resource to fetch. | 

### Return type

[**WirelessV1RatePlan**](WirelessV1RatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRatePlan

> ListRatePlanResponse listRatePlan(opts)





### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1RatePlanApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRatePlan(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRatePlanResponse**](ListRatePlanResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRatePlan

> WirelessV1RatePlan updateRatePlan(sid, opts)





### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1RatePlanApi();
let sid = "sid_example"; // String | The SID of the RatePlan resource to update.
let opts = {
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It does not have to be unique.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
};
apiInstance.updateRatePlan(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the RatePlan resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It does not have to be unique. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] 

### Return type

[**WirelessV1RatePlan**](WirelessV1RatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

