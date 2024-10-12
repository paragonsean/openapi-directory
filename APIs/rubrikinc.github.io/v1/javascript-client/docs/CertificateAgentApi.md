# RubrikRestApi.CertificateAgentApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markAgentSecondaryCertificate**](CertificateAgentApi.md#markAgentSecondaryCertificate) | **POST** /certificate/agent | Mark a certificate to be added to agents
[**queryAgentSecondaryCertificate**](CertificateAgentApi.md#queryAgentSecondaryCertificate) | **GET** /certificate/agent | Get all potential agent secondary cluster certificates
[**unmarkAgentSecondaryCertificate**](CertificateAgentApi.md#unmarkAgentSecondaryCertificate) | **DELETE** /certificate/agent/{id} | Unmark a certificate that was previously marked



## markAgentSecondaryCertificate

> AgentSecondaryCertificateInfo markAgentSecondaryCertificate(body)

Mark a certificate to be added to agents

Mark a secondary cluster certificate to be asynchronously synced to all Rubrik Backup Service instances for which this cluster is the primary.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateAgentApi();
let body = "body_example"; // String | ID of certificate to add.
apiInstance.markAgentSecondaryCertificate(body, (error, data, response) => {
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
 **body** | **String**| ID of certificate to add. | 

### Return type

[**AgentSecondaryCertificateInfo**](AgentSecondaryCertificateInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryAgentSecondaryCertificate

> AgentSecondaryCertificateInfoListResponse queryAgentSecondaryCertificate(opts)

Get all potential agent secondary cluster certificates

Get all certificates that have been added to the cluster and qualify to be secondary cluster certificates for the Rubrik Backup Service. This call retrieves any certificates that are detected to be Rubrik cluster certificates.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateAgentApi();
let opts = {
  'isAgentEnabled': true // Boolean | Filter based on whether or not certificates have been marked for use by agents.
};
apiInstance.queryAgentSecondaryCertificate(opts, (error, data, response) => {
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
 **isAgentEnabled** | **Boolean**| Filter based on whether or not certificates have been marked for use by agents. | [optional] 

### Return type

[**AgentSecondaryCertificateInfoListResponse**](AgentSecondaryCertificateInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unmarkAgentSecondaryCertificate

> unmarkAgentSecondaryCertificate(id)

Unmark a certificate that was previously marked

Unmark a previously marked secondary cluster certificate to be asynchronously removed from all Rubrik Backup Service instances for which this cluster is the primary.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateAgentApi();
let id = "id_example"; // String | ID of certificate to remove.
apiInstance.unmarkAgentSecondaryCertificate(id, (error, data, response) => {
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
 **id** | **String**| ID of certificate to remove. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

