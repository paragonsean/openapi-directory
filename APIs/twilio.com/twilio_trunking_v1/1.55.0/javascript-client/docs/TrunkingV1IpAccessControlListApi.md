# TwilioTrunking.TrunkingV1IpAccessControlListApi

All URIs are relative to *https://trunking.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#createIpAccessControlList) | **POST** /v1/Trunks/{TrunkSid}/IpAccessControlLists | 
[**deleteIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#deleteIpAccessControlList) | **DELETE** /v1/Trunks/{TrunkSid}/IpAccessControlLists/{Sid} | 
[**fetchIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#fetchIpAccessControlList) | **GET** /v1/Trunks/{TrunkSid}/IpAccessControlLists/{Sid} | 
[**listIpAccessControlList**](TrunkingV1IpAccessControlListApi.md#listIpAccessControlList) | **GET** /v1/Trunks/{TrunkSid}/IpAccessControlLists | 



## createIpAccessControlList

> TrunkingV1TrunkIpAccessControlList createIpAccessControlList(trunkSid, ipAccessControlListSid)



Associate an IP Access Control List with a Trunk

### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1IpAccessControlListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the IP Access Control List with.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk.
apiInstance.createIpAccessControlList(trunkSid, ipAccessControlListSid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk to associate the IP Access Control List with. | 
 **ipAccessControlListSid** | **String**| The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk. | 

### Return type

[**TrunkingV1TrunkIpAccessControlList**](TrunkingV1TrunkIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteIpAccessControlList

> deleteIpAccessControlList(trunkSid, sid)



Remove an associated IP Access Control List from a Trunk

### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1IpAccessControlListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the IP Access Control List.
let sid = "sid_example"; // String | The unique string that we created to identify the IpAccessControlList resource to delete.
apiInstance.deleteIpAccessControlList(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to delete the IP Access Control List. | 
 **sid** | **String**| The unique string that we created to identify the IpAccessControlList resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchIpAccessControlList

> TrunkingV1TrunkIpAccessControlList fetchIpAccessControlList(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1IpAccessControlListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the IP Access Control List.
let sid = "sid_example"; // String | The unique string that we created to identify the IpAccessControlList resource to fetch.
apiInstance.fetchIpAccessControlList(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to fetch the IP Access Control List. | 
 **sid** | **String**| The unique string that we created to identify the IpAccessControlList resource to fetch. | 

### Return type

[**TrunkingV1TrunkIpAccessControlList**](TrunkingV1TrunkIpAccessControlList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIpAccessControlList

> ListIpAccessControlListResponse listIpAccessControlList(trunkSid, opts)



List all IP Access Control Lists for a Trunk

### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1IpAccessControlListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the IP Access Control Lists.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listIpAccessControlList(trunkSid, opts, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to read the IP Access Control Lists. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListIpAccessControlListResponse**](ListIpAccessControlListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

