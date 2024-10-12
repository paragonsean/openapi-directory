# AcmeDnsApi.AcmeChallengeSetsApi

All URIs are relative to *https://acmedns.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acmednsAcmeChallengeSetsGet**](AcmeChallengeSetsApi.md#acmednsAcmeChallengeSetsGet) | **GET** /v1/acmeChallengeSets/{rootDomain} | 
[**acmednsAcmeChallengeSetsRotateChallenges**](AcmeChallengeSetsApi.md#acmednsAcmeChallengeSetsRotateChallenges) | **POST** /v1/acmeChallengeSets/{rootDomain}:rotateChallenges | 



## acmednsAcmeChallengeSetsGet

> AcmeChallengeSet acmednsAcmeChallengeSetsGet(rootDomain, opts)



Gets the ACME challenge set for a given domain name. Domain names must be provided in Punycode.

### Example

```javascript
import AcmeDnsApi from 'acme_dns_api';

let apiInstance = new AcmeDnsApi.AcmeChallengeSetsApi();
let rootDomain = "rootDomain_example"; // String | Required. SLD + TLD domain name to list challenges. For example, this would be \"google.com\" for any FQDN under \"google.com\". That includes challenges for \"subdomain.google.com\". This MAY be Unicode or Punycode.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.acmednsAcmeChallengeSetsGet(rootDomain, opts, (error, data, response) => {
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
 **rootDomain** | **String**| Required. SLD + TLD domain name to list challenges. For example, this would be \&quot;google.com\&quot; for any FQDN under \&quot;google.com\&quot;. That includes challenges for \&quot;subdomain.google.com\&quot;. This MAY be Unicode or Punycode. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**AcmeChallengeSet**](AcmeChallengeSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## acmednsAcmeChallengeSetsRotateChallenges

> AcmeChallengeSet acmednsAcmeChallengeSetsRotateChallenges(rootDomain, opts)



Rotate the ACME challenges for a given domain name. By default, removes any challenges that are older than 30 days. Domain names must be provided in Punycode.

### Example

```javascript
import AcmeDnsApi from 'acme_dns_api';

let apiInstance = new AcmeDnsApi.AcmeChallengeSetsApi();
let rootDomain = "rootDomain_example"; // String | Required. SLD + TLD domain name to update records for. For example, this would be \"google.com\" for any FQDN under \"google.com\". That includes challenges for \"subdomain.google.com\". This MAY be Unicode or Punycode.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'rotateChallengesRequest': new AcmeDnsApi.RotateChallengesRequest() // RotateChallengesRequest | 
};
apiInstance.acmednsAcmeChallengeSetsRotateChallenges(rootDomain, opts, (error, data, response) => {
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
 **rootDomain** | **String**| Required. SLD + TLD domain name to update records for. For example, this would be \&quot;google.com\&quot; for any FQDN under \&quot;google.com\&quot;. That includes challenges for \&quot;subdomain.google.com\&quot;. This MAY be Unicode or Punycode. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **rotateChallengesRequest** | [**RotateChallengesRequest**](RotateChallengesRequest.md)|  | [optional] 

### Return type

[**AcmeChallengeSet**](AcmeChallengeSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

