# InfluxOssApiService.SecretsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrgsIDSecrets**](SecretsApi.md#getOrgsIDSecrets) | **GET** /orgs/{orgID}/secrets | List all secret keys for an organization
[**patchOrgsIDSecrets**](SecretsApi.md#patchOrgsIDSecrets) | **PATCH** /orgs/{orgID}/secrets | Update secrets in an organization
[**postOrgsIDSecrets**](SecretsApi.md#postOrgsIDSecrets) | **POST** /orgs/{orgID}/secrets/delete | Delete secrets from an organization



## getOrgsIDSecrets

> SecretKeysResponse getOrgsIDSecrets(orgID, opts)

List all secret keys for an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SecretsApi();
let orgID = "orgID_example"; // String | The organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getOrgsIDSecrets(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**SecretKeysResponse**](SecretKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchOrgsIDSecrets

> patchOrgsIDSecrets(orgID, requestBody, opts)

Update secrets in an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SecretsApi();
let orgID = "orgID_example"; // String | The organization ID.
let requestBody = {key: "null"}; // {String: String} | Secret key value pairs to update/add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchOrgsIDSecrets(orgID, requestBody, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **requestBody** | [**{String: String}**](String.md)| Secret key value pairs to update/add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOrgsIDSecrets

> postOrgsIDSecrets(orgID, secretKeys, opts)

Delete secrets from an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SecretsApi();
let orgID = "orgID_example"; // String | The organization ID.
let secretKeys = new InfluxOssApiService.SecretKeys(); // SecretKeys | Secret key to delete
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postOrgsIDSecrets(orgID, secretKeys, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **secretKeys** | [**SecretKeys**](SecretKeys.md)| Secret key to delete | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

