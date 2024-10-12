# SnykApi.ImportProjectsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getImportJobDetails**](ImportProjectsApi.md#getImportJobDetails) | **GET** /org/{orgId}/integrations/{integrationId}/import/{jobId} | Get import job details
[**importTargets**](ImportProjectsApi.md#importTargets) | **POST** /org/{orgId}/integrations/{integrationId}/import | Import targets



## getImportJobDetails

> GetImportJobDetails200Response getImportJobDetails(orgId, integrationId, jobId)

Get import job details



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ImportProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
let jobId = "1a325d9d-b782-468a-a242-9a2073734f0b"; // String | The ID of the job. This can be found in the Location response header from the corresponding POST request that triggered the import job.
apiInstance.getImportJobDetails(orgId, integrationId, jobId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | 
 **jobId** | **String**| The ID of the job. This can be found in the Location response header from the corresponding POST request that triggered the import job. | 

### Return type

[**GetImportJobDetails200Response**](GetImportJobDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## importTargets

> importTargets(orgId, integrationId, opts)

Import targets



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.ImportProjectsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
let opts = {
  'importTargetsRequest': new SnykApi.ImportTargetsRequest() // ImportTargetsRequest | 
};
apiInstance.importTargets(orgId, integrationId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | 
 **importTargetsRequest** | [**ImportTargetsRequest**](ImportTargetsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

