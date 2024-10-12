# TwilioApi.Api20100401CredentialListMappingApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#createSipCredentialListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json | 
[**deleteSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#deleteSipCredentialListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json | 
[**fetchSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#fetchSipCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json | 
[**listSipCredentialListMapping**](Api20100401CredentialListMappingApi.md#listSipCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json | 



## createSipCredentialListMapping

> ApiV2010AccountSipSipDomainSipCredentialListMapping createSipCredentialListMapping(accountSid, domainSid, credentialListSid)



Create a CredentialListMapping resource for an account.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped.
let credentialListSid = "credentialListSid_example"; // String | A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.
apiInstance.createSipCredentialListMapping(accountSid, domainSid, credentialListSid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain for which the CredentialList resource will be mapped. | 
 **credentialListSid** | **String**| A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain. | 

### Return type

[**ApiV2010AccountSipSipDomainSipCredentialListMapping**](ApiV2010AccountSipSipDomainSipCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipCredentialListMapping

> deleteSipCredentialListMapping(accountSid, domainSid, sid)



Delete a CredentialListMapping resource from an account.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to delete.
apiInstance.deleteSipCredentialListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to delete. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipCredentialListMapping

> ApiV2010AccountSipSipDomainSipCredentialListMapping fetchSipCredentialListMapping(accountSid, domainSid, sid)



Fetch a single CredentialListMapping resource from an account.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the resource to fetch.
apiInstance.fetchSipCredentialListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch. | 
 **sid** | **String**| A 34 character string that uniquely identifies the resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipDomainSipCredentialListMapping**](ApiV2010AccountSipSipDomainSipCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipCredentialListMapping

> ListSipCredentialListMappingResponse listSipCredentialListMapping(accountSid, domainSid, opts)



Read multiple CredentialListMapping resources from an account.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401CredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
let domainSid = "domainSid_example"; // String | A 34 character string that uniquely identifies the SIP Domain that includes the resource to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipCredentialListMapping(accountSid, domainSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource. | 
 **domainSid** | **String**| A 34 character string that uniquely identifies the SIP Domain that includes the resource to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipCredentialListMappingResponse**](ListSipCredentialListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

