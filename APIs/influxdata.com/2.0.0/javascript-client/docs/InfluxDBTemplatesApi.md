# InfluxOssApiService.InfluxDBTemplatesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applyTemplate**](InfluxDBTemplatesApi.md#applyTemplate) | **POST** /templates/apply | Apply or dry-run an InfluxDB Template
[**createStack**](InfluxDBTemplatesApi.md#createStack) | **POST** /stacks | Create a new stack
[**deleteStack**](InfluxDBTemplatesApi.md#deleteStack) | **DELETE** /stacks/{stack_id} | Delete a stack and associated resources
[**exportTemplate**](InfluxDBTemplatesApi.md#exportTemplate) | **POST** /templates/export | Export a new Influx Template
[**listStacks**](InfluxDBTemplatesApi.md#listStacks) | **GET** /stacks | List all installed InfluxDB templates
[**readStack**](InfluxDBTemplatesApi.md#readStack) | **GET** /stacks/{stack_id} | Retrieve a stack
[**uninstallStack**](InfluxDBTemplatesApi.md#uninstallStack) | **POST** /stacks/{stack_id}/uninstall | Uninstall an InfluxDB Stack
[**updateStack**](InfluxDBTemplatesApi.md#updateStack) | **PATCH** /stacks/{stack_id} | Update an InfluxDB Stack



## applyTemplate

> TemplateSummary applyTemplate(templateApply)

Apply or dry-run an InfluxDB Template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let templateApply = new InfluxOssApiService.TemplateApply(); // TemplateApply | 
apiInstance.applyTemplate(templateApply, (error, data, response) => {
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
 **templateApply** | [**TemplateApply**](TemplateApply.md)|  | 

### Return type

[**TemplateSummary**](TemplateSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-jsonnet, text/yml
- **Accept**: application/json


## createStack

> Stack createStack(postStackRequest)

Create a new stack

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let postStackRequest = new InfluxOssApiService.PostStackRequest(); // PostStackRequest | Stack to create.
apiInstance.createStack(postStackRequest, (error, data, response) => {
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
 **postStackRequest** | [**PostStackRequest**](PostStackRequest.md)| Stack to create. | 

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStack

> deleteStack(stackId, orgID)

Delete a stack and associated resources

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let stackId = "stackId_example"; // String | Theidentifier of the stack.
let orgID = "orgID_example"; // String | The identifier of the organization.
apiInstance.deleteStack(stackId, orgID, (error, data, response) => {
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
 **stackId** | **String**| Theidentifier of the stack. | 
 **orgID** | **String**| The identifier of the organization. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportTemplate

> [TemplateInner] exportTemplate(opts)

Export a new Influx Template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let opts = {
  'exportTemplateRequest': new InfluxOssApiService.ExportTemplateRequest() // ExportTemplateRequest | Export resources as an InfluxDB template.
};
apiInstance.exportTemplate(opts, (error, data, response) => {
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
 **exportTemplateRequest** | [**ExportTemplateRequest**](ExportTemplateRequest.md)| Export resources as an InfluxDB template. | [optional] 

### Return type

[**[TemplateInner]**](TemplateInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/x-yaml


## listStacks

> ListStacks200Response listStacks(orgID, opts)

List all installed InfluxDB templates

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let orgID = "orgID_example"; // String | The organization id of the stacks
let opts = {
  'name': "name_example", // String | A collection of names to filter the list by.
  'stackID': "stackID_example" // String | A collection of stackIDs to filter the list by.
};
apiInstance.listStacks(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization id of the stacks | 
 **name** | **String**| A collection of names to filter the list by. | [optional] 
 **stackID** | **String**| A collection of stackIDs to filter the list by. | [optional] 

### Return type

[**ListStacks200Response**](ListStacks200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStack

> Stack readStack(stackId)

Retrieve a stack

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let stackId = "stackId_example"; // String | Theidentifier of the stack.
apiInstance.readStack(stackId, (error, data, response) => {
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
 **stackId** | **String**| Theidentifier of the stack. | 

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uninstallStack

> Stack uninstallStack(stackId)

Uninstall an InfluxDB Stack

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let stackId = "stackId_example"; // String | The stack id
apiInstance.uninstallStack(stackId, (error, data, response) => {
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
 **stackId** | **String**| The stack id | 

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateStack

> Stack updateStack(stackId, patchStackRequest)

Update an InfluxDB Stack

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.InfluxDBTemplatesApi();
let stackId = "stackId_example"; // String | Theidentifier of the stack.
let patchStackRequest = new InfluxOssApiService.PatchStackRequest(); // PatchStackRequest | Influx stack to update.
apiInstance.updateStack(stackId, patchStackRequest, (error, data, response) => {
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
 **stackId** | **String**| Theidentifier of the stack. | 
 **patchStackRequest** | [**PatchStackRequest**](PatchStackRequest.md)| Influx stack to update. | 

### Return type

[**Stack**](Stack.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

