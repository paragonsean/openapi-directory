# CloudDnsApi.ResourceRecordSetsApi

All URIs are relative to *https://dns.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dnsResourceRecordSetsCreate**](ResourceRecordSetsApi.md#dnsResourceRecordSetsCreate) | **POST** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets | 
[**dnsResourceRecordSetsDelete**](ResourceRecordSetsApi.md#dnsResourceRecordSetsDelete) | **DELETE** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type} | 
[**dnsResourceRecordSetsGet**](ResourceRecordSetsApi.md#dnsResourceRecordSetsGet) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type} | 
[**dnsResourceRecordSetsList**](ResourceRecordSetsApi.md#dnsResourceRecordSetsList) | **GET** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets | 
[**dnsResourceRecordSetsPatch**](ResourceRecordSetsApi.md#dnsResourceRecordSetsPatch) | **PATCH** /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type} | 



## dnsResourceRecordSetsCreate

> ResourceRecordSet dnsResourceRecordSetsCreate(project, managedZone, opts)



Creates a new ResourceRecordSet.

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

let apiInstance = new CloudDnsApi.ResourceRecordSetsApi();
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
  'clientOperationId': "clientOperationId_example", // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
  'resourceRecordSet': new CloudDnsApi.ResourceRecordSet() // ResourceRecordSet | 
};
apiInstance.dnsResourceRecordSetsCreate(project, managedZone, opts, (error, data, response) => {
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
 **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] 
 **resourceRecordSet** | [**ResourceRecordSet**](ResourceRecordSet.md)|  | [optional] 

### Return type

[**ResourceRecordSet**](ResourceRecordSet.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dnsResourceRecordSetsDelete

> dnsResourceRecordSetsDelete(project, managedZone, name, type, opts)



Deletes a previously created ResourceRecordSet.

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

let apiInstance = new CloudDnsApi.ResourceRecordSetsApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
let name = "name_example"; // String | Fully qualified domain name.
let type = "type_example"; // String | RRSet type.
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
  'clientOperationId': "clientOperationId_example" // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
};
apiInstance.dnsResourceRecordSetsDelete(project, managedZone, name, type, opts, (error, data, response) => {
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
 **project** | **String**| Identifies the project addressed by this request. | 
 **managedZone** | **String**| Identifies the managed zone addressed by this request. Can be the managed zone name or ID. | 
 **name** | **String**| Fully qualified domain name. | 
 **type** | **String**| RRSet type. | 
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

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dnsResourceRecordSetsGet

> ResourceRecordSet dnsResourceRecordSetsGet(project, managedZone, name, type, opts)



Fetches the representation of an existing ResourceRecordSet.

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

let apiInstance = new CloudDnsApi.ResourceRecordSetsApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
let name = "name_example"; // String | Fully qualified domain name.
let type = "type_example"; // String | RRSet type.
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
  'clientOperationId': "clientOperationId_example" // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
};
apiInstance.dnsResourceRecordSetsGet(project, managedZone, name, type, opts, (error, data, response) => {
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
 **name** | **String**| Fully qualified domain name. | 
 **type** | **String**| RRSet type. | 
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

### Return type

[**ResourceRecordSet**](ResourceRecordSet.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsResourceRecordSetsList

> ResourceRecordSetsListResponse dnsResourceRecordSetsList(project, managedZone, opts)



Enumerates ResourceRecordSets that you have created but not yet deleted.

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

let apiInstance = new CloudDnsApi.ResourceRecordSetsApi();
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
  'maxResults': 56, // Number | Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.
  'name': "name_example", // String | Restricts the list to return only records with this fully qualified domain name.
  'pageToken': "pageToken_example", // String | Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.
  'type': "type_example" // String | Restricts the list to return only records of this type. If present, the \"name\" parameter must also be present.
};
apiInstance.dnsResourceRecordSetsList(project, managedZone, opts, (error, data, response) => {
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
 **maxResults** | **Number**| Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return. | [optional] 
 **name** | **String**| Restricts the list to return only records with this fully qualified domain name. | [optional] 
 **pageToken** | **String**| Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request. | [optional] 
 **type** | **String**| Restricts the list to return only records of this type. If present, the \&quot;name\&quot; parameter must also be present. | [optional] 

### Return type

[**ResourceRecordSetsListResponse**](ResourceRecordSetsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dnsResourceRecordSetsPatch

> ResourceRecordSet dnsResourceRecordSetsPatch(project, managedZone, name, type, opts)



Applies a partial update to an existing ResourceRecordSet.

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

let apiInstance = new CloudDnsApi.ResourceRecordSetsApi();
let project = "project_example"; // String | Identifies the project addressed by this request.
let managedZone = "managedZone_example"; // String | Identifies the managed zone addressed by this request. Can be the managed zone name or ID.
let name = "name_example"; // String | Fully qualified domain name.
let type = "type_example"; // String | RRSet type.
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
  'resourceRecordSet': new CloudDnsApi.ResourceRecordSet() // ResourceRecordSet | 
};
apiInstance.dnsResourceRecordSetsPatch(project, managedZone, name, type, opts, (error, data, response) => {
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
 **name** | **String**| Fully qualified domain name. | 
 **type** | **String**| RRSet type. | 
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
 **resourceRecordSet** | [**ResourceRecordSet**](ResourceRecordSet.md)|  | [optional] 

### Return type

[**ResourceRecordSet**](ResourceRecordSet.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

