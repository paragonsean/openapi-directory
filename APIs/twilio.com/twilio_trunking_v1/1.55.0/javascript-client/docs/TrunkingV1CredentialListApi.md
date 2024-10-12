# TwilioTrunking.TrunkingV1CredentialListApi

All URIs are relative to *https://trunking.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCredentialList**](TrunkingV1CredentialListApi.md#createCredentialList) | **POST** /v1/Trunks/{TrunkSid}/CredentialLists | 
[**deleteCredentialList**](TrunkingV1CredentialListApi.md#deleteCredentialList) | **DELETE** /v1/Trunks/{TrunkSid}/CredentialLists/{Sid} | 
[**fetchCredentialList**](TrunkingV1CredentialListApi.md#fetchCredentialList) | **GET** /v1/Trunks/{TrunkSid}/CredentialLists/{Sid} | 
[**listCredentialList**](TrunkingV1CredentialListApi.md#listCredentialList) | **GET** /v1/Trunks/{TrunkSid}/CredentialLists | 



## createCredentialList

> TrunkingV1TrunkCredentialList createCredentialList(trunkSid, credentialListSid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1CredentialListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the credential list with.
let credentialListSid = "credentialListSid_example"; // String | The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list.
apiInstance.createCredentialList(trunkSid, credentialListSid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk to associate the credential list with. | 
 **credentialListSid** | **String**| The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list. | 

### Return type

[**TrunkingV1TrunkCredentialList**](TrunkingV1TrunkCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCredentialList

> deleteCredentialList(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1CredentialListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the credential list.
let sid = "sid_example"; // String | The unique string that we created to identify the CredentialList resource to delete.
apiInstance.deleteCredentialList(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to delete the credential list. | 
 **sid** | **String**| The unique string that we created to identify the CredentialList resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchCredentialList

> TrunkingV1TrunkCredentialList fetchCredentialList(trunkSid, sid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1CredentialListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the credential list.
let sid = "sid_example"; // String | The unique string that we created to identify the CredentialList resource to fetch.
apiInstance.fetchCredentialList(trunkSid, sid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to fetch the credential list. | 
 **sid** | **String**| The unique string that we created to identify the CredentialList resource to fetch. | 

### Return type

[**TrunkingV1TrunkCredentialList**](TrunkingV1TrunkCredentialList.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCredentialList

> ListCredentialListResponse listCredentialList(trunkSid, opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1CredentialListApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the credential lists.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCredentialList(trunkSid, opts, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to read the credential lists. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCredentialListResponse**](ListCredentialListResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

