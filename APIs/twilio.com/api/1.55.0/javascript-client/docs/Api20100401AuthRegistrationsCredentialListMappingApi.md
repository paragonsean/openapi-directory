# TwilioApi.Api20100401AuthRegistrationsCredentialListMappingApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipAuthRegistrationsCredentialListMapping**](Api20100401AuthRegistrationsCredentialListMappingApi.md#createSipAuthRegistrationsCredentialListMapping) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json | 
[**deleteSipAuthRegistrationsCredentialListMapping**](Api20100401AuthRegistrationsCredentialListMappingApi.md#deleteSipAuthRegistrationsCredentialListMapping) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json | 
[**fetchSipAuthRegistrationsCredentialListMapping**](Api20100401AuthRegistrationsCredentialListMappingApi.md#fetchSipAuthRegistrationsCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json | 
[**listSipAuthRegistrationsCredentialListMapping**](Api20100401AuthRegistrationsCredentialListMappingApi.md#listSipAuthRegistrationsCredentialListMapping) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json | 



## createSipAuthRegistrationsCredentialListMapping

> ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping createSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, credentialListSid)



Create a new credential list mapping resource

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthRegistrationsCredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that will contain the new resource.
let credentialListSid = "credentialListSid_example"; // String | The SID of the CredentialList resource to map to the SIP domain.
apiInstance.createSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, credentialListSid, (error, data, response) => {
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
 **credentialListSid** | **String**| The SID of the CredentialList resource to map to the SIP domain. | 

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipAuthRegistrationsCredentialListMapping

> deleteSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, sid)



Delete a credential list mapping from the requested domain

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthRegistrationsCredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete.
apiInstance.deleteSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to delete. | 
 **domainSid** | **String**| The SID of the SIP domain that contains the resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipAuthRegistrationsCredentialListMapping

> ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping fetchSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, sid)



Fetch a specific instance of a credential list mapping

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthRegistrationsCredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch.
apiInstance.fetchSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch. | 
 **domainSid** | **String**| The SID of the SIP domain that contains the resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the CredentialListMapping resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping**](ApiV2010AccountSipSipDomainSipAuthSipAuthRegistrationsSipAuthRegistrationsCredentialListMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipAuthRegistrationsCredentialListMapping

> ListSipAuthRegistrationsCredentialListMappingResponse listSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, opts)



Retrieve a list of credential list mappings belonging to the domain used in the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401AuthRegistrationsCredentialListMappingApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read.
let domainSid = "domainSid_example"; // String | The SID of the SIP domain that contains the resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipAuthRegistrationsCredentialListMapping(accountSid, domainSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resources to read. | 
 **domainSid** | **String**| The SID of the SIP domain that contains the resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipAuthRegistrationsCredentialListMappingResponse**](ListSipAuthRegistrationsCredentialListMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

