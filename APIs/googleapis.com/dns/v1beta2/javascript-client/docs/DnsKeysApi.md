# CloudDnsApi.DnsKeysApi

All URIs are relative to *https://dns.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsDnsKeysGet**](DnsKeysApi.md#dnsDnsKeysGet) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId} | 
[**dnsDnsKeysList**](DnsKeysApi.md#dnsDnsKeysList) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/dnsKeys | 



## dnsDnsKeysGet

> DnsKey dnsDnsKeysGet(project, managedZone, dnsKeyId, opts)



Fetches the representation of an existing DnsKey.

### Example

```javascript
import CloudDnsApi from 'cloud_dns_api';
let defaultClient = CloudDnsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudDnsApi.DnsKeysApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
let dnsKeyId = "dnsKeyId_example"; // String | The identifier of the requested DnsKey.
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
  'clientOperationId': "clientOperationId_example", // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
  'digestType': "digestType_example" // String | An optional comma-separated list of digest types to compute and display for key signing keys. If omitted, the recommended digest type is computed and displayed.
};
apiInstance.dnsDnsKeysGet(project, managedZone, dnsKeyId, opts, (error, data, response) => {
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
 **project** | **String**| Identifies the project addressed by this request. | 
 **managedZone** | **String**| Identifies the managed zone addressed by this request. Can be the managed zone name or ID. | 
 **dnsKeyId** | **String**| The identifier of the requested DnsKey. | 
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
 **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] 
 **digestType** | **String**| An optional comma-separated list of digest types to compute and display for key signing keys. If omitted, the recommended digest type is computed and displayed. | [optional] 

### Return type

[**DnsKey**](DnsKey.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsDnsKeysList

> DnsKeysListResponse dnsDnsKeysList(project, managedZone, opts)



Enumerates DnsKeys to a ResourceRecordSet collection.

### Example

```javascript
import CloudDnsApi from 'cloud_dns_api';
let defaultClient = CloudDnsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudDnsApi.DnsKeysApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
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
  'digestType': "digestType_example", // String | An optional comma-separated list of digest types to compute and display for key signing keys. If omitted, the recommended digest type is computed and displayed.
  'maxResults': 56, // Number | Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.
  'pageToken': "pageToken_example" // String | Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.
};
apiInstance.dnsDnsKeysList(project, managedZone, opts, (error, data, response) => {
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
 **project** | **String**| Identifies the project addressed by this request. | 
 **managedZone** | **String**| Identifies the managed zone addressed by this request. Can be the managed zone name or ID. | 
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
 **digestType** | **String**| An optional comma-separated list of digest types to compute and display for key signing keys. If omitted, the recommended digest type is computed and displayed. | [optional] 
 **maxResults** | **Number**| Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return. | [optional] 
 **pageToken** | **String**| Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request. | [optional] 

### Return type

[**DnsKeysListResponse**](DnsKeysListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

