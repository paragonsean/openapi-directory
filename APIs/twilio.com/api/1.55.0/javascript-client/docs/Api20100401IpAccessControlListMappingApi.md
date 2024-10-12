# TwilioApi.Api20100401IpAccessControlListMappingApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#createSipIpAccessControlListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json | 
[**deleteSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#deleteSipIpAccessControlListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json | 
[**fetchSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#fetchSipIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json | 
[**listSipIpAccessControlListMapping**](Api20100401IpAccessControlListMappingApi.md#listSipIpAccessControlListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json | 



## createSipIpAccessControlListMapping

> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping createSipIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid)



Create a new IpAccessControlListMapping resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
let ipAccessControlListSid = "ipAccessControlListSid_example"; // String | The unique id of the IP access control list to map to the SIP domain.
apiInstance.createSipIpAccessControlListMapping(accountSid, domainSid, ipAccessControlListSid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | 
 **ipAccessControlListSid** | **String**| The unique id of the IP access control list to map to the SIP domain. | 

### Return type

[**ApiV2010AccountSipSipDomainSipIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipIpAccessControlListMapping

> deleteSipIpAccessControlListMapping(accountSid, domainSid, sid)



Delete an IpAccessControlListMapping resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
apiInstance.deleteSipIpAccessControlListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipIpAccessControlListMapping

> ApiV2010AccountSipSipDomainSipIpAccessControlListMapping fetchSipIpAccessControlListMapping(accountSid, domainSid, sid)



Fetch an IpAccessControlListMapping resource.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to fetch.
apiInstance.fetchSipIpAccessControlListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipDomainSipIpAccessControlListMapping**](ApiV2010AccountSipSipDomainSipIpAccessControlListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipIpAccessControlListMapping

> ListSipIpAccessControlListMappingResponse listSipIpAccessControlListMapping(accountSid, domainSid, opts)



Retrieve a list of IpAccessControlListMapping resources.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401IpAccessControlListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the Account that is responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP domain.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipIpAccessControlListMapping(accountSid, domainSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the Account that is responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP domain. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipIpAccessControlListMappingResponse**](ListSipIpAccessControlListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

