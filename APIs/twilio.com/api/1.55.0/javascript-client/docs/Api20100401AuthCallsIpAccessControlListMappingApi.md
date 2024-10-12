# TwilioApi.Api20100401AuthCallsIpAccessControlListMappingApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#createSipAuthCallsIpAccessControlListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json | 
[**deleteSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#deleteSipAuthCallsIpAccessControlListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json | 
[**fetchSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#fetchSipAuthCallsIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json | 
[**listSipAuthCallsIpAccessControlListMapping**](Api20100401AuthCallsIpAccessControlListMappingApi.md#listSipAuthCallsIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json | 



## createSipAuthCallsIpAccessControlListMapping

> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping createSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid)



Create a new IP Access Control List mapping

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthCallsIpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that will contain the new resource.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The SID of the IpAccessControlList resource to map to the SIP domain.
apiInstance.createSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | 
 **domainSid** | **String**| The SID of the SIP domain that will contain the new resource. | 
 **ipAccessControlListSid** | **String**| The SID of the IpAccessControlList resource to map to the SIP domain. | 

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipAuthCallsIpAccessControlListMapping

> deleteSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid)



Delete an IP Access Control List mapping from the requested domain

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthCallsIpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete.
apiInstance.deleteSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete. | 
 **domainSid** | **String**| The SID of the SIP domain that contains the resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipAuthCallsIpAccessControlListMapping

> ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping fetchSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid)



Fetch a specific instance of an IP Access Control List mapping

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthCallsIpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch.
apiInstance.fetchSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch. | 
 **domainSid** | **String**| The SID of the SIP domain that contains the resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipAuthCallsIpAccessControlListMapping

> ListSipAuthCallsIpAccessControlListMappingResponse listSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, opts)



Retrieve a list of IP Access Control List mappings belonging to the domain used in the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthCallsIpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipAuthCallsIpAccessControlListMapping(accountSid, domainSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read. | 
 **domainSid** | **String**| The SID of the SIP domain that contains the resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipAuthCallsIpAccessControlListMappingResponse**](ListSipAuthCallsIpAccessControlListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

